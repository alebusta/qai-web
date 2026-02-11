"""
QAI HQ Bot — Comando /tarea
Gestión de tareas en INBOX.md desde Telegram.
"""
import re
import logging
from datetime import datetime
from services.github_reader import github_reader
from services.github_writer import github_writer

logger = logging.getLogger(__name__)

INBOX_PATH = "TorreDeControl/INBOX.md"

# Mapeo de prioridad a sección del INBOX
PRIORITY_SECTIONS = {
    "urgente": "## 🔥 URGENTE (Esta Semana)",
    "importante": "## 📋 IMPORTANTE (Este Mes)",
    "backlog": "## 💡💡 IDEAS / BACKLOG",
    "normal": "## 📋 IMPORTANTE (Este Mes)",  # default
}


def handle_tarea(args: str, chat_id: int) -> str:
    """
    Gestión de tareas desde Telegram.
    
    Subcomandos:
        /tarea nueva [texto]           → agrega tarea (prioridad normal)
        /tarea urgente [texto]         → agrega en sección urgente
        /tarea importante [texto]      → agrega en sección importante
        /tarea hecha [texto parcial]   → marca como completada
    """
    logger.info("📝 Comando /tarea ejecutado (args=%s)", args)

    if not args or not args.strip():
        return (
            "📝 *Gestión de tareas* — Uso:\n\n"
            "• `/tarea nueva Llamar a FedEx`\n"
            "• `/tarea urgente Revisar contrato CIAL`\n"
            "• `/tarea importante Preparar deck comercial`\n"
            "• `/tarea hecha Enviar NDA`\n"
        )

    parts = args.strip().split(maxsplit=1)
    subcommand = parts[0].lower()
    detail = parts[1] if len(parts) > 1 else ""

    if not detail:
        return "❌ Falta la descripción de la tarea. Ej: `/tarea nueva Llamar a FedEx`"

    if subcommand in ("nueva", "new", "agregar", "add", "normal"):
        return _add_task(detail, "normal")
    elif subcommand in ("urgente", "urgent", "fuego", "ya"):
        return _add_task(detail, "urgente")
    elif subcommand in ("importante", "important"):
        return _add_task(detail, "importante")
    elif subcommand in ("backlog", "idea", "luego"):
        return _add_task(detail, "backlog")
    elif subcommand in ("hecha", "done", "completada", "listo"):
        return _complete_task(detail)
    else:
        # Asumir que todo el args es una tarea nueva
        return _add_task(args.strip(), "normal")


def _add_task(description: str, priority: str) -> str:
    """Agrega una tarea al INBOX."""
    content = github_reader.read_inbox()
    if not content:
        return "❌ No pude leer INBOX.md para agregar la tarea."

    section_header = PRIORITY_SECTIONS.get(priority, PRIORITY_SECTIONS["normal"])
    task_line = f"- [ ] **{description}** _(vía Telegram, {_today()})_"

    # Buscar la sección e insertar la tarea después del header
    new_content = _insert_in_section(content, section_header, task_line)

    if new_content == content:
        # No encontró la sección, agregar al final
        new_content = content.rstrip() + f"\n\n{section_header}\n{task_line}\n"

    # Commit al repo
    success = github_writer.update_file(
        INBOX_PATH,
        new_content,
        f"📝 Nueva tarea (vía Telegram): {description[:50]}"
    )

    if success:
        # Invalidar cache
        github_reader.clear_cache()
        emoji = {"urgente": "🔥", "importante": "📋", "backlog": "💡"}.get(priority, "📝")
        return (
            f"✅ Tarea agregada al INBOX\n\n"
            f"{emoji} **{description}**\n"
            f"📌 Sección: {priority.capitalize()}"
        )
    else:
        return "❌ No pude escribir en el INBOX. Verifica que el token de GitHub tenga permisos de escritura."


def _complete_task(search_text: str) -> str:
    """Marca una tarea como completada en el INBOX."""
    content = github_reader.read_inbox()
    if not content:
        return "❌ No pude leer INBOX.md."

    # Buscar tarea que contenga el texto
    search_lower = search_text.lower()
    # Limpieza de palabras de ruido
    garbage = ["punto", "tarea", "hecha", "hecho", "completar", "completado", "marcar", "como", "lixto", "listo", "ok"]
    search_words = [w.strip("(),.[]") for w in search_lower.split() if w not in garbage and len(w) > 2]
    
    if not search_words:
        search_words = [w.strip("(),.[]") for w in search_lower.split() if len(w) > 1]

    lines = content.split("\n")
    found = False
    new_lines = []
    task_description = ""

    for line in lines:
        # Solo buscar en líneas que son tareas pendientes: - [ ]
        if not found and re.match(r"^-\s*\[\s*\]", line.strip()):
            line_lower = line.lower()
            matches = sum(1 for word in search_words if word in line_lower)
            
            # Umbral de coincidencia: al menos el 50% de las palabras o al menos 2 si hay varias
            threshold = max(1, len(search_words) // 2)
            if matches >= threshold and matches > 0:
                # Marcar como hecha: [x] + ✅ fecha
                task_description = line.strip().replace("- [ ]", "").strip()
                today = datetime.now().strftime("%d-%b")
                new_line = line.replace("[ ]", "[x]")
                if "✅" not in new_line:
                    new_line = new_line.strip() + f" ✅ {today}\n"
                new_lines.append(new_line)
                found = True
                logger.info("✅ Tarea encontrada y completada: %s", task_description)
                continue
        
        new_lines.append(line)

    if not found:
        return f"❌ No encontré tarea pendiente que contenga \"{search_text}\""

    new_content = "\n".join(new_lines)
    success = github_writer.update_file(
        INBOX_PATH,
        new_content,
        f"✅ Tarea completada (vía Telegram): {search_text[:50]}"
    )

    if success:
        github_reader.clear_cache()
        return f"✅ Tarea marcada como completada: _{search_text}_"
    else:
        return "❌ No pude actualizar el INBOX."


def _insert_in_section(content: str, section_header: str, task_line: str) -> str:
    """Inserta una línea después del header de sección."""
    lines = content.split("\n")
    new_lines = []
    inserted = False

    for i, line in enumerate(lines):
        new_lines.append(line)
        if not inserted and section_header in line:
            # Buscar la siguiente línea no vacía después del header
            # e insertar la tarea ahí
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                new_lines.append(lines[j])
                j += 1
            # Insertar si hay subsección (###)
            if j < len(lines) and lines[j].startswith("###"):
                # Insertar después de la subsección
                new_lines.append(lines[j])
                new_lines.append(task_line)
                # Marcar lo que ya agregamos para no duplicar
                for k in range(i + 1, j + 1):
                    lines[k] = "\x00"  # marcar como procesado
            else:
                new_lines.append(task_line)
            inserted = True

    if not inserted:
        return content  # No se encontró la sección

    # Limpiar líneas marcadas
    final_lines = [l for l in new_lines if l != "\x00"]
    return "\n".join(final_lines)


def _today() -> str:
    """Retorna fecha actual."""
    from datetime import datetime
    return datetime.now().strftime("%d-%b-%Y")
