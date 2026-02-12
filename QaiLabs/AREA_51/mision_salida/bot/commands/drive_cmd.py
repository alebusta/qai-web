"""
QAI HQ Bot — Comando /drive
Busca y lista archivos de Google Drive desde Telegram.
"""
import logging
from services.gdrive_service import get_gdrive
from services.doc_intelligence_service import get_doc_intelligence
from services.state_service import get_state

logger = logging.getLogger(__name__)


def handle_drive(args: str, chat_id: int) -> str:
    """
    Manejo de Google Drive via Telegram.

    Subcomandos:
        /drive buscar [término]    → busca archivos por nombre
        /drive carpeta [nombre]    → lista archivos de una carpeta conocida
        /drive carpetas            → muestra carpetas disponibles
        /drive leer [id]           → descarga y analiza un archivo con IA
    """
    logger.info("📁 Comando /drive ejecutado (args=%s)", args)

    parts = args.strip().split(maxsplit=1) if args else []
    subcommand = parts[0].lower() if parts else ""
    detail = parts[1].strip() if len(parts) > 1 else ""

    if subcommand in ("buscar", "search", "find"):
        if not detail:
            return "📁 Uso: `/drive buscar [término]`\nEj: `/drive buscar factura FedEx`"
        return _handle_search(detail, chat_id)

    elif subcommand in ("carpeta", "folder", "ls"):
        if not detail:
            return _handle_list_folders()
        return _handle_list_folder(detail, chat_id)

    elif subcommand in ("carpetas", "folders"):
        return _handle_list_folders()

    elif subcommand in ("leer", "read", "analizar"):
        if not detail:
            return "📁 Uso: `/drive leer [file_id]`\nConsigue el ID con `/drive buscar` o `/drive carpeta`."
        return _handle_read_file(detail, chat_id)

    else:
        return (
            "📁 *Drive* — Subcomandos:\n\n"
            "• `/drive buscar [término]` — Buscar archivos\n"
            "• `/drive carpeta [nombre]` — Ver contenido de carpeta\n"
            "• `/drive carpetas` — Ver carpetas disponibles\n"
            "• `/drive leer [id]` — Leer y analizar archivo con IA"
        )


def _handle_search(query: str, chat_id: int) -> str:
    """Busca archivos en Drive por nombre."""
    try:
        gdrive = get_gdrive()
        state = get_state()
        files = gdrive.search_files(query, max_results=8)

        if not files:
            return f"📁 No encontré archivos con *\"{query}\"* en Drive."

        lines = [f"🔍 *Resultados para \"{query}\"*\n"]
        for i, f in enumerate(files, 1):
            name = f["name"]
            link = f["link"]
            ftype = f["type"]
            fid = f["id"]
            if link:
                lines.append(f"{i}. {ftype} [{name}]({link})")
            else:
                lines.append(f"{i}. {ftype} {name}")

        # Guardar en estado para referencia por número
        state.set_user_state(chat_id, "last_drive_search", files)

        return "\n".join(lines) + "\n\nUsa `/drive leer [ID]` o `/drive leer [número]` para analizar."
    except Exception as e:
        logger.error("❌ Error buscando en Drive: %s", e)
        return f"❌ Error al buscar en Drive: {str(e)[:100]}"


def _handle_list_folder(folder_name: str, chat_id: int) -> str:
    """Lista archivos de una carpeta conocida."""
    try:
        gdrive = get_gdrive()
        state = get_state()
        files = gdrive.list_folder(folder_name)

        if not files:
            return f"📁 Carpeta *{folder_name}* vacía o sin acceso."

        # Check for error response
        if files and "error" in files[0]:
            return f"❌ {files[0]['error']}"

        lines = [f"📁 *Carpeta: {folder_name.title()}*\n"]
        for i, f in enumerate(files, 1):
            name = f["name"]
            link = f.get("link", "")
            ftype = f["type"]
            fid = f["id"]
            if link:
                lines.append(f"{i}. {ftype} [{name}]({link})")
            else:
                lines.append(f"{i}. {ftype} {name}")

        # Guardar en estado para referencia por número
        state.set_user_state(chat_id, "last_drive_search", files)

        return "\n".join(lines) + "\n\nUsa `/drive leer [ID]` o `/drive leer [número]` para analizar."
    except Exception as e:
        logger.error("❌ Error listando carpeta: %s", e)
        return f"❌ Error al listar carpeta: {str(e)[:100]}"


def _handle_list_folders() -> str:
    """Muestra carpetas disponibles."""
    try:
        gdrive = get_gdrive()
        folders = gdrive.get_available_folders()

        lines = ["📁 *Carpetas disponibles:*\n"]
        for name in folders:
            lines.append(f"• `{name}`")
        lines.append("\nUsa: `/drive carpeta [nombre]`")

        return "\n".join(lines)
    except Exception as e:
        logger.error("❌ Error: %s", e)
        return f"❌ Error: {str(e)[:100]}"


def _handle_read_file(file_detail: str, chat_id: int) -> str:
    """Lee y analiza un archivo de Drive."""
    try:
        state = get_state()
        file_id = file_detail.strip()

        # 1. Intentar resolver si es un número o palabra ordinal
        last_search = state.get_user_state(chat_id, "last_drive_search")
        
        # Diccionario básico de ordinales
        ordinals = {
            "primero": "1", "primer": "1", "1ro": "1", "1ra": "1",
            "segundo": "2", "2do": "2", "2da": "2",
            "tercero": "3", "tercer": "3", "3ro": "3", "3ra": "3",
            "cuarto": "4", "4to": "4",
            "quinto": "5", "5to": "5",
            "el": "", "la": "", "un": "", "una": "" # Limpieza básica de artículos
        }
        
        # Limpiar palabras comunes
        clean_id = file_id.lower().replace("el ", "").replace("la ", "").replace("un ", "").strip()
        if clean_id in ordinals:
            file_id = ordinals[clean_id]
        elif any(o in clean_id for o in ordinals if ordinals[o] != ""):
             # Caso como "segundo " o "el segundo"
             for o, val in ordinals.items():
                 if val != "" and o in clean_id:
                     file_id = val
                     break

        if file_id.isdigit() and last_search:
            idx = int(file_id) - 1
            if 0 <= idx < len(last_search):
                selected = last_search[idx]
                file_id = selected["id"]
                logger.info("🔢 Índice/Ordinal detectado: %d -> %s", idx + 1, file_id)

        doc_int = get_doc_intelligence()
        # Nzero informa que está trabajando
        return doc_int.analyze_drive_file(file_id, chat_id)
    except Exception as e:
        logger.error("❌ Error leyendo archivo: %s", e)
        return f"❌ Error al leer el archivo: {str(e)[:100]}"
