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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Herramienta de utilidad para PDFs de QAI')
    subparsers = parser.add_subparsers(dest='command')

    # Subcomando: merge
    merge_parser = subparsers.add_parser('merge', help='Une múltiples PDFs')
    merge_parser.add_argument('inputs', nargs='+', help='Archivos PDF de entrada')
    merge_parser.add_argument('--output', '-o', required=True, help='Archivo PDF de salida')

    args = parser.parse_args()

    if args.command == 'merge':
        merge_pdfs(args.output, args.inputs)
    else:
        parser.print_help()
