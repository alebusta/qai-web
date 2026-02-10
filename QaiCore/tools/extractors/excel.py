"""
Extractor de datos de archivos Excel (.xlsx, .xls).

Dependencias: pip install openpyxl xlrd
"""

import openpyxl
from pathlib import Path
from typing import Dict, List, Any


def extract_data_from_excel(
    excel_path: str,
    sheet_name: str = None,
    as_dict: bool = True
) -> Dict[str, Any] | List[List[Any]]:
    """
    Extrae datos de un archivo Excel.
    
    Args:
        excel_path: Ruta al archivo Excel
        sheet_name: Nombre de la hoja específica (None = hoja activa)
        as_dict: Si True, retorna {headers: [...], rows: [...]}, si False retorna lista de listas
        
    Returns:
        Datos extraídos en formato dict o lista según as_dict
    """
    try:
        workbook = openpyxl.load_workbook(excel_path, data_only=True)
        sheet = workbook[sheet_name] if sheet_name else workbook.active
        
        # Extraer todas las filas
        all_rows = list(sheet.iter_rows(values_only=True))
        
        # OMITIR FILAS VACÍAS AL INICIO (Metadata o headers vacíos)
        start_index = 0
        for i, row in enumerate(all_rows):
            if any(cell is not None and str(cell).strip() != "" for cell in row):
                start_index = i
                break
        
        filtered_rows = all_rows[start_index:]
        
        if not filtered_rows:
            return {"headers": [], "rows": []} if as_dict else []
        
        # Si queremos formato dict con headers
        if as_dict:
            # Usar la primera fila con datos como "probables headers"
            headers = [str(h) if h is not None else f"Col_{i}" for i, h in enumerate(filtered_rows[0])]
            data_rows = filtered_rows[1:]
            
            result = {
                "sheet_name": sheet.title,
                "headers": headers,
                "rows": data_rows,
                "total_rows": len(data_rows),
                "skipped_leading_rows": start_index
            }
            
            # Agregar info de otras hojas disponibles
            result["available_sheets"] = workbook.sheetnames
            
            return result
        else:
            return all_rows
            
    except Exception as e:
        error_msg = f"❌ Error extrayendo datos del Excel: {str(e)}"
        return {"error": error_msg} if as_dict else [[error_msg]]


def excel_to_markdown_table(excel_path: str, sheet_name: str = None, max_rows: int = 50) -> str:
    """
    Convierte Excel a tabla Markdown para fácil lectura por agentes IA.
    
    Args:
        excel_path: Ruta al archivo Excel
        sheet_name: Nombre de la hoja (None = activa)
        max_rows: Máximo de filas a incluir (para evitar output gigante)
        
    Returns:
        String con tabla en formato Markdown
    """
    data = extract_data_from_excel(excel_path, sheet_name)
    
    if isinstance(data, dict) and "error" in data:
        return data["error"]
    
    headers = data["headers"]
    rows = data["rows"][:max_rows]  # Limitar filas
    
    # Construir tabla Markdown
    md_lines = [
        f"# Sheet: {data['sheet_name']}",
        f"*(Mostrando {len(rows)} de {data['total_rows']} filas)*\n",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |"
    ]
    
    for row in rows:
        row_str = " | ".join(str(cell) if cell is not None else "" for cell in row)
        md_lines.append(f"| {row_str} |")
    
    if data['total_rows'] > max_rows:
        md_lines.append(f"\n*... y {data['total_rows'] - max_rows} filas más*")
    
    return "\n".join(md_lines)


# Ejemplo de uso
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python excel.py <ruta_archivo.xlsx> [nombre_hoja]")
        sys.exit(1)
    
    excel_file = sys.argv[1]
    sheet = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not Path(excel_file).exists():
        print(f"❌ Archivo no encontrado: {excel_file}")
        sys.exit(1)
    
    print(f"📊 Extrayendo datos de: {excel_file}")
    
    # Método 1: Como dict
    data = extract_data_from_excel(excel_file, sheet)
    print(f"\n✅ Hojas disponibles: {', '.join(data.get('available_sheets', []))}")
    print(f"✅ Hoja actual: {data.get('sheet_name', 'N/A')}")
    print(f"✅ Total filas: {data.get('total_rows', 0)}")
    
    # Método 2: Como Markdown (para agentes)
    print("\n" + "="*60)
    print("VISTA MARKDOWN (para agentes):")
    print("="*60)
    md_table = excel_to_markdown_table(excel_file, sheet, max_rows=10)
    print(md_table)
