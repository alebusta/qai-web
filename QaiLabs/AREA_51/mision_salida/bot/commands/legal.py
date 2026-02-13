"""
QAI HQ Bot — Comando /legal
Acceso al agente legal Lex.
"""
import logging
from services.llm_provider import get_llm
from persona import LEX_IDENTITY
from services.github_reader import github_reader

logger = logging.getLogger(__name__)

def handle_legal(args: str = "") -> str:
    """
    Consulta al agente legal Lex con contexto institucional.
    """
    if not args:
        return (
            "⚖️ **Lex (Agente Legal) está activo.**\n\n"
            "Escribe tu consulta. Ej: `/legal estatus patente`"
        )

    logger.info("⚖️ Consultando a Lex: %s", args)
    
    # 1. Obtener memoria institucional
    status_content = github_reader.read_status() or "No se pudo leer STATUS.md"
    inbox_content = github_reader.read_inbox() or "No se pudo leer INBOX.md"
    
    # 2. Construir prompt con contexto
    # Limitamos un poco el tamaño si es muy grande, pero STATUS/INBOX suelen ser manejables
    context = f"""
## MEMORIA INSTITUCIONAL (Torre de Control):

### STATUS ACTUAL:
{status_content}

### TAREAS EN INBOX:
{inbox_content}
"""

    prompt = f"{context}\n\nFounder pregunta: {args}"
    
    llm = get_llm()
    response = llm.chat(prompt, system_instruction=LEX_IDENTITY)
    
    return f"⚖️ **Lex:**\n\n{response}"
