"""
Script de validación para la Fase 3: Document Intelligence.
Prueba la descarga, extracción y análisis de un archivo real de Drive.
"""
import os
import sys
import logging

# Configurar path para imports
# Estamos en AREA_51/mision_salida/bot/scripts/test_phase3.py
# El root del bot es AREA_51/mision_salida/bot
scripts_dir = os.path.dirname(os.path.abspath(__file__))
bot_dir = os.path.dirname(scripts_dir)
mision_salida_dir = os.path.dirname(bot_dir)

if bot_dir not in sys.path:
    sys.path.insert(0, bot_dir)
if mision_salida_dir not in sys.path:
    sys.path.insert(0, mision_salida_dir)

# Cargar variables de entorno desde env.yaml
try:
    import yaml
    env_path = os.path.join(bot_dir, "env.yaml")
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            envs = yaml.safe_load(f)
            if envs:
                for key, value in envs.items():
                    os.environ[key] = str(value)
                print("✅ Variables de entorno cargadas desde env.yaml")
except ImportError:
    print("⚠️ PyYAML no instalado. No se cargaron variables de env.yaml")
except Exception as e:
    print(f"⚠️ Error cargando env.yaml: {e}")

from services.doc_intelligence_service import get_doc_intelligence

# Configurar logging básico para ver el progreso
logging.basicConfig(level=logging.INFO)

def test_analysis():
    print("\n🚀 Iniciando Prueba de Inteligencia de Documentos...\n")
    
    # ID del NDA de FedEx (Legal)
    test_file_id = "1CGHt_iKawXIClrDloM15Cz67Hmf3p7tK"
    
    doc_int = get_doc_intelligence()
    
    print(f"🔹 Solicitando análisis para el archivo ID: {test_file_id}...")
    result = doc_int.analyze_drive_file(test_file_id)
    
    print("\n" + "="*60)
    print("RESULTADO DEL ANÁLISIS")
    print("="*60)
    print(result)
    print("="*60 + "\n")

if __name__ == "__main__":
    test_analysis()
