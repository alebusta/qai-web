"""
QAI HQ Bot — Comando /drive
Busca y lista archivos de Google Drive desde Telegram.
"""
import logging
from services.gdrive_service import get_gdrive
from services.doc_intelligence_service import get_doc_intelligence

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
        return _handle_search(detail)

    elif subcommand in ("carpeta", "folder", "ls"):
        if not detail:
            return _handle_list_folders()
        return _handle_list_folder(detail)

    elif subcommand in ("carpetas", "folders"):
        return _handle_list_folders()

    elif subcommand in ("leer", "read", "analizar"):
        if not detail:
            return "📁 Uso: `/drive leer [file_id]`\nConsigue el ID con `/drive buscar` o `/drive carpeta`."
        return _handle_read_file(detail)

    else:
        return (
            "📁 *Drive* — Subcomandos:\n\n"
            "• `/drive buscar [término]` — Buscar archivos\n"
            "• `/drive carpeta [nombre]` — Ver contenido de carpeta\n"
            "• `/drive carpetas` — Ver carpetas disponibles\n"
            "• `/drive leer [id]` — Leer y analizar archivo con IA"
        )


def _handle_search(query: str) -> str:
    """Busca archivos en Drive por nombre."""
    try:
        gdrive = get_gdrive()
        files = gdrive.search_files(query, max_results=8)

        if not files:
            return f"📁 No encontré archivos con *\"{query}\"* en Drive."

        lines = [f"🔍 *Resultados para \"{query}\"*\n"]
        for f in files:
            name = f["name"]
            link = f["link"]
            ftype = f["type"]
            fid = f["id"]
            if link:
                lines.append(f"• {ftype} [{name}]({link})\n  ID: `{fid}`")
            else:
                lines.append(f"• {ftype} {name}\n  ID: `{fid}`")

        return "\n".join(lines) + "\n\nUsa `/drive leer [ID]` para analizar."
    except Exception as e:
        logger.error("❌ Error buscando en Drive: %s", e)
        return f"❌ Error al buscar en Drive: {str(e)[:100]}"


def _handle_list_folder(folder_name: str) -> str:
    """Lista archivos de una carpeta conocida."""
    try:
        gdrive = get_gdrive()
        files = gdrive.list_folder(folder_name)

        if not files:
            return f"📁 Carpeta *{folder_name}* vacía o sin acceso."

        # Check for error response
        if files and "error" in files[0]:
            return f"❌ {files[0]['error']}"

        lines = [f"📁 *Carpeta: {folder_name.title()}*\n"]
        for f in files:
            name = f["name"]
            link = f.get("link", "")
            ftype = f["type"]
            fid = f["id"]
            if link:
                lines.append(f"• {ftype} [{name}]({link})\n  ID: `{fid}`")
            else:
                lines.append(f"• {ftype} {name}\n  ID: `{fid}`")

        return "\n".join(lines) + "\n\nUsa `/drive leer [ID]` para analizar."
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


def _handle_read_file(file_id: str) -> str:
    """Lee y analiza un archivo de Drive."""
    try:
        doc_int = get_doc_intelligence()
        # Nzero informa que está trabajando
        return doc_int.analyze_drive_file(file_id)
    except Exception as e:
        logger.error("❌ Error leyendo archivo: %s", e)
        return f"❌ Error al leer el archivo: {str(e)[:100]}"
