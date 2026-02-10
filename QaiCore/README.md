# QaiCore - Infraestructura de Agentes IA

> **"Herramientas compartidas para que los no-gentes trabajen con eficiencia."**

---

## 🎯 ¿Qué es QaiCore?

QaiCore es la **biblioteca compartida** de The QAI Company que permite a los agentes IA (los "no-gentes") acceder a:
- **Herramientas de extracción** de documentos (PDF, Word, Excel, imágenes, etc.)
- **Perfiles de agentes especializados** (Lex-Legal, Finn-Finanzas, Builder-Dev)
- **Flujos de trabajo** (playbooks) estandarizados
- **Bases de conocimiento** específicas por dominio

---

## 📂 Estructura

```
/QaiCore/
├─ /tools/                          → Herramientas compartidas
│  ├─ document_processor.py         → 🔧 PUNTO DE ENTRADA PRINCIPAL
│  ├─ pdf_utils.py                  → 📑 Utilidades PDF (Merge/Split)
│  ├─ /extractors/
│  │  ├─ pdf.py                     → PDFs (con OCR Gemini)
│  │  ├─ docx.py                    → Word
│  │  ├─ pptx.py                    → PowerPoint
│  │  ├─ excel.py                   → Excel (con conversión a Markdown)
│  │  ├─ csv_parser.py              → CSV
│  │  └─ ocr.py                     → Imágenes (OCR con Gemini Vision)
│  └─ requirements.txt              → Dependencias
│
├─ /agents/                         → Perfiles de agentes especializados
│  ├─ /lex/                         → Agente Legal
│  │  ├─ profile.md                 → Quién es, qué hace
│  │  ├─ system_prompt.md           → Instrucciones para carga en IDE
│  │  ├─ tools.json                 → Configuración y permisos
│  │  └─ /knowledge_base/           → Docs legales de referencia
│  │     ├─ codigo_tributario_chile_resumen.md
│  │     └─ ...
│  ├─ /finn/                        → (Futuro) Agente Financiero
│  └─ /builder/                     → (Futuro) Agente Desarrollador
│
└─ /playbooks/                      → Flujos de trabajo ejecutables
    ├─ process_inbox_task.md         → Cómo procesar tareas del INBOX
    ├─ process_financial_inbox.md    → Gestión de facturas y gastos
    └─ coordinacion_inbox.md         → Protocolo de Landing Zone y Roles
```

---

## 🚀 Inicio Rápido

### Para Humanos (Alejandro)

**1. Setup del entorno (Windows, recomendado)**

Ejecuta el setup automático (crea `.venv`, instala dependencias y Chromium para PDFs de alta calidad):

```bat
cd C:\Users\abustamante\TheQaiCo\QaiCore
setup_windows.bat
```

**Alternativa manual**
```bash
cd /path/to/TheQaiCo/QaiCore
python -m venv .venv
.venv\\Scripts\\python.exe -m pip install -r requirements.txt
.venv\\Scripts\\python.exe -m playwright install chromium
```

**2. Configurar API Key (para OCR)**
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="tu-api-key-aqui"

# Windows CMD
set GEMINI_API_KEY=tu-api-key-aqui

# Linux/Mac
export GEMINI_API_KEY="tu-api-key-aqui"
```

**3. Probar Extracción Simple**
```bash
.\\qrun.bat .\\tools\\document_processor.py "C:/ruta/documento.pdf"
```

**4. Probar Propuesta PDF (calidad alta)**
```bash
.\\qrun.bat -m tools.proposal_pdf --help
```

> Nota: usa siempre `qrun.bat` para asegurar `.venv`.

Notas de portabilidad:
- Puedes ejecutar `qrun.bat` desde el root del repo con `.\\QaiCore\\qrun.bat ...`.
- `qrun.bat` configura `PYTHONPATH` para que `-m tools.*` funcione desde cualquier carpeta.

---

### Para Agentes IA

**Cargar un Agente (Ejemplo: Lex)**
```markdown
1. Abre IDE (Antigravity, Cursor, etc.)
2. Lee y carga /QaiCore/agents/lex/system_prompt.md completo
3. Listo! Ya puedes procesar tareas legales
```

**Usar Herramientas de Extracción**
```python
from qaicore.tools import extract_content

# Ejemplo 1: Extraer texto de PDF
text = extract_content("contrato.pdf")

# Ejemplo 2: Extraer Excel como Markdown (para LLMs)
table_md = extract_content("datos.xlsx", format_for_llm=True)

# Ejemplo 3: OCR de imagen
text = extract_content("factura_escaneada.jpg")
```

---

## 📖 Documentación por Componente

### 1. Tools (Herramientas)

#### `document_processor.py` ⭐ PRINCIPAL
**Función**: `extract_content(file_path, format_for_llm=False)`

**Formatos Soportados**:
- Texto: `.pdf`, `.docx`, `.pptx`
- Datos: `.xlsx`, `.xls`, `.csv`
- Imágenes: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`

