"""
Script de Autenticación Unificada (QaiCore + Bot)
-----------------------------------------------
Genera credenciales maestras para:
1. QaiCore Local (.pickle) -> Para scripts locales
2. Qai Bot Cloud (.json)   -> Para Cloud Functions (env.yaml)

Permisos Solicitados:
- Gmail: Enviar y Modificar (para etiquetas)
- Drive: Acceso Completo (para crear/organizar carpetas)
"""
import os
import json
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow

# Scopes Maestros
SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/drive",  # Full access
]

# Rutas Canónicas
HOME = os.path.expanduser("~")
CREDENTIALS_PATH = os.path.join(HOME, ".qai", "gdrive", "credentials.json")
TOKEN_PICKLE_PATH = os.path.join(HOME, ".qai", "gdrive", "token.pickle")
TOKEN_JSON_PATH = os.path.join(HOME, ".qai", "gmail", "bot_token.json")

def main():
    print("\n🔐 QAI UNIFIED AUTH WIZARD")
    print("===========================")
    
    if not os.path.exists(CREDENTIALS_PATH):
        print(f"❌ Error: No se encontró credentials.json en {CREDENTIALS_PATH}")
        return

    print(f"📋 Solicitando Scopes: {len(SCOPES)}")
    for s in SCOPES:
        print(f"   - {s.split('/')[-1]}")
    
    print("\n🚀 Abriendo navegador...")
    
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
    creds = flow.run_local_server(port=0)

    # 1. Guardar Pickle (Legacy/Local)
    os.makedirs(os.path.dirname(TOKEN_PICKLE_PATH), exist_ok=True)
    with open(TOKEN_PICKLE_PATH, 'wb') as token:
        pickle.dump(creds, token)
    print(f"\n✅ Token LOCAL actualizado: {TOKEN_PICKLE_PATH}")

    # 2. Guardar JSON (Cloud/Bot)
    token_data = {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "token_uri": creds.token_uri,
        "client_id": creds.client_id,
        "client_secret": creds.client_secret,
        "scopes": list(creds.scopes) if creds.scopes else SCOPES,
    }
    
    os.makedirs(os.path.dirname(TOKEN_JSON_PATH), exist_ok=True)
    with open(TOKEN_JSON_PATH, "w") as f:
        json.dump(token_data, f, indent=2)
    print(f"✅ Token CLOUD generado: {TOKEN_JSON_PATH}")

    # 3. Imprimir JSON para env.yaml
    json_str = json.dumps(token_data)
    print("\n" + "="*60)
    print("COPIA ESTO EN TU env.yaml (GOOGLE_OAUTH_TOKEN_JSON):")
    print("="*60)
    print(f"'{json_str}'")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
