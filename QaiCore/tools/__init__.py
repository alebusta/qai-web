"""
QaiCore Tools - Herramientas compartidas para agentes IA.
"""

from .document_processor import extract_content, get_file_info
from .extractors.pdf import extract_text_from_pdf
from .extractors.docx_extractor import extract_text_from_docx
from .extractors.pptx import extract_text_from_pptx
from .extractors.excel import extract_data_from_excel, excel_to_markdown_table
from .extractors.csv_parser import extract_data_from_csv, csv_to_markdown_table
from .extractors.ocr import extract_text_from_image

# md_to_pdf (FPDF) es opcional: no debe romper la importación del paquete tools.
try:
    from .md_to_pdf import md_to_pdf
except ModuleNotFoundError:  # pragma: no cover
    def md_to_pdf(*args, **kwargs):  # type: ignore
        raise RuntimeError(
            "md_to_pdf requiere la dependencia opcional 'fpdf' (recomendado: 'fpdf2'). "
            "Instala con: pip install fpdf2"
        )


def render_email_html(*args, **kwargs):  # type: ignore
    from .render_email import render_email_html as _impl

    return _impl(*args, **kwargs)


def md_proposal_to_pdf(*args, **kwargs):  # type: ignore
    from .proposal_pdf import md_proposal_to_pdf as _impl

    return _impl(*args, **kwargs)


def GmailToolWithPreview(*args, **kwargs):  # type: ignore
    from .gmail_preview import GmailToolWithPreview as _impl

    return _impl(*args, **kwargs)
from .time_utils import (
    get_current_datetime,
    get_current_context,
    calculate_task_urgency,
    prioritize_tasks,
    format_task_with_urgency
)

__all__ = [
    # Función principal (recomendada para agentes)
    'extract_content',
    'get_file_info',
    
    # Extractores específicos (uso avanzado)
    'extract_text_from_pdf',
    'extract_text_from_docx',
    'extract_text_from_pptx',
    'extract_data_from_excel',
    'excel_to_markdown_table',
    'extract_data_from_csv',
    'csv_to_markdown_table',
    'extract_text_from_image',
    'md_to_pdf',
    'render_email_html',
    'md_proposal_to_pdf',
    'GmailToolWithPreview',
    
    # Utilidades de tiempo
    'get_current_datetime',
    'get_current_context',
    'calculate_task_urgency',
    'prioritize_tasks',
    'format_task_with_urgency',
]
