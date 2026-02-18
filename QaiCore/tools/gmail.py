"""
Gmail Tool for QAI Agents
Allows agents (like Finn) to send emails using the Gmail API.
"""

import os
import sys

# Limpieza radical de proxies (bloquean Gmail API en terminales de IDE)
import os
for _k in list(os.environ):
    if "PROXY" in _k.upper():
        os.environ.pop(_k, None)

import base64
import pickle
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes necesarios para enviar correos
SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/drive.file' # Reutilizamos este para consistencia
]

TOKEN_PATH = r'c:\Users\abustamante\.qai\gmail\token_gmail.pickle'
CREDENTIALS_PATH = r'c:\Users\abustamante\.qai\gdrive\credentials.json'

class GmailTool:
    def __init__(self):
        self.creds = self._authenticate()
        
        # Nueva ubicación central de cache de discovery en .qai
        from pathlib import Path
        discovery_cache_dir = Path("c:/Users/abustamante/.qai/google_discovery")
        discovery_cache_dir.mkdir(parents=True, exist_ok=True)
        discovery_path = discovery_cache_dir / "gmail.v1.json"
        
        # 1. Intentar cargar desde cache local en .qai
        # 2. Intentar cargar desde site-packages (hack previo)
        # 3. Fallback: descarga y guarda en cache
        
        legacy_discovery_path = Path(sys.prefix) / "lib" / "site-packages" / "googleapiclient" / "discovery_cache" / "documents" / "gmail.v1.json"
        if not legacy_discovery_path.exists():
            legacy_discovery_path = Path(sys.prefix) / "Lib" / "site-packages" / "googleapiclient" / "discovery_cache" / "documents" / "gmail.v1.json"

        discovery_doc = None
        if discovery_path.exists():
            discovery_doc = discovery_path.read_text(encoding="utf-8")
        elif legacy_discovery_path.exists():
            discovery_doc = legacy_discovery_path.read_text(encoding="utf-8")
            # Migrar a la nueva cache
            discovery_path.write_text(discovery_doc, encoding="utf-8")
            
        if discovery_doc:
            from googleapiclient.discovery import build_from_document
            import json
            self.service = build_from_document(json.loads(discovery_doc), credentials=self.creds)
        else:
            sys.stderr.write("[-] Descargando Gmail API Discovery (Warm-up)...\n")
            self.service = build('gmail', 'v1', credentials=self.creds, static_discovery=False)


    def _authenticate(self):
        creds = None
        if os.path.exists(TOKEN_PATH):
            with open(TOKEN_PATH, 'rb') as token:
                creds = pickle.load(token)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(CREDENTIALS_PATH):
                    raise FileNotFoundError(f"No se encontró credentials.json en {CREDENTIALS_PATH}")
                # Nota: El usuario deberá ejecutar un script aparte para el primer login
                raise Exception("Credenciales expiradas o no encontradas. Ejecuta scripts/auth_gmail.py")
            
            with open(TOKEN_PATH, 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def list_messages(self, query='', max_results=10, label_ids=None):
        """
        Lista mensajes que coincidan con la búsqueda.
        """
        try:
            results = self.service.users().messages().list(
                userId='me', q=query, maxResults=max_results, labelIds=label_ids
            ).execute()
            return results.get('messages', [])
        except Exception as e:
            print(f"Error al listar mensajes: {e}")
            return []

    def get_message(self, message_id):
        """
        Obtiene el contenido completo de un mensaje y lo decodifica.
        """
        try:
            message = self.service.users().messages().get(
                userId='me', id=message_id, format='full'
            ).execute()
            
            payload = message.get('payload', {})
            headers = payload.get('headers', [])
            
            # Extraer Metadatos
            subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '(Sin Asunto)')
            sender = next((h['value'] for h in headers if h['name'].lower() == 'from'), '(Desconocido)')
            date = next((h['value'] for h in headers if h['name'].lower() == 'date'), '(Sin Fecha)')

            # Extraer Cuerpo (Body)
            body = ""
            html_body = ""

            def _decode_part(part_data, part_headers):
                """Decodifica bytes respetando el charset declarado en Content-Type."""
                raw = base64.urlsafe_b64decode(part_data)
                # Buscar charset en los headers de la parte
                charset = 'utf-8'
                for h in part_headers:
                    if h.get('name', '').lower() == 'content-type':
                        val = h.get('value', '')
                        for token in val.split(';'):
                            token = token.strip()
                            if token.lower().startswith('charset='):
                                charset = token.split('=', 1)[1].strip().strip('"\'')
                                break
                # Intentar con charset declarado, luego fallbacks
                for enc in [charset, 'utf-8', 'latin-1']:
                    try:
                        return raw.decode(enc)
                    except (UnicodeDecodeError, LookupError):
                        continue
                return raw.decode('utf-8', errors='replace')

            if 'parts' in payload:
                for part in payload['parts']:
                    part_headers = part.get('headers', [])
                    if part['mimeType'] == 'text/plain':
                        data = part.get('body', {}).get('data', '')
                        if data:
                            body = _decode_part(data, part_headers)
                    elif part['mimeType'] == 'text/html':
                        data = part.get('body', {}).get('data', '')
                        if data:
                            html_body = _decode_part(data, part_headers)
                    elif part['mimeType'].startswith('multipart/'):
                        # Recursión para multipart anidados (e.g. multipart/alternative)
                        for subpart in part.get('parts', []):
                            sub_headers = subpart.get('headers', [])
                            if subpart['mimeType'] == 'text/plain':
                                data = subpart.get('body', {}).get('data', '')
                                if data and not body:
                                    body = _decode_part(data, sub_headers)
                            elif subpart['mimeType'] == 'text/html':
                                data = subpart.get('body', {}).get('data', '')
                                if data and not html_body:
                                    html_body = _decode_part(data, sub_headers)
            else:
                data = payload.get('body', {}).get('data', '')
                if data:
                    raw_body = _decode_part(data, payload.get('headers', []))
                    if payload.get('mimeType') == 'text/html':
                        html_body = raw_body
                    else:
                        body = raw_body

            return {
                'id': message_id,
                'subject': subject,
                'from': sender,
                'date': date,
                'snippet': message.get('snippet', ''),
                'body': body,
                'html_body': html_body,
                'attachments': self._extract_attachments(payload)
            }
        except Exception as e:
            print(f"Error al obtener mensaje {message_id}: {e}")
            return None

    def _extract_attachments(self, payload):
        """
        Extrae información de los adjuntos del mensaje.
        """
        attachments = []
        if 'parts' in payload:
            for part in payload['parts']:
                if part.get('filename'):
                    attachments.append({
                        'filename': part['filename'],
                        'mimeType': part['mimeType'],
                        'id': part['body'].get('attachmentId'),
                        'size': part['body'].get('size')
                    })
                # Recursión para multipart/mixed o multipart/related
                elif 'parts' in part:
                    attachments.extend(self._extract_attachments(part))
        return attachments

    def download_attachment(self, message_id, attachment_id, filename, output_dir='temp_files'):
        """
        Descarga un adjunto específico.
        """
        try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            attachment = self.service.users().messages().attachments().get(
                userId='me', messageId=message_id, id=attachment_id
            ).execute()
            
            data = attachment.get('data')
            if data:
                file_data = base64.urlsafe_b64decode(data)
                target_path = os.path.join(output_dir, filename)
                with open(target_path, 'wb') as f:
                    f.write(file_data)
                return target_path
        except Exception as e:
            print(f"Error al descargar adjunto {attachment_id}: {e}")
            return None

    def trash_message(self, message_id):
        """
        Mueve un mensaje a la papelera.
        """
        try:
            self.service.users().messages().trash(userId='me', id=message_id).execute()
            return True
        except Exception as e:
            print(f"Error al mover {message_id} a papelera: {e}")
            return False

    def send_email(
        self,
        to,
        subject,
        body_html,
        logo_path=None,
        attachments=None,
        allow_duplicate=False,
        dedupe_window_minutes=30
    ):
        """
        Envía un email con formato HTML, logo incrustado y adjuntos opcionales.
        Utiliza una estructura de mensaje robusta (multipart/related) para asegurar
        que el logo se vea inline y no como adjunto.
        """
        from email.mime.application import MIMEApplication
        from email import encoders
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.image import MIMEImage

        # Idempotencia defensiva:
        # Evita duplicados cuando el operador reintenta por latencia de terminal.
        if not allow_duplicate and self._recent_sent_exists(
            to, subject, window_minutes=dedupe_window_minutes
        ):
            raise RuntimeError(
                f"Bloqueado envío duplicado: ya existe un correo reciente a '{to}' con asunto '{subject}'. "
                "Usa --allow-duplicate si realmente necesitas reenviarlo."
            )

        # 1. Contenedor Raíz (MIXED) - Permite cuerpo + adjuntos reales
        message = MIMEMultipart('mixed')
        message['to'] = to
        message['subject'] = subject

        # 2. Contenedor de Cuerpo (RELATED) - Encapsula HTML + Imágenes incrustadas (Logo)
        msg_body_root = MIMEMultipart('related')
        
        # 3. Contenedor Alternativo (HTML)
        msg_html = MIMEText(body_html, 'html')
        msg_body_root.attach(msg_html)

        # 4. Incrustar Logo en el bloque RELATED (No en el MIXED)
        if logo_path and os.path.exists(logo_path):
            with open(logo_path, 'rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-ID', '<logo_qai>')
                img.add_header('Content-Disposition', 'inline', filename=os.path.basename(logo_path))
                msg_body_root.attach(img)

        # Adjuntamos el bloque de cuerpo (con su logo) al mensaje raíz
        message.attach(msg_body_root)

        # 5. Adjuntar PDFs al bloque MIXED (Adjuntos reales)
        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as f:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(f.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename={os.path.basename(file_path)}'
                        )
                        message.attach(part)

        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        try:
            sent_message = self.service.users().messages().send(
                userId='me',
                body={'raw': raw_message}
            ).execute()
            return sent_message
        except Exception as e:
            print(f"Error al enviar email: {e}")
            raise e

    def _recent_sent_exists(self, to, subject, window_minutes=30):
        """
        Revisa si existe un correo reciente en 'Sent' con mismo destinatario + asunto.
        Sirve como guardrail anti-duplicado ante reintentos por incertidumbre.
        """
        try:
            cutoff_epoch = int(time.time() - (window_minutes * 60))
            query = f'to:{to} subject:"{subject}" after:{cutoff_epoch}'
            results = self.service.users().messages().list(
                userId='me',
                q=query,
                maxResults=5,
                labelIds=['SENT']
            ).execute()
            return bool(results.get('messages', []))
        except Exception:
            # En caso de error de verificación, no bloqueamos envío.
            return False

    def create_draft(self, to, subject, body_html, logo_path=None, attachments=None):
        """
        Crea un borrador en Gmail con el mismo formato que send_email.
        """
        from email.mime.application import MIMEApplication
        from email import encoders
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.image import MIMEImage

        # Estructura idéntica a send_email
        message = MIMEMultipart('mixed')
        message['to'] = to
        message['subject'] = subject

        msg_body_root = MIMEMultipart('related')
        msg_html = MIMEText(body_html, 'html')
        msg_body_root.attach(msg_html)

        if logo_path and os.path.exists(logo_path):
            with open(logo_path, 'rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-ID', '<logo_qai>')
                img.add_header('Content-Disposition', 'inline', filename=os.path.basename(logo_path))
                msg_body_root.attach(img)

        message.attach(msg_body_root)

        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as f:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(f.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename={os.path.basename(file_path)}'
                        )
                        message.attach(part)

        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        try:
            draft = self.service.users().drafts().create(
                userId='me',
                body={'message': {'raw': raw_message}}
            ).execute()
            return draft
        except Exception as e:
            print(f"Error al crear borrador: {e}")
            raise e

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='QAI Gmail CLI Tool')
    
    # Grupos de comandos
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponibles')

    # Comando: Send
    send_parser = subparsers.add_parser('send', help='Enviar un email')
    send_parser.add_argument('--to', required=True)
    send_parser.add_argument('--subject', required=True)
    send_parser.add_argument('--body', help='Cuerpo HTML como string (evitar en PowerShell si es muy largo)')
    send_parser.add_argument('--body-file', help='Ruta al archivo HTML del cuerpo (recomendado para email_preview.html)')
    send_parser.add_argument('--logo', help='Ruta al logo para incrustar')
    send_parser.add_argument('--attach', action='append', help='Ruta de archivo para adjuntar (puede usarse múltiples veces)')
    send_parser.add_argument('--allow-duplicate', action='store_true', help='Permite reenviar aunque exista un envío reciente con mismo destino+asunto')
    send_parser.add_argument('--dedupe-window-min', type=int, default=30, help='Ventana de deduplicación en minutos (default: 30)')

    # Comando: Draft
    draft_parser = subparsers.add_parser('draft', help='Crear un borrador')
    draft_parser.add_argument('--to', required=True)
    draft_parser.add_argument('--subject', required=True)
    draft_parser.add_argument('--body', help='Cuerpo HTML as string')
    draft_parser.add_argument('--body-file', help='Ruta al archivo HTML del cuerpo')
    draft_parser.add_argument('--logo', help='Ruta al logo')
    draft_parser.add_argument('--attach', action='append', help='Ruta de archivo para adjuntar')

    # Comando: List
    list_parser = subparsers.add_parser('list', help='Listar correos del inbox')
    list_parser.add_argument('--max', type=int, default=5, help='Máximo de resultados')
    list_parser.add_argument('--query', default='', help='Búsqueda específica (estilo Gmail)')

    # Comando: Read
    read_parser = subparsers.add_parser('read', help='Leer un correo específico')
    read_parser.add_argument('--id', required=True, help='ID del mensaje')

    # Comando: Trash
    trash_parser = subparsers.add_parser('trash', help='Borrar un correo')
    trash_parser.add_argument('--id', required=True, help='ID del mensaje')

    # Comando: Download
    download_parser = subparsers.add_parser('download', help='Descargar un adjunto')
    download_parser.add_argument('--id', required=True, help='ID del mensaje')
    download_parser.add_argument('--att-id', required=True, help='ID del adjunto')
    download_parser.add_argument('--filename', required=True, help='Nombre del archivo de salida')
    download_parser.add_argument('--dir', default='temp_files', help='Directorio de destino')

    args = parser.parse_args()
    gmail = GmailTool()

    if args.command == 'send':
        if args.body_file:
            with open(args.body_file, 'r', encoding='utf-8') as f:
                body_html = f.read()
        elif args.body:
            body_html = args.body
        else:
            parser.error('send requiere --body o --body-file')
        res = gmail.send_email(
            args.to,
            args.subject,
            body_html,
            args.logo,
            args.attach,
            allow_duplicate=args.allow_duplicate,
            dedupe_window_minutes=args.dedupe_window_min
        )
        print(f"✅ Email enviado con ID: {res['id']}")
    
    elif args.command == 'draft':
        if args.body_file:
            with open(args.body_file, 'r', encoding='utf-8') as f:
                body_html = f.read()
        elif args.body:
            body_html = args.body
        else:
            parser.error('draft requiere --body o --body-file')
        res = gmail.create_draft(args.to, args.subject, body_html, args.logo, args.attach)
        print(f"✅ Borrador creado con ID: {res['id']}")
    
    elif args.command == 'list':
        messages = gmail.list_messages(query=args.query, max_results=args.max)
        if not messages:
            print("📭 No se encontraron mensajes.")
        else:
            for m in messages:
                details = gmail.get_message(m['id'])
                if details:
                    print(f" - [{details['id']}] {details['subject'][:50]} (De: {details['from'][:30]})")

    elif args.command == 'read':
        details = gmail.get_message(args.id)
        if details:
            print(f"\n--- {details['subject']} ---")
            print(f"De: {details['from']}")
            print(f"Fecha: {details['date']}")
            print("-" * 20)
            if details['html_body']:
                print("--- HTML BODY ---")
                print(details['html_body'])
            else:
                print(details['body'] or details['snippet'])
            
            if details.get('attachments'):
                print("\n--- ATTACHMENTS ---")
                for att in details['attachments']:
                    print(f" - {att['filename']} ({att['mimeType']}, ID: {att['id']})")
            print("-" * 20)
        else:
            print("❌ No se pudo leer el mensaje.")

    elif args.command == 'trash':
        if gmail.trash_message(args.id):
            print(f"✅ Mensaje {args.id} movido a la papelera.")
        else:
            print(f"❌ Falló el borrado de {args.id}.")

    elif args.command == 'download':
        path = gmail.download_attachment(args.id, args.att_id, args.filename, args.dir)
        if path:
            print(f"✅ Adjunto guardado en: {path}")
        else:
            print("❌ Falló la descarga del adjunto.")
    
    else:
        parser.print_help()
