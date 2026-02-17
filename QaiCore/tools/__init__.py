"""
QaiCore Tools - Herramientas compartidas para agentes IA.
"""

# Función de conveniencia para carga perezosa
def _lazy_import(module_name: str, func_name: str):
    import importlib
    module = importlib.import_module(module_name)
    return getattr(module, func_name)

def extract_content(*args, **kwargs):
    return _lazy_import(".document_processor", "extract_content")(*args, **kwargs)

def get_file_info(*args, **kwargs):
    return _lazy_import(".document_processor", "get_file_info")(*args, **kwargs)

def extract_text_from_pdf(*args, **kwargs):
    return _lazy_import(".extractors.pdf", "extract_text_from_pdf")(*args, **kwargs)

def extract_text_from_docx(*args, **kwargs):
    return _lazy_import(".extractors.docx_extractor", "extract_text_from_docx")(*args, **kwargs)

def extract_text_from_pptx(*args, **kwargs):
    return _lazy_import(".extractors.pptx", "extract_text_from_pptx")(*args, **kwargs)

def extract_data_from_excel(*args, **kwargs):
    return _lazy_import(".extractors.excel", "extract_data_from_excel")(*args, **kwargs)

def excel_to_markdown_table(*args, **kwargs):
    return _lazy_import(".extractors.excel", "excel_to_markdown_table")(*args, **kwargs)

def extract_data_from_csv(*args, **kwargs):
    return _lazy_import(".extractors.csv_parser", "extract_data_from_csv")(*args, **kwargs)

def csv_to_markdown_table(*args, **kwargs):
    return _lazy_import(".extractors.csv_parser", "csv_to_markdown_table")(*args, **kwargs)

def extract_text_from_image(*args, **kwargs):
    return _lazy_import(".extractors.ocr", "extract_text_from_image")(*args, **kwargs)


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
