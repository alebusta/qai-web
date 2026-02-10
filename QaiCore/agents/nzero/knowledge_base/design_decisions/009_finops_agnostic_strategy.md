# ADR-009: Estrategia FinOps Agnóstica y Categorizada

**Fecha**: 2025-12-29  
**Estado**: Aceptado  
**Contexto**: QAI utiliza múltiples proveedores de nube, IA y SaaS (Google, OpenAI, Supabase, Cursor). Inicialmente, el seguimiento de costos era ad-hoc y enfocado en facturación única. Necesitamos una forma de escalar preservando la rentabilidad y entendiendo dónde se invierte el capital.

---

## Problema

La falta de una estructura clara para asignar costos financieros impedía diferenciar entre gastos de operación base, inversión en innovación y costos directos de productos vendidos (COGS).

**Por qué es importante**: Sin esta distinción, es imposible calcular márgenes reales por producto o decidir cuándo recortar gastos de experimentación sin afectar la operación.

---

## Alternativas Consideradas

### Opción 1: Seguimiento por Proveedor (Legacy)
**Descripción**: Mantener el control basado en lo que factura cada proveedor (GCP, AWS, etc.).
**Pros**: ✅ Simple de implementar.
**Cons**: ❌ No permite atribución de costos a proyectos. ❌ Difícil de ver el costo total de un producto que usa varios proveedores.

### Opción 2: Marco FinOps Maestro Agnóstico ⭐ **ELEGIDA**
**Descripción**: Centralizar la lógica financiera en Finn, independientemente de la tecnología. Clasificar todo en tres niveles: Fijo, Proyecto (Variable) y R&D (Variable).
**Pros**:
- ✅ Visibilidad total por producto/cliente.
- ✅ Independencia tecnológica (si cambiamos de OpenAI a Anthropic, el marco financiero no cambia).
- ✅ Facilita el cálculo del punto de equilibrio (Break-even).
**Cons**:
- ❌ Requiere disciplina en el etiquetado (tagging) de recursos.
- ❌ Mayor carga inicial de clasificación para Finn.

---

## Decisión

Adoptar un enfoque **Agnóstico de Plataforma** para FinOps, delegando en Finn la responsabilidad de clasificar y monitorear todos los gastos de QAI bajo tres categorías:
1. **Fijos**: Operación base (IDEs, Correo, Oficina).
2. **Proyecto**: Costos directos de productos billables (API Gemini para FedEx).
3. **R&D**: Inversión en innovación y experimentación (Labs).

**Justificación**: Este modelo es el que mejor escala con el espíritu de QAI de ser "agnósticos de modelos e infraestructura".

---

## Consecuencias

### Positivas
- Cálculo de márgenes brutos por proyecto 100% real.
- Optimización de costos fijos por volumen.
- "Sandbox financiero" para R&D con límites claros.

### Negativas / Trade-offs
- Necesidad de mantener una matriz de asignación de costos actualizada.

---

## Notas de Implementación

**Componentes Afectados**:
- Perfil de Finn (v1.2).
- Knowledge Base de Finn (`/finops/`).
- Reportes de STATUS.md.

**Archivos Relevantes**:
- [marco_finops_master.md](../../finn/knowledge_base/finops/marco_finops_master.md)
- [google_cloud_billing.md](../../finn/knowledge_base/finops/google_cloud_billing.md)

---

**Autor**: Nzero  
**Participantes**: Alejandro  
**Relacionado con**: [ADR-004: Criterios de Graduación Labs -> Prod](./004_criterios_graduacion_labs_prod.md)
