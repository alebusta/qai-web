"""
Procesador unificado de documentos.
Detecta automáticamente el tipo de archivo y extrae su contenido.

Este es el punto de entrada principal que los agentes deben usar.
"""

import sys
import os
from pathlib import Path
from typing import Union, Dict, Any

# Asegurar que el directorio raíz de la herramienta esté en el path
tools_dir = os.path.dirname(os.path.abspath(__file__))
if tools_dir not in sys.path:
    sys.path.insert(0, tools_dir)

# Importar extractores usando la estructura de subcarpetas
try:
    from extractors.pdf import extract_text_from_pdf
    from extractors.docx_extractor import extract_text_from_docx
    from extractors.pptx import extract_text_from_pptx
    from extractors.excel import extract_data_from_excel, excel_to_markdown_table
    from extractors.csv_parser import extract_data_from_csv, csv_to_markdown_table
    from extractors.ocr import extract_text_from_image
except ImportError:
    # Fallback para cuando se importa como parte de un paquete QaiCore
    from .extractors.pdf import extract_text_from_pdf
    from .extractors.docx_extractor import extract_text_from_docx
    from .extractors.pptx import extract_text_from_pptx
    from .extractors.excel import extract_data_from_excel, excel_to_markdown_table
    from .extractors.csv_parser import extract_data_from_csv, csv_to_markdown_table
    from .extractors.ocr import extract_text_from_image


def extract_content(
    file_path: str,
    format_for_llm: bool = False,
    **kwargs
) -> Union[str, Dict[str, Any]]:
    """
    Extrae contenido de cualquier archivo soportado.
    
    Formatos soportados:
    - PDF (.pdf)
    - Word (.docx)
    - PowerPoint (.pptx)
    - Excel (.xlsx, .xls)
    - CSV (.csv)
    - Imágenes (.png, .jpg, .jpeg, .gif, .bmp)
    
    Args:
        file_path: Ruta al archivo
        format_for_llm: Si True, retorna formato optimizado para LLMs (texto/markdown)
        **kwargs: Argumentos adicionales específicos del extractor
        
    Returns:
        - Para texto (PDF, DOCX, PPTX, imágenes): str
        - Para datos (Excel, CSV): dict (o str si format_for_llm=True)
        
    Example:
        >>> content = extract_content("contrato.pdf")
        >>> content = extract_content("datos.xlsx", format_for_llm=True)  # Retorna markdown
    """
    path = Path(file_path)
    
    if not path.exists():
        return f"❌ Error: Archivo no encontrado: {file_path}"
    
    extension = path.suffix.lower()
    
    # Mapeo de extensiones a extractores
    extractors = {
        '.pdf': lambda: extract_text_from_pdf(file_path, **kwargs),
        '.docx': lambda: extract_text_from_docx(file_path),
        '.pptx': lambda: extract_text_from_pptx(file_path),
        '.xlsx': lambda: excel_to_markdown_table(file_path, **kwargs) if format_for_llm 
                        else extract_data_from_excel(file_path, **kwargs),
        '.xls': lambda: excel_to_markdown_table(file_path, **kwargs) if format_for_llm 
                       else extract_data_from_excel(file_path, **kwargs),
        '.csv': lambda: csv_to_markdown_table(file_path, **kwargs) if format_for_llm 
                       else extract_data_from_csv(file_path, **kwargs),
        '.png': lambda: extract_text_from_image(file_path, **kwargs),
        '.jpg': lambda: extract_text_from_image(file_path, **kwargs),
        '.jpeg': lambda: extract_text_from_image(file_path, **kwargs),
        '.gif': lambda: extract_text_from_image(file_path, **kwargs),
        '.bmp': lambda: extract_text_from_image(file_path, **kwargs),
    }
    
    # Verificar si el formato es soportado
    if extension not in extractors:
        supported = ', '.join(extractors.keys())
        return f"❌ Error: Formato '{extension}' no soportado. Soportados: {supported}"
    
    # Ejecutar extractor correspondiente
    try:
        print(f"📄 Detectado: {extension.upper()[1:]} → Extrayendo contenido...")
        result = extractors[extension]()
        return result
    except Exception as e:
        return f"❌ Error procesando {extension}: {str(e)}"


def get_file_info(file_path: str) -> Dict[str, Any]:
    """
    Obtiene información sobre un archivo sin extraer todo el contenido.
    Útil para validación rápida.
    
    Args:
        file_path: Ruta al archivo
        
    Returns:
        Dict con metadata del archivo
    """
    path = Path(file_path)
    
    if not path.exists():
        return {"error": "Archivo no encontrado"}
    
    info = {
        "name": path.name,
        "extension": path.suffix.lower(),
        "size_bytes": path.stat().st_size,
        "size_mb": round(path.stat().st_size / (1024 * 1024), 2),
        "is_supported": path.suffix.lower() in [
            '.pdf', '.docx', '.pptx', '.xlsx', '.xls', '.csv',
            '.png', '.jpg', '.jpeg', '.gif', '.bmp'
        ]
    }
    
    return info


# Ejemplo de uso
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python document_processor.py <ruta_archivo>")
        print("\nFormatos soportados:")
        print("  - Texto: PDF, DOCX, PPTX")
        print("  - Datos: XLSX, XLS, CSV")
        print("  - Imágenes: PNG, JPG, JPEG, GIF, BMP")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Mostrar info del archivo
    print("="*60)
    print("INFORMACIÓN DEL ARCHIVO")
    print("="*60)
    info = get_file_info(file_path)
    for key, value in info.items():
        print(f"{key}: {value}")
    
    # Extraer contenido
    print("\n" + "="*60)
    print("EXTRAYENDO CONTENIDO...")
    print("="*60 + "\n")
    
    content = extract_content(file_path, format_for_llm=True)
    
    # Mostrar resultado (limitado si es muy largo)
    if isinstance(content, str):
        preview = content[:1000] + "..." if len(content) > 1000 else content
        print(preview)
        print(f"\n✅ Total extraído: {len(content)} caracteres")
    else:
        print(content)
