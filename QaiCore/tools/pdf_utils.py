import argparse
import os
from pypdf import PdfWriter

def merge_pdfs(output_path, pdf_list):
    """
    Une múltiples archivos PDF en uno solo.
    """
    writer = PdfWriter()
    for pdf in pdf_list:
        if not os.path.exists(pdf):
            print(f"⚠️ Error: No se encontró el archivo {pdf}")
            continue
        print(f"[-] Añadiendo {os.path.basename(pdf)}...")
        writer.append(pdf)
    
    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"[+] PDF unido exitosamente: {output_path}")

def slice_pdf(input_path, output_path, start_page, end_page=None):
    """
    Extrae un rango de páginas de un PDF.
    Las páginas son 1-indexed (ej: 34).
    """
    from pypdf import PdfReader, PdfWriter
    
    if not os.path.exists(input_path):
        print(f"❌ Error: No se encontró el archivo {input_path}")
        return False
    
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    start_idx = max(0, start_page - 1)
    end_idx = min(total_pages, end_page) if end_page else total_pages
    
    print(f"[-] Rebanando {os.path.basename(input_path)} (pág. {start_page} a {end_idx})...")
    
    for i in range(start_idx, end_idx):
        writer.add_page(reader.pages[i])
        
    with open(output_path, "wb") as f:
        writer.write(f)
        
    print(f"[+] PDF rebanado exitosamente: {output_path} ({end_idx - start_idx} páginas)")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Herramienta de utilidad para PDFs de QAI')
    subparsers = parser.add_subparsers(dest='command')

    # Subcomando: merge
    merge_parser = subparsers.add_parser('merge', help='Une múltiples PDFs')
    merge_parser.add_argument('inputs', nargs='+', help='Archivos PDF de entrada')
    merge_parser.add_argument('--output', '-o', required=True, help='Archivo PDF de salida')

    # Subcomando: slice
    slice_parser = subparsers.add_parser('slice', help='Extract a page range from a PDF')
    slice_parser.add_argument('input', help='Archivo PDF de entrada')
    slice_parser.add_argument('--output', '-o', required=True, help='Archivo PDF de salida')
    slice_parser.add_argument('--start', type=int, required=True, help='Página inicial (1-indexed)')
    slice_parser.add_argument('--end', type=int, default=None, help='Página final (opcional)')

    args = parser.parse_args()

    if args.command == 'merge':
        merge_pdfs(args.output, args.inputs)
    elif args.command == 'slice':
        slice_pdf(args.input, args.output, args.start, args.end)
    else:
        parser.print_help()
