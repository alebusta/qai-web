"""
QAI HQ Bot — Comando /help
Muestra lista de comandos disponibles.
"""
import logging

logger = logging.getLogger(__name__)

HELP_TEXT = """🤖 *Nzero — QAI HQ Bot*

📊 `/status` — Resumen del estado del HQ
📥 `/inbox` — Tareas pendientes del INBOX
🔥 `/pendientes` — Priorización urgente con IA

🏢 `/empresa rut` — RUT, dirección, socios, banco
📝 `/tarea nueva [texto]` — Agregar tarea al INBOX
📝 `/tarea urgente [texto]` — Agregar tarea urgente
✅ `/tarea hecha [texto]` — Marcar tarea completada
📂 `/ruta [búsqueda]` — Buscar archivos en el repo

📧 `/email leer` — Emails no leídos _(próximamente)_
❓ `/help` — Este menú

💡 También puedes escribir en *lenguaje natural*:
_"¿Cómo van los clientes?" — "Dame el RUT" — "¿Quién eres?"_

🔒 _Bot protegido — Solo usuarios autorizados_
"""


def handle_help() -> str:
    """Retorna el texto de ayuda."""
    logger.info("📋 Comando /help ejecutado")
    return HELP_TEXT
