import sys
import os
import csv
from datetime import datetime
from pathlib import Path

# Add project root to path for CLI execution
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

qai_core_root = Path(__file__).resolve().parents[1]
if str(qai_core_root) not in sys.path:
    sys.path.insert(0, str(qai_core_root))

from tools.gsheets import gsheets

def backup_finance():
    spreadsheet_id = '1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw'
    range_name = 'Registro_Diario!A1:J1000'
    backup_dir = project_root / 'Empresa' / '03_ADMINISTRACION_FINANZAS' / 'backups'
    
    # Create backup dir if not exists
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = backup_dir / f'backup_registro_diario_{timestamp}.csv'
    latest_path = backup_dir / 'registro_diario_latest.csv'
    
    print(f"Reading data from Google Sheet {spreadsheet_id}...")
    try:
        data = gsheets.read_range(spreadsheet_id, range_name)
        if not data:
            print("⚠️ No data found in the spreadsheet.")
            return

        with open(backup_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        
        # Also update the 'latest' symlink/copy
        with open(latest_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)

        print(f"✅ Local backup created successfully at: {backup_path}")
        print(f"✅ Updated latest backup at: {latest_path}")
        
    except Exception as e:
        print(f"❌ Error during backup: {str(e)}")

if __name__ == "__main__":
    backup_finance()
