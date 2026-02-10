"""
QAI HQ Bot — Comando /help
Muestra lista de comandos disponibles.
"""
import logging

logger = logging.getLogger(__name__)

HELP_TEXT = """🤖 *QAI HQ Bot* — Comandos disponibles

📊 `/status` — Resumen del estado del HQ
📥 `/inbox` — Tareas pendientes del INBOX
🔥 `/pendientes` — Solo tareas urgentes e importantes
📧 `/email leer` — Últimos emails no leídos
📧 `/email enviar [dest] [asunto]` — Crear borrador de email
❓ `/help` — Este menú

💡 También puedes escribir en *lenguage natural* y el bot interpretará tu intención.

🔒 _Bot protegido — Solo usuarios autorizados_
"""


def handle_help() -> str:
    """Retorna el texto de ayuda."""
    logger.info("📋 Comando /help ejecutado")
    return HELP_TEXT
