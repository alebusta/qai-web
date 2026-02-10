# QaiCore Setup Scripts

> **Propósito**: Scripts de configuración inicial y mantenimiento para herramientas de QaiCore.

---

## 📁 Estructura

```
/QaiCore/scripts/
  /setup/
    gdrive_initial_setup.py  ← Setup inicial de Google Drive API
    gdrive_test.py           ← Test de validación de upload
    README.md                ← Este archivo
```

---

## 🚀 Google Drive API Setup

### Prerrequisitos

Antes de ejecutar el setup, necesitas:

1. **Credentials de Google Cloud**:
   - Proyecto creado en Google Cloud Console
   - Google Drive API habilitada
   - OAuth2 credentials descargadas
   - Archivo guardado en: `c:\Users\[usuario]\.qai\gdrive\credentials.json`

2. **Dependencias Python instaladas**:
   ```bash
   pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

### Ejecución

```bash
cd c:\Users\abustamante\TheQaiCo
python QaiCore/scripts/setup/gdrive_initial_setup.py
```

**Qué hace**:
1. Abre navegador para autenticación OAuth2
2. Crea estructura de carpetas en Google Drive (15 carpetas)
3. Guarda configuración en: `c:\Users\[usuario]\.qai\config\gdrive_folders.json`
4. Guarda token en: `c:\Users\[usuario]\.qai\gdrive\token.pickle`

### Validación

Para verificar que todo funciona:

```bash
python QaiCore/scripts/setup/gdrive_test.py
```

**Resultado esperado**:
```
🧪 Probando upload a Google Drive...
Carpetas configuradas: 15 carpetas

✅ Upload exitoso!
📄 Nombre: test_upload.txt
🔗 Link: https://drive.google.com/...
```

---

## 🔧 Troubleshooting

### Error: "Access blocked: verification process not completed"

**Causa**: Tu email no está en la lista de test users de OAuth.

**Solución**:
1. Google Cloud Console → OAuth consent screen
2. Sección "Audience" → "+ ADD USERS"
3. Agregar tu email
4. Reintentar

### Error: "Google Drive API has not been used"

**Causa**: API no habilitada en el proyecto.

**Solución**:
1. Usar el link que aparece en el error
2. Click en "ENABLE"
3. Esperar 10 segundos
4. Reintentar

### Error: Import error

**Causa**: El script usa `importlib` para evitar conflictos con `__init__.py`.

**Solución**: Ya está resuelto en el código actual.

---

## 📝 Scripts de Mantenimiento

### gdrive_initial_setup.py

**Uso**: Una sola vez al configurar un nuevo ambiente.

**NO ejecutar** si ya tienes la estructura de carpetas creada (destruirá la estructura existente).

### gdrive_test.py

**Uso**: Cada vez que quieras validar que Drive funciona.

Seguro de ejecutar múltiples veces (solo sube un archivo de prueba).

---

## 🔄 Migración a Nueva Máquina

Si necesitas migrar a otra máquina:

1. **Copiar archivos de configuración**:
   ```bash
   # En máquina vieja
   Copy-Item c:\Users\[usuario]\.qai -Recurse -Destination "backup\.qai"
   
   # En máquina nueva
   Copy-Item "backup\.qai" -Recurse -Destination c:\Users\[usuario]\.qai
   ```

2. **NO ejecutar** `gdrive_initial_setup.py` de nuevo (usará config existente)

3. **Validar** con `gdrive_test.py`

---

## 📚 Documentación Relacionada

- **Walkthrough completo**: Ver walkthrough.md en artifacts
- **Código fuente**: `/QaiCore/tools/gdrive.py`
- **Decisión de diseño**: Ver ADR-006 en `/QaiCore/agents/nzero/knowledge_base/design_decisions/`

---

**Creado**: 27-Dic-2025  
**Última actualización**: 27-Dic-2025  
**Mantenedor**: Nzero (Agente Arquitecto)
