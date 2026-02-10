"""
Setup inicial de Google Drive para QAI Company
Crea la estructura de carpetas en Drive y guarda la configuración.
"""

import sys
import os
import importlib.util

# Cargar gdrive.py directamente sin pasar por __init__.py
spec = importlib.util.spec_from_file_location(
    "gdrive",
    r"c:\Users\abustamante\TheQaiCo\QaiCore\tools\gdrive.py"
)
gdrive_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gdrive_module)
gdrive = gdrive_module.gdrive

def setup_drive_structure():
    """
    Crea la estructura de carpetas en Google Drive.
    """
    print("🚀 Iniciando setup de Google Drive...")
    print("Si es la primera vez, se abrirá tu navegador para autenticar.\\n")
    
    try:
        # Crear carpeta raíz
        print("📁 Creando carpeta raíz...")
        qai_root = gdrive.create_folder('QAI Company - Administración y Finanzas')
        print(f"✅ Carpeta raíz creada: {qai_root['link']}\\n")
        
        # Crear estructura de Contabilidad
        print("📁 Creando estructura de Contabilidad...")
        contabilidad = gdrive.create_folder('Contabilidad', qai_root['id'])
        cont_2025 = gdrive.create_folder('2025', contabilidad['id'])
        cont_dic = gdrive.create_folder('12-Diciembre', cont_2025['id'])
        
        fact_recibidas = gdrive.create_folder('Facturas Recibidas', cont_dic['id'])
        fact_emitidas = gdrive.create_folder('Facturas Emitidas', cont_dic['id'])
        doc46_saas = gdrive.create_folder('Doc46 SaaS', cont_dic['id'])
        print("✅ Contabilidad creada\\n")
        
        # Crear estructura de Tributario
        print("📁 Creando estructura de Tributario...")
        tributario = gdrive.create_folder('Tributario', qai_root['id'])
        trib_2025 = gdrive.create_folder('2025', tributario['id'])
        trib_dic = gdrive.create_folder('12-Diciembre', trib_2025['id'])
        trib_anual = gdrive.create_folder('Anual', trib_2025['id'])
        print("✅ Tributario creado\\n")
        
        # Crear Documentos Legales
        print("📁 Creando Documentos Legales...")
        legales = gdrive.create_folder('Documentos Legales', qai_root['id'])
        escrituras = gdrive.create_folder('Escrituras', legales['id'])
        certificados = gdrive.create_folder('Certificados', legales['id'])
        print("✅ Documentos Legales creados\\n")
        
        # Guardar configuración
        config = {
            'root_folder_id': qai_root['id'],
            'root_link': qai_root['link'],
            
            # Contabilidad
            'contabilidad_id': contabilidad['id'],
            'contabilidad_2025_id': cont_2025['id'],
            'contabilidad_2025_12_id': cont_dic['id'],
            'facturas_recibidas_2025_12_id': fact_recibidas['id'],
            'facturas_emitidas_2025_12_id': fact_emitidas['id'],
            'doc46_saas_2025_12_id': doc46_saas['id'],
            
            # Tributario
            'tributario_id': tributario['id'],
            'tributario_2025_id': trib_2025['id'],
            'tributario_2025_12_id': trib_dic['id'],
            'tributario_2025_anual_id': trib_anual['id'],
            
            # Legales
            'legales_id': legales['id'],
            'escrituras_id': escrituras['id'],
            'certificados_id': certificados['id']
        }
        
        gdrive.save_config(config)
        print(f"💾 Configuración guardada en: c:\\Users\\abustamante\\.qai\\config\\gdrive_folders.json\\n")
        
        print("✅ Setup completado!")
        print(f"\\n📂 Carpeta raíz: {qai_root['link']}")
        print("\\n🎉 Ya puedes usar gdrive.upload_file() en tus agentes!\\n")
        
        return config
        
    except Exception as e:
        print(f"\\n❌ Error durante el setup: {str(e)}")
        print("\\nPor favor verifica:")
        print("1. Que credentials.json esté en: c:\\Users\\abustamante\\.qai\\gdrive\\credentials.json")
        print("2. Que tengas conexión a internet")
        print("3. Que hayas completado la autenticación en el navegador")
        raise

if __name__ == '__main__':
    setup_drive_structure()
