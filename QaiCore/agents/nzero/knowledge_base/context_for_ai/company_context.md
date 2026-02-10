# Context for AI - The QAI Company

> **Información crucial para que agentes IA entiendan el contexto de la empresa**

---

## 🎯 Filosofía QAI

### Principios Core

**1. Humano en el Centro, IA como Palanca**
- No reemplazar humanos, potenciarlos
- Human-in-the-loop para decisiones críticas
- IA ejecuta, humano valida

**2. Bootstrapped & Minimalist**
- Cero inversión externa
- Crecer a ritmo sostenible
- No escalar "a lo loco"

**3. Cero Burocracia**
- Documentar solo lo esencial
- Procesos livianos
- Decisiones rápidas

**4. Solopreneur + No-gentes**
- 1 humano (Alejandro)
- N agentes IA especializados
- Colaboración humano-IA efectiva

---

## 🏢 Estructura Organizacional

### La Trinidad

**TheQai** (El Cerebro):
- Estrategia, legal, admin
- No genera revenue directamente
- Documenta todo en `/Empresa/`

**QaiLabs** (Innovación):
- Validación de productos
- Prototipos y pilotos
- Pipeline de ideas

**QaiProd** (Ejecución):
- Productos SaaS en producción
- Revenue recurrente (MRR)
- CI/CD, monitoreo, SLAs

---

## 📊 Estado Actual (Dic 2025)

**Legal**:
- ✅ Empresa constituida (The QAI Company SpA)
- ✅ Cuenta bancaria activa
- 🟡 Facturación pendiente (esperando 1era OC)

**Productos**:
- **Invoice-Match** (QaiLabs → transitando a Prod)
  - Cliente: FedEx Chile
  - Estado: Piloto activo
  - Cotización: $800K CLP/mes
- **Gestión Zen** (QaiLabs)
  - JV 33/33/33
  - Estado: Validación con socios

**Revenue**:
- MRR Actual: $0
- MRR Proyectado Q1-2026: $800K (FedEx)

---

## 🎯 Prioridades Estratégicas

### Corto Plazo (Esta Semana)
1. Cerrar OC de FedEx
2. Implementar Dashboard Invoice-Match
3. Firmar MOU Gestión Zen

### Mediano Plazo (Este Mes)
1. Graduar Invoice-Match a QaiProd
2. Crear GitHub Organization
3. Primera factura electrónica

### Largo Plazo (Q1 2026)
1. Alcanzar $1.5M CLP MRR (punto equilibrio)
2. Segundo producto a producción
3. Building in Public en LinkedIn

---

## 🤖 Agentes Activos

### Nzero (Arquitecto) - YO
- Diseño de QaiCore
- Memoria institucional
- Decisiones arquitecturales

### Lex (Legal)
- Consultas tributarias
- Revisión contratos
- Compliance

### Finn (Futuro)
- Flujo de caja
- Análisis financiero
- Declaraciones

### Builder (Futuro)
- Implementación código
- Deployment
- DevOps

---

## 📝 Cómo Trabajamos

### Protocolo General
1. TODO agente lee STATUS e INBOX al inicio
2. Usa time_utils para contexto temporal
3. Actualiza STATUS al finalizar
4. Marca tareas en INBOX como [x]

### Torre de Control
- `/STATUS.md`: Dashboard de estado actual
- `/INBOX.md`: Tareas pendientes
- `/CHANGELOG.md`: Hitos importantes

### Documentación
- Español para docs de negocio
- Inglés para código/herramientas
- Markdown para todo

---

## ⚠️ Límites y Restricciones

**Lo que NO hacemos**:
- ❌ Escalar prematuramente
- ❌ Tomar deuda/inversión externa (por ahora)
- ❌ Sobre-documentar
- ❌ Procesos burocráticos

**Lo que SÍ hacemos**:
- ✅ Validar antes de escalar
- ✅ Bootstrapped profitability
- ✅ Minimalismo documentario
- ✅ Decisiones rápidas

---

## 💡 Decisiones Históricas Clave

[Se actualizará con links a ADRs importantes cuando se creen]

1. [ADR-001: Torre de Control](../design_decisions/001_torre_de_control.md)
2. [ADR-002: QaiCore Structure](../design_decisions/002_qaicore_structure.md)
3. [ADR-003: Profile vs System Prompt](../design_decisions/003_profile_vs_system_prompt.md)

---

**Última actualización**: 26-Dic-2025  
**Próxima revisión**: Trimestral o cuando cambie estrategia
