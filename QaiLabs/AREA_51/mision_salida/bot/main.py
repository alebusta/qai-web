"""
QAI HQ Bot — Main Entry Point
Google Cloud Function que recibe webhooks de Telegram.
Fase 2: Nzero + Gmail + Drive
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
from commands.empresa import handle_empresa
from commands.tarea import handle_tarea
from commands.ruta import handle_ruta
from commands.drive_cmd import handle_drive

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
    "/empresa": lambda args, cid: handle_empresa(args),
    "/tarea": lambda args, cid: handle_tarea(args, cid),
    "/ruta": lambda args, cid: handle_ruta(args),
    "/drive": lambda args, cid: handle_drive(args, cid),
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
            # check for callback_query
            callback_query = data.get("callback_query")
            if callback_query:
                logger.info("🔘 CallbackQuery recibido: %s", callback_query.get("data"))
                return _handle_callback_query(callback_query)

            # Puede ser un update de otro tipo (edited_message, etc.)
            logger.debug("Update sin mensaje ni callback, ignorado")
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


def _handle_callback_query(callback_query: dict) -> str:
    """Maneja interacciones con botones inline."""
    try:
        from commands.email_cmd import handle_email_callback
        
        cq_id = callback_query.get("id")
        data = callback_query.get("data", "")
        message = callback_query.get("message", {})
        chat_id = message.get("chat", {}).get("id")
        
        # Ack inmediato para que deje de cargar
        telegram_service.answer_callback_query(cq_id)

        if not chat_id:
            logger.error("CallbackQuery sin chat_id valid")
            return "OK", 200

        # Ruteo de callbacks
        # Convención: prefix:payload (ej: "email_read:12345")
        if data.startswith("email_read:"):
            msg_id = data.split(":", 1)[1]
            response = handle_email_callback("read", msg_id, chat_id)
            telegram_service.send_message(chat_id, response)
        
        elif data.startswith("email_draft:"):
            action = data.split(":", 1)[1] # send, edit, cancel
            response = handle_email_callback("draft", action, chat_id)
            telegram_service.send_message(chat_id, response)

        return "OK", 200

    except Exception as e:
        logger.error("❌ Error en callback: %s", e)
        return "OK", 200


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

    # Mensaje de texto libre → interpretar con Nzero
    return _handle_natural_language(text, chat_id)


def _handle_natural_language(text: str, chat_id: int) -> str:
    """Interpreta mensajes en lenguaje natural con personalidad Nzero."""
    from services.llm_provider import get_llm
    from persona import NZERO_IDENTITY, NZERO_NLP_ROUTER

    llm = get_llm()

    # Paso 1: Determinar intención
    router_prompt = f"""{NZERO_NLP_ROUTER}

Mensaje del usuario: "{text}"
"""

    try:
        result = llm.chat(router_prompt).strip()

        # Mapear resultado del LLM a comandos
        if result.startswith("CMD:"):
            cmd = result.split("CMD:")[1].strip().split()[0]
            extra = result.split(cmd, 1)[-1].strip() if len(result.split(cmd, 1)) > 1 else ""

            cmd_map = {
                "status": lambda: handle_status(),
                "inbox": lambda: handle_inbox(""),
                "pendientes": lambda: handle_pendientes(),
                "email_leer": lambda: handle_email(f"leer {extra}".strip(), chat_id),
                "email_buscar": lambda: handle_email(f"buscar {extra}", chat_id),
                "email_enviar": lambda: handle_email("enviar", chat_id),
                "email_redactar": lambda: handle_email(f"redactar {extra}", chat_id),
                "empresa": lambda: handle_empresa(extra),
                "ruta": lambda: handle_ruta(extra),
                "tarea_nueva": lambda: handle_tarea(f"nueva {extra}", chat_id),
                "tarea_hecha": lambda: handle_tarea(f"hecha {extra}", chat_id),
                "drive_buscar": lambda: handle_drive(f"buscar {extra}", chat_id),
                "drive_carpeta": lambda: handle_drive(f"carpeta {extra}", chat_id),
            }

            handler = cmd_map.get(cmd)
            if handler:
                return handler()

        # Paso 2: Si no es un comando, responder como Nzero
        # Usar system prompt completo solo para respuestas conversacionales
        persona_prompt = f"""{NZERO_IDENTITY}

El Founder te escribió por Telegram:
"{text}"

Responde como Nzero. Sé conciso (máx 5-8 líneas)."""

        response = llm.chat(persona_prompt).strip()
        return response

    except Exception as e:
        logger.error("❌ Error en NL processing: %s", e)
        return "❓ No entendí tu mensaje. Prueba con /help para ver los comandos disponibles."
