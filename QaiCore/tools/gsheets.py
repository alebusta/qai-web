"""
Google Sheets Tool for QAI Agents
Allows agents (like Finn) to interact with Google Sheets.
"""

import sys
import os
from pathlib import Path

# Add QaiCore root to path for CLI execution
qai_core_root = Path(__file__).resolve().parents[1]
if str(qai_core_root) not in sys.path:
    sys.path.insert(0, str(qai_core_root))

from googleapiclient.discovery import build
import json

# Direct import to avoid heavy tools.__init__
# We add the parent directory to sys.path and import gdrive directly
_tools_dir = str(Path(__file__).parent)
if _tools_dir not in sys.path:
    sys.path.append(_tools_dir)

try:
    from gdrive import get_gdrive
except ImportError:
    # Fallback for when running from QaiCore root
    import gdrive
    get_gdrive = gdrive.get_gdrive


# Scopes are technically managed by gdrive tool, but for reference:
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']

class GSheetsTool:
    """
    Herramienta para que agentes interactúen con Google Sheets.
    """
    
    def __init__(self):
        # Reutilizamos las credenciales ya autenticadas por el tool de GDrive
        self.gdrive = get_gdrive()
        _ = self.gdrive.service 
        self.creds = self.gdrive._creds
        
        discovery_path = Path(sys.prefix) / "lib" / "site-packages" / "googleapiclient" / "discovery_cache" / "documents" / "sheets.v4.json"
        
        # Fallback for some Windows Python installations where it might be in 'Lib' instead of 'lib'
        if not discovery_path.exists():
            discovery_path = Path(sys.prefix) / "Lib" / "site-packages" / "googleapiclient" / "discovery_cache" / "documents" / "sheets.v4.json"
            
        if discovery_path.exists():
            with open(discovery_path, 'r') as f:
                discovery_doc = f.read()
            from googleapiclient.discovery import build_from_document
            self.service = build_from_document(discovery_doc, credentials=self.creds)
        else:
            self.service = build('sheets', 'v4', credentials=self.creds, static_discovery=True)
    
    def create_spreadsheet(self, title):
        """
        Crea una nueva planilla de Google Sheets.
        """
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = self.service.spreadsheets().create(
            body=spreadsheet,
            fields='spreadsheetId,spreadsheetUrl'
        ).execute()
        
        return {
            'id': spreadsheet.get('spreadsheetId'),
            'url': spreadsheet.get('spreadsheetUrl')
        }
    
    def add_sheet(self, spreadsheet_id, title):
        """
        Agrega una nueva pestaña (hoja) a la planilla.
        """
        body = {
            'requests': [{
                'addSheet': {
                    'properties': {
                        'title': title
                    }
                }
            }]
        }
        res = self.service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body
        ).execute()
        return res
    
    def append_row(self, spreadsheet_id, range_name, values):
        """
        Agrega una fila de datos a una planilla.
        
        Args:
            spreadsheet_id: ID de la planilla
            range_name: Nombre de la hoja o rango (ej: 'Hoja 1!A1')
            values: Lista de valores [col1, col2, ...]
        """
        body = {
            'values': [values]
        }
        result = self.service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()
        
        return result
    
    def read_range(self, spreadsheet_id, range_name):
        """
        Lee un rango de celdas.
        """
        result = self.service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        
        return result.get('values', [])
    
    def update_cells(self, spreadsheet_id, range_name, values):
        """
        Actualiza un rango de celdas específico.
        """
        body = {
            'values': values
        }
        result = self.service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()
        
        return result

# Instancia global (singleton)
gsheets = GSheetsTool()

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='QAI GSheets CLI')
    parser.add_argument('--spreadsheet_id', type=str, help='ID de la planilla')
    parser.add_argument('--append', type=str, help='Nombre de hoja para agregar fila')
    parser.add_argument('--data', type=str, help='Datos en formato JSON (lista de valores)')
    parser.add_argument('--read', type=str, help='Rango para leer (ej: Hoja1!A1:B10)')
    parser.add_argument('--create', type=str, help='Título para nueva planilla')
    parser.add_argument('--add_sheet', type=str, help='Nombre para nueva pestaña')

    args = parser.parse_args()

    if args.create:
        res = gsheets.create_spreadsheet(args.create)
        print(json.dumps(res, indent=2))
    elif args.spreadsheet_id:
        if args.add_sheet:
            res = gsheets.add_sheet(args.spreadsheet_id, args.add_sheet)
            print(f"✅ Pestaña '{args.add_sheet}' creada")
        elif args.append and args.data:
            values = json.loads(args.data)
            res = gsheets.append_row(args.spreadsheet_id, args.append, values)
            print("✅ Fila agregada")
        elif args.read:
            res = gsheets.read_range(args.spreadsheet_id, args.read)
            print(json.dumps(res, indent=2))
    else:
        parser.print_help()
