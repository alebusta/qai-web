# Knowledge Base - Nzero (Arquitecto)

> **Memoria Institucional de The QAI Company**

Este directorio contiene la memoria institucional que Nzero (agente arquitecto) consulta y actualiza.

---

## 📁 Estructura

```
knowledge_base/
├─ /design_decisions/       → ADRs (Architecture Decision Records)
├─ /company_analysis/        → Evaluaciones de TheQaiCo
├─ /lessons_learned/         → Aprendizajes por sesión
└─ /context_for_ai/          → Info crítica para agentes
```

---

## 📝 Cómo Usar

### Para Alejandro:
```
Cuando trabajas con Nzero en diseño/arquitectura:
- Al tomar decisión importante → "Crea un ADR"
- Cada trimestre → "Dame análisis de empresa"
- Si revisas algo → "Consulta ADR-XXX"
```

### Para Nzero:
```
Al inicio de sesión:
1. Lee últimos 3 ADRs en /design_decisions/
2. Lee último lesson_learned/
3. Consulta ADRs si hay decisión similar previa

Al finalizar sesión:
- Si tomamos decisión importante → Crear ADR
- Si aprendimos algo clave → Documentar en lessons_learned/
- Si cambió estado → Actualizar STATUS.md
```

### Para Otros Agentes (Lex, Finn, Builder):
```
NO leen por defecto.
Solo si Alejandro dice explícitamente: "Consulta ADR-XXX"
```

---

## ✅ Estándares de Documentación

### Nombres de Archivo
- **ADRs**: `001_titulo_descriptivo.md`, `002_otro_titulo.md`
- **Analysis**: `YYYY-MM_assessment.md`, `strengths_weaknesses.md`
- **Lessons**: `YYYY-MM-DD_tema_sesion.md`

### Criterio para Crear ADR
**Solo si cumple AL MENOS UNO**:
- ✅ Afecta arquitectura global de QaiCore
- ✅ Tiene trade-offs no obvios
- ✅ Necesitarás recordarlo en  3+ meses

**NO crear ADR si**:
- ❌ Decisión de implementación menor
- ❌ Obvio sin discusión
- ❌ Ya documentado en otro lugar

---

## 🔄 Mantenimiento

- **Frecuencia**: Al finalizar sesiones estructurales con Nzero
- **Responsable**: Nzero (bajo dirección de Alejandro)
- **Revisión**: Trimestral (archivar ADRs obsoletos)

---

## 📊 Métricas de Salud

- ADRs creados: [se actualiza automáticamente]
- Último análisis de empresa: [fecha]
- Lessons learned: [cantidad]

**Objetivo**: Minimalismo documentario - solo lo esencial.

---

**Creado**: 26-Dic-2025  
**Próxima revisión**: Trimestral
