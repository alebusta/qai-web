"""
QAI HQ Bot — Google Drive Service
Busca y lista archivos de Drive para uso en Cloud Functions.
"""
import json
import io
import logging
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

logger = logging.getLogger(__name__)

# Mapeo de nombres amigables → folder IDs
# Se carga desde la variable de entorno DRIVE_FOLDER_MAP
_DEFAULT_FOLDER_MAP = {
    "root": "1lf_KkEk8CV3N40aNzQTsHXQ0aCrkKWro",
    "contabilidad": "1nuSZV_iIDctTCmbhXXhMJfd5XxEFSIYL",
    "tributario": "1EvcyiRbXRJcHj1soQq-st0SgGwXUuV-P",
    "legales": "165wBgQefhYiw49rGhVOQ_WE8OVWSxee2",
    "escrituras": "15T8mOYUXXznLzTQqY9_RgctYpT80Gcv1",
    "certificados": "1nD5B1lOUsglDbC5gte8zLA1MdTcMKn71",
    "actas": "1Ieyd6PtP-3vooPePJ4nmxXR7E8Ieyf-O",
    "registros": "1cxSL7Iz3j99yNsaLW6KRCrggBJKXHs3_",
    "clientes": "1g_uGZn3qge52z0oH_8ta_BcpkC-QTMGi",
}


