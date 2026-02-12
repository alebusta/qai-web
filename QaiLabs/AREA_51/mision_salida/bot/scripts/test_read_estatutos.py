"""
Script para probar lectura de 'estatutos' en Drive.
"""
import sys
import os
import logging

# Set up paths
current_dir = os.path.dirname(os.path.abspath(__file__))
bot_dir = os.path.dirname(current_dir)
sys.path.insert(0, bot_dir)

# Load env variables manually
env_path = os.path.join(bot_dir, "env.yaml")
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line and not line.strip().startswith("#"):
                key, val = line.strip().split(":", 1)
                os.environ[key.strip()] = val.strip().strip("'").strip('"')

from services.gdrive_service import get_gdrive

logging.basicConfig(level=logging.INFO)

def test_read():
    print("\n🔍 Buscando 'estatutos' en Drive...\n")
    gdrive = get_gdrive()
    
    # 1. Buscar archivo
    results = gdrive.search_files("estatutos")
    
    if not results:
        print("❌ No encontrados.")
        return

    for r in results:
        print(f"📄 Encontrado: {r['name']}")
        print(f"🔗 Link: {r['link']}")
        print(f"ID: {r['id']}")
        print("-" * 20)

if __name__ == "__main__":
    test_read()
