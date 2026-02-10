# ADR-001: Torre de Control - Memoria Compartida para Agentes

**Fecha**: 2025-12-26  
**Estado**: Aceptado  
**Contexto**: Como solopreneur trabajando con múltiples agentes IA en diferentes sesiones, se perdía contexto crítico entre conversaciones.

---

## Problema

**Síntoma**: Cada nueva sesión con un agente requería re-explicar:
- Estado actual de la empresa
- Tareas pendientes
- Decisiones tomadas previamente
- Progreso en proyectos

**Impacto**: 
- 15-30 min perdidos al inicio de cada sesión
- Riesgo de inconsistencias (agente A no sabe lo que hizo agente B)
- No había "single source of truth"

---

## Alternativas Consideradas

### Opción 1: Repetir contexto manualmente cada sesión
**Pros**:
- ✅ Simple, sin setup

**Cons**:
- ❌ Ineficiente (pierde tiempo)
- ❌ Propenso a errores (olvidas mencionar algo)
- ❌ No escala (más agentes = más repetición)

---

### Opción 2: Documento único mega-completo
**Pros**:
- ✅ Todo en un lugar

**Cons**:
- ❌ Se vuelve gigante e ilegible
- ❌ Difícil mantener actualizado
- ❌ Agente debe leer 50 páginas cada vez

---

### Opción 3: Sistema "Torre de Control" ⭐ **ELEGIDA**
**Descripción**: Directorio `/TorreDeControl/` con archivos específicos que TODO agente lee al inicio.

**Pros**:
- ✅ Modular (STATUS, INBOX, CHANGELOG separados)
- ✅ Fácil de actualizar (agentes escriben en archivos específicos)
- ✅ Escalable (agregar nuevo agente = leer mismos archivos)
- ✅ Protocolo claro: "SIEMPRE leer STATUS + INBOX al inicio"

**Cons**:
- ❌ Requiere disciplina (agentes deben seguir protocolo)
- ❌ Setup inicial (crear estructura)

**Por qué se eligió**: Balance entre simplicidad y efectividad. 80% del contexto en <5 archivos.

---

## Decisión

Crear `/TorreDeControl/` con:

1. **STATUS.md**: Dashboard del estado actual
   - Empresa (legal, admin)
   - Clientes y proyectos
   - Productos
   - Financiero
   - Prioridades semanales

2. **INBOX.md**: Buzón de tareas pendientes
   - Urgente (esta semana)
   - Importante (este mes)
   - Ideas / Backlog
   - Completado

3. **CHANGELOG.md**: Hitos y decisiones importantes
   - Solo eventos que querrás recordar en 3-6 meses
   - No tareas rutinarias

4. **AGENT_ACTIVITY.md**: Registro cronológico de acciones
   - Trazabilidad de qué hizo cada agente y cuándo.

5. **DISCOVERY_LOG.md**: Hallazgos y señales de alto ancho de banda
   - Evita perder "Eurekas" o cambios en playbooks.

**Protocolo obligatorio** para TODOS los agentes:
```markdown
88: 1. Leer STATUS.md
89: 2. Leer INBOX.md
90: 3. Revisar AGENT_ACTIVITY.md y DISCOVERY_LOG.md
91: 4. Mencionar: "He revisado STATUS. Veo que [contexto]"
92: 5. Al finalizar: Actualizar STATUS/INBOX/ACTIVITY según corresponda
```

---

## Consecuencias

### Positivas
- Sesiones arrancan en <2 min (vs 15-30 min antes)
- Agentes tienen contexto consistente
- Founder puede cambiar de IDE/LLM sin perder continuidad
- Base para coordinación multi-agente futura

### Negativas / Trade-offs
- Requiere disciplina de actualización
- Si STATUS desactualizado, agentes trabajan con info incorrecta
- Archivos deben mantenerse concisos (riesgo de saturación)

### Mitigaciones
- Protocolo simple de actualización (marcar [x] en INBOX)
- Revisión semanal de STATUS (viernes 5pm)
- CHANGELOG solo para hitos (no crecer infinitamente)
- **Sincronización Multi-Agente**: Mandatorio actualizar metadatos (fechas de cabecera), ser explícitos en el estado de ramas (`main` vs `develop`) y aplicar la **Regla de los 4 Puntos** (Atomicidad: STATUS + INBOX + CHANGELOG + ACTIVITY) para garantizar consistencia absoluta entre agentes.

---

## Notas de Implementación

**Componentes Afectados**:
- Todos los agentes (Nzero, Lex, Finn, Builder)

**Archivos Creados**:
- `/TorreDeControl/STATUS.md`
- `/TorreDeControl/INBOX.md`
124: - `/TorreDeControl/CHANGELOG.md`
125: - `/TorreDeControl/AGENT_ACTIVITY.md`
126: - `/TorreDeControl/DISCOVERY_LOG.md`
127: - `/TorreDeControl/README.md`
128: - `/TorreDeControl/PROMPTS_INICIO.md`

**Código de Ejemplo** (para agentes):
```python
# Al inicio de sesión
status = read_file("/TorreDeControl/STATUS.md")
inbox = read_file("/TorreDeControl/INBOX.md")
print(f"Contexto actual: {extract_key_points(status)}")
```

---

## Alternativas Futuras

Si Torre de Control se vuelve insostenible:
- Migrar a base de datos (SQLite) con queries
- Usar RAG con embeddings para búsqueda semántica
- Crear dashboard web en vez de archivos markdown

Por ahora, simplicidad > sofisticación.

---

**Autor**: Nzero (Antigravity)  
**Participantes**: Alejandro  
**Relacionado con**: ADR-002 (QaiCore Structure)  
**Creado**: 26-Dic-2025
