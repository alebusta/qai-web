"""
QAI HQ Bot — Comando /ruta
Busca rutas de archivos en el repositorio.
"""
import logging
from services.github_reader import github_reader
from config import config
import requests

logger = logging.getLogger(__name__)

# Índice de archivos clave con rutas y descripción
KNOWN_PATHS = {
    "status": {"path": "TorreDeControl/STATUS.md", "desc": "Estado actual del HQ"},
    "inbox": {"path": "TorreDeControl/INBOX.md", "desc": "Tareas pendientes"},
    "estatutos": {"path": "Empresa/04_LEGAL/ESTATUTOS_QAI_COMPANY.md", "desc": "Estatutos de la SpA"},
    "actas": {"path": "Empresa/04_LEGAL/actas/", "desc": "Libro de Actas"},
    "accionistas": {"path": "Empresa/04_LEGAL/registros_oficiales/", "desc": "Registro de Accionistas"},
    "finanzas": {"path": "Empresa/03_ADMINISTRACION_FINANZAS/", "desc": "Contabilidad y finanzas"},
    "contabilidad": {"path": "Empresa/03_ADMINISTRACION_FINANZAS/contabilidad/", "desc": "Libros contables"},
    "tributario": {"path": "Empresa/03_ADMINISTRACION_FINANZAS/MANUAL_TRIBUTARIO_Y_OPERATIVO.md", "desc": "Manual tributario SII"},
    "clientes": {"path": "Empresa/02_COMERCIAL/", "desc": "Área comercial y clientes"},
    "protocolo_clientes": {"path": "Empresa/02_COMERCIAL/PROTOCOLO_ORGANIZACION_CLIENTES.md", "desc": "Protocolo de organización de clientes"},
    "estrategia": {"path": "Empresa/01_ESTRATEGIA/", "desc": "Estrategia y manifiesto"},
    "manifiesto": {"path": "Empresa/01_ESTRATEGIA/MANIFIESTO_QAI.md", "desc": "Manifiesto QAI"},
    "overview": {"path": "Empresa/01_ESTRATEGIA/THE_QAI_COMPANY_OVERVIEW.md", "desc": "Overview de la empresa"},
    "legal": {"path": "Empresa/04_LEGAL/", "desc": "Documentos legales"},
    "roadmap": {"path": "Empresa/04_LEGAL/ROADMAP_CONSTITUCION_QAI.md", "desc": "Roadmap de constitución"},
    "prototipos": {"path": "QaiLabs/PROTOTIPOS/", "desc": "Prototipos de productos"},
    "invoice": {"path": "QaiLabs/PROTOTIPOS/invoice-match/", "desc": "Invoice-Match (FedEx)"},
    "agentes": {"path": "QaiCore/agents/", "desc": "Agentes de QAI (Nzero, Lex, Finn)"},
    "nzero": {"path": "QaiCore/agents/NZERO/", "desc": "Perfil del agente Nzero"},
    "lex": {"path": "QaiCore/agents/LEX/", "desc": "Perfil del agente Lex"},
    "finn": {"path": "QaiCore/agents/FINN/", "desc": "Perfil del agente Finn"},
    "tools": {"path": "QaiCore/tools/", "desc": "Herramientas compartidas"},
    "playbooks": {"path": "QaiCore/playbooks/", "desc": "Playbooks operativos"},
    "bot": {"path": "QaiLabs/AREA_51/mision_salida/bot/", "desc": "Bot de Telegram"},
    "costos": {"path": "QaiLabs/AREA_51/mision_salida/COSTOS.md", "desc": "Costos del bot"},
    "certificados": {"path": "Empresa/03_ADMINISTRACION_FINANZAS/documentos_legales/", "desc": "Certificados SII y documentos"},
    "fedex": {"path": "Clientes/FEDEX/", "desc": "Carpeta cliente FedEx"},
    "cial": {"path": "Clientes/CIAL/", "desc": "Carpeta cliente CIAL Alimentos"},
    "gestionzen": {"path": "Clientes/GESTIONZEN/", "desc": "Carpeta Gestión Zen"},
}


def handle_ruta(args: str = "") -> str:
    """
    Busca rutas de archivos.
    
    /ruta [búsqueda] → busca en el índice
    /ruta            → muestra carpetas principales
    """
    logger.info("📂 Comando /ruta ejecutado (args=%s)", args)

    if not args or not args.strip():
        return _show_main_dirs()

    query = args.strip().lower()

    # Buscar en índice conocido
    results = _search_index(query)

    if results:
        lines = [f"📂 *Resultados para \"{args.strip()}\":*\n"]
        for key, info in results:
            lines.append(f"• `{info['path']}`\n  _{info['desc']}_")
        return "\n".join(lines)

    # Si no hay match local, buscar via GitHub API
    api_results = _search_github(query)
    if api_results:
        lines = [f"📂 *Búsqueda en repo para \"{args.strip()}\":*\n"]
        for path in api_results[:8]:
            lines.append(f"• `{path}`")
        return "\n".join(lines)

    return f"❌ No encontré archivos que coincidan con \"{args.strip()}\""


def _show_main_dirs() -> str:
    """Muestra las carpetas principales."""
    return (
        "📂 *Carpetas principales del HQ:*\n\n"
        "🏢 `Empresa/` — Datos corporativos\n"
        "  ├─ `01_ESTRATEGIA/`\n"
        "  ├─ `02_COMERCIAL/`\n"
        "  ├─ `03_ADMINISTRACION_FINANZAS/`\n"
        "  └─ `04_LEGAL/`\n\n"
        "🔬 `QaiLabs/` — Productos y R&D\n"
        "  ├─ `PROTOTIPOS/`\n"
        "  └─ `AREA_51/`\n\n"
        "🤖 `QaiCore/` — Agentes y herramientas\n"
        "  ├─ `agents/`\n"
        "  └─ `tools/`\n\n"
        "📊 `TorreDeControl/` — STATUS e INBOX\n"
        "👥 `Clientes/` — Carpetas por cliente\n\n"
        "💡 Busca algo específico: `/ruta estatutos`"
    )


def _search_index(query: str) -> list:
    """Busca en el índice conocido."""
    results = []
    for key, info in KNOWN_PATHS.items():
        if (
            query in key
            or query in info["path"].lower()
            or query in info["desc"].lower()
        ):
            results.append((key, info))
    return results[:6]  # Max 6 resultados


def _search_github(query: str) -> list[str]:
    """Busca archivos en el repo via GitHub API."""
    url = f"https://api.github.com/search/code?q={query}+repo:{config.GITHUB_REPO}"
    headers = {
        "Authorization": f"token {config.GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        items = response.json().get("items", [])
        return [item["path"] for item in items]
    except Exception as e:
        logger.error("Error buscando en GitHub: %s", e)
        return []
