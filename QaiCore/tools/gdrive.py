"""
Google Drive Tool for QAI Agents
Allows agents (like Finn) to upload/download files to Google Drive.
"""

import sys
import os
import json
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive.file']
TOKEN_PATH = r'c:\Users\abustamante\.qai\gdrive\token.pickle'
CREDENTIALS_PATH = r'c:\Users\abustamante\.qai\gdrive\credentials.json'
CONFIG_PATH = r'c:\Users\abustamante\.qai\config\gdrive_folders.json'

class GDriveTool:
    """
    Herramienta para que agentes interactúen con Google Drive.
    """
    
    def __init__(self):
        self._service = None
        self._creds = None
        self.folders = self._load_config()
    
    @property
    def service(self):
        """
        Carga perezosa del servicio de Google Drive.
        Solo se inicializa cuando se requiere realizar una acción.
        """
        if self._service is None:
            sys.stderr.write("[-] Inicializando Google Drive Service...\n")
            self._creds = self._authenticate()
            
            # Nueva ubicación central de cache de discovery en .qai
            from pathlib import Path
            discovery_cache_dir = Path("c:/Users/abustamante/.qai/google_discovery")
            discovery_cache_dir.mkdir(parents=True, exist_ok=True)
            discovery_path = discovery_cache_dir / "drive.v3.json"
            
            legacy_discovery_path = Path(sys.prefix) / "lib" / "site-packages" / "googleapiclient" / "discovery_cache" / "documents" / "drive.v3.json"
            if not legacy_discovery_path.exists():
                legacy_discovery_path = Path(sys.prefix) / "Lib" / "site-packages" / "googleapiclient" / "discovery_cache" / "documents" / "drive.v3.json"

            discovery_doc = None
            if discovery_path.exists():
                discovery_doc = discovery_path.read_text(encoding="utf-8")
            elif legacy_discovery_path.exists():
                discovery_doc = legacy_discovery_path.read_text(encoding="utf-8")
                discovery_path.write_text(discovery_doc, encoding="utf-8")
                
            if discovery_doc:
                from googleapiclient.discovery import build_from_document
                self._service = build_from_document(json.loads(discovery_doc), credentials=self._creds)
            else:
                sys.stderr.write("[-] Descargando Drive API Discovery (Warm-up)...\n")
                self._service = build('drive', 'v3', credentials=self._creds, static_discovery=False)
            
            sys.stderr.write("[+] Servicio listo.\n")
        return self._service


    def upload_file(self, local_path, drive_folder_id, description=None):
        """
        Sube archivo a Drive y retorna link público.
        """
        sys.stderr.write(f"[-] Subiendo {os.path.basename(local_path)}...\n")
        file_metadata = {
            'name': os.path.basename(local_path),
            'parents': [drive_folder_id],
            'description': description or ''
        }
        media = MediaFileUpload(local_path, resumable=True)
        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, name, webViewLink'
        ).execute()
        
        sys.stderr.write(f"[+] Subida completada: {file.get('id')}\n")
        return {
            'id': file.get('id'),
            'name': file.get('name'),
            'link': file.get('webViewLink')
        }
    
    def download_file(self, file_id, local_path):
        """
        Descarga archivo de Drive.
        """
        sys.stderr.write(f"[-] Descargando archivo {file_id}...\n")
        request = self.service.files().get_media(fileId=file_id)
        with open(local_path, 'wb') as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                sys.stderr.write(f"[-] Progreso: {int(status.progress() * 100)}%\n")
        return local_path
    
    def list_files(self, folder_id, query=None):
        """
        Lista archivos en una carpeta.
        """
        sys.stderr.write(f"[-] Listando archivos en carpeta {folder_id}...\n")
        q = f"'{folder_id}' in parents and trashed=false"
        if query:
            q += f" and {query}"
        
        results = self.service.files().list(
            q=q,
            fields='files(id, name, webViewLink, createdTime, size)',
            orderBy='createdTime desc'
        ).execute()
        
        return results.get('files', [])
    
    def move_file(self, file_id, target_folder_id):
        """
        Mueve un archivo a otra carpeta (actualiza parents en Drive).
        """
        file = self.service.files().get(fileId=file_id, fields='parents').execute()
        parents = file.get('parents', [])
        if not parents:
            raise ValueError(f"Archivo {file_id} no tiene carpeta padre")
        self.service.files().update(
            fileId=file_id,
            addParents=target_folder_id,
            removeParents=','.join(parents)
        ).execute()
        sys.stderr.write(f"[+] Archivo {file_id} movido a carpeta {target_folder_id}\n")
        return {'id': file_id, 'parents': [target_folder_id]}

    def create_folder(self, name, parent_folder_id=None):
        """
        Crea carpeta en Drive.
        """
        sys.stderr.write(f"[-] Creando carpeta '{name}'...\n")
        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_folder_id:
            file_metadata['parents'] = [parent_folder_id]
        
        folder = self.service.files().create(
            body=file_metadata,
            fields='id, name, webViewLink'
        ).execute()
        
        return {
            'id': folder.get('id'),
            'name': folder.get('name'),
            'link': folder.get('webViewLink')
        }
    
    def rename_file(self, file_id, new_name):
        """
        Renombra un archivo en Drive. Retorna el file actualizado.
        """
        sys.stderr.write(f"[-] Renombrando archivo {file_id} a '{new_name}'...\n")
        file = self.service.files().update(
            fileId=file_id,
            body={'name': new_name},
            fields='id, name, webViewLink'
        ).execute()
        sys.stderr.write(f"[+] Renombrado: {file.get('name')}\n")
        return {'id': file.get('id'), 'name': file.get('name'), 'link': file.get('webViewLink')}

    def delete_file(self, file_id):
        """
        Mueve archivo a la papelera.
        """
        sys.stderr.write(f"[-] Eliminando (papelera) archivo {file_id}...\n")
        self.service.files().update(
            fileId=file_id,
            body={'trashed': True}
        ).execute()
    
    def _authenticate(self):
        """
        Autenticación OAuth2 con Google.
        """
        creds = None
        
        if os.path.exists(TOKEN_PATH):
            with open(TOKEN_PATH, 'rb') as token:
                creds = pickle.load(token)
        
        if not creds or not creds.valid:
            sys.stderr.write("[-] Autenticación requerida/expirada...\n")
            if creds and creds.expired and creds.refresh_token:
                sys.stderr.write("[-] Refrescando token...\n")
                creds.refresh(Request())
            else:
                if not os.path.exists(CREDENTIALS_PATH):
                    raise FileNotFoundError(
                        f'No se encontró credentials.json en: {CREDENTIALS_PATH}'
                    )
                sys.stderr.write("[-] Iniciando flujo de autenticación interactivo...\n")
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_PATH, SCOPES)
                creds = flow.run_local_server(port=0)
            
            os.makedirs(os.path.dirname(TOKEN_PATH), exist_ok=True)
            with open(TOKEN_PATH, 'wb') as token:
                pickle.dump(creds, token)
        
        return creds
    
    def _load_config(self):
        """
        Carga IDs de carpetas desde config local.
        """
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'r') as f:
                return json.load(f)
        return {}

    def save_config(self, config):
        """
        Guarda IDs de carpetas en config local.
        """
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, 'w') as f:
            json.dump(config, f, indent=2)
        self.folders = config

