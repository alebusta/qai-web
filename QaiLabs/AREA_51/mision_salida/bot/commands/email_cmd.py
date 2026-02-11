"""
QAI HQ Bot — Comando /email
Lee emails, busca, y envía con human-in-the-loop y persistencia (Firestore).
Fase 2.5: Stateless + Inline Buttons.
"""
import logging
from services.gmail_service import get_gmail
from services.state_service import get_state
from services.telegram_service import telegram_service

logger = logging.getLogger(__name__)

def handle_email(args: str, chat_id: int) -> str:
    """
    Manejo de emails via Telegram.
    """
    logger.info("📧 Comando /email ejecutado (args=%s)", args)

    parts = args.strip().split(maxsplit=1) if args else []
    subcommand = parts[0].lower() if parts else ""
    detail = parts[1].strip() if len(parts) > 1 else ""

    if subcommand in ("leer", "read", "ver", "inbox"):
        return _handle_read(chat_id)
    elif subcommand in ("buscar", "search", "find"):
        if not detail:
            return "📧 Uso: `/email buscar [query]`\nEj: `/email buscar from:banco`"
        return _handle_search(detail, chat_id)
    elif subcommand in ("enviar", "send", "mandar"):
        return _handle_create_draft(detail, chat_id)
    elif subcommand in ("redactar", "draft", "write"):
        return _handle_ai_draft(detail, chat_id)
    else:
        return (
            "📧 *Email* — Comandos:\n\n"
            "• `/email leer` — Ver emails (con botones)\n"
            "• `/email buscar [q]` — Buscar (ej: `from:banco`)\n"
            "• `/email enviar [to] [subject]` — Crear borrador manual\n"
            "• `/email redactar [to] [instrucción]` — Redacción con IA\n\n"
            "_Usa_ `/confirmar` _para enviar el borrador actual._"
        )


def handle_email_callback(type: str, payload: str, chat_id: int) -> str:
    """Maneja callbacks de botones inline."""
    if type == "read":
        # payload es message_id
        return _read_message_full(payload)
    elif type == "draft":
        # payload es action (send, edit, cancel)
        if payload == "send":
            return handle_confirm(chat_id)
        elif payload == "cancel":
            get_state().clear_draft(chat_id)
            return "🗑️ Borrador descartado."
    return "❓ Acción desconocida"


def _handle_read(chat_id: int) -> str:
    """Lista últimos emails no leídos con botones inline."""
    try:
        gmail = get_gmail()
        messages = gmail.list_unread(max_results=5)

        if not messages:
            return "📭 *Inbox limpio* — No hay emails sin leer."

        telegram_service.send_message(chat_id, f"📧 *{len(messages)} emails sin leer:*")

        # Enviar cada email como mensaje separado con su botón "Leer"
        # Esto es mejor para móvil que un solo mensaje largo con muchos botones
        for m in messages:
            sender = _clean_sender(m.get("from", "?"))
            subject = m.get("subject", "(Sin asunto)")
            msg_id = m.get("id")
            
            text = f"📩 *{subject}*\n_De: {sender}_"
            
            # Botón inline
            keyboard = {
                "inline_keyboard": [[
                    {"text": "👁️ Leer", "callback_data": f"email_read:{msg_id}"}
                ]]
            }
            
            telegram_service.send_message(chat_id, text, reply_markup=keyboard)

        return "" # Ya enviamos los mensajes
    except Exception as e:
        logger.error("❌ Error leyendo emails: %s", e)
        return f"❌ Error al leer emails: {str(e)[:100]}"


def _handle_search(query: str, chat_id: int) -> str:
    """Busca emails y muestra resultados con botones."""
    try:
        gmail = get_gmail()
        messages = gmail.search_messages(query, max_results=5)

        if not messages:
            return f"📧 No encontré emails con *\"{query}\"*."

        telegram_service.send_message(chat_id, f"🔍 *Resultados para \"{query}\":*")

        for m in messages:
            sender = _clean_sender(m.get("from", "?"))
            subject = m.get("subject", "(Sin asunto)")
            date = m.get("date", "")[:10]
            msg_id = m.get("id")

            text = f"🔎 *{subject}*\n_De: {sender} | {date}_"
            
            keyboard = {
                "inline_keyboard": [[
                    {"text": "👁️ Leer", "callback_data": f"email_read:{msg_id}"}
                ]]
            }
            telegram_service.send_message(chat_id, text, reply_markup=keyboard)

        return ""
    except Exception as e:
        logger.error("❌ Error buscando emails: %s", e)
        return f"❌ Error al buscar: {str(e)[:100]}"


