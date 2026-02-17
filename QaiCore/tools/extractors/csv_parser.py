"""
Extractor de datos de archivos CSV.

Dependencias: Solo usa librería estándar de Python (csv)
"""

import csv
from pathlib import Path
from typing import List, Dict, Any


def extract_data_from_csv(
    csv_path: str,
    delimiter: str = None,
    encoding: str = None,
    header_row: int = None,
    as_dict: bool = True
) -> Dict[str, Any]:
    """
    Extrae datos de un archivo CSV con detección inteligente.
    
    Args:
        csv_path: Ruta al archivo CSV
        delimiter: Delimitador (None = auto-detectar)
        encoding: Encoding (None = intentar utf-8 y fallback a latin-1)
        header_row: Índice de la fila de cabecera (None = auto-detectar)
        as_dict: Retornar con headers separados
        
    Returns:
        Dict con headers, rows y metadata
    """
    path = Path(csv_path)
    encodings = [encoding] if encoding else ['utf-8', 'latin-1', 'cp1252', 'utf-16']
    
    all_rows = []
    actual_encoding = 'utf-8'
    
    for enc in encodings:
        try:
            with open(csv_path, 'r', encoding=enc) as f:
                lines = f.readlines()
                
                # Pre-proceso: Limpiar líneas envueltas en comillas (típico de Banco Chile)
                # Si una línea empieza y termina con comillas y tiene delimitadores dentro,
                # las quitamos primero para no confundir al csv.reader
                cleaned_lines = []
                for line in lines:
                    line = line.strip()
                    if line.startswith('"') and line.endswith('"') and (';' in line or ',' in line):
                        # Quitar comillas externas y des-escapar comillas dobles internas
                        line = line[1:-1].replace('""', '"')
                    cleaned_lines.append(line)
                
                content = "\n".join(cleaned_lines)

                # Detectar delimitador si no se provee
                if delimiter is None:
                    sample = "\n".join(cleaned_lines[:5])
                    delimiter = ';' if sample.count(';') > sample.count(',') else ','
                
                # Usar csv module para parsear el contenido
                import io
                reader = csv.reader(io.StringIO(content), delimiter=delimiter)
                all_rows = list(reader)
                actual_encoding = enc
                break
        except Exception:
            continue
            
    if not all_rows:
        return {"error": "❌ No se pudo leer el archivo CSV (problema de encoding o vacío)"}

    # Detectar Header Row (similar a Excel)
    keywords = {'fecha', 'descripcion', 'descripción', 'monto', 'cargo', 'abono', 'saldo', 'total', 'rut', 'nro', 'detalle'}
    
    best_header_idx = 0
    max_matches = 0
    
    if header_row is None:
        for i, row in enumerate(all_rows[:20]): # Mirar primeras 20 filas
            row_str = [str(c).lower() for c in row if c is not None]
            matches = [k for k in keywords if any(k in cell for cell in row_str)]
            num_matches = len(matches)
            
            # Bonus si contiene 'fecha'
            if any('fecha' in s for s in row_str):
                num_matches += 2
                
            if num_matches > max_matches:
                max_matches = num_matches
                best_header_idx = i
        
        # Fallback si no hay matches
        if max_matches < 2:
            for i, row in enumerate(all_rows[:5]):
                if len([c for c in row if c and str(c).strip()]) > 2:
                    best_header_idx = i
                    break
        
        detected_header_idx = best_header_idx
    else:
        detected_header_idx = header_row

    headers_raw = all_rows[detected_header_idx]
    data_rows = all_rows[detected_header_idx + 1:]
    
    # Limpiar celdas vacías y filas finales
    while data_rows and (not data_rows[-1] or all(not str(c).strip() for c in data_rows[-1])):
        data_rows.pop()

    if as_dict:
        # Limpiar headers
        headers = []
        for i, h in enumerate(headers_raw):
            name = str(h).strip() if h is not None else f"Col_{i}"
            if name == "":
                name = f"Col_{i}"
            headers.append(name)
            
        return {
            "headers": headers,
            "rows": data_rows,
            "total_rows": len(data_rows),
            "delimiter": delimiter,
            "encoding": actual_encoding,
            "header_row_index": detected_header_idx
        }
    else:
        return all_rows


def csv_to_markdown_table(csv_path: str, max_rows: int = 50, **kwargs) -> str:
    """
    Convierte CSV a tabla Markdown.
    """
    data = extract_data_from_csv(csv_path, **kwargs)
    
    if "error" in data:
        return data["error"]
    
    headers = data["headers"]
    rows = data["rows"][:max_rows]
    
    md_lines = [
        f"# CSV: {Path(csv_path).name}",
        f"*(Detected {data['delimiter']} delimiter, {data['encoding']} encoding. Headers at row {data['header_row_index']})*",
        f"*(Showing {len(rows)} of {data['total_rows']} data rows)*\n",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |"
    ]
    
    for row in rows:
        # Limpiar strings de celdas (eliminar excesos de espacios o comillas duplicadas)
        clean_row = [str(c).replace('\n', ' ').strip() for c in row]
        md_lines.append("| " + " | ".join(clean_row) + " |")
    
    if data['total_rows'] > max_rows:
        md_lines.append(f"\n*... y {data['total_rows'] - max_rows} filas más*")
    
    return "\n".join(md_lines)


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
    
    data = extract_data_from_csv(csv_file)
    if "error" in data:
        print(data["error"])
        sys.exit(1)
        
    print(f"✅ Delimitador: '{data['delimiter']}' | Encoding: {data['encoding']}")
    print(f"✅ Cabecera en fila: {data['header_row_index']}")
    print(f"✅ Total filas: {data.get('total_rows', 0)}")
    
    print("\n" + "="*60)
    print("VISTA MARKDOWN (para agentes):")
    print("="*60)
    print(csv_to_markdown_table(csv_file, max_rows=15))

