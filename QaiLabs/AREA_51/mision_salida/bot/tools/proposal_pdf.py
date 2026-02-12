"""Branded proposal renderer: Markdown -> HTML/CSS -> PDF (Playwright).

--- DEPRECATED / LEGACY TOOL ---
DO NOT USE for QAI Executive Horizon proposals.
This tool does not handle margins or font synchronization correctly.
PRIMARY TOOL: QaiCore/tools/generate_all_pdfs.py
------------------------------------------------

This is the foundation for high-quality, consistent client proposals.

Goals:
- Respect QAI corporate identity (logo + footer)
- Produce clean, modern A4 PDF output
- Keep content in Markdown for writing speed

Usage:
    python -m tools.proposal_pdf \
    --input Empresa/02_COMERCIAL/clientes/CIAL/propuesta_vt_cial/for_pdf.md \
    --output Empresa/02_COMERCIAL/clientes/CIAL/propuesta_vt_cial/propuesta_vt_cial.pdf \
    --client "CIAL Alimentos" \
    --title "Sistema de Vigilancia Tecnológica" \
    --subtitle "Radar vivo para decisiones en operaciones, supply y producto" \
    --date "20 de enero de 2026"

Notes:
- Requires: playwright + installed chromium (`python -m playwright install chromium`)
- Requires: markdown (Python-Markdown)
"""

from __future__ import annotations

import argparse
import base64
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable

import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.sane_lists import SaneListExtension
from markdown.extensions.smarty import SmartyExtension
from markdown.extensions.tables import TableExtension
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[2]

DEFAULT_LOGO_PATH = ROOT / "Empresa" / "01_ESTRATEGIA" / "IDENTIDAD_VISUAL" / "logoQAI_transparent.png"
if not DEFAULT_LOGO_PATH.exists():
    DEFAULT_LOGO_PATH = ROOT / "Empresa" / "01_ESTRATEGIA" / "IDENTIDAD_VISUAL" / "logoQAI.png"
DEFAULT_TEMPLATE_PATH = ROOT / "Empresa" / "02_COMERCIAL" / "templates" / "proposal" / "proposal_base.html"
DEFAULT_CSS_PATH = ROOT / "Empresa" / "02_COMERCIAL" / "templates" / "proposal" / "proposal_style.css"


@dataclass
class ProposalMeta:
    title: str
    subtitle: str
    client: str
    contact: str
    version: str
    date_str: str


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _data_uri_for_png(path: Path) -> str:
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:image/png;base64,{b64}"


def _markdown_to_html(markdown_text: str) -> str:
    # Use extension instances to avoid expensive entry_points scanning.
    md_engine = markdown.Markdown(
        extensions=[
            TableExtension(),
            FencedCodeExtension(),
            SaneListExtension(),
            SmartyExtension(),
        ],
        output_format="html5",
    )
    return md_engine.convert(markdown_text)


def render_proposal_html(
    *,
    markdown_text: str,
    meta: ProposalMeta,
    logo_path: Path = DEFAULT_LOGO_PATH,
    template_path: Path = DEFAULT_TEMPLATE_PATH,
    css_path: Path = DEFAULT_CSS_PATH,
) -> str:
    template = _read_text(template_path)
    css = _read_text(css_path)

    content_html = _markdown_to_html(markdown_text)

    html = template
    html = html.replace("/* {{CSS}} */", css)
    html = html.replace("{{LOGO_URI}}", _data_uri_for_png(logo_path))
    html = html.replace("{{TITLE}}", meta.title)
    html = html.replace("{{SUBTITLE}}", meta.subtitle)
    html = html.replace("{{CLIENT}}", meta.client)
    html = html.replace("{{CONTACT}}", meta.contact)
    html = html.replace("{{VERSION}}", meta.version)
    html = html.replace("{{DATE}}", meta.date_str)
    html = html.replace("{{CONTENT_HTML}}", content_html)
    return html


def html_to_pdf(*, html: str, pdf_path: Path) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.set_content(html, wait_until="networkidle")

        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "18mm", "right": "18mm", "bottom": "18mm", "left": "18mm"},
        )

        browser.close()


def md_proposal_to_pdf(
    *,
    input_md: Path,
    output_pdf: Path,
    meta: ProposalMeta,
    logo_path: Path = DEFAULT_LOGO_PATH,
    write_html_preview: bool = True,
) -> Path:
    markdown_text = _read_text(input_md)

    html = render_proposal_html(
        markdown_text=markdown_text,
        meta=meta,
        logo_path=logo_path,
    )

    if write_html_preview:
        preview_path = ROOT / "TorreDeControl" / "temp_files" / "proposal_preview.html"
        preview_path.parent.mkdir(parents=True, exist_ok=True)
        preview_path.write_text(html, encoding="utf-8")

    html_to_pdf(html=html, pdf_path=output_pdf)
    return output_pdf


def _cli(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render branded proposal PDF (Markdown -> HTML/CSS -> PDF)")
    parser.add_argument("--input", required=True, help="Ruta al .md")
    parser.add_argument("--output", required=True, help="Ruta de salida .pdf")

    parser.add_argument("--title", required=True, help="Título (portada)")
    parser.add_argument("--subtitle", default="", help="Subtítulo (portada)")
    parser.add_argument("--client", required=True, help="Cliente")
    parser.add_argument("--contact", default="The QAI Company", help="Contacto")
    parser.add_argument("--version", default="v1", help="Versión")
    parser.add_argument("--date", default=date.today().isoformat(), help="Fecha")
    parser.add_argument("--logo", default=str(DEFAULT_LOGO_PATH), help="Ruta logo PNG")
    parser.add_argument("--no-preview", action="store_true", help="No generar preview HTML")

    args = parser.parse_args(list(argv) if argv is not None else None)

    meta = ProposalMeta(
        title=args.title,
        subtitle=args.subtitle,
        client=args.client,
        contact=args.contact,
        version=args.version,
        date_str=args.date,
    )

    out = md_proposal_to_pdf(
        input_md=Path(args.input),
        output_pdf=Path(args.output),
        meta=meta,
        logo_path=Path(args.logo),
        write_html_preview=not args.no_preview,
    )

    print(f"PDF generado: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
