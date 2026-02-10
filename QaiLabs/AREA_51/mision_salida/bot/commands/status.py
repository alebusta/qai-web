"""
QAI HQ Bot — Comando /status
Lee STATUS.md del HQ y genera un resumen inteligente.
"""
import logging
from services.github_reader import github_reader
from services.llm_provider import get_llm

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """Eres Nzero, el agente arquitecto de QAI Company. 
Tu tarea es resumir el STATUS del HQ digital para el Founder (Alejandro) quien te lee desde Telegram.

Reglas:
- Responde en español
- Máximo 15 líneas
- Usa emojis para secciones
- Resalta items 🔴 (bloqueado) y 🟡 (en proceso)
- Los items ✅ solo menciónalos si son recientes (últimos 3 días)
- Formato: bullets concisos, sin tablas
- Al final, indica la fecha de última actualización del STATUS
"""


def handle_status() -> str:
    """Lee STATUS.md y genera resumen para Telegram."""
    logger.info("📊 Comando /status ejecutado")

    # Leer STATUS.md desde GitHub
    content = github_reader.read_status()
    if not content:
        return "❌ No pude leer STATUS.md desde el repositorio. Verifica el acceso."

    # Resumir con LLM
    llm = get_llm()
    prompt = f"Resume el siguiente STATUS del HQ digital:\n\n{content}"

    try:
        summary = llm.chat(prompt, system_instruction=SYSTEM_PROMPT)
        return f"📊 *Estado del HQ* (via {llm.name})\n\n{summary}"
    except Exception as e:
        logger.error("❌ Error al resumir STATUS: %s", e)
        # Fallback: extraer primeras líneas relevantes
        return _fallback_summary(content)


def _fallback_summary(content: str) -> str:
    """Resumen básico sin LLM (fallback)."""
    lines = content.split("\n")
    relevant = []
    for line in lines:
        stripped = line.strip()
        if any(marker in stripped for marker in ["🔴", "🟡", "🟢", "✅"]):
            relevant.append(stripped)
        if len(relevant) >= 10:
            break

    if relevant:
        return "📊 *Estado del HQ* (modo fallback)\n\n" + "\n".join(relevant)
    return "📊 STATUS cargado pero no pude generar un resumen."
