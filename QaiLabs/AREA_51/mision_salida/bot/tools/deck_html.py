"""Branded deck renderer (16:9): Markdown -> HTML (slides).

MVP goals:
- Keep writing in Markdown.
- Use QAI Brand Kit tokens (CSS) for consistent look.
- Generate a local preview HTML for HITL.

Slide format:
- Slides are separated by a line containing only: ---
- Each slide supports Markdown (headings, lists, tables, etc.)

Usage:
  .\QaiCore\qrun.bat -m tools.deck_html \
    --input Empresa/02_COMERCIAL/clientes/CIAL/propuesta_vt_cial/deck.md \
    --output TorreDeControl/temp_files/deck_preview.html \
    --client "CIAL Alimentos" \
    --title "Sistema de Vigilancia Tecnológica" \
    --subtitle "Radar vivo para decisiones" \
    --date "20 de enero de 2026"

Notes:
- This tool produces HTML only (for now). You can print-to-PDF from a browser.
"""

from __future__ import annotations

import argparse
import base64
import html
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable

import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.sane_lists import SaneListExtension
from markdown.extensions.smarty import SmartyExtension
from markdown.extensions.tables import TableExtension


ROOT = Path(__file__).resolve().parents[2]

DEFAULT_LOGO_PATH = ROOT / "Empresa" / "01_ESTRATEGIA" / "IDENTIDAD_VISUAL" / "logoQAI_transparent.png"
if not DEFAULT_LOGO_PATH.exists():
  DEFAULT_LOGO_PATH = ROOT / "Empresa" / "01_ESTRATEGIA" / "IDENTIDAD_VISUAL" / "logoQAI.png"
DEFAULT_TEMPLATE_PATH = ROOT / "Empresa" / "02_COMERCIAL" / "templates" / "deck" / "deck_base.html"
DEFAULT_CSS_PATH = ROOT / "Empresa" / "02_COMERCIAL" / "templates" / "deck" / "deck_style.css"
DEFAULT_PREVIEW_PATH = ROOT / "TorreDeControl" / "temp_files" / "deck_preview.html"


@dataclass
class DeckMeta:
    title: str
    subtitle: str
    client: str
    date_str: str


@dataclass
class Slide:
  title: str
  markdown_body: str
  dense: bool
  variant: str


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _data_uri_for_png(path: Path) -> str:
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:image/png;base64,{b64}"


_SPLIT_RE = re.compile(r"^---\s*$", re.MULTILINE)
_H2_RE = re.compile(r"^##\s+", re.MULTILINE)


def _split_slides(markdown_text: str) -> list[str]:
    raw = markdown_text.replace("\r\n", "\n").strip()
    if not raw:
        return []

    # Prefer explicit separators when present.
    if _SPLIT_RE.search(raw):
        parts = [p.strip() for p in _SPLIT_RE.split(raw)]
        return [p for p in parts if p]

    # Fallback: split by H2 sections (common in outline-style decks).
    # If there's no H2, treat whole document as one slide.
    if not _H2_RE.search(raw):
        return [raw]

    lines = raw.split("\n")
    # Drop leading H1 title block if present.
    if lines and lines[0].startswith("# "):
        # Remove the first line and following blank lines.
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    normalized = "\n".join(lines)

    # Split, preserving the H2 heading in each slide.
    chunks: list[str] = []
    current: list[str] = []
    for line in normalized.split("\n"):
        if line.startswith("## ") and current:
            chunks.append("\n".join(current).strip())
            current = [line]
        else:
            current.append(line)
    if current:
        chunks.append("\n".join(current).strip())
    return [c for c in chunks if c]


def _markdown_to_html(markdown_text: str) -> str:
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


_ATX_TITLE_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$")


def _parse_slide(slide_markdown: str) -> Slide:
    lines = slide_markdown.replace("\r\n", "\n").strip().split("\n")
    title = ""
    body_lines = lines

    if lines:
        match = _ATX_TITLE_RE.match(lines[0].strip())
        if match:
            title = match.group(2).strip()
            body_lines = lines[1:]
            while body_lines and not body_lines[0].strip():
                body_lines = body_lines[1:]

    body = "\n".join(body_lines).strip()
    line_count = sum(1 for l in body_lines if l.strip())
    bullet_count = sum(1 for l in body_lines if l.lstrip().startswith(("- ", "* ")))
    has_visual_blocks = any(token in body for token in ("cards-", "steps", "<table", "<div class=\"callout\""))
    dense = has_visual_blocks or line_count >= 18 or bullet_count >= 8 or len(body) >= 900
    variant = "closing" if re.match(r"^(cierre|gracias)(\b|\s|:)", title.strip(), flags=re.IGNORECASE) else "default"
    return Slide(title=title, markdown_body=body, dense=dense, variant=variant)


