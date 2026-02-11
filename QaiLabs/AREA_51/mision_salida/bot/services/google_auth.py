"""
QAI HQ Bot — Google Auth Service
Autenticación OAuth2 para Gmail y Drive en Cloud Functions.

Estrategia: OAuth Refresh Token persistente.
El token se genera una vez localmente (scripts/auth_google_bot.py)
y se almacena como variable de entorno GOOGLE_OAUTH_TOKEN_JSON.
"""
import json
import logging
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

logger = logging.getLogger(__name__)

# Scopes necesarios para Gmail + Drive
SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/drive.readonly",
]


def get_google_credentials() -> Credentials:
    """
    Obtiene credenciales Google OAuth2 desde la variable de entorno.

    La variable GOOGLE_OAUTH_TOKEN_JSON debe contener un JSON con:
    {
        "token": "...",
        "refresh_token": "...",
        "token_uri": "https://oauth2.googleapis.com/token",
        "client_id": "...",
        "client_secret": "...",
        "scopes": [...]
    }
    """
    from config import config

    token_json = config.GOOGLE_OAUTH_TOKEN_JSON
    if not token_json:
        raise ValueError(
            "GOOGLE_OAUTH_TOKEN_JSON no configurado. "
            "Ejecuta scripts/auth_google_bot.py para generar el token."
        )

    try:
        token_data = json.loads(token_json)
    except json.JSONDecodeError as e:
        raise ValueError(f"GOOGLE_OAUTH_TOKEN_JSON no es JSON válido: {e}")

    creds = Credentials(
        token=token_data.get("token"),
        refresh_token=token_data.get("refresh_token"),
        token_uri=token_data.get("token_uri", "https://oauth2.googleapis.com/token"),
        client_id=token_data.get("client_id"),
        client_secret=token_data.get("client_secret"),
        scopes=token_data.get("scopes", SCOPES),
    )

    # Refrescar si está expirado
    if creds.expired or not creds.valid:
        logger.info("🔄 Refrescando token de Google OAuth...")
        try:
            creds.refresh(Request())
            logger.info("✅ Token refrescado exitosamente")
        except Exception as e:
            logger.error("❌ Error refrescando token: %s", e)
            raise ValueError(
                "Token de Google expirado y no se pudo refrescar. "
                "Re-ejecuta scripts/auth_google_bot.py"
            ) from e

    return creds
