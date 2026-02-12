"""
QAI HQ Bot — Gmail Service
Lee y envía emails via Gmail API para uso en Cloud Functions.
"""
import base64
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from googleapiclient.discovery import build

logger = logging.getLogger(__name__)


class GmailService:
    """Servicio para interactuar con Gmail API."""

    def __init__(self):
        from services.google_auth import get_google_credentials

        creds = get_google_credentials()
        self._service = build("gmail", "v1", credentials=creds)
        logger.info("📧 GmailService inicializado")

    def list_unread(self, max_results: int = 5) -> list[dict]:
        """
        Lista emails no leídos del inbox.

        Returns:
            Lista de dicts con id, subject, from, date, snippet.
        """
        try:
            results = (
                self._service.users()
                .messages()
                .list(
                    userId="me",
                    q="is:unread",
                    maxResults=max_results,
                    labelIds=["INBOX"],
                )
                .execute()
            )
            messages = results.get("messages", [])
            if not messages:
                return []

            return [self._get_summary(m["id"]) for m in messages]
        except Exception as e:
            logger.error("❌ Error listando emails: %s", e)
            return []

    def search_messages(self, query: str, max_results: int = 5) -> list[dict]:
        """
        Busca emails con query estilo Gmail.
        Ej: 'from:banco', 'subject:factura', 'has:attachment'
        """
        try:
            results = (
                self._service.users()
                .messages()
                .list(userId="me", q=query, maxResults=max_results)
                .execute()
            )
            messages = results.get("messages", [])
            if not messages:
                return []

            return [self._get_summary(m["id"]) for m in messages]
        except Exception as e:
            logger.error("❌ Error buscando emails: %s", e)
            return []

    def get_message(self, message_id: str) -> dict | None:
        """Lee el contenido completo de un mensaje."""
        try:
            message = (
                self._service.users()
                .messages()
                .get(userId="me", id=message_id, format="full")
                .execute()
            )

            payload = message.get("payload", {})
            headers = payload.get("headers", [])

            subject = next(
                (h["value"] for h in headers if h["name"].lower() == "subject"),
                "(Sin Asunto)",
            )
            sender = next(
                (h["value"] for h in headers if h["name"].lower() == "from"),
                "(Desconocido)",
            )
            date = next(
                (h["value"] for h in headers if h["name"].lower() == "date"),
                "(Sin Fecha)",
            )

            body = self._extract_body(payload)

            return {
                "id": message_id,
                "subject": subject,
                "from": sender,
                "date": date,
                "snippet": message.get("snippet", ""),
                "body": body,
            }
        except Exception as e:
            logger.error("❌ Error leyendo mensaje %s: %s", message_id, e)
            return None

    def send_email(self, to: str, subject: str, body_text: str) -> dict | None:
        """
        Envía un email con soporte HTML y plantilla corporativa.
        Incluye versión texto plano como fallback.
        """
        try:
            from utils.email_templates import wrap_corporate_template

            # Crear mensaje multipart (HTML + Texto Plano)
            message = MIMEMultipart("alternative")
            message["to"] = to
            message["subject"] = subject

            # Parte 1: Texto plano (para clientes antiguos / preview)
            part_text = MIMEText(body_text, "plain")
            
            # Parte 2: HTML (con branding)
            # Primero sanitizamos un poco el texto para HTML básico
            html_content = body_text.replace("\n", "<br>")
            full_html = wrap_corporate_template(html_content)
            part_html = MIMEText(full_html, "html")

            # Adjuntar partes (el orden importa: el último es el preferido por el cliente)
            message.attach(part_text)
            message.attach(part_html)

            raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

            sent = (
                self._service.users()
                .messages()
                .send(userId="me", body={"raw": raw})
                .execute()
            )
            logger.info("📤 Email enviado a %s (ID: %s)", to, sent.get("id"))
            return sent
        except Exception as e:
            logger.error("❌ Error enviando email: %s", e)
            return None

    def _get_summary(self, message_id: str) -> dict:
        """Obtiene un resumen rápido de un mensaje (metadata only)."""
        try:
            message = (
                self._service.users()
                .messages()
                .get(userId="me", id=message_id, format="metadata",
                     metadataHeaders=["Subject", "From", "Date"])
                .execute()
            )

            headers = message.get("payload", {}).get("headers", [])
            subject = next(
                (h["value"] for h in headers if h["name"].lower() == "subject"),
                "(Sin Asunto)",
            )
            sender = next(
                (h["value"] for h in headers if h["name"].lower() == "from"),
                "(Desconocido)",
            )
            date = next(
                (h["value"] for h in headers if h["name"].lower() == "date"),
                "(Sin Fecha)",
            )

            return {
                "id": message_id,
                "subject": subject,
                "from": sender,
                "date": date,
                "snippet": message.get("snippet", ""),
            }
        except Exception as e:
            logger.error("❌ Error obteniendo resumen de %s: %s", message_id, e)
            return {"id": message_id, "subject": "Error", "from": "?", "date": "?", "snippet": ""}

    def _extract_body(self, payload: dict) -> str:
        """Extrae el body (texto plano preferido) del payload."""
        if "parts" in payload:
            for part in payload["parts"]:
                if part["mimeType"] == "text/plain":
                    data = part.get("body", {}).get("data", "")
                    if data:
                        return base64.urlsafe_b64decode(data).decode("utf-8")
            # Fallback: intentar HTML
            for part in payload["parts"]:
                if part["mimeType"] == "text/html":
                    data = part.get("body", {}).get("data", "")
                    if data:
                        html = base64.urlsafe_b64decode(data).decode("utf-8")
                        # Limpieza básica de HTML para Telegram
                        import re
                        text = re.sub(r"<[^>]+>", "", html)
                        return text[:2000]
        else:
            data = payload.get("body", {}).get("data", "")
            if data:
                return base64.urlsafe_b64decode(data).decode("utf-8")
        return "(Sin contenido)"


# Singleton con lazy init
_gmail_instance = None


def get_gmail() -> GmailService:
    """Factory con lazy init para GmailService."""
    global _gmail_instance
    if _gmail_instance is None:
        _gmail_instance = GmailService()
    return _gmail_instance
