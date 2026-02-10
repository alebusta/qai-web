"""Markdown to PDF converter with professional styling for QAI proposals.

--- DEPRECATED / LEGACY TOOL ---
DO NOT USE for QAI Executive Horizon proposals.
This tool produces basic FPDF output and ignores the high-fidelity CSS/Design.
PRIMARY TOOL: QaiCore/tools/generate_all_pdfs.py
------------------------------------------------

Uses fpdf2 (fpdf) to render polished PDFs from Markdown files.
Supports: headings (#), bullet lists, tables, and professional layout.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable

from fpdf import FPDF  # type: ignore


class ProposalPDF(FPDF):
    """Extended FPDF with QAI branding and professional layout."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_num = 0
        self.title_text = ""
        self.subtitle_text = ""

    def header(self):
        """Page header with subtle branding."""
        if self.page_num > 0:  # Changed from > 1 to show on all pages
            self.set_y(10)
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(128, 128, 128)
            self.cell(0, 10, "QAI SpA", 0, 1, "R")
            self.set_text_color(0, 0, 0)

    def footer(self):
        """Page footer with Folio numbering."""
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Folio {self.page_no()}", 0, 0, "C")
        self.set_text_color(0, 0, 0)

    def on_page(self):
        """DEPRECATED"""
        pass


def md_to_pdf(md_path: str | Path, pdf_path: str | Path, title: str | None = None) -> str:
    """Convert Markdown to professional PDF.
    
    Args:
        md_path: Path to Markdown file.
        pdf_path: Path to output PDF.
        title: Optional custom title for the document.
    
    Returns:
        Path to generated PDF.
    """
    md_file = Path(md_path)
    pdf_file = Path(pdf_path)

    content = md_file.read_text(encoding="utf-8")
    lines = content.splitlines()

    # Detect ACTA documents and capture title metadata lines
    first_h1_index = next((i for i, line in enumerate(lines) if line.lstrip().startswith("#")), None)
    acta_mode = False
    title_subtitles: list[str] = []
    skip_title_line_indices: set[int] = set()
    if first_h1_index is not None:
        h1_text = lines[first_h1_index].lstrip("#").strip()
        acta_mode = "ACTA" in h1_text.upper()
        if acta_mode:
            j = first_h1_index + 1
            while j < len(lines):
                candidate = lines[j].strip()
                if candidate == "":
                    break
                if re.fullmatch(r"\*\*.+\*\*", candidate):
                    title_subtitles.append(candidate[2:-2].strip())
                    skip_title_line_indices.add(j)
                    j += 1
                    continue
                break

    # Wider margins for legal documents (30mm left, 20mm right)
    pdf = ProposalPDF(orientation="P", unit="mm", format="A4")
    pdf.set_left_margin(30)
    pdf.set_right_margin(20)
    if acta_mode:
        pdf.set_auto_page_break(auto=True, margin=12)
    else:
        pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    pdf.set_font("Helvetica", size=11)

    # Track if we've processed the first heading
    first_h1 = True
    in_table = False
    table_rows = []

    for idx, line in enumerate(lines):
        stripped = line.strip()

        if idx in skip_title_line_indices:
            continue

        # Handle explicit line breaks "\" which the user uses for spacing
        if stripped == "\\":
            pdf.ln(7)
            continue

        if acta_mode and stripped == "---":
            continue

        if acta_mode and stripped in {"Firmas:", "**Firmas:**"}:
            pdf.add_page()
            pdf.set_font("Helvetica", "B", 12)
            pdf.ln(2)
            pdf.multi_cell(0, 8, "Firmas:")
            pdf.ln(2)
            continue

        # Skip empty lines briefly, but use them for spacing
        if stripped == "":
            if not in_table:
                pdf.ln(3)
            continue

        # Handle headings
        if stripped.startswith("#"):
            if in_table:
                _render_table(pdf, table_rows)
                table_rows = []
                in_table = False

            level = len(stripped) - len(stripped.lstrip("#"))
            text = stripped.lstrip("#").strip()

            if level == 1:
                if first_h1:
                    # Title page for first H1
                    pdf.set_font("Helvetica", "B", 24)
                    if acta_mode:
                        pdf.set_text_color(0, 0, 0)
                    else:
                        pdf.set_text_color(25, 118, 210)  # Professional blue
                    pdf.ln(50)
                    if acta_mode:
                        pdf.set_x(pdf.l_margin)
                        pdf.multi_cell(0, 15, text, 0, "C")
                        if title_subtitles:
                            pdf.ln(5)
                            pdf.set_font("Helvetica", "B", 16)
                            pdf.set_x(pdf.l_margin)
                            pdf.multi_cell(0, 10, title_subtitles[0], 0, "C")
                            if len(title_subtitles) > 1:
                                pdf.set_font("Helvetica", "", 12)
                                pdf.set_x(pdf.l_margin)
                                pdf.multi_cell(0, 8, title_subtitles[1], 0, "C")
                    else:
                        pdf.multi_cell(0, 15, text.upper(), 0, "C")
                    pdf.set_text_color(0, 0, 0)
                    pdf.ln(60)
                    pdf.add_page()
                    pdf.set_font("Helvetica", size=11)
                    first_h1 = False
                else:
                    # New section heading
                    if acta_mode:
                        pdf.set_font("Helvetica", "B", 14)
                        pdf.ln(5)
                        pdf.multi_cell(0, 10, text)
                        pdf.ln(2)
                    else:
                        pdf.set_font("Helvetica", "B", 16)
                        pdf.set_text_color(25, 118, 210)
                        pdf.multi_cell(0, 10, text.upper())
                        pdf.set_text_color(0, 0, 0)
                        pdf.set_font("Helvetica", size=11)
                        pdf.ln(2)
            else:
                if acta_mode:
                    pdf.set_font("Helvetica", "B", 12)
                    pdf.ln(2)
                    pdf.multi_cell(0, 8, text)
                else:
                    pdf.set_font("Helvetica", "B", 13)
                    pdf.set_text_color(66, 133, 244)
                    pdf.multi_cell(0, 8, text.upper())
                    pdf.set_text_color(0, 0, 0)
                    pdf.set_font("Helvetica", size=11)
                    pdf.ln(1)
            continue

        if acta_mode and re.fullmatch(r"\*\*.+\*\*", stripped):
            heading_text = stripped[2:-2].strip()
            if heading_text in {"ASISTENTES:", "TABLA:", "ACUERDOS:"}:
                pdf.set_font("Helvetica", "B", 12)
                pdf.ln(2)
                pdf.multi_cell(0, 8, heading_text)
                pdf.ln(1)
                continue
            if re.match(r"^(PRIMERO|SEGUNDO|TERCERO|CUARTO|QUINTO|SEXTO|SEPTIMO|OCTAVO|NOVENO|DECIMO):", heading_text):
                pdf.set_font("Helvetica", "B", 11)
                pdf.ln(1)
                pdf.multi_cell(0, 7, heading_text)
                pdf.ln(1)
                continue

        # Skip metadata that was already put on the title page
        if not first_h1 and stripped in ["**THE QAI COMPANY SpA**", "**RUT: 78.313.539-6**"]:
             # Optimization: only skip if it's right after the title page (first few lines)
             if pdf.page_no() == 2:
                 continue

        # Handle tables (lines with |)
        if "|" in stripped:
            if not in_table:
                in_table = True
            # Split by | and clean
            cells = [cell.strip() for cell in stripped.split("|")[1:-1]]
            table_rows.append(cells)
            continue

        # Finish table if we hit a non-table line
        if in_table:
            _render_table(pdf, table_rows)
            table_rows = []
            in_table = False

        # Handle bullet lists (only real list markers)
        is_bullet = bool(re.match(r"^[-*]\s+", stripped))
        
        # PROCESS INLINE FORMATTING (BOLD)
        parts = re.split(r'(\*\*.+?\*\*)', stripped)
        
        if is_bullet:
            pdf.set_x(pdf.l_margin + 5)
            pdf.write(7, "- ")
            # Remove the bullet marker from the first part
            if parts and parts[0]:
                parts[0] = re.sub(r"^[-*]\s+", "", parts[0]).strip()

        for part in parts:
            if part.startswith("**") and part.endswith("**"):
                pdf.set_font("Helvetica", "B", 11)
                pdf.write(7, part[2:-2])
                pdf.set_font("Helvetica", "", 11)
            else:
                pdf.set_font("Helvetica", "", 11)
                pdf.write(7, part)
        pdf.ln(7)

    # Finish any remaining table
    if in_table and table_rows:
        _render_table(pdf, table_rows)

    pdf_file.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(pdf_file))
    return str(pdf_file)


