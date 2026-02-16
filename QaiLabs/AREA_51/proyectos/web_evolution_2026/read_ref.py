
import sys
import os
sys.path.append(r'c:\Users\abustamante\TheQaiCo\QaiCore')
from tools.gdrive import get_gdrive

drive = get_gdrive()
file_id = '1TR2sALk_ST5hY_Q9th-agvON_zt34LL0XjI-hSKupxo'
# Export to text/plain
try:
    print(f"Exporting file {file_id}...")
    content = drive.service.files().export_media(fileId=file_id, mimeType='text/plain').execute()
    # Content is bytes, need to decode
    print(content.decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
