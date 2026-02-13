"""
QAI HQ Bot — Comando /finanzas
Acceso al agente financiero Finn.
"""
import logging
from services.llm_provider import get_llm
from persona import FINN_IDENTITY
from services.github_reader import github_reader

logger = logging.getLogger(__name__)

def handle_finanzas(args: str = "") -> str:
    """
    Consulta al agente financiero Finn con contexto institucional.
    """
    if not args:
        return (
            "💰 **Finn (Agente Financiero) está activo.**\n\n"
            "Escribe tu consulta. Ej: `/finanzas cual es el runway?`"
        )

    logger.info("💰 Consultando a Finn: %s", args)
    
    # 1. Obtener memoria institucional
    status_content = github_reader.read_status() or "No se pudo leer STATUS.md"
    inbox_content = github_reader.read_inbox() or "No se pudo leer INBOX.md"
    
    # 2. Construir prompt con contexto
    context = f"""
## MEMORIA INSTITUCIONAL (Torre de Control):

### STATUS ACTUAL:
{status_content}

### TAREAS EN INBOX:
{inbox_content}
"""

    prompt = f"{context}\n\nFounder pregunta: {args}"
    
    llm = get_llm()
    response = llm.chat(prompt, system_instruction=FINN_IDENTITY)
    
    return f"💰 **Finn:**\n\n{response}"