def _render_table(pdf: FPDF, rows: list[list[str]]) -> None:
    """Render a simple table in the PDF."""
    if not rows:
        return

    pdf.set_font("Helvetica", size=10)
    col_width = (pdf.w - 2 * pdf.l_margin) / len(rows[0]) if rows else 0

    # Header row
    pdf.set_fill_color(25, 118, 210)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 10)
    for cell in rows[0]:
        pdf.cell(col_width, 8, cell, 1, 0, "C", 1)
    pdf.ln()

    # Data rows
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", size=10)
    for row_idx, row in enumerate(rows[1:], 1):
        for col_idx, cell in enumerate(row):
            fill = row_idx % 2 == 0
            if fill:
                pdf.set_fill_color(240, 248, 255)
            for line in pdf.multi_cell(col_width, 6, cell, 1, "L", fill, split_only=True):
                pass
            # Simplified: just use cell for now
            pdf.cell(col_width, 6, cell[:30], 1, 0, "L", fill)
        pdf.ln()

    pdf.set_font("Helvetica", size=11)
    pdf.ln(3)


def _cli(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert Markdown to professional PDF (styled).")
    parser.add_argument("input", help="Ruta al archivo .md")
    parser.add_argument("output", help="Ruta de salida .pdf")
    parser.add_argument("--title", default=None, help="Título personalizado (opcional)")
    args = parser.parse_args(argv)

    result = md_to_pdf(args.input, args.output, title=args.title)
    print(f"PDF generado: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
