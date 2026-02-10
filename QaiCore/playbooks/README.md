# Playbooks QaiCore

> **Workflows estandarizados para operaciones comunes**

---

## 📋 Playbooks Disponibles

### Financieros (Finn)

- [`registrar_gasto_ingreso.md`](registrar_gasto_ingreso.md)
  - **Propósito**: Workflow paso a paso para registrar operaciones financieras diarias
  - **Cuándo usar**: Cada vez que hay un gasto o ingreso que registrar
  - **Output**: Registro en Google Sheets, actualización de métricas

- [`emitir_doc46_extranjero.md`](emitir_doc46_extranjero.md)
  - **Propósito**: Emisión de Factura de Compra (Doc. 46) para recuperar IVA de SaaS extranjeros
  - **Cuándo usar**: Mensualmente para invoices de Cursor, GitHub, AWS, etc.
  - **Output**: Doc. 46 emitido en SII, crédito fiscal recuperado.

- [`facturar_cliente_saas.md`](facturar_cliente_saas.md)
  - **Propósito**: Flujo completo desde OC hasta cobranza de facturación SaaS
  - **Cuándo usar**: Cuando se recibe OC o se debe facturar período recurrente
  - **Output**: Factura emitida, registrada en contabilidad, tracking de cobranza

- [`conciliacion_bancaria.md`](conciliacion_bancaria.md)
  - **Propósito**: Proceso de conciliación entre extracto bancario y registros contables
  - **Cuándo usar**: Mensualmente o cuando se detecten discrepancias
  - **Output**: Registro Diario y extracto bancario 100% conciliados

- [`registro_movimiento_bancario.md`](registro_movimiento_bancario.md)
  - **Propósito**: Workflow para registrar movimientos bancarios (transferencias, cargos, abonos)
  - **Cuándo usar**: Al procesar extractos bancarios o cartolas
  - **Output**: Movimientos registrados en Google Sheets con clasificación contable

- [`generar_asientos_libro_diario.md`](generar_asientos_libro_diario.md)
  - **Propósito**: Generación de asientos contables formales para Libro Diario
  - **Cuándo usar**: Mensualmente o para eventos contables específicos
  - **Output**: Asientos contables con debe/haber balanceados

### Legales (Lex)

- [`process_inbox_task.md`](process_inbox_task.md)
  - **Propósito**: Procesar tareas legales del INBOX de Torre de Control
  - **Cuándo usar**: Cuando hay tareas marcadas con `[Legal]` en INBOX
  - **Output**: Respuestas, análisis, documentos según tipo de tarea

### Financieros/Legales (Finn + Lex)

- [`process_financial_inbox.md`](process_financial_inbox.md)
  - **Propósito**: Procesar tareas financieras del INBOX
  - **Cuándo usar**: Tareas marcadas con `[Finanzas]`
  - **Output**: Registros, reportes, análisis según tipo

### Coordinación (Nzero)

- [`coordinacion_inbox.md`](coordinacion_inbox.md)
  - **Propósito**: Protocolo de triage y asignación de tareas a agentes especialistas
  - **Cuándo usar**: Al procesar INBOX con múltiples tipos de tareas
  - **Output**: Tareas asignadas al agente correcto, Landing Zone organizada

---

## 🎯 Uso de Playbooks

### Para Agentes

1. Identificar la tarea/operación a realizar
2. Buscar playbook correspondiente
3. Seguir pasos del workflow
4. Documentar resultado según criterios del playbook

### Para Humanos

- Consultar playbooks para entender procesos
- Verificar que agentes siguen workflows estandarizados
- Proponer mejoras o nuevos playbooks según necesidades

---

## 📝 Crear Nuevo Playbook

**Estructura mínima**:
```markdown
# Playbook: [Nombre]

> **Workflow para [descripción]**

## 🎯 Objetivo
[Qué logra este playbook]

## 🔄 Trigger
[Cuándo ejecutarlo]

## 📋 Pre-requisitos
[Qué se necesita antes]

## 🛠️ Pasos del Workflow
[Pasos detallados]

## ✅ Criterios de Éxito
[Qué debe lograrse]

## 🚨 Casos Especiales
[Excepciones y casos edge]
```

---

**Última actualización**: 10-Ene-2026

