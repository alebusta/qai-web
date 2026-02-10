import asyncio
from playwright.async_api import async_playwright
import os
import sys

# --- QAI GOLDEN TOOL: HIGH-FIDELITY PDF ENGINE ---
# DO NOT DELETE or "Simplify" this script during cleanup.
# ------------------------------------------------

async def generate_pdf(url, output_path, is_landscape=True):
    # IDE COMPATIBILITY: Some terminals (like Cursor/VSCode) restrict process execution.
    # We use args that improve stability in these environments.
    launch_args = [
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--disable-dev-shm-usage",
        "--disable-gpu"
    ]
    
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(args=launch_args)
        except Exception as e:
            if "WinError 5" in str(e) or "Access is denied" in str(e):
                print("\n[!] ERROR DE PERMISOS DETECTADO (WinError 5)")
                print("El terminal de su IDE (Cursor/VSCode) está bloqueando la ejecución de Chromium.")
                print("SOLUCIÓN: Ejecute este comando en un terminal EXTERNO (CMD o PowerShell) o run as Administrator.")
                print(f"Comando sugerido: QaiCore\\qrun.bat {sys.argv[0]} {' '.join(sys.argv[1:])}")
            raise e

        page = await browser.new_page()
        
        print(f"Navigating to {url}...")
        try:
            await page.goto(url, wait_until="networkidle", timeout=60000)
        except Exception as e:
            print(f"[!] Fallo al cargar la URL: {url}. ¿Está el servidor en el puerto 8585?")
            await browser.close()
            raise e
        
        # Additional wait for fonts to ensure Material Icons load
        await page.evaluate("document.fonts.ready")
        
        if is_landscape:
            # For Decks (1280x720)
            await page.pdf(
                path=output_path,
                width="1280px",
                height="720px",
                print_background=True,
                margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"},
                scale=1.0,
                prefer_css_page_size=True
            )
        else:
            # For Proposals (A4)
            await page.pdf(
                path=output_path,
                format="A4",
                print_background=True,
                margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"},
                scale=1.0,
                prefer_css_page_size=True
            )
        
        await browser.close()
        print(f"PDF successfully generated at {output_path}")

async def main():
    # If arguments are provided: [base_url] [base_path] [filename_html_deck] [filename_html_proposal]
    if len(sys.argv) > 3:
        target_url_base = sys.argv[1]
        target_path_base = sys.argv[2]
        deck_file = sys.argv[3]
        proposal_file = sys.argv[4] if len(sys.argv) > 4 else None
    else:
        # Defaults to CIAL for backwards compatibility in this session
        target_url_base = "http://localhost:8585/Empresa/02_COMERCIAL/clientes/CIAL/entrega/"
        target_path_base = r"C:\Users\abustamante\TheQaiCo\Empresa\02_COMERCIAL\clientes\CIAL\entrega"
        deck_file = "Deck_CIAL.html"
        proposal_file = "Propuesta_ESTR_CIAL.html"

    # Generate Deck
    if deck_file:
        await generate_pdf(
            target_url_base + deck_file,
            os.path.join(target_path_base, deck_file.replace(".html", ".pdf")),
            is_landscape=True
        )
    
    # Generate Proposal
    if proposal_file:
        await generate_pdf(
            target_url_base + proposal_file,
            os.path.join(target_path_base, proposal_file.replace(".html", ".pdf")),
            is_landscape=False
        )

def _print_fallback_guide():
    """Guía cuando el IDE bloquea subprocesos (WinError 5)."""
    qaicore_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    repo_root = os.path.dirname(qaicore_dir)
    script_rel = os.path.join("QaiCore", "tools", "generate_all_pdfs.py")
    qrun_rel = os.path.join("QaiCore", "qrun.bat")
    args_str = " ".join(f'"{a}"' for a in sys.argv[1:])
    cmd = f"{qrun_rel} {script_rel} {args_str}" if args_str.strip() else f"{qrun_rel} {script_rel}"
    print("\n" + "=" * 60)
    print("[!] ERROR DE PERMISOS (WinError 5 / Access denied)")
    print("El terminal del IDE (Cursor/VSCode) está bloqueando la ejecución de Chromium.")
    print("SOLUCIÓN: Ejecute en un terminal EXTERNO (CMD o PowerShell):")
    print("=" * 60)
    print(f"  cd /d \"{repo_root}\"")
    print(f"  {cmd}")
    print("=" * 60)
    print("Previo: tener el servidor activo en la raíz: python -m http.server 8585")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except PermissionError as e:
        if e.winerror == 5 or "Access is denied" in str(e):
            _print_fallback_guide()
        raise
    except Exception as e:
        if "WinError 5" in str(e) or "Access is denied" in str(e):
            _print_fallback_guide()
        raise