**Ejemplo**:
```python
# Detecta automáticamente el tipo
content = extract_content("cualquier_archivo.pdf")
```

**Ver**: [tools/document_processor.py](tools/document_processor.py)

---

#### `time_utils.py` ⭐ GESTIÓN DE TIEMPO

**Funciones Principales**:
- `get_current_context()` → Retorna fecha/hora en lenguaje natural
- `prioritize_tasks(tasks)` → Ordena tareas por urgencia
- `calculate_task_urgency(task)` → Analiza deadline y días restantes

**Uso**:
```python
from qaicore.tools import get_current_context, prioritize_tasks

# Contexto temporal
print(get_current_context())
# → "Hoy es Jueves 26 de Diciembre de 2025, 13:15"

# Priorizar tareas del INBOX
tareas = [
    "- [ ] Revisar contrato (hasta 28-Dic)",
    "- [ ] Tarea sin deadline"
]
priorizadas = prioritize_tasks(tareas)
# → Ordena por urgencia con indicadores 🔴🟠🟡🟢
```

**Formatos de Fecha Soportados**:
- `15-Dic` o `15/12/2025` o `2025-12-15`
- `hasta 15 de diciembre` (lenguaje natural)

**Ver**: [tools/time_utils.py](tools/time_utils.py) | [Ejemplos](tools/time_utils_examples.md)

---

#### Extractors Específicos

| Módulo | Función | Uso |
|:---|:---|:---|
| `pdf.py` | `extract_text_from_pdf()` | PDFs con fallback a OCR Gemini |
| `docx.py` | `extract_text_from_docx()` | Word con tablas |
| `pptx.py` | `extract_text_from_pptx()` | PowerPoint con tablas |
| `excel.py` | `extract_data_from_excel()`<br>`excel_to_markdown_table()` | Excel como dict o markdown |
| `csv_parser.py` | `extract_data_from_csv()`<br>`csv_to_markdown_table()` | CSV como dict o markdown |
| `ocr.py` | `extract_text_from_image()` | OCR con Gemini Vision |

**Nota**: Usa `document_processor.extract_content()` en vez de llamar extractors directamente (salvo casos avanzados).

---

### 2. Agents (Agentes Especializados)

#### Nzero - Agente Arquitecto ✅ Operativo

**Especialización**: Diseño de Sistemas y Memoria Institucional

**Capacidades**:
- Decisiones arquitecturales (estructura de QaiCore)
- Documentación de ADRs (Architecture Decision Records)
- Análisis empresarial (fortalezas, debilidades)
- Preservación de contexto entre sesiones

**Cómo Usar**:
1. Lee [`/agents/nzero/system_prompt.md`](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/system_prompt.md)
2. Carga prompt completo en tu IDE
3. Consulta como: "Nzero, analiza la estructura actual"

**Knowledge Base**: 
- Design Decisions (ADRs)
- Company Analysis
- Lessons Learned
- Context for AI

---

#### Lex - Agente Legal ✅ Operativo

**Especialización**: Derecho Comercial y Tributario Chileno

**Capacidades**:
- Consultas tributarias (IVA, F29, Pro Pyme)
- Revisión de contratos (análisis de riesgos)
- Recordatorios de cumplimiento legal

**Cómo Usar**:
1. Lee [`/agents/lex/system_prompt.md`](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/lex/system_prompt.md)
2. Carga prompt completo en tu IDE
3. Consulta como: "Lex, ¿cuándo debo declarar IVA?"

**Knowledge Base**: 
- Código Tributario Chile (resumen)
- Ley de Sociedades SpA
- Casos de QAI

---

#### Finn - Agente Financiero ✅ Operativo

**Especialización**: Gestión de Tesorería, Facturación y Runway

**Capacidades**:
- Registro diario de gastos/ingresos en GSheets
- Generación de correos de cobranza y seguimiento (Templates)
- Análisis de Runway y P&L

---

#### Builder - Agente Desarrollador 🚧 Futuro

**Próximamente**: Deployment, code review, debugging asistido

---

### 3. Playbooks (Flujos de Trabajo)

#### Financieros (Finn)

- **`registrar_gasto_ingreso.md`**: Workflow paso a paso para registrar operaciones financieras diarias
- **`facturar_cliente_saas.md`**: Flujo completo desde OC hasta cobranza de facturación SaaS

#### Legales (Lex)

- **`process_inbox_task.md`**: Procesa automáticamente tareas del `/TorreDeControl/INBOX.md`
  - Tipos: Consulta legal/tributaria, Revisión de documento, Generar documento