def _render_slide_shell(
    *,
    inner_html: str,
    slide_title: str,
    dense: bool,
    variant: str,
    meta: DeckMeta,
    logo_uri: str,
    page_num: int,
    total: int,
) -> str:
    # Cover (slide 1): special layout
    if page_num == 1:
        return f"""
<div class=\"slide-wrap\">
<section class=\"slide slide--cover\">
  <div class=\"cover-frame\"></div>
  <div class=\"safe\">
    <div class=\"topbar\">
      <div class=\"brand\">
        <img class=\"logo\" src=\"{logo_uri}\" alt=\"The QAI Company\" />
        <div class=\"kicker\">Propuesta</div>
      </div>
      <div class=\"meta\">{meta.date_str}</div>
    </div>

    <div style=\"margin-top: 78px;\">
      <h1 class=\"h1\">{meta.title}</h1>
      <div class=\"subtitle\">{meta.subtitle}</div>
      <div class=\"rule\"></div>
      <div class=\"card-row\">
        <div class=\"card\"><div class=\"label\">Cliente</div><div class=\"value\">{meta.client}</div></div>
        <div class=\"card\"><div class=\"label\">Equipo</div><div class=\"value\">The QAI Company</div></div>
        <div class=\"card\"><div class=\"label\">Versión</div><div class=\"value\">v1</div></div>
      </div>
    </div>

    <div class=\"footer\">
      <div>The QAI Company SpA</div>
      <div class=\"pagenum\">{page_num}/{total}</div>
    </div>
  </div>
</section>
 </div>
"""

    # Closing variant
    if variant == "closing":
        return f"""
<div class=\"slide-wrap\">
<section class=\"slide slide--closing\">
  <div class=\"safe\">
    <div class=\"closing-center\">
      <img class=\"logo logo--xl\" src=\"{logo_uri}\" alt=\"The QAI Company\" />
      <div class=\"closing-title\">{html.escape(slide_title) if slide_title else "Gracias"}</div>
      <div class=\"closing-sub\">{inner_html}</div>
    </div>

    <div class=\"footer\">
      <div></div>
      <div class=\"pagenum\">{page_num}/{total}</div>
    </div>
  </div>
</section>
</div>
"""

    # Regular slides
    dense_class = " slide--dense" if dense else ""
    title_html = f"<h2 class=\"slide-title\">{html.escape(slide_title)}</h2>" if slide_title else ""
    return f"""
<div class=\"slide-wrap\">
<section class=\"slide{dense_class}\">
  <div class=\"safe\">
    <div class=\"topbar\">
      <div class=\"brand\">
        <img class=\"logo\" src=\"{logo_uri}\" alt=\"The QAI Company\" />
      </div>
      <div class=\"meta\">{meta.client}</div>
    </div>

    {title_html}
    <div class=\"body\">{inner_html}</div>

    <div class=\"footer\">
      <div>{meta.title}</div>
      <div class=\"pagenum\">{page_num}/{total}</div>
    </div>
  </div>
</section>
</div>
"""


def render_deck_html(
    *,
    markdown_text: str,
    meta: DeckMeta,
    logo_path: Path = DEFAULT_LOGO_PATH,
    template_path: Path = DEFAULT_TEMPLATE_PATH,
    css_path: Path = DEFAULT_CSS_PATH,
) -> str:
    template = _read_text(template_path)
    css = _read_text(css_path)
    logo_uri = _data_uri_for_png(logo_path)

    slides_md = _split_slides(markdown_text)
    if not slides_md:
        raise ValueError("El deck está vacío o no tiene contenido.")

    # Always generate a cover slide from meta, then render markdown slides.
    slides = [_parse_slide(s) for s in slides_md]
    slides_html_inner = [_markdown_to_html(s.markdown_body) for s in slides]
    total = 1 + len(slides_html_inner)

    slides_shell: list[str] = []
    slides_shell.append(
      _render_slide_shell(
        inner_html="",
        slide_title="",
        dense=False,
        variant="cover",
        meta=meta,
        logo_uri=logo_uri,
        page_num=1,
        total=total,
      )
    )
    for idx, (slide, inner) in enumerate(zip(slides, slides_html_inner, strict=True), start=2):
      slides_shell.append(
        _render_slide_shell(
          inner_html=inner,
          slide_title=slide.title,
          dense=slide.dense,
          variant=slide.variant,
          meta=meta,
          logo_uri=logo_uri,
          page_num=idx,
          total=total,
        )
      )

    html = template
    html = html.replace("/* {{CSS}} */", css)
    html = html.replace("{{TITLE}}", meta.title)
    html = html.replace("{{SLIDES_HTML}}", "\n".join(slides_shell))
    return html


def _cli(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render branded deck HTML (Markdown slides -> HTML)")
    parser.add_argument("--input", required=True, help="Ruta al deck .md")
    parser.add_argument("--output", default=str(DEFAULT_PREVIEW_PATH), help="Ruta salida .html")

    parser.add_argument("--title", required=True, help="Título")
    parser.add_argument("--subtitle", default="", help="Subtítulo")
    parser.add_argument("--client", required=True, help="Cliente")
    parser.add_argument("--date", default=date.today().isoformat(), help="Fecha")
    parser.add_argument("--logo", default=str(DEFAULT_LOGO_PATH), help="Ruta logo PNG")

    args = parser.parse_args(list(argv) if argv is not None else None)

    meta = DeckMeta(
        title=args.title,
        subtitle=args.subtitle,
        client=args.client,
        date_str=args.date,
    )

    md_text = _read_text(Path(args.input))
    html = render_deck_html(
        markdown_text=md_text,
        meta=meta,
        logo_path=Path(args.logo),
    )

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    print(f"Deck HTML generado: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
