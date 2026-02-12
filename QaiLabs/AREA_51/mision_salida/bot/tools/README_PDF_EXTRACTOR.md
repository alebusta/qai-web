# Herramienta: Extractor de PDFs con OCR

## 🎯 Propósito

Extraer texto de cualquier tipo de PDF:
- PDFs con texto embebido (facturas digitales, estatutos)
- PDFs escaneados sin texto (comprobantes bancarios, documentos físicos)

---

## ✅ Agentes Autorizados

- ✅ **Finn** (Agente Financiero)
- ✅ **Lex** (Agente Legal)
- ✅ Cualquier agente que necesite procesar documentos

---

## 📖 Cómo Usar

### Opción 1: Via document_processor.py (Recomendado)

```python
from qaicore.tools import extract_content

# Extraer texto de cualquier PDF
text = extract_content('c:\\ruta\\al\\documento.pdf')
print(text)
```

### Opción 2: Via CLI

```powershell
cd .\QaiCore
.\qrun.bat .\tools\document_processor.py "c:\ruta\al\documento.pdf"
```

---

## 🔄 Cómo Funciona (3 Niveles de Fallback)

### Nivel 1: pypdf (Automático)
- **Qué hace**: Extrae texto directamente del PDF
- **Cuándo funciona**: PDFs con texto embebido
- **Velocidad**: Instantáneo
- **Costo**: Gratis

### Nivel 2: Tesseract OCR (Automático)
- **Qué hace**: Convierte PDF a imagen y extrae texto con OCR
- **Cuándo funciona**: PDFs escaneados sin texto
- **Velocidad**: 2-3 segundos
- **Costo**: Gratis
- **Requiere**: poppler + Tesseract (ya instalados)

### Nivel 3: Gemini API (Automático si Tesseract falla)
- **Qué hace**: Usa Gemini Vision para OCR
- **Cuándo funciona**: Si Tesseract falla o no está disponible
- **Velocidad**: 3-5 segundos
- **Costo**: Usa crédito de API key "backoffice"
- **Modelo**: gemini-2.5-flash-lite

---

## ❌ Qué NO Hacer

### 🚫 NO Modificar Herramientas

**NUNCA modifiques estos archivos**:
- ❌ `/QaiCore/tools/extractors/pdf.py`
- ❌ `/QaiCore/tools/document_processor.py`
- ❌ Cualquier archivo en `/QaiCore/tools/`

**Si algo no funciona**: Reporta el error (ver abajo)

### 🚫 NO Crear Herramientas Temporales

**NUNCA crees**:
- ❌ Scripts temporales en `/temp_files/`
- ❌ Wrappers alternativos
- ❌ Soluciones "quick fix"

**Usa siempre**: Las herramientas oficiales de `/QaiCore/tools/`

---

## 🐛 Protocolo de Reporte de Errores

### Si la herramienta falla:

1. **Capturar información del error**:
   ```python
   # Ejecutar y capturar output completo
   .\\qrun.bat .\\tools\\document_processor.py "archivo.pdf"
   ```

2. **Reportar al usuario**:
   ```
   ⚠️ ERROR: Extractor de PDF falló
   
   Archivo: [nombre del PDF]
   Error: [mensaje de error completo]
   
   He intentado:
   - Nivel 1 (pypdf): [resultado]
   - Nivel 2 (Tesseract): [resultado]
   - Nivel 3 (Gemini): [resultado]
   
   Necesito que Nzero revise la herramienta.
   ```

3. **Registrar en AGENT_ACTIVITY.md**:
   ```markdown
   | 07-Ene 11:XX | Finn | Error en extractor PDF | documento.pdf | ⚠️ Reportado a usuario |
   ```

4. **NO intentar arreglar**: Esperar instrucciones

---

## 📊 Ejemplos de Uso

### Ejemplo 1: Procesar Comprobante Bancario

```python
from qaicore.tools import extract_content

# PDF escaneado sin texto
text = extract_content('c:\\temp_files\\Comprobante_1110644516.pdf')

# Output esperado:
# Santiago, 7 de enero de 2026
# Comprobante de transferencia de fondos
# N° de comprobante: 1110644516
# Monto transferido: $50.000
# ...
```

### Ejemplo 2: Procesar Estatutos

```python
# PDF con texto embebido
text = extract_content('c:\\docs\\ESTATUTOS_QAI_COMPANY.pdf')

# Output esperado:
# Gobierno de Chile
# Ministerio de Economía...
# CERTIFICADO DE ESTATUTO ACTUALIZADO
# ...
```

---

## 🔧 Troubleshooting

### Error: "Token has been expired or revoked"

**Causa**: Token de Google Drive expirado (no afecta OCR)  
**Solución**: Ver `/QaiCore/tools/TROUBLESHOOTING_GDRIVE.md`

### Error: "Tesseract not found"

**Causa**: Tesseract no está en PATH  
**Acción**: Reportar a usuario (ya debería estar instalado)

### Error: "GEMINI_API_KEY no configurada"

**Causa**: Variable de entorno no está configurada  
**Acción**: Reportar a usuario (solo afecta Nivel 3)

### Error: "429 RESOURCE_EXHAUSTED"

**Causa**: Cuota de Gemini API excedida  
**Acción**: Reportar a usuario, Tesseract seguirá funcionando

---

## 📝 Registro de Uso

**Siempre registra en AGENT_ACTIVITY.md**:

```markdown
| DD-Mes HH:MM | [Agente] | Procesado PDF | [nombre_archivo.pdf] | ✅ [X caracteres extraídos] |
```

**Ejemplo**:
```markdown
| 07-Ene 10:30 | Finn | Procesado PDF | Comprobante_1110644516.pdf | ✅ 622 caracteres |
```

---

## 🔐 Seguridad

### API Keys
- ✅ Gemini API key "backoffice" configurada como variable de entorno
- ❌ NUNCA expongas API keys en logs o código
- ✅ Uso pre-autorizado para OCR de documentos financieros/legales

### Protocolo Human-in-the-Loop
- ✅ OCR de documentos: Pre-autorizado
- ❌ Otros usos de Gemini: Requieren aprobación

Ver: `/QaiCore/PROTOCOL_API_KEYS.md`

---

## 📚 Archivos Relacionados

- **Herramienta principal**: `/QaiCore/tools/document_processor.py`
- **Extractor PDF**: `/QaiCore/tools/extractors/pdf.py`
- **Troubleshooting**: `/QaiCore/tools/TROUBLESHOOTING_GDRIVE.md`
- **Protocolo API Keys**: `/QaiCore/PROTOCOL_API_KEYS.md`

---

## ✅ Checklist para Agentes

Antes de usar:
- [ ] Verificar que el archivo existe
- [ ] Usar herramienta oficial (`document_processor.py`)
- [ ] NO modificar código de herramientas

Si falla:
- [ ] Capturar error completo
- [ ] Reportar al usuario con detalles
- [ ] Registrar en `AGENT_ACTIVITY.md`
- [ ] NO intentar arreglar por cuenta propia

Después de usar:
- [ ] Registrar en `AGENT_ACTIVITY.md`
- [ ] Confirmar extracción exitosa al usuario

---

**Última actualización**: 07-Ene-2026  
**Mantenedor**: Nzero  
**Contacto para issues**: Reportar a usuario (Alejandro)
