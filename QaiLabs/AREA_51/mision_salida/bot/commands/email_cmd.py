"""
QAI HQ Bot — Comando /email
Lee emails y crea borradores con human-in-the-loop.
"""
import logging
from services.llm_provider import get_llm

logger = logging.getLogger(__name__)

# Estado temporal de borradores pendientes de confirmación
_pending_drafts: dict[int, dict] = {}  # chat_id -> draft_info


def handle_email(args: str, chat_id: int) -> str:
    """
    Manejo de emails via Telegram.
    
    Subcomandos:
        /email leer     → últimos emails no leídos
        /email enviar   → crear borrador (human-in-the-loop)
    """
    logger.info("📧 Comando /email ejecutado (args=%s)", args)

    parts = args.strip().split(maxsplit=1) if args else []
    subcommand = parts[0].lower() if parts else ""

    if subcommand in ("leer", "read", "ver"):
        return _handle_read()
    elif subcommand in ("enviar", "send", "mandar"):
        detail = parts[1] if len(parts) > 1 else ""
        return _handle_send_draft(detail, chat_id)
    else:
        return (
            "📧 *Email* — Subcomandos:\n\n"
            "• `/email leer` — Ver últimos emails\n"
            "• `/email enviar [destino] [asunto]` — Crear borrador\n\n"
            "⚠️ _Función requiere configuración de Gmail OAuth. "
            "Se implementará en la siguiente iteración._"
        )


def _handle_read() -> str:
    """Lee últimos emails (stub - requiere OAuth setup)."""
    return (
        "📧 *Leer emails*\n\n"
        "⚠️ _Esta función requiere configurar Gmail OAuth en Google Cloud Functions. "
        "Será habilitada en la iteración 2 del bot._\n\n"
        "Por ahora, usa el IDE para leer emails con Nzero."
    )


def _handle_send_draft(detail: str, chat_id: int) -> str:
    """Crea borrador de email (stub con human-in-the-loop)."""
    if not detail:
        return (
            "📧 Para crear un borrador:\n"
            "`/email enviar destinatario@email.com Asunto del correo`\n\n"
            "Luego te mostraré un preview y esperaré tu `/confirmar` para enviarlo."
        )

    # Parse destino y asunto
    parts = detail.split(maxsplit=1)
    dest = parts[0]
    subject = parts[1] if len(parts) > 1 else "(Sin asunto)"

    # Guardar borrador pendiente
    _pending_drafts[chat_id] = {
        "to": dest,
        "subject": subject,
        "status": "draft",
    }

    return (
        f"📧 *Borrador creado*\n\n"
        f"📬 *Para:* {dest}\n"
        f"📝 *Asunto:* {subject}\n\n"
        "⚠️ _Función de envío se habilitará en la iteración 2. "
        "Por ahora, el borrador queda registrado como pendiente._\n\n"
        "En el futuro: envía `/confirmar` para despachar."
    )


def handle_confirm(chat_id: int) -> str:
    """Confirma y envía un borrador pendiente."""
    if chat_id not in _pending_drafts:
        return "❌ No hay ningún borrador pendiente para confirmar."

    draft = _pending_drafts.pop(chat_id)
    return (
        f"⚠️ Función de envío aún no habilitada.\n"
        f"Borrador descartado: {draft['subject']} → {draft['to']}"
    )
