"""
QAI HQ Bot — Comando /email
Lee emails, busca, y envía con human-in-the-loop.
Fase 2: Integración real con Gmail API.
"""
import logging
from services.gmail_service import get_gmail

logger = logging.getLogger(__name__)

# Estado temporal de borradores pendientes de confirmación
_pending_drafts: dict[int, dict] = {}  # chat_id -> draft_info

# Cache de últimos emails listados (para /email leer N)
_last_listed: dict[int, list[dict]] = {}  # chat_id -> [messages]


def handle_email(args: str, chat_id: int) -> str:
    """
    Manejo de emails via Telegram.

    Subcomandos:
        /email leer         → últimos emails no leídos
        /email buscar [q]   → buscar emails con query Gmail
        /email enviar       → crear borrador (human-in-the-loop)
    """
    logger.info("📧 Comando /email ejecutado (args=%s)", args)

    parts = args.strip().split(maxsplit=1) if args else []
    subcommand = parts[0].lower() if parts else ""
    detail = parts[1].strip() if len(parts) > 1 else ""

    if subcommand in ("leer", "read", "ver", "inbox"):
        # Si tiene un número, leer ese email específico
        if detail and detail.isdigit():
            return _handle_read_one(int(detail), chat_id)
        return _handle_read(chat_id)
    elif subcommand in ("buscar", "search", "find"):
        if not detail:
            return "📧 Uso: `/email buscar [query]`\nEj: `/email buscar from:banco`"
        return _handle_search(detail)
    elif subcommand in ("enviar", "send", "mandar"):
        return _handle_send_draft(detail, chat_id)
    else:
        return (
            "📧 *Email* — Subcomandos:\n\n"
            "• `/email leer` — Ver últimos emails no leídos\n"
            "• `/email leer [N]` — Leer email N completo\n"
            "• `/email buscar [query]` — Buscar (ej: `from:banco`)\n"
            "• `/email enviar [destino] [asunto]` — Crear borrador\n\n"
            "_Luego usa_ `/confirmar` _para enviar._"
        )


def _handle_read(chat_id: int) -> str:
    """Lista últimos emails no leídos."""
    try:
        gmail = get_gmail()
        messages = gmail.list_unread(max_results=5)

        if not messages:
            return "📭 *Inbox limpio* — No hay emails sin leer."

        # Guardar en cache para /email leer N
        _last_listed[chat_id] = messages

        lines = [f"📧 *{len(messages)} emails sin leer:*\n"]
        for i, m in enumerate(messages, 1):
            sender = m.get("from", "?")
            if "<" in sender:
                sender = sender.split("<")[0].strip().strip('"')
            subject = m.get("subject", "(Sin asunto)")
            snippet = m.get("snippet", "")[:80]
            lines.append(f"*{i}.* {subject}")
            lines.append(f"   _De: {sender}_")
            if snippet:
                lines.append(f"   {snippet}...")
            lines.append("")

        lines.append("_Usa_ `/email leer [N]` _para leer uno completo._")
        return "\n".join(lines)
    except Exception as e:
        logger.error("❌ Error leyendo emails: %s", e)
        return f"❌ Error al leer emails: {str(e)[:100]}"


def _handle_read_one(index: int, chat_id: int) -> str:
    """Lee el contenido completo de un email por su número en la lista."""
    cached = _last_listed.get(chat_id, [])
    if not cached:
        return "❌ Primero lista los emails con `/email leer`, luego usa `/email leer [N]`."

    if index < 1 or index > len(cached):
        return f"❌ Número inválido. Escoge entre 1 y {len(cached)}."

    msg_summary = cached[index - 1]
    msg_id = msg_summary.get("id")
    if not msg_id:
        return "❌ No se pudo obtener el ID del mensaje."

    try:
        gmail = get_gmail()
        full_msg = gmail.get_message(msg_id)

        if not full_msg:
            return "❌ Error al leer el mensaje completo."

        sender = full_msg.get("from", "?")
        subject = full_msg.get("subject", "(Sin asunto)")
        date = full_msg.get("date", "")
        body = full_msg.get("body", full_msg.get("snippet", ""))

        # Truncar body si es muy largo para Telegram
        if len(body) > 3000:
            body = body[:3000] + "\n\n_... (truncado)_"

        return (
            f"📨 *Email #{index}*\n\n"
            f"📝 *Asunto:* {subject}\n"
            f"👤 *De:* {sender}\n"
            f"📅 *Fecha:* {date}\n\n"
            f"——\n{body}"
        )
    except Exception as e:
        logger.error("❌ Error leyendo email #%d: %s", index, e)
        return f"❌ Error al leer email: {str(e)[:100]}"


def _handle_search(query: str) -> str:
    """Busca emails con query estilo Gmail."""
    try:
        gmail = get_gmail()
        messages = gmail.search_messages(query, max_results=5)

        if not messages:
            return f"📧 No encontré emails con *\"{query}\"*."

        lines = [f"🔍 *Resultados para \"{query}\"*\n"]
        for i, m in enumerate(messages, 1):
            sender = m.get("from", "?")
            if "<" in sender:
                sender = sender.split("<")[0].strip().strip('"')
            subject = m.get("subject", "(Sin asunto)")
            date = m.get("date", "")
            # Simplificar fecha
            if "," in date:
                date = date.split(",")[1].strip()[:12]
            lines.append(f"*{i}.* {subject}")
            lines.append(f"   _De: {sender} | {date}_")
            lines.append("")

        return "\n".join(lines)
    except Exception as e:
        logger.error("❌ Error buscando emails: %s", e)
        return f"❌ Error al buscar: {str(e)[:100]}"


def _handle_send_draft(detail: str, chat_id: int) -> str:
    """Crea borrador de email con human-in-the-loop."""
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

    # Validar que parece un email
    if "@" not in dest:
        return "❌ El destinatario no parece un email válido. Formato: `usuario@dominio.com`"

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
        f"Envía `/confirmar` para despachar este email.\n"
        f"(Se enviará como texto plano desde alebusta@qai.cl)"
    )


def handle_confirm(chat_id: int) -> str:
    """Confirma y envía un borrador pendiente."""
    if chat_id not in _pending_drafts:
        return "❌ No hay ningún borrador pendiente para confirmar."

    draft = _pending_drafts.pop(chat_id)

    try:
        gmail = get_gmail()
        body_text = f"Email enviado desde QAI Bot por Nzero.\n\nAsunto: {draft['subject']}"
        result = gmail.send_email(draft["to"], draft["subject"], body_text)

        if result:
            return (
                f"✅ *Email enviado*\n\n"
                f"📬 *Para:* {draft['to']}\n"
                f"📝 *Asunto:* {draft['subject']}\n"
                f"🆔 ID: `{result.get('id', 'N/A')}`"
            )
        else:
            return "❌ Error enviando el email. Revisa los logs."
    except Exception as e:
        logger.error("❌ Error enviando email: %s", e)
        # Restaurar borrador en caso de error
        _pending_drafts[chat_id] = draft
        return f"❌ Error al enviar: {str(e)[:100]}\nEl borrador sigue pendiente, intenta `/confirmar` de nuevo."
