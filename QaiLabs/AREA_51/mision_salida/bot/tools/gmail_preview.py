"""Local HTML preview for QAI emails.

This is intentionally independent from Gmail API auth so it can be used in HITL
flows without requiring tokens.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PREVIEW_PATH = ROOT / "TorreDeControl" / "temp_files" / "email_preview.html"
DEFAULT_LOGO_PATH = ROOT / "Empresa" / "01_ESTRATEGIA" / "IDENTIDAD_VISUAL" / "logoQAI.png"
if not DEFAULT_LOGO_PATH.exists():
	DEFAULT_LOGO_PATH = ROOT / "Empresa" / "01_ESTRATEGIA" / "IDENTIDAD_VISUAL" / "logoQAI_transparent.png"


class GmailToolWithPreview:
	def generate_preview(self, subject: str, body_html: str, output_path: str | None = None) -> str:
		"""Genera un archivo HTML local para previsualizar el correo."""
		preview_path = Path(output_path) if output_path else DEFAULT_PREVIEW_PATH
		preview_path.parent.mkdir(parents=True, exist_ok=True)

		preview_html = body_html
		if DEFAULT_LOGO_PATH.exists():
			# Use the local server URL since the server is running at the root
			logo_url = "http://localhost:8585/Empresa/01_ESTRATEGIA/IDENTIDAD_VISUAL/logoQAI.png"
			preview_html = preview_html.replace("cid:logo_qai", logo_url)

		preview_path.write_text(
			f"<!-- SUBJECT: {subject} -->\n" + preview_html,
			encoding="utf-8",
		)
		return str(preview_path)


if __name__ == "__main__":
	print("Módulo de preview cargado correctamente.")
