# Playbook: Procesar Tarea Legal del INBOX

> **Workflow para que Lex (o cualquier agente) procese tareas legales pendientes**

---

## 🎯 Objetivo

Procesar automáticamente tareas marcadas con `[Legal]` en el INBOX de Torre de Control.

---

## 🔄 Trigger (Cuándo ejecutar)

- Hay una tarea con tag `[Legal]` en `/TorreDeControl/INBOX.md`
- Usuario solicita explícitamente: "Procesa el INBOX legal"

---

## 📋 Pre-requisitos

- Lex agent cargado con `system_prompt.md`
- Acceso a `/TorreDeControl/` y knowledge_base

---

## 🛠️ Pasos del Workflow

### 1. Leer Contexto Inicial
```markdown
ACCIÓN: Leer STATUS.md e INBOX.md

EJEMPLO:
- Abrir /TorreDeControl/STATUS.md
- Abrir /TorreDeControl/INBOX.md
- Buscar tareas con [ ] [Legal] o similar

SALIDA ESPERADA:
- Lista de tareas legales pendientes
- Contexto del estado actual de la empresa
```

---

### 2. Identificar Tarea Prioritaria
```markdown
CRITERIO DE PRIORIDAD:
1. Urgencias (plazos legales críticos)
2. Tareas con documentos adjuntos
3. Consultas simples

ACCIÓN:
- Seleccionar primera tarea urgente
- Si hay múltiples, preguntar al usuario cuál procesar primero
```

---

### 3. Clasificar Tipo de Tarea

**Tipo A: Consulta Tributaria/Legal**
```markdown
EJEMPLO:
- [ ] [Legal] ¿Cuándo debo hacer primera declaración IVA?
- [ ] [Legal] ¿Necesito patente municipal para mis giros?

PROCESO:
→ IR A PASO 4A
```

**Tipo B: Revisión de Documento**
```markdown
EJEMPLO:
- [ ] [Legal] Revisar contrato FedEx (/docs/contrato_fedex.pdf)
- [ ] [Legal] Analizar MOU Gestión Zen (/docs/mou_gz.docx)

PROCESO:
→ IR A PASO 4B
```

**Tipo C: Generar Documento**
```markdown
EJEMPLO:
- [ ] [Legal] Crear borrador contrato servicios para nuevo cliente
- [ ] [Legal] Redactar carta autorización domicilio

PROCESO:
→ IR A PASO 4C
```

---

### 4A. Procesar Consulta Tributaria/Legal

```python
# PASO 1: Consultar knowledge_base
knowledge_base_path = "/QaiCore/agents/lex/knowledge_base/"

# Buscar archivo relevante
if "IVA" in query or "F29" in query:
    read("codigo_tributario_chile_resumen.md")
elif "SpA" in query or "sociedad" in query:
    read("ley_sociedades_spa.md")
elif "constitucion" in query:
    read("casos/constitucion_qai_2025.md")

# PASO 2: Formular respuesta
response = f"""
He revisado el STATUS. Veo que [contexto relevante].

Consultando knowledge_base...

Según [fuente]:
- [Respuesta específica con citas]
- [Plazos si aplican]
- [Recomendaciones]

IMPORTANTE: [Disclaimers o validaciones necesarias]
"""

# PASO 3: Actualizar INBOX
mark_task_as_completed("[Legal] [descripción tarea]")

# PASO 4: Actualizar STATUS
append_to_status(f"✅ {date}: Consulta legal respondida - Lex")
```

**SALIDA ESPERADA**:
- Respuesta fundamentada al usuario
- Tarea marcada como `[x]` en INBOX
- Nota en STATUS

---

### 4B. Procesar Revisión de Documento

```python
from qaicore.tools import extract_content, get_file_info

# PASO 1: Obtener ruta del documento
doc_path = extract_path_from_task()  # ej: "/docs/contrato_fedex.pdf"

# PASO 2: Verificar documento
info = get_file_info(doc_path)
print(f"Documento: {info['name']}, Tamaño: {info['size_mb']} MB")

# PASO 3: Extraer contenido
text = extract_content(doc_path, format_for_llm=True)

#PASO 4: Analizar (buscar cláusulas problemáticas)
red_flags = ["penalidad", "jurisdicción", "exclusividad", "renovación automática"]
issues = []

for flag in red_flags:
    if flag in text.lower():
        issues.append(find_clause_context(text, flag))

# PASO 5: Generar análisis
analysis = f"""
# Análisis Legal: {info['name']}

**Fecha**: {date}
**Analizado por**: Lex
**Tipo**: Contrato B2B

## 🔴 Riesgos Altos
{format_issues(issues, level="alto")}

## 🟡 Riesgos Medios
{format_issues(issues, level="medio")}

## ✅ Aspectos Aceptables
{format_acceptable_clauses(text)}

## 📝 Recomendaciones
1. [Acción específica]
2. [Acción específica]
3. [Si requiere abogado externo]

## 📎 Anexos
- Documento original: {doc_path}
- Cláusulas extraídas: [ver abajo]
"""

# PASO 6: Guardar análisis
save_file(f"/TorreDeControl/analisis_{info['name']}.md", analysis)

# PASO 7: Actualizar INBOX y STATUS
mark_task_as_completed()
update_status(f"✅ Contrato {info['name']} analizado → Ver /TorreDeControl/analisis_...")
```

**SALIDA ESPERADA**:
- Archivo `analisis_[nombre].md` creado en TorreDeControl
- Tarea marcada como `[x]`
- STATUS actualizado con link al análisis

---

### 4C. Generar Documento (Placeholder - Futuro)

```markdown
ESTADO: NO IMPLEMENTADO AÚN

RAZÓN: Requiere plantillas aprobadas por abogado externo

ALTERNATIVA POR AHORA:
1. Lex sugiere términos clave a incluir
2. Referencias a plantillas en knowledge_base/plantillas/
3. Usuario o abogado externo redacta versión final
```

---

## 5. Notificar Usuario

```markdown
Si la tarea SE COMPLETÓ:
"✅ Tarea legal procesada: [Descripción]
Ver resultado en: [Ruta]"

Si REQUIERE VALIDACIÓN EXTERNA:
"⚠️ Tarea procesada con análisis preliminar.
REQUIERE revisión por abogado externo antes de firmar/enviar."

Si NO SE PUDO PROCESAR:
"❌ No pude procesar la tarea por: [Razón]
Acción sugerida: [Qué hacer]"
```

---

## ✅ Criterios de Éxito

- Tarea marcada como `[x]` en INBOX
- Respuesta/análisis generado (según tipo)
- STATUS.md actualizado con resultado
- Usuario notificado con siguiente acción clara

---

## 🚨 Casos Especiales

### Si el documento es muy grande (>20 páginas)
```
1. Extraer solo primeras 10 páginas
2. Analizar secciones críticas (cláusulas tipo)
3. Avisar que es análisis parcial
```

### Si no hay info en knowledge_base
```
1. Reconocer limitación
2. Sugerir fuentes externas confiables (SII, BCN)
3. Ofrecer preparar las preguntas clave
```

### Si hay urgencia legal real
```
1. Escalar inmediatamente con tag ⚠️ URGENTE
2. No procesar si hay riesgo legal alto sin validación
```

---

**Versión**: 1.0  
**Creado**: 26-Dic-2025  
**Próxima actualización**: Cuando se agreguen más tipos de tareas
