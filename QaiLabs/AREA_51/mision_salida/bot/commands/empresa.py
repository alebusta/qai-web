"""
QAI HQ Bot — Comando /empresa
Datos de la empresa desde el repo.
"""
import logging
from services.github_reader import github_reader

logger = logging.getLogger(__name__)

# Datos de acceso rápido (cache estático del repo)
COMPANY_DATA = {
    "nombre": "THE QAI COMPANY SpA",
    "rut": "78.313.539-6",
    "tipo": "Sociedad por Acciones (SpA)",
    "direccion": "Santiago, Chile",
    "giro": "Actividades de consultoría de informática y de gestión de instalaciones informáticas",
    "socios": [
        {"nombre": "Alejandro Bustamante Serrano", "rut": "13.234.078-1", "acciones": 5, "porcentaje": "50%", "cargo": "CEO / CTO"},
        {"nombre": "Iliana Alejandra Alzurutt Padrón", "rut": "22.983.691-9", "acciones": 5, "porcentaje": "50%", "cargo": "Socia"},
    ],
    "capital": "$1.000.000 CLP (suscrito y pagado)",
    "constitucion": "20 de Diciembre de 2025",
    "banco": "Banco Chile - Cuenta Vista 00-001-24253-56 (Operativa)",
}

# Aliases para búsqueda natural
ALIASES = {
    "rut": ["rut", "rol", "tributario", "sii"],
    "direccion": ["direccion", "domicilio", "donde", "ubicacion", "oficina"],
    "socios": ["socios", "accionistas", "dueños", "founders", "fundadores", "quienes"],
    "banco": ["banco", "cuenta", "bancaria", "transferencia", "deposito"],
    "capital": ["capital", "acciones", "patrimonio"],
    "giro": ["giro", "actividad", "rubro"],
    "todo": ["empresa", "datos", "info", "informacion", "resumen"],
}


def handle_empresa(args: str = "") -> str:
    """
    Consulta datos de la empresa.
    
    Subcomandos: rut, direccion, socios, banco, capital, giro
    Sin args: resumen completo.
    """
    logger.info("🏢 Comando /empresa ejecutado (args=%s)", args)

    query = args.strip().lower() if args else "todo"

    # Buscar por alias
    matched = _match_alias(query)

    if matched == "rut":
        return f"🏢 **RUT:** `{COMPANY_DATA['rut']}`\n_{COMPANY_DATA['nombre']}_"

    elif matched == "direccion":
        return f"📍 **Dirección:** {COMPANY_DATA['direccion']}"

    elif matched == "socios":
        lines = ["👥 **Socios / Accionistas:**\n"]
        for s in COMPANY_DATA["socios"]:
            lines.append(
                f"• **{s['nombre']}**\n"
                f"  RUT: `{s['rut']}` | {s['acciones']} acciones ({s['porcentaje']}) | {s['cargo']}"
            )
        return "\n".join(lines)

    elif matched == "banco":
        return (
            "🏦 **Datos bancarios:**\n\n"
            "• **Banco:** Banco Chile\n"
            "• **Tipo:** Cuenta Vista\n"
            f"• **Número:** `{COMPANY_DATA['banco'].split(' ')[3]}`\n"
            "• **Estado:** Operativa Total ✅"
        )

    elif matched == "capital":
        return (
            f"💰 **Capital:** {COMPANY_DATA['capital']}\n"
            f"📊 **Acciones totales:** 10 (5 + 5, 50% cada socio)"
        )

    elif matched == "giro":
        return f"📋 **Giro:** {COMPANY_DATA['giro']}"

    else:
        # Resumen completo
        return _full_summary()


def _match_alias(query: str) -> str:
    """Busca coincidencia en aliases."""
    for key, aliases in ALIASES.items():
        if any(alias in query for alias in aliases):
            return key
    return "todo"


def _full_summary() -> str:
    """Resumen completo de la empresa."""
    socios_str = " / ".join(
        f"{s['nombre']} ({s['porcentaje']})" for s in COMPANY_DATA["socios"]
    )
    return (
        f"🏢 *{COMPANY_DATA['nombre']}*\n\n"
        f"📋 **RUT:** `{COMPANY_DATA['rut']}`\n"
        f"📋 **Tipo:** {COMPANY_DATA['tipo']}\n"
        f"📋 **Giro:** {COMPANY_DATA['giro']}\n"
        f"📍 **Dirección:** {COMPANY_DATA['direccion']}\n"
        f"💰 **Capital:** {COMPANY_DATA['capital']}\n"
        f"👥 **Socios:** {socios_str}\n"
        f"📅 **Constitución:** {COMPANY_DATA['constitucion']}"
    )
