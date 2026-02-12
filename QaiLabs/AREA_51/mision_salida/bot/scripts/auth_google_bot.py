"""
QAI HQ Bot — Script de Autenticación Google (Gmail + Drive)
Genera el token OAuth JSON necesario para el bot en Cloud Functions.

INSTRUCCIONES:
1. Asegúrate de tener credentials.json en ~/.qai/gdrive/credentials.json
2. Ejecuta este script: python scripts/auth_google_bot.py
3. Se abrirá el navegador para autorizar Gmail + Drive
4. El script imprimirá un JSON — copia y pega en env.yaml como GOOGLE_OAUTH_TOKEN_JSON
"""

import os
import json
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow

# Scopes necesarios para Gmail (leer/enviar) + Drive (solo lectura)
SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/drive",  # Full access para crear carpetas
]

CREDENTIALS_PATH = os.path.join(
    os.path.expanduser("~"), ".qai", "gdrive", "credentials.json"
)


def main():
    if not os.path.exists(CREDENTIALS_PATH):
        print(f"❌ No se encontró credentials.json en: {CREDENTIALS_PATH}")
        print("   Descárgalo desde Google Cloud Console → APIs & Services → Credentials")
        return

    print("🚀 Iniciando autorización para Gmail + Drive...")
    print(f"   Scopes: {SCOPES}")
    print("   Se abrirá tu navegador para autorizar la app.\n")

    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
    creds = flow.run_local_server(port=0)

    # Generar el JSON para env.yaml
    token_data = {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "token_uri": creds.token_uri,
        "client_id": creds.client_id,
        "client_secret": creds.client_secret,
        "scopes": list(creds.scopes) if creds.scopes else SCOPES,
    }

    token_json = json.dumps(token_data)

    print("\n" + "=" * 60)
    print("✅ AUTORIZACIÓN EXITOSA")
    print("=" * 60)
    print("\nCopia el siguiente JSON y pégalo en env.yaml como GOOGLE_OAUTH_TOKEN_JSON:")
    print(f"\nGOOGLE_OAUTH_TOKEN_JSON: '{token_json}'")
    print("\n" + "=" * 60)

    # También guardar como archivo de referencia
    backup_path = os.path.join(
        os.path.expanduser("~"), ".qai", "gmail", "bot_token.json"
    )
    os.makedirs(os.path.dirname(backup_path), exist_ok=True)
    with open(backup_path, "w") as f:
        json.dump(token_data, f, indent=2)
    print(f"\n📋 Backup guardado en: {backup_path}")


if __name__ == "__main__":
    main()
