"""
QAI HQ Bot — GitHub Writer Service
Escribe/modifica archivos en el repo via GitHub API.
"""
import base64
import logging
import requests
from config import config

logger = logging.getLogger(__name__)


class GitHubWriter:
    """Escribe archivos al repo QAI en GitHub."""

    BASE_URL = "https://api.github.com"

    @property
    def _headers(self) -> dict:
        return {
            "Authorization": f"token {config.GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        }

    def update_file(
        self, path: str, new_content: str, commit_message: str
    ) -> bool:
        """
        Actualiza un archivo existente en el repo.
        
        Args:
            path: Ruta relativa (ej: 'TorreDeControl/INBOX.md')
            new_content: Contenido completo nuevo del archivo
            commit_message: Mensaje del commit
        
        Returns:
            True si el commit fue exitoso
        """
        url = (
            f"{self.BASE_URL}/repos/{config.GITHUB_REPO}"
            f"/contents/{path}"
        )

        try:
            # 1. Obtener SHA actual del archivo
            response = requests.get(url, headers=self._headers, timeout=10)
            response.raise_for_status()
            current_sha = response.json()["sha"]

            # 2. Hacer PUT con el nuevo contenido
            payload = {
                "message": commit_message,
                "content": base64.b64encode(new_content.encode("utf-8")).decode("ascii"),
                "sha": current_sha,
                "branch": config.GITHUB_BRANCH,
            }

            put_response = requests.put(
                url, headers=self._headers, json=payload, timeout=15
            )
            put_response.raise_for_status()

            logger.info(
                "✅ Archivo actualizado: %s (commit: %s)",
                path,
                commit_message[:50],
            )
            return True

        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            body = e.response.text
            if status_code == 409:
                logger.error("❌ Conflicto al escribir %s (archivo cambió). Body: %s", path, body)
            elif status_code == 403:
                logger.error("❌ Sin permisos de escritura para %s (Forbidden). Token puede ser inválido o sin scopes. Body: %s", path, body)
            elif status_code == 404:
                logger.error("❌ Archivo/Repo no encontrado: %s. Body: %s", path, body)
            else:
                logger.error("❌ Error HTTP %s al escribir %s: %s. Body: %s", status_code, path, e, body)
            return False
        except requests.exceptions.RequestException as e:
            logger.error("❌ Error de red al escribir %s: %s", path, e)
            return False


# Singleton
github_writer = GitHubWriter()
