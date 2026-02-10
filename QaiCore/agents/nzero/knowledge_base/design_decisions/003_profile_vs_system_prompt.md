# ADR-003: Profile.md vs System_Prompt.md

**Fecha**: 2025-12-26  
**Estado**: Aceptado  
**Contexto**: Al crear agentes especializados (Lex, Nzero), necesitábamos claridad sobre qué documentar y para quién.

---

## Problema

**Confusión inicial**: ¿Qué va en `profile.md` vs `system_prompt.md`?

**Riesgo de**:
- Duplicar información
- Archivos gigantes e ilegibles
- No saber cuál actualizar cuando cambia algo

---

## Alternativas Consideradas

### Opción 1: Un solo archivo "README.md" por agente
**Pros**:
- ✅ Simple, todo en un lugar

**Cons**:
- ❌ Mezcla audiencias (humanos vs agente)
- ❌ Se vuelve gigante (50+ páginas)
- ❌ Agente debe leer info irrelevante para él

---

### Opción 2: profile.md + system_prompt.md separados ⭐ **ELEGIDA**

**Separación clara por audiencia**:

| Archivo | Audiencia | Propósito | Tono |
|:---|:---|:---|:---|
| `profile.md` | Humanos | Job Description | Descriptivo |
| `system_prompt.md` | El agente | Manual de Procedimientos | Imperativo |

**Pros**:
- ✅ Cada archivo con propósito claro
- ✅ Agente no lee documentación humana
- ✅ Humanos no leen detalles operativos del agente

**Cons**:
- ❌ Dos archivos para mantener

**Por qué se eligió**: Separación de responsabilidades > conveniencia de un solo archivo.

---

## Decisión

### profile.md (Para Humanos)

**Contenido**:
- ✅ Identidad y especialización
- ✅ Responsabilidades (qué hace, qué NO hace)
- ✅ Estructura de knowledge base
- ✅ Métricas de éxito
- ✅ Historial de versiones

**Ejemplo de uso**:
```
"Hmm, ¿qué hace Lex exactamente?"
→ Lees profile.md y entiendes su role
```

**Formato**: Documentación limpia, breve (~100 líneas)

---

### system_prompt.md (Para el Agente)

**Contenido**:
- ✅ Protocolo obligatorio (qué hacer SIEMPRE al inicio)
- ✅ Ejemplos de interacción (input/output concretos)
- ✅ Casos especiales y edge cases
- ✅ Tono y estilo de comunicación
- ✅ Límites y disclaimers

**Ejemplo de uso**:
```
"Hola, carga /QaiCore/agents/lex/system_prompt.md"
→ El agente lee todo y sabe exactamente cómo comportarse
```

**Formato**: Instrucciones explícitas, detallado (~200+ líneas)

---

## Reglas de Oro

### Actualizar profile.md cuando:
- Cambias responsabilidades del agente
- Agregas/quitas herramientas
- Cambias métricas de éxito
- Cambias estructura de knowledge base

### Actualizar system_prompt.md cuando:
- Descubres que el agente olvida hacer algo
- Necesitas agregar nuevo caso especial
- Cambias el protocolo operativo
- Ajustas tono/estilo

### NO duplicar:
- Información en ambos archivos (elige dónde va)
- Si cambias uno, verifica si el otro necesita ajuste

---

## Consecuencias

### Positivas
- Claridad total sobre qué documentar dónde
- Humanos no saturados con detalles operativos
- Agentes no leen "marketing" innecesario
- Onboarding rápido (lee profile, usa system_prompt)

### Negativas / Trade-offs
- Requiere disciplina de actualización
- Riesgo de desincronización si no se mantienen

### Mitigaciones
- Revisión trimestral de ambos archivos
- Al cambiar agente, preguntarse: "¿Afecta profile o prompt?"

---

## Analogía

**profile.md** = Job Description de un empleado  
*"Lex es responsable de consultas legales..."*

**system_prompt.md** = Manual de Procedimientos del empleado  
*"AL INICIAR: 1) Lee STATUS.md, 2) Lee INBOX.md, 3) Menciona fecha..."*

---

## Notas de Implementación

**Agentes Creados con este patrón**:
- Nzero (Arquitecto)
- Lex (Legal)

**Futuros** (usar mismo patrón):
- Finn (Financiero)
- Builder (Dev)

---

## Alternativas Futuras

Si la separación se vuelve problemática:
- Generar `system_prompt.md` automáticamente desde `profile.md` + templates
- Usar YAML front-matter en un solo archivo con secciones

Por ahora: **Simplicidad > automatización**.

---

**Autor**: Nzero  
**Participantes**: Alejandro  
**Relacionado con**: ADR-002 (QaiCore Structure)  
**Creado**: 26-Dic-2025
