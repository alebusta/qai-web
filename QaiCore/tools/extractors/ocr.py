"""
Extractor de texto de imágenes usando OCR con Gemini Vision API.

Dependencias: pip install google-genai pillow
"""

from PIL import Image
from pathlib import Path
import os


def extract_text_from_image(image_path: str, language: str = "auto") -> str:
    """
    Extrae texto de una imagen usando Gemini Vision API.
    
    Args:
        image_path: Ruta a la imagen (PNG, JPG, JPEG, etc.)
        language: Idioma esperado ("auto", "es", "en", etc.)
        
    Returns:
        Texto extraído de la imagen
    """
    try:
        from google import genai
        
        # Verificar API key
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            return "❌ Error: GEMINI_API_KEY no configurada. Configura la variable de entorno."
        
        # Verificar que el archivo existe
        if not Path(image_path).exists():
            return f"❌ Error: Imagen no encontrada: {image_path}"
        
        # Cargar imagen
        img = Image.open(image_path)
        
        # Crear cliente Gemini
        client = genai.Client(api_key=api_key)
        
        # Preparar prompt
        if language == "auto":
            prompt = """Extract ALL text from this image exactly as it appears.

Rules:
- Preserve line breaks and formatting
- Include ALL text visible in the image
- Return ONLY the extracted text, no explanations or descriptions
- If there's no text, return "NO TEXT FOUND"
"""
        else:
            prompt = f"""Extract ALL text from this image in {language}.

Rules:
- Preserve line breaks and formatting
- Include ALL text visible in the image
- Return ONLY the extracted text in {language}, no explanations
- If there's no text, return "NO TEXT FOUND"
"""
        
        # Llamar a Gemini Vision
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=[prompt, img]
        )
        
        return response.text
        
    except ImportError as e:
        missing = str(e).split("'")[1] if "'" in str(e) else "desconocida"
        return f"❌ Error: Librería faltante '{missing}'. Instala con: pip install google-genai pillow"
    except Exception as e:
        return f"❌ Error en OCR: {str(e)}"


def extract_text_from_multiple_images(image_paths: list[str]) -> dict[str, str]:
    """
    Extrae texto de múltiples imágenes.
    
    Args:
        image_paths: Lista de rutas a imágenes
        
    Returns:
        Dict con {ruta: texto_extraído}
    """
    results = {}
    total = len(image_paths)
    
    print(f"📸 Procesando {total} imágenes...")
    
    for i, img_path in enumerate(image_paths, 1):
        print(f"   [{i}/{total}] {Path(img_path).name}")
        results[img_path] = extract_text_from_image(img_path)
    
    return results


# Ejemplo de uso
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python ocr.py <ruta_imagen.png|jpg>")
        sys.exit(1)
    
    image_file = sys.argv[1]
    
    if not Path(image_file).exists():
        print(f"❌ Archivo no encontrado: {image_file}")
        sys.exit(1)
    
    print(f"📸 Extrayendo texto de: {image_file}")
    text = extract_text_from_image(image_file)
    
    print("\n" + "="*60)
    print("TEXTO EXTRAÍDO:")
    print("="*60)
    print(text)
    print("="*60)
    print(f"\n✅ Total extraído: {len(text)} caracteres")
