"""
Script de prueba para verificar que Google Drive funciona correctamente
"""

import sys
import importlib.util

# Cargar gdrive.py directamente
spec = importlib.util.spec_from_file_location(
    "gdrive",
    r"c:\Users\abustamante\TheQaiCo\QaiCore\tools\gdrive.py"
)
gdrive_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gdrive_module)
gdrive = gdrive_module.gdrive

print("🧪 Probando upload a Google Drive...")
print(f"Carpetas configuradas: {len(gdrive.folders)} carpetas\\n")

# Subir archivo de prueba
try:
    result = gdrive.upload_file(
        local_path='test_upload.txt',
        drive_folder_id=gdrive.folders['facturas_recibidas_2025_12_id'],
        description='Archivo de prueba - Setup Google Drive API'
    )
    
    print("✅ Upload exitoso!")
    print(f"📄 Nombre: {result['name']}")
    print(f"🔗 Link: {result['link']}")
    print(f"🆔 File ID: {result['id']}")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
