"""
QAI HQ Bot — Configuración
Carga y valida variables de entorno necesarias para el bot.
"""
import os
import logging

logger = logging.getLogger(__name__)


class Config:
    """Configuración centralizada del bot QAI HQ."""

    def __init__(self):
        # === Telegram ===
        self.TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
        self.ALLOWED_CHAT_IDS = self._parse_chat_ids(
            os.environ.get("ALLOWED_CHAT_IDS", "")
        )

        # === GitHub ===
        self.GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
        self.GITHUB_REPO = os.environ.get("GITHUB_REPO", "qai-labs/TheQaiCo")
        self.GITHUB_BRANCH = os.environ.get("GITHUB_BRANCH", "master")

        # === Google APIs (Gmail + Drive) ===
        self.GOOGLE_OAUTH_TOKEN_JSON = os.environ.get("GOOGLE_OAUTH_TOKEN_JSON")
        self.GOOGLE_DELEGATED_USER = os.environ.get(
            "GOOGLE_DELEGATED_USER", "alebusta@qai.cl"
        )
        self.DRIVE_FOLDER_MAP = os.environ.get("DRIVE_FOLDER_MAP")

        # === LLM ===
        self.LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "gemini")
        self.GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
        self.GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
        self.CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY")

        # === General ===
        self.LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
        self.MAX_REQUESTS_PER_MINUTE = int(
            os.environ.get("MAX_REQUESTS_PER_MINUTE", "30")
        )

    def _parse_chat_ids(self, raw: str) -> list[int]:
        """Parsea lista de chat_ids desde string separado por comas."""
        if not raw:
            return []
        try:
            return [int(cid.strip()) for cid in raw.split(",") if cid.strip()]
        except ValueError:
            logger.error("ALLOWED_CHAT_IDS contiene valores no numéricos: %s", raw)
            return []

    def validate(self) -> list[str]:
        """Valida que todas las variables críticas estén configuradas."""
        errors = []
        if not self.TELEGRAM_BOT_TOKEN:
            errors.append("TELEGRAM_BOT_TOKEN no configurado")
        if not self.ALLOWED_CHAT_IDS:
            errors.append("ALLOWED_CHAT_IDS no configurado")
        if not self.GITHUB_TOKEN:
            errors.append("GITHUB_TOKEN no configurado")
        if self.LLM_PROVIDER == "gemini" and not self.GEMINI_API_KEY:
            errors.append("GEMINI_API_KEY no configurado (LLM_PROVIDER=gemini)")
        if self.LLM_PROVIDER == "groq" and not self.GROQ_API_KEY:
            errors.append("GROQ_API_KEY no configurado (LLM_PROVIDER=groq)")
        return errors


# Singleton
config = Config()
