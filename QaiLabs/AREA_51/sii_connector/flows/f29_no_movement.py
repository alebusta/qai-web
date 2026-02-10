"""Flujo automatizado para declarar IVA (F29) sin movimiento."""

import os
import shutil
import sys
import time
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from sii_auth import SIIClient, SIIConnectionError


def _cleanup_screenshots(base_dir: Path, keep_days: int) -> None:
    """Elimina carpetas de capturas antiguas bajo output/screenshots/."""
    if keep_days <= 0:
        return
    screenshots_dir = base_dir / "screenshots"
    if not screenshots_dir.exists():
        return
    cutoff = time.time() - (keep_days * 86400)
    for entry in screenshots_dir.iterdir():
        if not entry.is_dir():
            continue
        try:
            if entry.stat().st_mtime < cutoff:
                shutil.rmtree(entry, ignore_errors=True)
        except OSError:
            continue


def declare_f29_sin_movimiento(
    periodo: Optional[str] = None,
    *,
    headless: bool = False,
    download_dir: Optional[Path] = None,
    cleanup_screenshots_days: int = 30,
) -> dict:
    """Ejecuta el flujo de autenticación + declaración sin movimiento."""
    load_dotenv()
    rut = os.getenv("SII_RUT")
    password = os.getenv("SII_PASSWORD")

    if not rut or not password:
        raise ValueError(
            "Faltan credenciales. Define SII_RUT y SII_PASSWORD en tu archivo .env"
        )

    download_dir = download_dir or Path("output")

    try:
        with SIIClient(headless=headless, artifact_dir=download_dir) as sii:
            print("\n=== Declaración F29 sin movimiento ===")
            print(f"Autenticando RUT: {rut}")

            if not sii.login_with_rut_password(rut, password):
                raise SIIConnectionError("No se pudo completar el inicio de sesión en el SII.")

            # Navegar al formulario F29
            if not sii.navigate_to_f29_no_movement(periodo=periodo):
                if getattr(sii, "period_already_declared", False):
                    print("\nℹ️  El período ya tiene una declaración vigente.")
                    print("   Para rectificar, dirígete a 'Consultar estado de declaración' en el SII.")
                    return {
                        'estado': 'ya_declarado',
                        'mensaje': 'El período ya tiene una declaración vigente',
                        'screenshot': sii.last_period_declared_screenshot,
                    }
                print("\nℹ️  No se pudo completar la navegación al formulario F29.")
                return {'estado': 'error', 'mensaje': 'Error al navegar al formulario F29'}

            # Intentar enviar la declaración
            resultado = sii.submit_f29_no_movement(download_dir=download_dir)

            # Manejar el resultado
            if resultado.get('estado') == 'ya_declarado':
                print("\nℹ️  El período ya tiene una declaración vigente.")
                print("   Para rectificar, dirígete a 'Consultar estado de declaración' en el SII.")
                if 'screenshot' in resultado:
                    print(f"   Captura de pantalla guardada en: {resultado['screenshot']}")
                return resultado

            if 'error' in resultado.get('estado', ''):
                print(f"\n❌ Error: {resultado.get('mensaje', 'Error desconocido')}")
                return resultado

            # Si llegamos aquí, la declaración se envió correctamente
            print("\n✅ Flujo completado exitosamente")
            print(f"Período: {resultado.get('periodo', 'No especificado')}")
            if resultado.get("folio"):
                print(f"Folio / Número de control: {resultado['folio']}")
            if 'screenshot' in resultado:
                print(f"Captura de confirmación: {resultado['screenshot']}")
            if resultado.get("certificado_href"):
                print(f"Certificado disponible en: {resultado['certificado_href']}")

            return resultado
    finally:
        _cleanup_screenshots(download_dir, cleanup_screenshots_days)


if __name__ == "__main__":
    declare_f29_sin_movimiento()
