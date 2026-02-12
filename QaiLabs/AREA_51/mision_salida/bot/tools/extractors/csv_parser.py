"""
Extractor de datos de archivos CSV.

Dependencias: Solo usa librería estándar de Python (csv)
"""

import csv
from pathlib import Path
from typing import List, Dict, Any


def extract_data_from_csv(
    csv_path: str,
    has_header: bool = True,
    delimiter: str = ',',
    encoding: str = 'utf-8'
) -> Dict[str, Any]:
    """
    Extrae datos de un archivo CSV.
    
    Args:
        csv_path: Ruta al archivo CSV
        has_header: Si True, la primera fila son headers
        delimiter: Delimitador usado (default: coma)
        encoding: Encoding del archivo (default: utf-8)
        
    Returns:
        Dict con headers y rows
    """
    try:
        with open(csv_path, 'r', encoding=encoding) as file:
            reader = csv.reader(file, delimiter=delimiter)
            all_rows = list(reader)
            
            if not all_rows:
                return {"headers": [], "rows": [], "total_rows": 0}
            
            if has_header:
                headers = all_rows[0]
                data_rows = all_rows[1:]
            else:
                # Generar headers genéricos
                num_cols = len(all_rows[0]) if all_rows else 0
                headers = [f"Col_{i+1}" for i in range(num_cols)]
                data_rows = all_rows
            
            return {
                "headers": headers,
                "rows": data_rows,
                "total_rows": len(data_rows)
            }
            
    except Exception as e:
        return {"error": f"❌ Error extrayendo datos del CSV: {str(e)}"}


def csv_to_markdown_table(csv_path: str, max_rows: int = 50, **kwargs) -> str:
    """
    Convierte CSV a tabla Markdown para fácil lectura por agentes IA.
    
    Args:
        csv_path: Ruta al archivo CSV
        max_rows: Máximo de filas a mostrar
        **kwargs: Parámetros adicionales para extract_data_from_csv
        
    Returns:
        String con tabla en formato Markdown
    """
    data = extract_data_from_csv(csv_path, **kwargs)
    
    if "error" in data:
        return data["error"]
    
    headers = data["headers"]
    rows = data["rows"][:max_rows]
    
    # Construir tabla Markdown
    md_lines = [
        f"# CSV: {Path(csv_path).name}",
        f"*(Mostrando {len(rows)} de {data['total_rows']} filas)*\n",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |"
    ]
    
    for row in rows:
        row_str = " | ".join(str(cell) for cell in row)
        md_lines.append(f"| {row_str} |")
    
    if data['total_rows'] > max_rows:
        md_lines.append(f"\n*... y {data['total_rows'] - max_rows} filas más*")
    
    return "\n".join(md_lines)


# Ejemplo de uso
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python csv_parser.py <ruta_archivo.csv>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    
    if not Path(csv_file).exists():
        print(f"❌ Archivo no encontrado: {csv_file}")
        sys.exit(1)
    
    print(f"📊 Extrayendo datos de: {csv_file}")
    
    # Método 1: Como dict
    data = extract_data_from_csv(csv_file)
    print(f"\n✅ Headers: {', '.join(data.get('headers', []))}")
    print(f"✅ Total filas: {data.get('total_rows', 0)}")
    
    # Método 2: Como Markdown
    print("\n" + "="*60)
    print("VISTA MARKDOWN (para agentes):")
    print("="*60)
    md_table = csv_to_markdown_table(csv_file, max_rows=10)
    print(md_table)
