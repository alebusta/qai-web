"""
QAI HQ Bot — Main Entry Point
Google Cloud Function que recibe webhooks de Telegram.
"""
import json
import logging
import os
import sys

# Agregar el directorio actual al path para imports relativos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import functions_framework
from config import config
from security.auth import auth_guard
from services.telegram_service import telegram_service
from commands.help import handle_help
from commands.status import handle_status
from commands.inbox import handle_inbox
from commands.pendientes import handle_pendientes
from commands.email_cmd import handle_email, handle_confirm

# Configurar logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("qai_bot")


# === Validación al inicio ===
_config_errors = config.validate()
if _config_errors:
    logger.warning("⚠️ Configuración incompleta: %s", _config_errors)


# === Mapeo de comandos ===
COMMANDS = {
    "/start": lambda args, cid: handle_help(),
    "/help": lambda args, cid: handle_help(),
    "/status": lambda args, cid: handle_status(),
    "/inbox": lambda args, cid: handle_inbox(args),
    "/pendientes": lambda args, cid: handle_pendientes(),
    "/email": lambda args, cid: handle_email(args, cid),
    "/confirmar": lambda args, cid: handle_confirm(cid),
}


@functions_framework.http
def webhook(request):
    """
    Entry point para Google Cloud Functions.
    Recibe POST de Telegram webhook, procesa el comando, y responde.
    """
    # Solo aceptar POST
    if request.method != "POST":
        return "OK", 200

    try:
        data = request.get_json(silent=True)
        if not data:
            logger.warning("Request vacío recibido")
            return "OK", 200

        # Extraer mensaje
        message = data.get("message")
        if not message:
            # Puede ser un update de otro tipo (edited_message, callback, etc.)
            logger.debug("Update sin mensaje, ignorado")
            return "OK", 200

        chat_id = message.get("chat", {}).get("id")
        text = message.get("text", "").strip()
        username = message.get("from", {}).get("username", "unknown")

        if not chat_id or not text:
            return "OK", 200

        logger.info("📩 Mensaje de @%s (chat_id=%s): %s", username, chat_id, text[:50])

        # === Verificar acceso ===
        allowed, reason = auth_guard.check_access(chat_id)
        if not allowed:
            if reason == "rate_limited":
                telegram_service.send_message(
                    chat_id, "⏱️ Demasiadas solicitudes. Espera un momento."
                )
            # Si no autorizado, silencio total (no revelar existencia)
            return "OK", 200

        # === Enviar "escribiendo..." ===
        telegram_service.send_typing_action(chat_id)

        # === Procesar comando ===
        response = _process_message(text, chat_id)

        # === Enviar respuesta ===
        telegram_service.send_message(chat_id, response)

        return "OK", 200

    except Exception as e:
        logger.error("❌ Error procesando webhook: %s", e, exc_info=True)
        return "OK", 200  # Siempre retornar 200 a Telegram


def _process_message(text: str, chat_id: int) -> str:
    """Procesa un mensaje y retorna la respuesta."""
    # Detectar comando
    if text.startswith("/"):
        parts = text.split(maxsplit=1)
        command = parts[0].lower().split("@")[0]  # Remover @bot_name si existe
        args = parts[1] if len(parts) > 1 else ""

        handler = COMMANDS.get(command)
        if handler:
            return handler(args, chat_id)
        else:
            return f"❓ Comando `{command}` no reconocido. Escribe /help para ver opciones."

    # Mensaje de texto libre → interpretar con LLM
    return _handle_natural_language(text, chat_id)


def _handle_natural_language(text: str, chat_id: int) -> str:
    """Interpreta mensajes en lenguaje natural."""
    from services.llm_provider import get_llm

    llm = get_llm()

    prompt = f"""El usuario envió este mensaje desde Telegram:
"{text}"

Determina qué acción quiere realizar. Las opciones son:
1. Ver STATUS del HQ → responde exactamente: CMD:status
2. Ver INBOX/pendientes → responde exactamente: CMD:inbox
3. Ver pendientes urgentes → responde exactamente: CMD:pendientes
4. Leer emails → responde exactamente: CMD:email_leer
5. Enviar email → responde exactamente: CMD:email_enviar
6. Otra cosa → responde directamente al usuario de forma breve y útil

Solo responde con el CMD si es claro. Si no, responde naturalmente."""

    try:
        result = llm.chat(prompt).strip()

        # Mapear resultado del LLM a comandos
        cmd_map = {
            "CMD:status": lambda: handle_status(),
            "CMD:inbox": lambda: handle_inbox(""),
            "CMD:pendientes": lambda: handle_pendientes(),
            "CMD:email_leer": lambda: handle_email("leer", chat_id),
            "CMD:email_enviar": lambda: handle_email("enviar", chat_id),
        }

        if result in cmd_map:
            return cmd_map[result]()

        # Si no es un comando, el LLM respondió directamente
        return result

    except Exception as e:
        logger.error("❌ Error en NL processing: %s", e)
        return "❓ No entendí tu mensaje. Prueba con /help para ver los comandos disponibles."