class GDriveService:
    """Servicio para interactuar con Google Drive API (solo lectura)."""

    def __init__(self):
        from services.google_auth import get_google_credentials
        from config import config

        creds = get_google_credentials()
        self._service = build("drive", "v3", credentials=creds)

        # Cargar folder map (desde env o defaults)
        self._folder_map = self._load_folder_map(config.DRIVE_FOLDER_MAP)
        logger.info(
            "📁 GDriveService inicializado (%d carpetas mapeadas)",
            len(self._folder_map),
        )

    def _load_folder_map(self, env_value: str | None) -> dict[str, str]:
        """Carga el mapeo de carpetas desde env var o usa defaults."""
        if env_value:
            try:
                return json.loads(env_value)
            except json.JSONDecodeError:
                logger.warning("DRIVE_FOLDER_MAP no es JSON válido, usando defaults")
        return _DEFAULT_FOLDER_MAP.copy()

    def search_files(self, query: str, max_results: int = 10) -> list[dict]:
        """
        Busca archivos por nombre en todo el Drive.

        Args:
            query: Texto a buscar en el nombre del archivo.
            max_results: Máximo de resultados.

        Returns:
            Lista de dicts con id, name, link, mimeType.
        """
        try:
            q = f"name contains '{query}' and trashed=false"
            results = (
                self._service.files()
                .list(
                    q=q,
                    fields="files(id, name, webViewLink, mimeType, createdTime)",
                    orderBy="modifiedTime desc",
                    pageSize=max_results,
                )
                .execute()
            )
            return [
                {
                    "id": f["id"],
                    "name": f["name"],
                    "link": f.get("webViewLink", ""),
                    "type": self._friendly_type(f.get("mimeType", "")),
                }
                for f in results.get("files", [])
            ]
        except Exception as e:
            logger.error("❌ Error buscando archivos: %s", e)
            return []

    def list_folder(self, folder_name: str, max_results: int = 15) -> list[dict]:
        """
        Lista archivos de una carpeta conocida.

        Args:
            folder_name: Nombre amigable de la carpeta (ej: 'contabilidad', 'legales').

        Returns:
            Lista de dicts con id, name, link, type.
        """
        folder_id = self._folder_map.get(folder_name.lower())
        if not folder_id:
            available = ", ".join(sorted(self._folder_map.keys()))
            return [{"error": f"Carpeta '{folder_name}' no encontrada. Disponibles: {available}"}]

        try:
            q = f"'{folder_id}' in parents and trashed=false"
            results = (
                self._service.files()
                .list(
                    q=q,
                    fields="files(id, name, webViewLink, mimeType, createdTime)",
                    orderBy="modifiedTime desc",
                    pageSize=max_results,
                )
                .execute()
            )
            return [
                {
                    "id": f["id"],
                    "name": f["name"],
                    "link": f.get("webViewLink", ""),
                    "type": self._friendly_type(f.get("mimeType", "")),
                }
                for f in results.get("files", [])
            ]
        except Exception as e:
            logger.error("❌ Error listando carpeta %s: %s", folder_name, e)
            return []

    def get_file_metadata(self, file_id: str) -> dict | None:
        """Obtiene metadata básica de un archivo."""
        try:
            return (
                self._service.files()
                .get(fileId=file_id, fields="id, name, mimeType, webViewLink")
                .execute()
            )
        except Exception as e:
            logger.error("❌ Error obteniendo metadata de %s: %s", file_id, e)
            return None

    def download_file(self, file_id: str, local_path: str) -> bool:
        """Descarga un archivo de Drive a una ruta local."""
        try:
            request = self._service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                if status:
                    logger.info("⏳ Descargando %s: %d%%", file_id, int(status.progress() * 100))

            with open(local_path, "wb") as f:
                f.write(fh.getbuffer())
            
            logger.info("✅ Archivo descargado: %s", local_path)
            return True
        except Exception as e:
            logger.error("❌ Error descargando archivo %s: %s", file_id, e)
            return False

    def get_file_link(self, file_id: str) -> str | None:
        """Obtiene el webViewLink de un archivo por su ID."""
        try:
            file = (
                self._service.files()
                .get(fileId=file_id, fields="webViewLink, name")
                .execute()
            )
            return file.get("webViewLink")
        except Exception as e:
            logger.error("❌ Error obteniendo link de %s: %s", file_id, e)
            return None

    def get_available_folders(self) -> list[str]:
        """Retorna los nombres de carpetas disponibles."""
        return sorted(self._folder_map.keys())

    def _friendly_type(self, mime_type: str) -> str:
        """Convierte mimeType a nombre amigable."""
        type_map = {
            "application/pdf": "📄 PDF",
            "application/vnd.google-apps.spreadsheet": "📊 Sheets",
            "application/vnd.google-apps.document": "📝 Doc",
            "application/vnd.google-apps.folder": "📁 Carpeta",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "📊 Excel",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "📝 Word",
            "image/png": "🖼️ PNG",
            "image/jpeg": "🖼️ JPG",
        }
        return type_map.get(mime_type, "📎 Archivo")


    def create_folder(self, name: str, parent_id: str = None) -> str | None:
        """Crea una carpeta en Drive. Retorna el ID de la nueva carpeta."""
        try:
            file_metadata = {
                "name": name,
                "mimeType": "application/vnd.google-apps.folder",
            }
            if parent_id:
                file_metadata["parents"] = [parent_id]

            file = (
                self._service.files()
                .create(body=file_metadata, fields="id")
                .execute()
            )
            folder_id = file.get("id")
            logger.info("📁 Carpeta creada: %s (%s)", name, folder_id)
            return folder_id
        except Exception as e:
            logger.error("❌ Error creando carpeta %s: %s", name, e)
            return None

    def ensure_client_structure(self, client_name: str) -> dict[str, str]:
        """
        Asegura que exista la estructura estándar para un cliente:
        - Clientes/{client_name}/
        - Clientes/{client_name}/01_insumos
        - Clientes/{client_name}/02_entregas
        - Clientes/{client_name}/03_gestion
        
        Retorna mapa de IDs: {'root': id, '01': id, ...}
        """
        clientes_root_id = self._folder_map.get("clientes")
        if not clientes_root_id:
            logger.error("❌ No configurado folder ID para 'clientes'")
            return {}

        # 1. Buscar/Crear carpeta del cliente
        q = f"'{clientes_root_id}' in parents and name = '{client_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed=false"
        results = self._service.files().list(q=q, fields="files(id)").execute()
        files = results.get("files", [])
        
        if files:
            client_id = files[0]["id"]
            logger.info("✅ Cliente existente: %s (%s)", client_name, client_id)
        else:
            logger.info("🆕 Creando cliente: %s", client_name)
            client_id = self.create_folder(client_name, parent_id=clientes_root_id)
            if not client_id:
                return {}

        # 2. Estructura estándar
        subfolders = ["01_insumos", "02_entregas", "03_gestion"]
        ids = {"root": client_id}

        # Listar subcarpetas actuales para no duplicar
        q_subs = f"'{client_id}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed=false"
        subs_res = self._service.files().list(q=q_subs, fields="files(id, name)").execute()
        existing_subs = {f["name"]: f["id"] for f in subs_res.get("files", [])}

        for sub in subfolders:
            if sub in existing_subs:
                ids[sub] = existing_subs[sub]
            else:
                new_id = self.create_folder(sub, parent_id=client_id)
                if new_id:
                    ids[sub] = new_id

        return ids


# Singleton con lazy init
_gdrive_instance = None


def get_gdrive() -> GDriveService:
    """Factory con lazy init para GDriveService."""
    global _gdrive_instance
    if _gdrive_instance is None:
        _gdrive_instance = GDriveService()
    return _gdrive_instance
