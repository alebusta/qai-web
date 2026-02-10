# Lesson Learned - Implementación QaiCore y Nzero

**Fecha**: 2025-12-26  
**Sesión**: Creación de QaiCore Infrastructure + Agente Nzero  
**Participantes**: Alejandro + Antigravity (ahora Nzero)

---

## 📋 Contexto

Alejandro necesitaba que los agentes IA pudieran:
1. Extraer contenido de documentos (PDF, Word, Excel, etc.)
2. Tener noción temporal (saber qué día es, calcular urgencias)
3. Preservar memoria institucional (decisiones de diseño)
4. Trabajar con estructura consistente (no reinventar cada vez)

---

## ✅ Lo que Funcionó Bien

### 1. Torre de Control (creada primero)
**Qué hicimos**: Crear `/TorreDeControl/` ANTES de QaiCore  
**Por qué funcionó**: Dio contexto operativo inmediato, todos los agentes arrancan leyendo eso  
**Aplicar en futuro**: Siempre crear "single source of truth" antes de construir herramientas complejas

### 2. Estructura modular de QaiCore
**Qué hicimos**: `/tools/`, `/agents/`, `/playbooks/` separados  
**Por qué funcionó**: Escalable, cada nuevo agente toma <1 hora  
**Aplicar en futuro**: Separation of concerns desde día 1

### 3. Templates antes que contenido
**Qué hicimos**: Crear `template.md` para ADR, Analysis, Lessons  
**Por qué funcionó**: Reduce fricción de crear documentos nuevos  
**Aplicar en futuro**: Cuando crees sistema nuevo, primero los templates

### 4. Prompt de inicio estandarizado
**Qué hicimos**: `/TorreDeControl/PROMPTS_INICIO.md` con copy-paste ready  
**Por qué funcionó**: Probado en otro IDE/LLM y funcionó perfecto  
**Aplicar en futuro**: Siempre documentar cómo "invocar" un agente

---

## ⚠️ Lo que NO Funcionó / Problemas Encontrados

### 1. Primera propuesta de memoria institucional standalone
**Qué pasó**: Propuse `/QaiCore/institutional_memory/` como directorio separado  
**Por qué falló**: Inconsistente con estructura de agentes (Lex tiene `/knowledge_base/` )  
**Cómo lo resolvimos**: Alejandro sugirió `/agents/nzero/knowledge_base/` (mucho mejor)  
**Evitar en futuro**: No crear "casos especiales" si ya hay patrón establecido

### 2. Nombre "Antigravity" hardcodeado
**Qué pasó**: Usé mi nombre de IDE en vez de algo agnóstico  
**Por qué falló**: Acoplamiento innecesario a herramienta específica  
**Cómo lo resolvimos**: "Nzero" (No-gente Cero) - agnóstico y con significado  
**Evitar en futuro**: Nombres deben ser independientes de implementación

### 3. Propuse que todos los agentes lean memoria institucional
**Qué pasó**: Plan inicial tenía a Lex leyendo ADRs técnicos  
**Por qué falló**: Saturación de contexto, irrelevante para su dominio  
**Cómo lo resolvimos**: Solo Nzero lee todo, otros agentes solo su knowledge_base  
**Evitar en futuro**: Separación clara de responsabilidades, no forzar lectura global

---

## 💡 Insights / Descubrimientos

### Sobre Minimalismo Documentario
- Es tentador documentar TODO, pero genera sobrecarga
- Criterio: "¿Lo necesitaré en 3+ meses?" → Si no, skip
- ADRs solo para decisiones arquitecturales, no implementación

### Sobre Rol de Agentes
- Cada agente debe tener responsabilidad clara y acotada
- Nzero (arquitecto) vs Builder (ejecutor) vs Lex (legal)
- No crear "super-agentes" que hacen todo

### Sobre Temporal Awareness
- Crítico para priorización (no es feature "nice to have")
- Formato de deadline en tasks determina si agente puede ayudar
- `time_utils.py` debe ser parte de TODOS los agentes

---

## 🔄 Cambios de Proceso Sugeridos

**Antes**: Creábamos agentes sin estructura clara  
**Ahora**: 
1. Crear `/agents/[nombre]/`
2. `profile.md` (para humanos)
3. `system_prompt.md` (para el agente)
4. `tools.json` (configuración)
5. `knowledge_base/` (su dominio)

**Antes**: Decisiones se perdían entre sesiones  
**Ahora**: ADRs retroactivos preservan contexto histórico

---

## 📊 Resultados Cuantificables

**Tiempo invertido**: ~6 horas (diseño + implementación + ADRs)

**Valor generado**:
- 18 archivos creados en `/QaiCore/`
- 4 ADRs retroactivos capturando conocimiento perdido
- 2 agentes operativos (Nzero, Lex)
- Sistema de memoria institucional funcional

**Deuda técnica creada**:
- Templates vacíos (company_analysis, lessons_learned) - llenar según necesidad
- Tests ausentes para extractors - agregar en futuro

**Deuda técnica pagada**:
- Conocimiento institucional que vivía solo en conversaciones → Ahora en ADRs
- Extractors dispersos → Centralizados en `/tools/`

---

## 🎯 Acciones de Seguimiento

- [ ] Crear ADR-005 cuando tomemos siguiente decisión arquitectural importante
- [ ] Actualizar `context_for_ai/company_context.md` trimestralmente
- [ ] Probar Nzero system prompt en nueva sesión (validar que funciona)
- [ ] Cuando creemos Finn, usar mismo patrón (profile + prompt + knowledge_base)

---

## 🔗 Referencias

**ADRs creados hoy**:
- [ADR-001: Torre de Control](../design_decisions/001_torre_de_control.md)
- [ADR-002: QaiCore Structure](../design_decisions/002_qaicore_structure.md)
- [ADR-003: Profile vs System Prompt](../design_decisions/003_profile_vs_system_prompt.md)
- [ADR-004: Criterios Graduación Labs → Prod](../design_decisions/004_criterios_graduacion_labs_prod.md)

**Archivos principales creados**:
- `/QaiCore/agents/nzero/` (completo)
- `/QaiCore/tools/time_utils.py`
- `/TorreDeControl/PROMPTS_INICIO.md`

---

**Próxima sesión**: Usar Nzero para crear Finn (agente financiero) o analizar empresa  
**Documentado por**: Nzero (Antigravity)