def _read_message_full(msg_id: str) -> str:
    """Lee un mensaje completo por ID (stateless)."""
    try:
        gmail = get_gmail()
        full_msg = gmail.get_message(msg_id)

        if not full_msg:
            return "❌ No se pudo recuperar el email."

        sender = full_msg.get("from", "?")
        subject = full_msg.get("subject", "(Sin asunto)")
        date = full_msg.get("date", "")
        body = full_msg.get("body", full_msg.get("snippet", ""))

        if len(body) > 3000:
            body = body[:3000] + "\n\n_... (truncado)_"

        return (
            f"📨 *Lectura de Email*\n\n"
            f"📝 *Asunto:* {subject}\n"
            f"👤 *De:* {sender}\n"
            f"📅 *Fecha:* {date}\n\n"
            f"——\n{body}"
        )
    except Exception as e:
        logger.error("❌ Error leyendo mensaje full: %s", e)
        return f"❌ Error: {str(e)[:100]}"


def _handle_create_draft(detail: str, chat_id: int) -> str:
    """Crea borrador manual."""
    if not detail:
        return "📧 Uso: `/email enviar [email] [asunto]`"

    parts = detail.split(maxsplit=1)
    dest = parts[0]
    subject = parts[1] if len(parts) > 1 else "(Sin asunto)"

    if "@" not in dest:
        return "❌ Email inválido."

    # Guardar en StateService (Firestore)
    draft = {
        "to": dest,
        "subject": subject,
        "body": "...", # Pendiente de cuerpo real si quisiéramos
        "status": "draft_manual",
        "timestamp": 0
    }
    get_state().save_draft(chat_id, draft)

    keyboard = {
        "inline_keyboard": [[
            {"text": "✅ Enviar Vacío (Test)", "callback_data": "email_draft:send"},
            {"text": "❌ Cancelar", "callback_data": "email_draft:cancel"}
        ]]
    }

    return f"📧 *Borrador Creado*\nPara: {dest}\nAsunto: {subject}\n\n(Envia cuerpo vacío por ahora, WIP)", keyboard


def _handle_ai_draft(detail: str, chat_id: int) -> str:
    """Redacta email con IA."""
    if not detail:
        return "📧 Uso: `/email redactar [email] [instrucciones]`"
    
    parts = detail.split(maxsplit=1)
    dest = parts[0]
    instructions = parts[1] if len(parts) > 1 else ""

    if "@" not in dest:
        return "❌ Email inválido."
    
    if not instructions:
        return "❌ Faltan instrucciones. Ej: `/email redactar juan@test.com Invitación a reunión`"

    telegram_service.send_message(chat_id, "🤖 *Redactando con IA...*")
    telegram_service.send_typing_action(chat_id)

    # Generar con LLM
    try:
        from services.llm_provider import get_llm
        llm = get_llm()
        
        prompt = f"""
        Como Nzero (asistente ejecutivo de The QAI Company), redacta un email profesional para: {dest}
        
        Instrucciones del usuario: "{instructions}"
        
        Remitente: Alejandro Bustamante (CEO, The QAI Company)
        
        Formato de salida requerido (JSON):
        {{
            "subject": "Asunto del correo",
            "body": "Cuerpo del correo (texto plano, firma incluida, tono profesional pero cercano)"
        }}
        """
        
        response = llm.chat(prompt).strip()
        # Limpiar markdown de json si existe
        if "```json" in response:
            response = response.split("```json")[1].split("```")[0].strip()
        elif "```" in response:
             response = response.split("```")[1].split("```")[0].strip()
        
        import json
        data = json.loads(response)
        
        subject = data.get("subject", "Asunto Propuesto")
        body = data.get("body", "")

        # Guardar Draft
        draft = {
            "to": dest,
            "subject": subject,
            "body": body,
            "status": "draft_ai",
            "timestamp": 0
        }
        get_state().save_draft(chat_id, draft)
        
        keyboard = {
            "inline_keyboard": [[
                {"text": "✅ Enviar Ahora", "callback_data": "email_draft:send"},
                {"text": "❌ Cancelar", "callback_data": "email_draft:cancel"}
            ]]
        }
        
        return (
            f"🤖 *Borrador Generado*\n\n"
            f"📬 *Para:* {dest}\n"
            f"📝 *Asunto:* {subject}\n\n"
            f"——\n{body}\n——", 
            keyboard
        )

    except Exception as e:
        logger.error("Error redactando: %s", e)
        return f"❌ Error generando borrador: {e}"


def handle_confirm(chat_id: int) -> str:
    """Confirma el borrador actual."""
    state = get_state()
    draft = state.get_draft(chat_id)

    if not draft:
        return "❌ No hay borrador activo. Usa `/email enviar` primero."

    try:
        gmail = get_gmail()
        # Si el draft tiene body generado por IA, usarlo. Si no, texto default.
        body_text = draft.get("body", "Email enviado desde QAI Bot.")
        
        result = gmail.send_email(draft["to"], draft["subject"], body_text)
        
        if result:
            state.clear_draft(chat_id)
            return f"✅ Email enviado a {draft['to']}."
        else:
            return "❌ Falló el envío."
    except Exception as e:
        return f"❌ Error: {e}"


def _clean_sender(sender: str) -> str:
    if "<" in sender:
        return sender.split("<")[0].strip().strip('"')
    return sender
