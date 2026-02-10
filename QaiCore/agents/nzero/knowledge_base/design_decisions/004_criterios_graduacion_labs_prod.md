# ADR-004: Criterios de Graduación Labs → Prod

**Fecha**: 2025-12-26 (retroactivo basado en análisis inicial)  
**Estado**: Aceptado  
**Contexto**: Necesitábamos criterios objetivos para decidir cuándo un producto pasa de QaiLabs (validación) a QaiProd (producción).

---

## Problema

**Situación**: Productos como Invoice-Match y Gestión Zen estaban en un limbo:
- Funcionalmente completos
- Con clientes potenciales/pilotos
- Pero sin claridad sobre cuándo "graduarlos"

**Riesgo sin criterios claros**:
- Productos quedan estancados en Labs eternamente
- O se gradúan prematuramente (antes de estar listos)
- Inconsistencias en expectativas de calidad

---

## Alternativas Consideradas

### Opción 1: Graduación por "feeling" del founder
**Pros**:
- ✅ Flexible

**Cons**:
- ❌ Arbitrario
- ❌ No escalable
- ❌ Difícil explicar a terceros (socios, inversores)

---

### Opción 2: Criterios técnicos complejos (100% tests, CI/CD, monitoring, etc.)
**Pros**:
- ✅ Riguroso
- ✅ Alta calidad

**Cons**:
- ❌ Over-engineering para etapa actual
- ❌ Retrasa graduación innecesariamente
- ❌ No refleja realidad de bootstrapped startup

---

### Opción 3: Criterios mínimos viables ⭐ **ELEGIDA**

**Regla simple**: **Si alguien PAGA o firmó compromiso jurídico → PROD**

**Criterios específicos**:
1. ✅ Cliente confirmado con contrato/OC firmada
2. ✅ URL en producción funcionando
3. ✅ SLA informal (respondes bugs en <24hrs)
4. ✅ Código en repositorio (no necesariamente corporativo aún)

**Pros**:
- ✅ Objetivo (sí/no, no subjetivo)
- ✅ Refleja realidad del negocio
- ✅ Fuerza a tener cliente ANTES de sobre-optimizar

**Cons**:
- ❌ Puede graduarse código "no perfecto"
- ❌ Deuda técnica permitida

**Por qué se eligió**: **Validación de mercado > perfección técnica** en etapa de bootstrapping.

---

## Decisión

### Checklist de Graduación

```markdown
## [Producto X] - Graduación Labs → Prod

### ✅ Obligatorios
- [ ] Cliente confirmado (OC firmada o contrato jurídico)
- [ ] URL producción activa y funcional
- [ ] Founder puede responder bugs en <24hrs
- [ ] Código en algún repositorio (recuperable)

### ✅ Recomendados (no bloqueantes)
- [ ] CI/CD básico (auto-deploy)
- [ ] Tests de funcionalidad crítica
- [ ] Documentación de uso para cliente
- [ ] Monitoreo básico (error tracking)

### 🔄 Post-Graduación (iterar)
- [ ] Migrar código a repo corporativo `/QaiProd/`
- [ ] Mejorar tests coverage
- [ ] Implementar monitoreo avanzado
- [ ] SLA formal documentado
```

**Criterio de ejecución**: Si cumple los 4 obligatorios → Graduar HOY, mejorar después.

---

## Casos Reales

### Invoice-Match (FedEx)
**Estado Dic-2025**:
- ✅ Cliente: FedEx Chile (cotización enviada)
- ✅ URL: invoice-match.qai.cl (funcionando)
- ✅ SLA informal: Alejandro responde en <24hrs
- ✅ Código: En repo personal (pendiente mover)

**Decisión**: **GRADUADO A PROD** (aunque código aún no en `/QaiProd/`)

**Próximo paso**: Mover código a `/QaiProd/invoice-match/` esta semana.

---

### Gestión Zen
**Estado Dic-2025**:
- 🟡 Cliente: MOU pendiente de firma con socios JV
- ✅ Producto funcionando
- 🔴 Cliente NO confirmado jurídicamente aún

**Decisión**: **PERMANECE EN LABS** hasta firma de MOU o primer cliente real.

**Trigger de graduación**: Firma de MOU o 1er administrador de condominios pagando.

---

## Consecuencias

### Positivas
- Claridad total sobre cuándo graduar
- Fuerza a validar con clientes ANTES de over-engineer
- Permite "deuda técnica controlada" en early stage
- Facilita comunicación con socios/clientes

### Negativas / Trade-offs
- Código en Prod puede no ser "perfecto"
- Riesgo de bugs en producción
- Presión para iterar rápido post-launch

### Mitigaciones
- SLA informal permite tiempo de respuesta
- Post-graduación se itera hacia mejores prácticas
- Expectativas claras con cliente sobre etapa del producto

---

## Evolución Futura

**Cuando QAI tenga >$5M MRR**, reconsiderar criterios:
- Agregar tests como obligatorio
- Monitoring avanzado requerido
- SLA formal por escrito

**Por ahora** (bootstrapped): **Validación > Perfección**.

---

**Autor**: Nzero (basado en análisis inicial de Antigravity)  
**Participantes**: Alejandro  
**Relacionado con**: Estructura Trinity (TheQai/QaiLabs/QaiProd)  
**Creado**: 26-Dic-2025 (retroactivo)