#### Financieros/Legales

- **`coordinacion_inbox.md`**: Protocolo de *Triage* y flujo de Landing Zone (`temp_files`) para asignación de tareas a agentes especialistas (Nzero).

---

### 4. Herramientas Core (Tools)

- **`gdrive.py`**: Interacción completa con Google Drive.
- **`gmail.py`**: Envío de emails corporativos vía Gmail API (requiere token OAuth2).
- **`pdf_utils.py`**: Utilidades para manipulación de PDFs (Merge).
- **`generate_all_pdfs.py`**: 💎 **Motor de Alta Fidelidad** para entregables premium (Deck y Propuesta) en 16:9 y A4.
- **`document_processor.py`**: Extracción y análisis de documentos (PDF, DOCX, OCR).

- **`process_financial_inbox.md`**: Procesa tareas financieras del INBOX

**Ver**: [playbooks/README.md](playbooks/README.md) para lista completa y detalles

---

## 🛠️ Uso Avanzado

### Extender con Nuevo Agente

```markdown
1. Crear /QaiCore/agents/[nombre]/
2. Crear profile.md (basado en lex/profile.md)
3. Crear system_prompt.md
4. Crear knowledge_base/ con docs relevantes
5. Crear tools.json
6. Actualizar este README
```

### Agregar Nuevo Extractor

```python
# Crear: /tools/extractors/nuevo_formato.py

def extract_from_nuevo_formato(file_path: str) -> str:
    # Tu lógica
    return extracted_text

# Luego agregarlo a document_processor.py:
extractors = {
    '.nuevo': lambda: extract_from_nuevo_formato(file_path),
    # ... otros
}
```

---

## 🔐 Seguridad y Buenas Prácticas

### API Keys
```bash
# NUNCA hagas commit de API keys
# Usa variables de entorno:
GEMINI_API_KEY=xxx
```

### Permisos de Agentes
Cada agente tiene permisos definidos en `tools.json`:
```json
{
  "permissions": {
    "read": ["/TorreDeControl/**"],
    "write": ["/TorreDeControl/analisis_*.md"],
    "forbidden": ["/QaiProd/**"]
  }
}
```

---

## 📊 Métricas y Monitoreo

### Costos Estimados (OCR con Gemini)

| Volumen Mensual | Costo Aprox (USD) |
|:---|---:|
| 10 PDFs escaneados | $0.50 |
| 50 PDFs escaneados | $2.50 |
| 100 PDFs escaneados | $5.00 |

**Nota**: PDFs con texto extraíble NO usan Gemini (gratis).

---

## 🐛 Troubleshooting

### Error: "GEMINI_API_KEY no configurada"
```bash
# Configura la variable de entorno
export GEMINI_API_KEY="your-key"
```

### Error: "Librería faltante 'x'"
```bash
pip install -r requirements.txt
```

### OCR de PDF no funciona
```
1. Verifica que pdf2image esté instalado
2. En Windows, instala Poppler: 
   https://github.com/oschwartz10612/poppler-windows/releases/
3. Agrega Poppler a PATH
```

---

## 🔄 Roadmap

### ✅ Completado (V1.0 - Dic 2025)
- [x] Extractores para 7 formatos (PDF, DOCX, PPTX, Excel, CSV, imágenes)
- [x] OCR con Gemini Vision API
- [x] Agente Lex (Legal) completo
- [x] Playbook de procesamiento de INBOX

### 🚧 En Progreso
- [ ] Agente Finn (Financiero)
- [ ] Tests automatizados para extractors
- [ ] Migrar código de Invoice-Match y Gestión Zen a QaiProd

### 💡 Futuro (2026)
- [ ] RAG con embeddings para knowledge bases grandes
- [ ] Agente Builder (Dev)
- [ ] UI web para invocar agentes
- [ ] Sistema multi-agente con coordinación

---

## 📞 Soporte

**Para usuarios internos (Alejandro)**:
- Pregunta directamente al agente correspondiente en el IDE
- Revisa `/TorreDeControl/STATUS.md` para estado actual

**Para contribuciones externas**:
- Por ahora: sistema interno, no abierto a contribuciones

---

## 📝 Changelog

### V1.1 (02-Ene-2026)
- ✨ Implementación de Landing Zone (`temp_files`) y Protocolo de Triage.
- ✨ Sistema de Templates para correos corporativos (FedEx, Socios).
- ✨ Definición de roles y facultades por agente (Nzero, Finn, Lex).
- ✨ Agente Finn marcado como operativo con integraciones GSheets.

### V1.0 (26-Dic-2025)

---

**Mantenido por**: The QAI Company (Ale + Agentes)  
**Licencia**: Privado (uso interno)  
**Última actualización**: 02-Ene-2026
