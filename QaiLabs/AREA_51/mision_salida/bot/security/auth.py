"""
QAI HQ Bot — Seguridad y Autenticación
Whitelist de chat_ids, rate limiting y logging de accesos.
"""
import time
import logging
from collections import defaultdict
from config import config

logger = logging.getLogger(__name__)


class AuthGuard:
    """Controla acceso al bot mediante whitelist y rate limiting."""

    def __init__(self):
        self._request_log: dict[int, list[float]] = defaultdict(list)

    def is_authorized(self, chat_id: int) -> bool:
        """Verifica si un chat_id está en la whitelist."""
        authorized = chat_id in config.ALLOWED_CHAT_IDS

        if authorized:
            logger.info("✅ Acceso autorizado: chat_id=%s", chat_id)
        else:
            logger.warning("🚫 Acceso DENEGADO: chat_id=%s", chat_id)

        return authorized

    def is_rate_limited(self, chat_id: int) -> bool:
        """Verifica si un chat_id excedió el límite de requests por minuto."""
        now = time.time()
        window = 60  # 1 minuto

        # Limpiar requests viejos
        self._request_log[chat_id] = [
            t for t in self._request_log[chat_id] if now - t < window
        ]

        if len(self._request_log[chat_id]) >= config.MAX_REQUESTS_PER_MINUTE:
            logger.warning(
                "⏱️ Rate limit excedido: chat_id=%s (%d req/min)",
                chat_id,
                len(self._request_log[chat_id]),
            )
            return True

        self._request_log[chat_id].append(now)
        return False

    def check_access(self, chat_id: int) -> tuple[bool, str]:
        """
        Verifica acceso completo (auth + rate limit).
        Returns: (allowed: bool, reason: str)
        """
        if not self.is_authorized(chat_id):
            return False, "no_auth"
        if self.is_rate_limited(chat_id):
            return False, "rate_limited"
        return True, "ok"


# Singleton
auth_guard = AuthGuard()
