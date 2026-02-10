"""
Script de Autorización Inicial para Gmail API
Este script abre el navegador para que el usuario autorice el envío de emails.
"""

import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify',  # Gestión total (Leer/Archivar/Etiquetar)
    'https://www.googleapis.com/auth/drive.file'
]

TOKEN_PATH = r'c:\Users\abustamante\.qai\gmail\token_gmail.pickle'
CREDENTIALS_PATH = r'c:\Users\abustamante\.qai\gdrive\credentials.json'

def main():
    if not os.path.exists(CREDENTIALS_PATH):
        print(f"❌ Error: No se encontró credentials.json en {CREDENTIALS_PATH}")
        return

    print("🚀 Iniciando proceso de autorización de Gmail...")
    print("Se abrirá una ventana en tu navegador para que autorices el acceso.")
    
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
    creds = flow.run_local_server(port=0)

    # Guardar el token
    os.makedirs(os.path.dirname(TOKEN_PATH), exist_ok=True)
    with open(TOKEN_PATH, 'wb') as token:
        pickle.dump(creds, token)
    
    print(f"✅ Autorización exitosa! Token guardado en: {TOKEN_PATH}")

if __name__ == "__main__":
    main()
