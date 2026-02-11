"""
QAI HQ Bot — Telegram Service
Envía mensajes formateados via Telegram Bot API.
"""
import logging
import requests
from config import config

logger = logging.getLogger(__name__)

# Límite de Telegram para mensajes
MAX_MESSAGE_LENGTH = 4096


class TelegramService:
    """Servicio para enviar mensajes via Telegram Bot API."""

    BASE_URL = "https://api.telegram.org/bot{token}"

    def __init__(self):
        self._base_url = self.BASE_URL.format(token=config.TELEGRAM_BOT_TOKEN)

    def send_message(
        self, chat_id: int, text: str, parse_mode: str = "Markdown", reply_markup: dict = None, reply_to_message_id: int = None
    ) -> bool:
        """
        Envía un mensaje a un chat de Telegram.
        Si el texto es muy largo, lo divide en partes.
        """
        if len(text) <= MAX_MESSAGE_LENGTH:
            return self._send_single(chat_id, text, parse_mode, reply_markup, reply_to_message_id)
        else:
            return self._send_long(chat_id, text, parse_mode, reply_to_message_id)

    def _send_single(
        self, chat_id: int, text: str, parse_mode: str, reply_markup: dict = None, reply_to_message_id: int = None
    ) -> bool:
        """Envía un solo mensaje."""
        url = f"{self._base_url}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
        }
        if reply_markup:
            payload["reply_markup"] = reply_markup
        if reply_to_message_id:
            payload["reply_to_message_id"] = reply_to_message_id

        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            logger.info("📤 Mensaje enviado a chat_id=%s (%d chars)", chat_id, len(text))
            return True
        except requests.exceptions.RequestException as e:
            logger.error("❌ Error enviando mensaje: %s", e)
            # Retry sin parse_mode (a veces Markdown mal formateado falla)
            if parse_mode:
                logger.info("🔄 Reintentando sin parse_mode...")
                # No enviamos reply_markup en el reintento para simplificar
                return self._send_single(chat_id, text, parse_mode="", reply_markup=None)
            return False

    def _send_long(
        self, chat_id: int, text: str, parse_mode: str, reply_to_message_id: int = None
    ) -> bool:
        """Divide y envía un mensaje largo en partes."""
        chunks = self._split_text(text)
        logger.info("📤 Mensaje largo: dividido en %d partes", len(chunks))

        success = True
        for i, chunk in enumerate(chunks):
            part_header = f"📄 Parte {i + 1}/{len(chunks)}\n\n" if len(chunks) > 1 else ""
            # Solo la última parte podría llevar botones, pero por ahora simplificamos sin botones en mensajes largos
            if not self._send_single(chat_id, part_header + chunk, parse_mode, reply_markup=None, reply_to_message_id=reply_to_message_id):
                success = False

        return success

    def answer_callback_query(self, callback_query_id: str, text: str = "") -> bool:
        """Responde a un callback query para detener el loading state en el cliente."""
        url = f"{self._base_url}/answerCallbackQuery"
        payload = {
            "callback_query_id": callback_query_id,
            "text": text
        }
        try:
            requests.post(url, json=payload, timeout=5)
            return True
        except requests.exceptions.RequestException:
            return False

    def _split_text(self, text: str, max_len: int = MAX_MESSAGE_LENGTH - 50) -> list[str]:
        """Divide texto en chunks respetando saltos de línea."""
        chunks = []
        current = ""

        for line in text.split("\n"):
            if len(current) + len(line) + 1 > max_len:
                if current:
                    chunks.append(current)
                current = line
            else:
                current = f"{current}\n{line}" if current else line

        if current:
            chunks.append(current)

        return chunks if chunks else [text[:max_len]]

    def send_typing_action(self, chat_id: int) -> None:
        """Envía indicador de 'escribiendo...' al chat."""
        url = f"{self._base_url}/sendChatAction"
        try:
            requests.post(
                url,
                json={"chat_id": chat_id, "action": "typing"},
                timeout=5,
            )
        except requests.exceptions.RequestException:
            pass  # No es crítico


# Singleton
telegram_service = TelegramService()
