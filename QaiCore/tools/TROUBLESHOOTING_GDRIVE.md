# Troubleshooting: Google Drive Token Expiration

## 🚨 Síntoma

Cuando intentas usar `gdrive.py` o `gsheets.py`, obtienes:

```
RefreshError: 'invalid_grant: Token has been expired or revoked.'
```

O:

```
google.auth.exceptions.RefreshError: Token has been expired or revoked
```

---

## 🔍 Diagnóstico Rápido

### Paso 1: Verificar Estado del Token

```powershell
cd .\QaiCore
.\qrun.bat -c "import pickle; from pathlib import Path; token_path = Path.home() / '.qai' / 'gdrive' / 'token.pickle'; creds = pickle.load(open(token_path, 'rb')); print(f'Token válido: {creds.valid}'); print(f'Token expirado: {creds.expired}'); print(f'Expira en: {creds.expiry}')"
```

**Si dice `Token expirado: True`** → Continúa al Paso 2

---

### Paso 2: Verificar Última Modificación

```powershell
Get-Item "c:\Users\abustamante\.qai\gdrive\token.pickle" | Select-Object LastWriteTime
```

**Si hace más de 7 días** → Token expiró por inactividad

---

## 🔧 Solución

### Opción A: Renovación Rápida (Recomendado)

```powershell
# 1. Eliminar token expirado
Remove-Item "c:\Users\abustamante\.qai\gdrive\token.pickle"

# 2. Forzar re-autenticación
cd .\QaiCore
.\qrun.bat .\tools\gdrive.py --show-folders
```

**Qué pasará**:
1. Se abrirá tu navegador
2. Deberás autorizar "QAI-Agents"
3. Nuevo token se guardará automáticamente

---

### Opción B: Script Dedicado

Si la Opción A falla, usa este script:

```python
# Archivo: renew_gdrive_token.py
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from pathlib import Path

SCOPES = [
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets'
]

CREDS_PATH = Path.home() / '.qai' / 'gdrive' / 'credentials.json'
TOKEN_PATH = Path.home() / '.qai' / 'gdrive' / 'token.pickle'

print(f"🔐 Iniciando renovación de token...")
flow = InstalledAppFlow.from_client_secrets_file(str(CREDS_PATH), SCOPES)
creds = flow.run_local_server(port=0)

with open(TOKEN_PATH, 'wb') as token:
    pickle.dump(creds, token)

print(f"✅ Token renovado. Válido hasta: {creds.expiry}")
```

---

## ✅ Validación

Después de renovar, verifica:

```powershell
# Test 1: Listar carpetas
cd .\QaiCore
.\qrun.bat .\tools\gdrive.py --show-folders

# Test 2: Leer Google Sheets
cd .\QaiCore
.\qrun.bat .\tools\gsheets.py --spreadsheet_id "1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw" --read "Registro_Diario!A1:B2"
```

**Si ambos funcionan** → ✅ Problema resuelto

---

## 🔄 Prevención

### ¿Por qué expira?

- **Access Token**: Expira en 1 hora (se renueva automáticamente)
- **Refresh Token**: Expira después de **~7 días de inactividad**

### Cómo prevenir

**Opción 1**: Usar herramientas al menos 1 vez por semana

**Opción 2**: Migrar a Service Account (no expira nunca)
- Mejor para automatización
- Requiere configuración en Google Cloud Console

---

## 📝 Para Agentes IA

Si eres un agente (Finn, Lex, etc.) y encuentras este error:

### ❌ NO HAGAS

- ❌ Intentar múltiples fallbacks sin diagnosticar
- ❌ Crear workarounds manuales
- ❌ Asumir que es un problema de código

### ✅ SÍ HAZ

1. ✅ Reportar al usuario: "Token de Google Drive expirado"
2. ✅ Sugerir: "Ejecuta: `Remove-Item token.pickle` y re-autentica"
3. ✅ Registrar en `AGENT_ACTIVITY.md`: "Detectado token expirado, solicitada renovación"
4. ✅ Esperar confirmación del usuario antes de continuar

---

## 🆘 Si Nada Funciona

### Problema: credentials.json no existe

```powershell
# Verificar
Test-Path "c:\Users\abustamante\.qai\gdrive\credentials.json"
```

**Solución**: Descargar de Google Cloud Console
1. https://console.cloud.google.com/apis/credentials
2. Proyecto: QAI-Agents
3. OAuth 2.0 Client IDs → Descargar JSON
4. Guardar como: `c:\Users\abustamante\.qai\gdrive\credentials.json`

---

### Problema: redirect_uri_mismatch

**Solución**: Agregar URIs en Google Cloud Console
1. https://console.cloud.google.com/apis/credentials
2. Editar OAuth 2.0 Client ID
3. Agregar: `http://localhost:8080/` y `http://localhost`

---

**Última actualización**: 07-Ene-2026  
**Basado en**: Sesión de diagnóstico real (Finn + Nzero)