# Singleton perezoso
_gdrive_instance = None

def get_gdrive():
    global _gdrive_instance
    if _gdrive_instance is None:
        _gdrive_instance = GDriveTool()
    return _gdrive_instance

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='QAI GDrive CLI')
    parser.add_argument('--upload', type=str, help='Ruta local para subir')
    parser.add_argument('--folder', type=str, help='ID de carpeta en Drive')
    parser.add_argument('--desc', type=str, help='Descripción del archivo')
    parser.add_argument('--list', type=str, help='ID de carpeta para listar')
    parser.add_argument('--download', type=str, help='ID de archivo para descargar')
    parser.add_argument('--output', type=str, help='Ruta local para descarga')
    parser.add_argument('--create-folder', type=str, help='Nombre de la carpeta a crear')
    parser.add_argument('--parent', type=str, help='ID de la carpeta padre para el nuevo folder')
    parser.add_argument('--show-folders', action='store_true', help='Muestra el mapeo de nombres de carpeta a IDs')
    parser.add_argument('--move', type=str, help='ID del archivo a mover')
    parser.add_argument('--to-folder', type=str, help='ID de la carpeta destino (usar con --move)')
    parser.add_argument('--rename', type=str, help='ID del archivo a renombrar')
    parser.add_argument('--name', type=str, help='Nuevo nombre (usar con --rename)')
    parser.add_argument('--trash', type=str, help='ID del archivo a enviar a la papelera')

    args = parser.parse_args()
    
    # Obtener instancia solo después de parsear argumentos
    gdrive_cli = get_gdrive()

    if args.upload and args.folder:
        res = gdrive_cli.upload_file(args.upload, args.folder, args.desc)
        print(json.dumps(res, indent=2))
    elif args.list:
        res = gdrive_cli.list_files(args.list)
        print(json.dumps(res, indent=2))
    elif args.download and args.output:
        res = gdrive_cli.download_file(args.download, args.output)
        print(f"✅ Descargado en: {res}")
    elif args.create_folder:
        res = gdrive_cli.create_folder(args.create_folder, args.parent)
        print(json.dumps(res, indent=2))
    elif args.show_folders:
        print(json.dumps(gdrive_cli.folders, indent=2))
    elif args.move and args.to_folder:
        res = gdrive_cli.move_file(args.move, args.to_folder)
        print(json.dumps(res, indent=2))
    elif args.rename and args.name:
        res = gdrive_cli.rename_file(args.rename, args.name)
        print(json.dumps(res, indent=2))
    elif args.trash:
        gdrive_cli.delete_file(args.trash)
        print('✅ Archivo enviado a la papelera')
    else:
        parser.print_help()
