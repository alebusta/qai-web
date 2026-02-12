"""
Extractor de texto de archivos PDF.
Usa OCR con Gemini Vision API si el PDF no tiene texto extraíble.

Dependencias: pip install pypdf2 google-genai pillow pdf2image
"""

try:
    from pypdf import PdfReader
except ImportError:
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        PdfReader = None
from pathlib import Path


def extract_text_from_pdf(pdf_path: str, use_ocr_if_needed: bool = True) -> str:
    """
    Extrae texto de un archivo PDF.
    
    Args:
        pdf_path: Ruta al archivo PDF
        use_ocr_if_needed: Si es True, usa OCR con Gemini si el PDF no tiene texto
        
    Returns:
        Texto extraído del PDF
    """
    try:
        if PdfReader is None:
            return "❌ Error: No se encontró una librería para leer PDF (pypdf o PyPDF2). Ejecuta: pip install pypdf"

        # Intentar extracción directa
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            text_parts = []
            
            for page in reader.pages:
                page_text = page.extract_text() or ""
                text_parts.append(page_text)
            
            full_text = "\n".join(text_parts)
            
            # Si encontramos texto, retornarlo
            if full_text.strip():
                return full_text
            
            # Si no hay texto y OCR está habilitado, usar OCR
            if use_ocr_if_needed:
                print(f"⚠️  PDF sin texto extraíble, usando OCR...")
                return _extract_with_ocr(pdf_path)
            else:
                return ""
                
    except Exception as e:
        return f"❌ Error extrayendo texto del PDF: {str(e)}"


def _extract_with_ocr(pdf_path: str) -> str:
    """
    Usa OCR para extraer texto de PDF mediante pdf2image + Tesseract.
    Fallback a Gemini si Tesseract no está disponible.
    """
    try:
        from pdf2image import convert_from_path
        import os
        import shutil
        import sys
        
        # 1. Configurar paths dinámicamente (Robustez QAI-tica)
        # Prioridad: 1. Variable de entorno 2. Búsqueda en sistema 3. Defaults conocidos
        
        # Poppler
        poppler_path = os.getenv('POPPLER_PATH')
        if not poppler_path:
            # Intentar encontrar en PATH
            if shutil.which('pdfinfo'):
                poppler_path = None # Usar PATH por defecto
            else:
                # Fallback común en Windows (QAI Environment)
                common_paths = [
                    r"C:\Program Files\poppler-24.08.0\Library\bin",
                    r"C:\Program Files\poppler\Library\bin"
                ]
                for p in common_paths:
                    if os.path.exists(p):
                        poppler_path = p
                        break
        
        # Tesseract
        tesseract_cmd = os.getenv('TESSERACT_CMD')
        if not tesseract_cmd:
             # Intentar encontrar en PATH
            if shutil.which('tesseract'):
                tesseract_cmd = 'tesseract'
            else:
                # Fallback común en Windows
                default_tess = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                if os.path.exists(default_tess):
                    tesseract_cmd = default_tess

        # 2. Ejecutar Conversión
        print("   Convirtiendo PDF a imagen...")
        try:
            # Si poppler_path es None, pdf2image usará el PATH del sistema
            images = convert_from_path(pdf_path, dpi=200, poppler_path=poppler_path)
            print(f"   ✅ Convertido a {len(images)} imagen(es)")
        except Exception as e:
            print(f"   ⚠️ Error en conversión pdf2image: {e}")
            raise e

        # 3. Intentar OCR con Tesseract (Nivel 2)
        try:
            import pytesseract
            
            if tesseract_cmd:
                pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
            
            print("   Extrayendo texto con Tesseract OCR...")
            all_text = []
            for i, img in enumerate(images, 1):
                if len(images) > 1:
                    print(f"      Procesando página {i}/{len(images)}...")
                
                page_text = pytesseract.image_to_string(img, lang='spa')
                
                if len(images) > 1:
                    all_text.append(f"--- Página {i} ---\n{page_text}")
                else:
                    all_text.append(page_text)
            
            return "\n\n".join(all_text)
            
        except (ImportError, Exception) as e:
            print(f"   ⚠️  Tesseract no disponible o falló: {e}")
            print("   Intentando con Gemini API...")
            
            # 4. Fallback a Gemini (Nivel 3)
            from google import genai
            
            api_key = os.getenv('GEMINI_API_KEY')
            if not api_key:
                return "❌ Error: Tesseract falló y GEMINI_API_KEY no configurada."
            
            client = genai.Client(api_key=api_key)
            
            all_text = []
            for i, img in enumerate(images, 1):
                print(f"      Procesando página {i}/{len(images)} con Gemini...")
                
                prompt = """Extract ALL text from this image exactly as it appears.
                
Rules:
- Preserve line breaks and formatting
- Include ALL text
- Return ONLY the extracted text, no explanations"""
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash-lite',
                    contents=[prompt, img]
                )
                
                page_text = response.text
                all_text.append(f"--- Página {i} ---\n{page_text}")
            
            return "\n\n".join(all_text)
        
    except ImportError as e:
        missing_lib = str(e).split("'")[1] if "'" in str(e) else "desconocida"
        return f"❌ Error: Librería faltante '{missing_lib}'. Instala con: pip install pdf2image pillow pytesseract"
    except Exception as e:
        return f"❌ Error en OCR: {str(e)}"


# Ejemplo de uso
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python pdf.py <ruta_archivo.pdf>")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    
    if not Path(pdf_file).exists():
        print(f"❌ Archivo no encontrado: {pdf_file}")
        sys.exit(1)
    
    print(f"📄 Extrayendo texto de: {pdf_file}")
    text = extract_text_from_pdf(pdf_file)
    
    print("\n" + "="*50)
    print(text[:500] + "..." if len(text) > 500 else text)
    print("="*50)
    print(f"\n✅ Total extraído: {len(text)} caracteres")
