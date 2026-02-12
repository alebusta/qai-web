"""Render QAI corporate emails from templates.

This tool standardizes the HTML output used by GmailToolWithPreview / GmailTool.
It is intentionally lightweight (no heavy dependencies) and focuses on:
- Using the official corporate base template
- Rendering a clean HTML body from simple Markdown-like input
- Producing a local preview file (Human-in-the-loop)

Usage:
	python -m tools.render_email render --body "Hola..." --name "Nzero" --role "COO" --preview
	python -m tools.render_email render --body-md path/to/body.md --name "Nzero" --role "COO" --out temp.html
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable

try:
    import markdown
except ImportError:
    markdown = None


DEFAULT_BASE_TEMPLATE = (
	Path(__file__).resolve().parents[2]
	/ "Empresa"
	/ "03_ADMINISTRACION_FINANZAS"
	/ "templates"
	/ "BASE_EMAIL_CORPORATIVO.md"
)


def _read_text(path: Path) -> str:
	return path.read_text(encoding="utf-8")


def _escape_html(text: str) -> str:
	return (
		text.replace("&", "&amp;")
		.replace("<", "&lt;")
		.replace(">", "&gt;")
		.replace('"', "&quot;")
	)


def _render_markdown(md: str) -> str:
    """Robust Markdown-to-HTML renderer using the markdown library.
    
    Falls back to a very simple line-based renderer if the library is missing.
    """
    if markdown:
        return markdown.markdown(md, extensions=['fenced_code', 'tables'])
    
    # Fallback to very simple renderer
    lines = [line.rstrip() for line in md.replace("\r\n", "\n").split("\n")]
    blocks: list[str] = []
    for line in lines:
        if not line.strip(): continue
        blocks.append(f"<p>{_escape_html(line)}</p>")
    return "\n".join(blocks)


def render_email_html(
	*,
	base_template_path: str | Path = DEFAULT_BASE_TEMPLATE,
	body: str,
	agent_name: str,
	agent_role: str,
) -> str:
	base_path = Path(base_template_path)
	base_html = _read_text(base_path)

	body_html = _render_markdown(body)

	html = base_html
	html = html.replace("{{CUERPO_EMAIL}}", body_html)
	html = html.replace("{{NOMBRE_AGENTE}}", _escape_html(agent_name))
	html = html.replace("{{ROL_AGENTE}}", _escape_html(agent_role))
	return html


def _apply_vars(text: str, vars_kv: dict[str, str]) -> str:
	for key, value in vars_kv.items():
		text = text.replace(f"{{{{{key}}}}}", value)
	return text


def _cli(argv: Iterable[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description="Render email HTML using QAI corporate templates")

	sub = parser.add_subparsers(dest="command", required=True)

	render = sub.add_parser("render", help="Render email HTML")
	render.add_argument(
		"--base",
		default=str(DEFAULT_BASE_TEMPLATE),
		help="Ruta al template base (HTML dentro de .md)",
	)
	render.add_argument("--body", default=None, help="Cuerpo del email (markdown simple)")
	render.add_argument("--body-md", default=None, help="Ruta a archivo .md con el cuerpo")
	render.add_argument("--name", required=True, help="Nombre del agente (firma)")
	render.add_argument("--role", required=True, help="Rol del agente (firma)")
	render.add_argument("--subject", default="(Sin asunto)", help="Asunto (solo para preview)")
	render.add_argument(
		"--var",
		action="append",
		default=[],
		help="Sustitución simple: KEY=VALUE para reemplazar {{KEY}} en el cuerpo",
	)
	render.add_argument(
		"--out",
		default=None,
		help="Ruta de salida HTML (si no se especifica, imprime a stdout)",
	)
	render.add_argument(
		"--preview",
		action="store_true",
		help="Genera preview en TorreDeControl/temp_files/email_preview.html",
	)

	args = parser.parse_args(list(argv) if argv is not None else None)

	if args.command == "render":
		if bool(args.body) == bool(args.body_md):
			raise SystemExit("Debes usar exactamente uno: --body o --body-md")

		body = args.body if args.body is not None else Path(args.body_md).read_text(encoding="utf-8")

		vars_kv: dict[str, str] = {}
		for raw in args.var:
			if "=" not in raw:
				raise SystemExit(f"--var inválido (usa KEY=VALUE): {raw}")
			key, value = raw.split("=", 1)
			key = key.strip()
			if not key:
				raise SystemExit(f"--var inválido (KEY vacío): {raw}")
			vars_kv[key] = value.strip()

		body = _apply_vars(body, vars_kv)

		html = render_email_html(
			base_template_path=args.base,
			body=body,
			agent_name=args.name,
			agent_role=args.role,
		)

		if args.preview:
			try:
				from .gmail_preview import GmailToolWithPreview
			except ImportError:
				from gmail_preview import GmailToolWithPreview

			tool = GmailToolWithPreview()
			path = tool.generate_preview(args.subject, html)
			print(f"Preview generado: {path}")

		if args.out:
			out_path = Path(args.out)
			out_path.parent.mkdir(parents=True, exist_ok=True)
			out_path.write_text(html, encoding="utf-8")
			print(f"HTML generado: {out_path}")
		else:
			print(html)

		return 0

	raise SystemExit("Comando no soportado")


if __name__ == "__main__":
	raise SystemExit(_cli())
