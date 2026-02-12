# QAI Gmail Tool (Guía para Agentes)

Esta herramienta permite a los agentes de QAI interactuar con Gmail de forma segura y estructurada.

## Capacidades
- **Enviar correos**: Formato HTML con soporte para logo corporativo.
- **Listar Inbox**: Ver últimos correos o buscar por query.
- **Leer Mensajes**: Obtener cuerpo (body) y metadatos.
- **Gestión**: Mover a papelera (`trash`).

## Uso vía CLI

### 1. Listar correos
```bash
cd .\QaiCore
.\qrun.bat .\tools\gmail.py list --max 5
```

### 2. Leer un correo
```bash
cd .\QaiCore
.\qrun.bat .\tools\gmail.py read --id [MESSAGE_ID]
```

### 3. Enviar correo corporativo
```bash
cd .\QaiCore
.\qrun.bat .\tools\gmail.py send --to "cliente@ejemplo.com" --subject "Hola" --body "<h1>Cuerpo HTML</h1>" --logo "path/to/logo.png"
```

## Uso en Código Python
```python
from tools.gmail import GmailTool

tool = GmailTool()
messages = tool.list_messages(query='from:banco', max_results=3)
for msg in messages:
    details = tool.get_message(msg['id'])
    print(details['subject'])
```

## Seguridad y Scopes
Requiere `gmail.modify`. Si el token expira o necesita nuevos permisos, ejecutar `QaiCore/scripts/auth_gmail.py`.
