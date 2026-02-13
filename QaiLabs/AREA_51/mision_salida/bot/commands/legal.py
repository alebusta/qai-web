"""
QAI HQ Bot — Comando /legal
Acceso al agente legal Lex.
"""
import logging
from services.llm_provider import get_llm
from persona import LEX_IDENTITY

logger = logging.getLogger(__name__)

def handle_legal(args: str = "") -> str:
    """
    Consulta al agente legal Lex.
    """
    if not args:
        return (
            "⚖️ **Lex (Agente Legal) está activo.**\n\n"
            "Puedo ayudarte con:\n"
            "• Revisión de contratos\n"
            "• Patentes municipales\n"
            "• Consultas societarias\n\n"
            "Escribe tu consulta después del comando. Ej: `/legal que necesito para la patente?`"
        )

    logger.info("⚖️ Consultando a Lex: %s", args)
    
    llm = get_llm()
    
    # Podríamos agregar contexto de archivos analizados recientemente aquí
    prompt = f"Founder pregunta: {args}"
    
    response = llm.chat(prompt, system_instruction=LEX_IDENTITY)
    return f"⚖️ **Lex:**\n\n{response}"
