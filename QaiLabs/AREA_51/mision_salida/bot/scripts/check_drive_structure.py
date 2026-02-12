"""
Script para verificar la estructura de carpetas en Google Drive
y validar si se cumple el protocolo de "Clientes".
"""
import sys
import os
import json
import logging

# Set up paths
current_dir = os.path.dirname(os.path.abspath(__file__))
bot_dir = os.path.dirname(current_dir)
sys.path.insert(0, bot_dir)

# Load env variables manually from env.yaml (simple parser)
env_path = os.path.join(bot_dir, "env.yaml")
if os.path.exists(env_path):
    print(f"Loading env from {env_path}...")
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"): continue
            if ":" in line:
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip()
                # Remove outer quotes if present
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                os.environ[key] = val
else:
    print("⚠️ env.yaml not found!")

# Now import services
try:
    from services.gdrive_service import get_gdrive
except ImportError as e:
    print(f"Error importing services: {e}")
    sys.exit(1)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("check_structure")

def check_structure():
    print("\n🚀 Iniciando chequeo de estructura en Drive...\n")
    try:
        gdrive = get_gdrive()
    except Exception as e:
        print(f"❌ Error inicializando GDrive: {e}")
        return

    # 1. Listar ROOT
    root_id = gdrive._folder_map.get("root")
    print(f"📂 Listando ROOT ({root_id})...")
    
    try:
        root_files = gdrive.list_folder("root", max_results=30)
    except Exception as e:
        print(f"❌ Error listando root: {e}")
        return

    clientes_folder = None
    
    # Buscar carpeta "Clientes" o "Commercial"
    for f in root_files:
        name = f['name']
        fid = f['id']
        ftype = f['type']
        print(f"   • {name} [{ftype}]")
        
        if "cliente" in name.lower() and "carpeta" in ftype.lower():
            clientes_folder = f
            
    # Si no está en root, buscar globalmente
    if not clientes_folder:
        print("\n⚠️ Carpeta 'Clientes' no encontrada en root. Buscando globalmente...")
        results = gdrive.search_files("Clientes", max_results=5)
        for r in results:
             if "carpeta" in r['type'].lower():
                 clientes_folder = r
                 print(f"   ✅ Encontrada por búsqueda: {r['name']} ({r['id']})")
                 break

    if not clientes_folder:
        print("\n❌ NO se encontró carpeta de Clientes en Drive.")
        return

    # 2. Listar Clientes
    cid = clientes_folder['id']
    name = clientes_folder['name']
    print(f"\n📂 Analizando carpeta de Clientes: {name} ({cid})")
    
    # Hack: inyectar al mapa para poder usar list_folder
    gdrive._folder_map["_temp_clientes"] = cid
    
    clients = gdrive.list_folder("_temp_clientes", max_results=20)
    
    if not clients:
        print("   (Carpeta vacía)")
    
    for c in clients:
        if "carpeta" not in c['type'].lower():
            continue
            
        cname = c['name']
        cid = c['id']
        print(f"\n   👤 Cliente: {cname}")
        
        # 3. Chequear estructura interna
        key = f"_client_{cid}".lower()
        gdrive._folder_map[key] = cid
        subfolders = gdrive.list_folder(key, max_results=20)
        
        if subfolders and 'error' in subfolders[0]:
            print(f"      ❌ Error accediendo a cliente {cname}: {subfolders[0]['error']}")
            continue
            
        sub_names = [s['name'] for s in subfolders if 'name' in s]
        
        required = ["01", "02", "03"] # Buscamos prefijos
        found_map = {r: False for r in required}
        
        for s in sub_names:
            for r in required:
                if s.startswith(r):
                    found_map[r] = True
        
        missing = [r for r, found in found_map.items() if not found]
        
        if missing:
            print(f"      ⚠️ Faltan carpetas estándar: {missing}")
            print(f"      📂 Estructura actual: {sub_names}")
        else:
            print(f"      ✅ Estructura OK: {sub_names}")
            
        # 4. Chequear Propuestas/Cotizaciones en '02_entregas' (si existe)
        entregas_folder = next((s for s in subfolders if s['name'].startswith("02")), None)
        if entregas_folder:
            print(f"      📄 Revisando entregables en {entregas_folder['name']}...")
            gdrive._folder_map[f"_entregas_{cid}"] = entregas_folder['id']
            files = gdrive.list_folder(f"_entregas_{cid}", max_results=10)
            file_names = [f['name'] for f in files]
            if not file_names:
                print("         (Vacía)")
            else:
                for fn in file_names:
                    print(f"         - {fn}")

if __name__ == "__main__":
    check_structure()
