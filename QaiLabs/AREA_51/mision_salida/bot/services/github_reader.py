"""
QAI HQ Bot — GitHub Reader Service
Lee archivos del repositorio de QAI via GitHub API.
"""
import time
import logging
import requests
from config import config

logger = logging.getLogger(__name__)


class GitHubReader:
    """Lee archivos del repo QAI en GitHub."""

    BASE_URL = "https://api.github.com"

    def __init__(self):
        self._cache: dict[str, tuple[str, float]] = {}  # path -> (content, timestamp)
        self._cache_ttl = 300  # 5 minutos

    @property
    def _headers(self) -> dict:
        return {
            "Authorization": f"token {config.GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3.raw",
        }

    def read_file(self, path: str) -> str | None:
        """
        Lee un archivo del repo.
        
        Args:
            path: Ruta relativa al root del repo (ej: 'TorreDeControl/STATUS.md')
        
        Returns:
            Contenido del archivo como string, o None si hay error.
        """
        # Verificar cache
        if path in self._cache:
            content, cached_at = self._cache[path]
            if time.time() - cached_at < self._cache_ttl:
                logger.debug("Cache hit: %s", path)
                return content

        # Fetch from GitHub
        url = (
            f"{self.BASE_URL}/repos/{config.GITHUB_REPO}"
            f"/contents/{path}?ref={config.GITHUB_BRANCH}"
        )

        try:
            response = requests.get(url, headers=self._headers, timeout=10)
            response.raise_for_status()
            content = response.text

            # Guardar en cache
            self._cache[path] = (content, time.time())
            logger.info("📄 Leído de GitHub: %s (%d chars)", path, len(content))
            return content

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                logger.error("❌ Archivo no encontrado en GitHub: %s", path)
            else:
                logger.error("❌ Error HTTP al leer %s: %s", path, e)
            return None
        except requests.exceptions.RequestException as e:
            logger.error("❌ Error de red al leer %s: %s", path, e)
            return None

    def read_status(self) -> str | None:
        """Lee TorreDeControl/STATUS.md"""
        return self.read_file("TorreDeControl/STATUS.md")

    def read_inbox(self) -> str | None:
        """Lee TorreDeControl/INBOX.md"""
        return self.read_file("TorreDeControl/INBOX.md")

    def clear_cache(self):
        """Limpia el cache completo."""
        self._cache.clear()
        logger.info("🗑️ Cache limpiado")


# Singleton
github_reader = GitHubReader()
