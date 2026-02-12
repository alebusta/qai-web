"""
Script de Estandarización de Estructura de Clientes en Drive (QaiCore)
----------------------------------------------------------------------
Aplica el protocolo de carpetas (01, 02, 03) a los clientes listados.
Usa la herramienta oficial `QaiCore.tools.gdrive`.

Uso:
    python QaiCore/scripts/standardize_clients.py
"""
import sys
import os
import time

# Add QaiCore to path
current_dir = os.path.dirname(os.path.abspath(__file__))
qaicore_dir = os.path.dirname(current_dir)
sys.path.insert(0, qaicore_dir)

from tools.gdrive import get_gdrive

def ensure_client_structure(gdrive, client_name):
    print(f"\n🔹 Verificando Cliente: {client_name}")
    
    # Obtener ID de carpeta raiz "Clientes"
    # Nota: Hardcodeado por ahora o leer de config json
    # ID Clientes: 1g_uGZn3qge52z0oH_8ta_BcpkC-QTMGi
    CLIENTES_ROOT_ID = "1g_uGZn3qge52z0oH_8ta_BcpkC-QTMGi"

    # 1. Buscar carpeta del cliente
    # Nota: El metodo list_files de gdrive.py retorna lista.
    results = gdrive.list_files(CLIENTES_ROOT_ID, query=f"name = '{client_name}' and mimeType = 'application/vnd.google-apps.folder'")
    
    if results:
        client_id = results[0]['id']
        print(f"   ✅ Carpeta cliente existe: {client_id}")
    else:
        print(f"   🆕 Creando carpeta cliente...")
        res = gdrive.create_folder(client_name, parent_folder_id=CLIENTES_ROOT_ID)
        client_id = res['id']
        print(f"   ✅ Carpeta creada: {client_id}")

    # 2. Verificar subcarpetas
    SUBFOLDERS = ["01_insumos", "02_entregas", "03_gestion"]
    
    # Listar contenido actual
    current_subs = gdrive.list_files(client_id, query="mimeType = 'application/vnd.google-apps.folder'")
    existing_names = [f['name'] for f in current_subs]

    for sub in SUBFOLDERS:
        if sub in existing_names:
            print(f"      OK: {sub}")
        else:
            print(f"      🛠️ Creando: {sub}")
            gdrive.create_folder(sub, parent_folder_id=client_id)

def main():
    print("🚀 QAI Standardizer - Protocolo Drive Clientes")
    
    gdrive = get_gdrive()
    
    # Lista de Clientes Activos/Prospectos
    CLIENTES = ["FedEx", "CIAL Alimentos", "GestionZen"]

    for client in CLIENTES:
        try:
            ensure_client_structure(gdrive, client)
        except Exception as e:
            print(f"❌ Error en {client}: {e}")
        
    print("\n🏁 Proceso finalizado.")

if __name__ == "__main__":
    main()
