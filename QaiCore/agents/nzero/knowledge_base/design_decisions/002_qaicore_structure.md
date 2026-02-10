# ADR-002: Estructura Modular QaiCore

**Fecha**: 2025-12-26  
**Estado**: Aceptado  
**Contexto**: Necesitábamos organizar herramientas, agentes y workflows de forma escalable y reutilizable.

---

## Problema

**Situación inicial**:
- Código disperso en múltiples lugares
- Cada agente reinventaba extractores de documentos
- No había knowledge bases compartidas
- Difícil agregar nuevos agentes

**Impacto**:
- Duplicación masiva de código
- Inconsistencias entre agentes
- Setup de nuevo agente toma días

---

## Alternativas Consideradas

### Opción 1: Un solo agente monolítico "SuperAgent"
**Pros**:
- ✅ Simple de implementar inicialmente

**Cons**:
- ❌ No escala (un agente no puede ser experto en todo)
- ❌ Context window explota rápidamente
- ❌ Difícil mantener

---

### Opción 2: Agentes independientes con código duplicado
**Pros**:
- ✅ Autonomía total por agente

**Cons**:
- ❌ Duplicación masiva (cada uno su PDF extractor)
- ❌ Inconsistencias de calidad
- ❌ Cambios deben replicarse manualmente

---

### Opción 3: Biblioteca compartida + Agentes especializados ⭐ **ELEGIDA**

**Descripción**: Crear `/QaiCore/` con:
- `/tools/`: Herramientas compartidas (extractors, utils)
- `/agents/`: Perfiles especializados por dominio
- `/playbooks/`: Workflows estandarizados

**Pros**:
- ✅ DRY (Don't Repeat Yourself)
- ✅ Especialización por dominio
- ✅ Escalable (agregar agente = <1 hora)
- ✅ Calidad consistente en extractors

**Cons**:
- ❌ Requiere más setup inicial
- ❌ Cambio en tools afecta a todos

**Por qué se eligió**: Escalabilidad > simplicidad inicial. Inversión de 1 día ahorra semanas futuras.

---

## Decisión

### Estructura Final

```
/QaiCore/
├─ /tools/                  → Herramientas compartidas
│  ├─ document_processor.py  (router principal)
│  ├─ time_utils.py          (temporal awareness)
│  └─ /extractors/
│     ├─ pdf.py
│     ├─ docx.py
│     ├─ excel.py
│     └─ ...
│
├─ /agents/                 → Agentes especializados
│  ├─ /nzero/               (Arquitecto)
│  │  ├─ profile.md
│  │  ├─ system_prompt.md
│  │  ├─ tools.json
│  │  └─ knowledge_base/
│  ├─ /lex/                 (Legal)
│  ├─ /finn/                (Financiero - futuro)
│  └─ /builder/             (Dev - futuro)
│
└─ /playbooks/              → Workflows estandarizados
   ├─ process_inbox_task.md
   ├─ deploy_prod.md
   └─ ...
```

### Principios de Diseño

1. **Separation of Concerns**:
   - Tools = QUÉ herramientas
   - Agents = QUIÉN las usa
   - Playbooks = CÓMO usarlas

2. **Reutilización**:
   - Todos los agentes usan mismo `extract_content()`
   - Knowledge bases independientes por dominio

3. **Especialización**:
   - Lex = Legal (no hace código)
   - Builder = Dev (no hace legal)
   - Nzero = Arquitectura (coordina, no ejecuta)

---

## Consecuencias

### Positivas
- Nuevo agente se crea en <1 hora (vs 1 día antes)
- Extractors mantienen calidad consistente
- Knowledge bases centralizadas por dominio
- Fácil migrar de IDE/LLM (solo cambias quién lee los prompts)

### Negativas / Trade-offs
- Cambio en `/tools/` requiere verificar que no rompe agentes
- Requiere versionado más cuidadoso
- Setup inicial tomó 4-5 horas

### Mitigaciones
- Tests para extractors críticos (futuro)
- Versionado semántico de tools
- Documentación clara en cada componente

---

## Notas de Implementación

**Archivos Creados** (26-Dic-2025):
- 7 extractors en `/tools/extractors/`
- 2 agentes completos (Nzero, Lex)
- 1 playbook (`process_inbox_task.md`)
- `requirements.txt` con dependencias

**Próximos Agentes** (roadmap):
- Finn (Financiero): Q1 2026
- Builder (Dev): Q1 2026

---

## Evolución Futura

**Si QaiCore crece demasiado**:
- Extraer `/tools/` como package PyPI independiente
- Crear `/QaiCore/tests/` con suite completa
- Agregar `/QaiCore/api/` para comunicación inter-agentes

**Por ahora**: Mantener simple, agregar complejidad solo cuando sea necesario.

---

**Autor**: Nzero  
**Participantes**: Alejandro  
**Relacionado con**: ADR-001 (Torre de Control), ADR-003 (Profile vs System Prompt)  
**Creado**: 26-Dic-2025
