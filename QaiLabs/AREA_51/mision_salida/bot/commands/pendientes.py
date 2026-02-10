"""
QAI HQ Bot — Comando /pendientes
Combina STATUS + INBOX para mostrar solo lo urgente/importante.
"""
import logging
from services.github_reader import github_reader
from services.llm_provider import get_llm

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """Eres Nzero, el agente arquitecto de QAI Company.
Tu tarea es crear una lista priorizada de acciones pendientes para el Founder (Alejandro).

Reglas:
- Español, máximo 15 líneas
- Combina info del STATUS (items 🔴 y 🟡) con INBOX (tareas [ ] pendientes)
- Categoriza: 🔴 Bloqueado / 🟡 En proceso / 📋 Pendiente
- Orden: lo más urgente primero
- Para cada item: qué hacer y quién lo bloquea (si aplica)
- No incluir tareas ya completadas [x]
"""


def handle_pendientes() -> str:
    """Genera lista priorizada de pendientes combinando STATUS e INBOX."""
    logger.info("🔥 Comando /pendientes ejecutado")

    status = github_reader.read_status()
    inbox = github_reader.read_inbox()

    if not status and not inbox:
        return "❌ No pude leer STATUS ni INBOX desde el repositorio."

    # Combinar y resumir con LLM
    combined = ""
    if status:
        combined += f"=== STATUS.md ===\n{status}\n\n"
    if inbox:
        combined += f"=== INBOX.md ===\n{inbox}"

    llm = get_llm()
    prompt = f"Genera la lista priorizada de pendientes basándote en:\n\n{combined}"

    try:
        summary = llm.chat(prompt, system_instruction=SYSTEM_PROMPT)
        return f"🔥 *Pendientes priorizados* (via {llm.name})\n\n{summary}"
    except Exception as e:
        logger.error("❌ Error al generar pendientes: %s", e)
        return "❌ Error al generar lista de pendientes. Intenta con `/inbox` para ver el raw."
