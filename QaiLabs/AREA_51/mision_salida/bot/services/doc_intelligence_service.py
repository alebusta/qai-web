"""
QAI HQ Bot — Document Intelligence Service
Combina GDrive, QaiCore Extractors y LLM para analizar documentos.
"""
import os
import logging
import sys
from typing import Dict, Any

# Asegurar que QaiCore esté en el path para los extractores
# El bot está en AREA_51/mision_salida/bot
# QaiCore está en la raíz: ../../../QaiCore
current_dir = os.path.dirname(os.path.abspath(__file__))
qaicore_dir = os.path.abspath(os.path.join(current_dir, "../../../../../QaiCore"))
if qaicore_dir not in sys.path:
    sys.path.insert(0, qaicore_dir)

logger = logging.getLogger(__name__)

class DocIntelligenceService:
    def __init__(self):
        from services.gdrive_service import get_gdrive
        from services.llm_provider import get_llm
        self._gdrive = get_gdrive()
        self._llm = get_llm()
        
    def analyze_drive_file(self, file_id: str, chat_id: int) -> str:
        """
        Descarga, extrae y analiza un archivo de Drive.
        """
        from services.state_service import get_state
        state = get_state()

        # 1. Obtener metadata
        meta = self._gdrive.get_file_metadata(file_id)
        if not meta:
            return "❌ No pude encontrar la información del archivo en Drive."
            
        file_name = meta.get("name")
        mime_type = meta.get("mimeType")
        
        logger.info("🧠 Analizando archivo: %s (%s)", file_name, file_id)
        
        # 2. Descargar a temporal
        temp_path = os.path.join(os.getcwd(), "temp_files")
        os.makedirs(temp_path, exist_ok=True)
        local_file = os.path.join(temp_path, file_name)
        
        success = self._gdrive.download_file(file_id, local_file)
        if not success:
            return f"❌ Falló la descarga del archivo '{file_name}'."
            
        try:
            # 3. Extraer contenido usando QaiCore
            from tools.document_processor import extract_content
            
            content = extract_content(local_file, format_for_llm=True)
            
            if not content or (isinstance(content, str) and content.startswith("❌")):
                return f"⚠️ No pude extraer texto de '{file_name}': {content}"
            
            # 4. Analizar con LLM
            prompt = f"""Analiza el siguiente documento extraído de Google Drive.
Nombre: {file_name}
Tipo: {mime_type}

Contenido:
{content[:5000]}

Instrucción:
1. Clasifica el documento como: 'LEGAL', 'FINANCIERO', 'COMERCIAL' o 'GENERAL'.
2. Haz un resumen ejecutivo corto (máximo 150 palabras). 
3. Identifica puntos clave, fechas importantes o montos si aplica.

Responde en este formato:
CATEGORIA: [CATEGORIA]
RESUMEN: [RESUMEN]
"""
            analysis_text = self._llm.chat(prompt, system_instruction="Eres Nzero, el COO digital de QAI.")
            
            # 5. Interpretar sugerencia de agente
            suggestion = ""
            category = "GENERAL"
            if "CATEGORIA: LEGAL" in analysis_text:
                category = "LEGAL"
                suggestion = "\n\n⚖️ **Sugerencia**: Este documento es de naturaleza legal. ¿Deseas que llame a **Lex** para un análisis jurídico profundo?"
            elif "CATEGORIA: FINANCIERO" in analysis_text:
                category = "FINANCIERO"
                suggestion = "\n\n💰 **Sugerencia**: Este archivo tiene contenido financiero. ¿Debería consultar con **Finn** sobre los números?"
            elif "CATEGORIA: COMERCIAL" in analysis_text:
                category = "COMERCIAL"

            # Limpiar el tag CATEGORIA de la respuesta final para el usuario
            final_resp = analysis_text.replace("CATEGORIA:", "📁 **Categoría**:").replace("RESUMEN:", "📝 **Resumen**:")
            
            # 6. GUARDAR CONTEXTO EN ESTADO
            from datetime import datetime
            doc_context = {
                "file_name": file_name,
                "category": category,
                "analysis": analysis_text,
                "timestamp": datetime.now().isoformat()
            }
            state.set_user_state(chat_id, "last_document_context", doc_context)
            logger.info("💾 Contexto de documento guardado para %s", chat_id)

            # Limpieza
            try:
                os.remove(local_file)
            except:
                pass
                
            return f"✅ **Análisis de: {file_name}**\n\n{final_resp}{suggestion}"
            
        except Exception as e:
            logger.error("❌ Error en análisis de documento: %s", e)
            return f"❌ Error crítico procesando '{file_name}': {str(e)}"

# Singleton
_doc_intelligence_instance = None

def get_doc_intelligence() -> DocIntelligenceService:
    global _doc_intelligence_instance
    if _doc_intelligence_instance is None:
        _doc_intelligence_instance = DocIntelligenceService()
    return _doc_intelligence_instance
