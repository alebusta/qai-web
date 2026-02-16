
import sys
import os
sys.path.append(r'c:\Users\abustamante\TheQaiCo\QaiCore')
from tools.gdrive import get_gdrive

try:
    drive = get_gdrive()
    # Search for the file in the whole drive
    query = "name contains 'Referentes' and trashed = false"
    print(f"Searching for: {query}")
    results = drive.service.files().list(q=query, fields="files(id, name, mimeType, webViewLink)").execute()
    files = results.get('files', [])
    for f in files:
        print(f"Found: {f['name']} ({f['mimeType']}) - ID: {f['id']}")
except Exception as e:
    print(f"Error: {e}")
