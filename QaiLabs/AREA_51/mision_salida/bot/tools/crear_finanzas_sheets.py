"""
Script para crear el sistema completo de Google Sheets financiero de QAI.
Crea todas las hojas con estructura base, headers y fórmulas iniciales.

Uso desde raíz:
    .\QaiCore\qrun.bat .\QaiCore\tools\crear_finanzas_sheets.py

Uso desde QaiCore/:
    .\qrun.bat .\tools\crear_finanzas_sheets.py
"""

import sys
import os
from pathlib import Path

# Determinar el directorio base
script_dir = Path(__file__).parent.absolute()
tools_dir = script_dir
qaicore_dir = tools_dir.parent

# Agregar directorios al path
sys.path.insert(0, str(tools_dir))
sys.path.insert(0, str(qaicore_dir))

from googleapiclient.discovery import build

# Usar gdrive para obtener credenciales
try:
    # Importar gdrive directamente
    import importlib.util
    gdrive_path = tools_dir / 'gdrive.py'
    spec = importlib.util.spec_from_file_location("gdrive", gdrive_path)
    gdrive_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gdrive_module)
    
    gdrive = gdrive_module.gdrive
    creds = gdrive.creds
    sheets_service = build('sheets', 'v4', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)
    
except Exception as e:
    print(f"❌ Error inicializando servicios: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

def crear_sistema_financiero():
    """
    Crea el spreadsheet completo con todas las hojas necesarias.
    """
    
    # 1. Crear spreadsheet principal
    print("📊 Creando spreadsheet principal...")
    spreadsheet = {
        'properties': {
            'title': 'QAI_Finanzas_2026'
        }
    }
    spreadsheet = sheets_service.spreadsheets().create(
        body=spreadsheet,
        fields='spreadsheetId,spreadsheetUrl'
    ).execute()
    
    spreadsheet_id = spreadsheet.get('spreadsheetId')
    spreadsheet_url = spreadsheet.get('spreadsheetUrl')
    
    print(f"✅ Spreadsheet creado: {spreadsheet_url}")
    print(f"   ID: {spreadsheet_id}")
    
    # 2. Crear nuestras hojas y eliminar la por defecto
    print("\n📝 Creando hojas del sistema...")
    
    # Obtener metadatos para identificar la hoja por defecto
    spreadsheet_metadata = sheets_service.spreadsheets().get(
        spreadsheetId=spreadsheet_id
    ).execute()
    default_sheet_id = spreadsheet_metadata['sheets'][0]['properties']['sheetId']
    
    # Definir todas las hojas a crear
    sheets_to_create = [
        {'title': 'Registro_Diario', 'index': 0},
        {'title': 'Runway', 'index': 1},
        {'title': 'PyL', 'index': 2},
        {'title': 'Prestamos_Socio', 'index': 3},
        {'title': 'Control_Facturacion', 'index': 4},
        {'title': 'Costos_Proyecto', 'index': 5}
    ]
    
    # Preparar requests: Agregar hojas nuevas + Eliminar la por defecto al final
    requests = [{
        'addSheet': {
            'properties': {
                'title': sheet['title'],
                'index': sheet['index']
            }
        }
    } for sheet in sheets_to_create]
    
    # Agregar el request de borrado de la hoja inicial
    requests.append({
        'deleteSheet': {'sheetId': default_sheet_id}
    })
    
    sheets_service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={'requests': requests}
    ).execute()
    
    print("✅ Hojas creadas (y default eliminada)")
    
    # 3. Configurar estructura de cada hoja
    print("\n📋 Configurando estructura de hojas...")
    
    # Hoja 1: Registro Diario
    print("   → Registro Diario...")
    headers_registro = [
        ['Fecha', 'Tipo', 'Concepto', 'Categoría FinOps', 'Cuenta Contable', 
         'Monto Neto', 'IVA', 'Monto Bruto', 'Proyecto', 'Comprobante', 'Estado', 'Notas']
    ]
    
    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range='Registro_Diario!A1:L1',
        valueInputOption='USER_ENTERED',
        body={'values': headers_registro}
    ).execute()
    
    # Agregar fila de totales (fila 2)
    formulas_registro = [
        ['', 'TOTALES', '', '', '', 
         '=SUM(F3:F)', '=SUM(G3:G)', '=SUM(H3:H)', '', '', '', '']
    ]
    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range='Registro_Diario!A2:L2',
        valueInputOption='USER_ENTERED',
        body={'values': formulas_registro}
    ).execute()
    
    # Hoja 2: Runway
    print("   → Runway...")
    headers_runway = [
        ['Resumen Ejecutivo'],
        ['Saldo Actual:', ''],
        ['Burn Rate Mensual:', ''],
        ['Runway (meses):', ''],
        ['Última actualización:', ''],
        [''],
        ['Mes', 'Saldo Inicial', 'Ingresos - Invoice Match', 'Ingresos - Otros SaaS', 
         'Ingresos - Consultoría', 'Ingresos - Capacitación', 'Préstamos Socio', 
         'Total Ingresos', 'Gastos Fijos', 'Costos Variables - Invoice Match', 
         'Costos Variables - Gestión Zen', 'Costos Variables - R&D', 'Comisiones', 
         'Otros Gastos', 'Total Egresos', 'Flujo Neto', 'Saldo Final', 'Runway (meses)']
    ]
    
    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range='Runway!A1:R8',
        valueInputOption='USER_ENTERED',
        body={'values': headers_runway}
    ).execute()
    
    # Hoja 3: P&L
    print("   → P&L...")
    headers_pyl = [
        ['INGRESOS OPERACIONALES', 'Ene', 'Feb', 'Mar', 'Acum Q1'],
        ['Invoice Match', '', '', '', ''],
        ['Otros SaaS', '', '', '', ''],
        ['Consultoría', '', '', '', ''],
        ['Capacitación', '', '', '', ''],
        ['TOTAL INGRESOS', '=SUM(B2:B5)', '=SUM(C2:C5)', '=SUM(D2:D5)', '=SUM(E2:E5)'],
        [''],
        ['COSTOS DIRECTOS (COGS)', '', '', '', ''],
        ['Invoice Match', '', '', '', ''],
        ['Otros SaaS', '', '', '', ''],
        ['Consultoría', '', '', '', ''],
        ['Capacitación', '', '', '', ''],
        ['TOTAL COSTOS DIRECTOS', '=SUM(B9:B12)', '=SUM(C9:C12)', '=SUM(D9:D12)', '=SUM(E9:E12)'],
        ['MARGEN BRUTO', '=B6-B13', '=C6-C13', '=D6-D13', '=E6-E13'],
        ['% MARGEN BRUTO', '=SI(B6>0, B14/B6*100, 0)', '=SI(C6>0, C14/C6*100, 0)', '=SI(D6>0, D14/D6*100, 0)', '=SI(E6>0, E14/E6*100, 0)'],
        [''],
        ['GASTOS OPERACIONALES', '', '', '', ''],
        ['Gastos Fijos', '180200', '180200', '180200', '=SUM(B18:D18)'],
        ['Gastos R&D', '', '', '', ''],
        ['Comisiones', '', '', '', ''],
        ['TOTAL GASTOS OPEX', '=SUM(B18:B20)', '=SUM(C18:C20)', '=SUM(D18:D20)', '=SUM(E18:E20)'],
        [''],
        ['RESULTADO OPERACIONAL', '=B14-B21', '=C14-C21', '=D14-D21', '=E14-E21'],
        ['RESULTADO NETO', '=B23', '=C23', '=D23', '=E23']
    ]
    
    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range='PyL!A1:E24',
        valueInputOption='USER_ENTERED',
        body={'values': headers_pyl}
    ).execute()
    
    # Hoja 4: Préstamos del Socio
    print("   → Préstamos del Socio...")
    headers_prestamos = [
        ['Resumen Ejecutivo'],
        ['Total Prestado:', ''],
        ['Total Devuelto:', ''],
        ['Saldo Pendiente:', ''],
        ['Última actualización:', ''],
        [''],
        ['Fecha', 'Concepto', 'Monto', 'Saldo Acumulado', 'Fecha Devolución', 
         'Monto Devolución', 'Saldo Pendiente', 'Notas']
    ]
    
    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range='Prestamos_Socio!A1:H7',
        valueInputOption='USER_ENTERED',
        body={'values': headers_prestamos}
    ).execute()
    
    # Hoja 5: Control de Facturación
    print("   → Control de Facturación...")
    headers_facturacion = [
        ['Número', 'Fecha Emisión', 'Cliente', 'Producto/Servicio', 'Período', 
         'Monto Neto', 'IVA', 'Monto Bruto', 'Estado Cobranza', 'Fecha Vencimiento', 
         'Fecha Pago', 'Link Factura', 'Notas']
    ]
    
    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range='Control_Facturacion!A1:M1',
        valueInputOption='USER_ENTERED',
        body={'values': headers_facturacion}
    ).execute()
    
    # Hoja 6: Costos por Proyecto
    print("   → Costos por Proyecto...")
    headers_costos = [
        ['INVOICE MATCH'],
        ['Concepto', 'Mes Actual', 'Mes Anterior', 'Promedio 3M', 'Notas'],
        ['Gemini API', '', '', '', ''],
        ['Supabase', '23750', '23750', '23750', '$25 USD/mes fijo'],
        ['Otros', '', '', '', ''],
        ['TOTAL', '=SUM(B3:B5)', '=SUM(C3:C5)', '=SUM(D3:D5)', ''],
        [''],
        ['GESTIÓN ZEN'],
        ['Concepto', 'Mes Actual', 'Mes Anterior', 'Promedio 3M', 'Notas'],
        ['Groq API', '', '', '', ''],
        ['Gemini API', '', '', '', ''],
        ['Supabase', '23750', '23750', '23750', '$25 USD/mes fijo'],
        ['TOTAL', '=SUM(B10:B12)', '=SUM(C10:C12)', '=SUM(D10:D12)', '']
    ]
    
    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range='Costos_Proyecto!A1:E13',
        valueInputOption='USER_ENTERED',
        body={'values': headers_costos}
    ).execute()
    
    print("✅ Estructura configurada")
    
    # 4. Mover a carpeta de Finanzas en Drive
    print("\n📁 Moviendo a carpeta de Finanzas en Drive...")
    try:
        # Cargar configuración de carpetas
        CONFIG_PATH = r'c:\Users\abustamante\.qai\config\gdrive_folders.json'
        if os.path.exists(CONFIG_PATH):
            import json
            with open(CONFIG_PATH, 'r') as f:
                folders = json.load(f)
            
            finanzas_folder_id = None
            # Buscar carpeta de Finanzas
            for folder_name, folder_id in folders.items():
                if 'finanza' in folder_name.lower() or 'administracion' in folder_name.lower():
                    finanzas_folder_id = folder_id
                    break
            
            if finanzas_folder_id:
                # Mover archivo a carpeta
                file = drive_service.files().get(fileId=spreadsheet_id, fields='parents').execute()
                previous_parents = ",".join(file.get('parents'))
                
                drive_service.files().update(
                    fileId=spreadsheet_id,
                    addParents=finanzas_folder_id,
                    removeParents=previous_parents,
                    fields='id, parents'
                ).execute()
                print(f"✅ Movido a carpeta de Finanzas")
            else:
                print("⚠️ No se encontró carpeta de Finanzas, dejar en raíz")
        else:
            print("⚠️ No se encontró configuración de carpetas, dejar en raíz")
    except Exception as e:
        print(f"⚠️ No se pudo mover a carpeta (continuando): {e}")
    
    print("\n" + "="*60)
    print("✅ SISTEMA FINANCIERO CREADO EXITOSAMENTE")
    print("="*60)
    print(f"\n📊 URL: {spreadsheet_url}")
    print(f"🆔 ID: {spreadsheet_id}")
    print("\n📝 Próximos pasos:")
    print("   1. Revisar estructura de hojas")
    print("   2. Configurar validaciones de datos (listas desplegables)")
    print("   3. Ajustar fórmulas según necesidades específicas")
    print("   4. Ver documentación en: Empresa/03_ADMINISTRACION_FINANZAS/PLANTILLAS_GOOGLE_SHEETS.md")
    
    return {
        'spreadsheet_id': spreadsheet_id,
        'spreadsheet_url': spreadsheet_url
    }

if __name__ == "__main__":
    try:
        result = crear_sistema_financiero()
        print(f"\n✅ Completado. ID: {result['spreadsheet_id']}")
        print(f"   URL: {result['spreadsheet_url']}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
