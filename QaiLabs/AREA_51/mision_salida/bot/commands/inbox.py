"""
QAI HQ Bot — Comando /inbox
Lee INBOX.md y muestra tareas pendientes organizadas por prioridad.
"""
import re
import logging
from services.github_reader import github_reader

logger = logging.getLogger(__name__)


def handle_inbox(args: str = "") -> str:
    """
    Lee INBOX.md y muestra solo tareas pendientes.
    
    Args:
        args: Filtro opcional ('urgente', 'importante', 'todo')
    """
    logger.info("📥 Comando /inbox ejecutado (args=%s)", args)

    content = github_reader.read_inbox()
    if not content:
        return "❌ No pude leer INBOX.md desde el repositorio."

    # Extraer tareas no completadas
    pending = _extract_pending_tasks(content)

    if not pending:
        return "✅ *¡Inbox limpio!* No hay tareas pendientes."

    # Filtrar por sección si se pidió
    filter_key = args.strip().lower() if args else ""
    if filter_key in ("urgente", "urgentes", "🔥"):
        pending = {k: v for k, v in pending.items() if "URGENTE" in k.upper()}
    elif filter_key in ("importante", "importantes"):
        pending = {k: v for k, v in pending.items() if "IMPORTANTE" in k.upper()}

    # Formatear respuesta
    return _format_response(pending)


def _extract_pending_tasks(content: str) -> dict[str, list[str]]:
    """Extrae tareas [ ] (pendientes) del INBOX, agrupadas por sección."""
    sections: dict[str, list[str]] = {}
    current_section = "General"

    for line in content.split("\n"):
        stripped = line.strip()

        # Detectar secciones (##)
        if stripped.startswith("## "):
            current_section = stripped.lstrip("#").strip()
            continue
        if stripped.startswith("### "):
            current_section = stripped.lstrip("#").strip()
            continue

        # Detectar tareas pendientes
        if re.match(r"^-\s*\[\s*\]", stripped):
            task_text = re.sub(r"^-\s*\[\s*\]\s*", "", stripped)
            # Limpiar markdown
            task_text = task_text.strip("*").strip()
            if task_text:
                if current_section not in sections:
                    sections[current_section] = []
                sections[current_section].append(task_text)

    return sections


def _format_response(pending: dict[str, list[str]]) -> str:
    """Formatea las tareas pendientes para Telegram."""
    total = sum(len(tasks) for tasks in pending.values())
    lines = [f"📥 *INBOX* — {total} tareas pendientes\n"]

    for section, tasks in pending.items():
        # Asignar emoji por tipo de sección
        if "URGENTE" in section.upper():
            emoji = "🔥"
        elif "IMPORTANTE" in section.upper():
            emoji = "📋"
        elif "BACKLOG" in section.upper() or "IDEAS" in section.upper():
            emoji = "💡"
        else:
            emoji = "📌"

        lines.append(f"\n{emoji} *{section}* ({len(tasks)})")
        for task in tasks[:8]:  # Max 8 por sección
            # Truncar tareas muy largas
            display = task[:100] + "..." if len(task) > 100 else task
            lines.append(f"  • {display}")
        if len(tasks) > 8:
            lines.append(f"  _...y {len(tasks) - 8} más_")

    return "\n".join(lines)
