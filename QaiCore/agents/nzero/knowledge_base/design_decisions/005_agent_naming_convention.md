# ADR-005: Convención de Nombres de Agentes (CFO → Finn)

**Fecha**: 2025-12-26  
**Estado**: Aceptado  
**Contexto**: Buscamos nombres autoexplicativos y fáciles de invocar para los no-gentes. El acrónimo "CFO" es correcto pero menos natural en prompts. Se decide usar nombres amigables, empezando por renombrar el agente financiero a "Finn".

---

## Problema

- Los acrónimos (CFO, CTO, etc.) son estándar pero menos conversacionales.  
- En invocación diaria, nombres cortos y humanos reducen fricción ("Finn, revisa flujo de caja...").  
- Se requiere un precedente claro para futuras creaciones de agentes.

---

## Alternativas Consideradas

### Opción 1: Mantener acrónimos funcionales (p.ej., CFO)
- ✅ Estándar corporativo global  
- ❌ Menos amigable para prompts y multi-idioma  
- ❌ Puede generar confusión en documentos no técnicos

### Opción 2: Nombres amigables por rol/persona (p.ej., Finn) ⭐ ELEGIDA
- ✅ Invocación natural en conversaciones y prompts  
- ✅ Identidad clara y memorable  
- ❌ Requiere documentar alias y actualizar referencias  
- ❌ Riesgo de inconsistencia sin convención

### Opción 3: Nombres descriptivos largos (p.ej., "Agente Financiero")
- ✅ Claridad semántica  
- ❌ Poco práctico para invocar y para rutas de carpeta

---

## Decisión

Adoptar **nombres amigables y únicos** para los agentes, manteniendo un **alias funcional** cuando sea útil.

- Canonical: "Finn" (Agente Financiero)  
- Alias aceptado: "CFO"  
- Carpeta futura: `/QaiCore/agents/finn/` (cuando se cree el agente)  
- Documentos: usar "Finn (Agente Financiero)" como forma preferida

---

## Consecuencias

### Positivas
- Menor fricción al invocar agentes en sesiones  
- Identidades consistentes y memorables  
- Precedente claro para futuros agentes (Builder, Rainmaker, etc.)

### Trade-offs
- Necesita actualización de documentación existente  
- Requiere mantener mapeo de alias donde sea relevante

---

## Implementación y Alcance

1. Actualizar documentación a "Finn" en repositorio (completado).  
2. Mantener alias "CFO" en textos explicativos cuando agregue claridad.  
3. Al crear el agente: estructura estándar `profile.md`, `system_prompt.md`, `tools.json`, `knowledge_base/` bajo `/agents/finn/`.  
4. En prompts humanos/IA, preferir: "Finn, [acción]".

---

## Reglas de Naming (Guía Rápida)

- **Canonicals**: 1 palabra, corta, fácil de pronunciar (p.ej., Finn, Lex, Nzero).  
- **Rol visible**: En paréntesis al presentarlo (p.ej., "Finn (Agente Financiero)").  
- **Aliases**: Mantener acrónimo funcional si es estándar (p.ej., CFO → Finn).  
- **Rutas**: Carpeta coincide con el canonical (p.ej., `/agents/finn/`).

---

## Migración

- Reemplazar menciones directas de "CFO" por "Finn" en docs operativos;  
- Donde aporte contexto, dejar "Finn (alias: CFO)";  
- Referenciar este ADR desde nuevas guías de estilo si aplica.

---

## Estado de Ejecución

- Documentación actualizada a "Finn" en QaiCore, Torre de Control y Empresa.  
- Carpeta de agente `finn/` pendiente de creación (se hará al activar el agente financiero).
