"""
QAI HQ Bot — Comando /finanzas
Acceso al agente financiero Finn.
"""
import logging
from services.llm_provider import get_llm
from persona import FINN_IDENTITY

logger = logging.getLogger(__name__)

def handle_finanzas(args: str = "") -> str:
    """
    Consulta al agente financiero Finn.
    """
    if not args:
        return (
            "💰 **Finn (Agente Financiero) está activo.**\n\n"
            "Puedo ayudarte con:\n"
            "• Flujo de caja y Runway\n"
            "• SII e Impuestos\n"
            "• Control de gastos\n\n"
            "Escribe tu consulta después del comando. Ej: `/finanzas cual es el runway actual?`"
        )

    logger.info("💰 Consultando a Finn: %s", args)
    
    llm = get_llm()
    
    # En el futuro, Finn debería tener acceso a los datos de GSheets aquí.
    # Por ahora responde con su conocimiento base y lo que sepa del negocio.
    prompt = f"Founder pregunta: {args}"
    
    response = llm.chat(prompt, system_instruction=FINN_IDENTITY)
    return f"💰 **Finn:**\n\n{response}"
