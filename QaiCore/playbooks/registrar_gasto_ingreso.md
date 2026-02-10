# Playbook: Registrar Gasto o Ingreso Diario

> **Workflow para que Finn registre operaciones financieras en el sistema contable**

---

## 🎯 Objetivo

Registrar de forma consistente y completa cada operación financiera (gasto o ingreso) en el sistema contable de QAI, asegurando trazabilidad, correcta clasificación y actualización de métricas.

---

## 🔄 Trigger (Cuándo ejecutar)

- Alejandro realiza un gasto con tarjeta/cuenta de QAI
- Alejandro recibe un ingreso en cuenta de QAI
- Hay un movimiento bancario que requiere registro
- Usuario solicita: "Registra este gasto/ingreso"

---

## 📋 Pre-requisitos

- Acceso a Google Sheets (Registro Diario)
- Acceso a Google Drive (archivo de comprobantes)
- Plan de Cuentas disponible
- Información del movimiento (monto, fecha, concepto)

---

## 🛠️ Pasos del Workflow

### 1. Obtener Información del Movimiento

**Datos Requeridos**:
- **Fecha**: ¿Cuándo ocurrió?
- **Monto**: ¿Cuánto?
- **Concepto**: ¿Qué es? (proveedor, cliente, descripción)
- **Documento**: ¿Hay factura/comprobante?
- **Tipo**: ¿Gasto o Ingreso?
- **Método de Pago**: ¿Tarjeta, transferencia, efectivo?

**Si falta información**:
```
"Necesito [dato faltante] para registrar correctamente. ¿Me lo proporcionas?"
```

---

### 2. Clasificar la Operación

**Para GASTOS**:
- **Categoría FinOps**: ¿Fijo / Variable Proyecto / Variable R&D?
- **Proyecto/Producto**: ¿Invoice Match / Gestión Zen / QaiCore / General?
- **Cuenta Contable**: Según Plan de Cuentas
- **IVA**: ¿Afecto / Exento? ¿Con Factura de Compra (Doc. 46) si es extranjero?

**Para INGRESOS**:
- **Cliente**: ¿Quién paga?
- **Producto/Servicio**: ¿Invoice Match / Consultoría / Capacitación?
- **Tipo**: ¿Suscripción mensual / Pago único / Préstamo?
- **IVA**: ¿Afecto (19%) / Exento?
- **Cuenta Contable**: Según Plan de Cuentas

**Tabla de Decisión Rápida**:

| Tipo | Categoría | Cuenta Contable | Notas |
|:---|:---:|:---|:---|
| Suscripción Tech (Cursor, Copilot) | Fijo | 61.01.03 Suscripciones Tech | Doc. 46 si extranjero |
| Oficina Virtual | Fijo | 61.01.01 Oficina Virtual | Si aplica |
| Contador | Fijo | 61.01.02 Contador | Si aplica |
| APIs por proyecto (Gemini, Groq) | Variable Proyecto | 51.01.XX Costos Directos | Tracking por proyecto |
| Supabase por proyecto | Variable Proyecto | 51.01.XX Costos Directos | $25 USD/proyecto |
| Experimentos R&D | Variable R&D | 61.02.01 Experimentos IA | |
| Facturación Cliente SaaS | Ingreso | 41.01.01 Ventas Invoice Match | + IVA Débito |
| Pago Consultoría | Ingreso | 41.01.02 Ventas Consultoría | + IVA Débito |
| Préstamo Socio | Pasivo | 21.01 Préstamos Socios | NO es ingreso operacional |

**Referencia Completa**: Ver [Plan de Cuentas](../../QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md) para estructura completa y tabla de decisión detallada.

---

### 3. Registrar en Google Sheets (Registro Diario)

**⚠️ PROTOCOLO ZERO-LOSS FINANCE (CRÍTICO)**:
- **ANTES** de escribir en el GSheet, debes ejecutar:  
   `.\QaiCore\qrun.bat .\QaiCore\tools\backup_finance.py`
- Esto crea una copia de seguridad local en CSV por si falla la escritura o se corrompen los datos.

**Estructura de la Hoja**:
```
| Fecha | Tipo | Concepto | Categoría | Cuenta | Monto Neto | IVA | Retención | Monto Bruto | Monto Pagado | Proyecto | Comprobante | Notas |
```

**Pasos**:
1. Ejecutar backup local preventivo.
2. Abrir Google Sheet Master: `QAI_Finanzas_2026` (ID: `1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw`).
3. Insertar nueva fila.
4. Completar campos según clasificación del paso 2.
5. Validar fórmulas automáticas (IVA, Totales).
6. Verificar que el monto coincida con extracto bancario.
7. Ejecutar backup local post-registro para confirmar persistencia.

**Ejemplo de Registro (Gasto)**:
```
Fecha: 30-Dic-2025
Tipo: GASTO
Concepto: Cursor IDE - Suscripción Mensual
Categoría: Fijo
Cuenta: 61.01.03 Suscripciones Tech
Monto Neto: $19.000 CLP (USD $20)
IVA: $0 (Doc. 46 a emitir)
Monto Bruto: $19.000 CLP
Proyecto: General
Comprobante: invoice_cursor_2025-12.pdf
Notas: Factura de Compra (Doc. 46) pendiente
Cuenta Bancaria: 11.02 Banco Chile
```

**Ejemplo de Registro (Ingreso)**:
```
Fecha: 05-Ene-2026
Tipo: INGRESO
Concepto: FedEx - Invoice Match - Enero 2026
Categoría: SaaS Recurrente
Cuenta: 41.01.01 Ventas Invoice Match
Monto Neto: $800.000 CLP
IVA: $152.000 CLP
Monto Bruto: $952.000 CLP
Proyecto: Invoice Match
Comprobante: factura_001_fedex_ene2026.pdf
Notas: Primera factura, cobranza a 30 días
Cuenta Bancaria: 12.01 Cuentas por Cobrar (hasta que cobre en 11.02 Banco Chile)
```

**Nota**: Cuando se reciba el pago, registrar movimiento bancario usando [Protocolo de Registro de Movimiento Bancario](registro_movimiento_bancario.md).

---

### 4. Archivar Comprobante

**Proceso**:
1. Si hay documento (factura, comprobante, extracto):
   - **Destino Estándar**: `/Empresa/03_ADMINISTRACION_FINANZAS/comprobantes/[Año]/[Mes]/[Subcarpeta]/`
   - **Subcarpetas Obligatorias**:
     - `01-Facturas_Recibidas`: Invoices de proveedores locales.
     - `02-Facturas_Emitidas`: Ventas de QAI.
     - `03-SaaS_Extranjero_Doc46`: Receipts de Apple, Google, AWS, Cursor, etc.
     - `04-Comprobantes_Pago`: TEF, transferencias, boletas de pago.
     - `05-Cartolas`: Solo estados de cuenta mensuales finales.
   - **Nombre de Archivo**: `YYYY-MM-DD_[tipo]_[concepto].pdf`
   - Actualizar columna "Comprobante" en Google Sheet con link/nombre.
   - **⚠️ IMPORTANTE**: Si el archivo estaba en `temp_files/` (landing zone), **eliminarlo** después de subirlo a Drive.
2. Si NO hay documento: Note en columna "Notas" y tarea en INBOX.

---

### 5. Actualizar Métricas Impactadas

**Si es GASTO**:
- ✅ Actualizar Runway (recalcular saldo disponible)
- ✅ Actualizar categoría de costo (Fijo/Variable)
- ✅ Actualizar costo por proyecto (si aplica)

**Si es INGRESO**:
- ✅ Actualizar MRR (si es recurrente)
- ✅ Actualizar Runway (recalcular saldo disponible)
- ✅ Actualizar P&L del período

**Actualización Runway**:
```
Runway (meses) = Saldo en Banco / Burn Rate Mensual
```

---

### 6. Registrar IVA (si aplica)

**Para GASTOS con IVA (Servicios Extranjeros)**:
- ✅ Verificar si requiere Factura de Compra (Doc. 46)
- ✅ Si sí: Agregar tarea en INBOX: "Emitir Doc. 46 para [concepto]"
- ✅ Si ya existe: Registrar IVA Crédito Fiscal

**Para INGRESOS con IVA**:
- ✅ IVA Débito Fiscal se registra automáticamente en factura
- ✅ Se declara en F29 del mes correspondiente

---

### 7. Actualizar Documentación

**Registrar en**:
- ✅ Google Sheet: Registro Diario (ya hecho en paso 3)
- ✅ AGENT_ACTIVITY.md: Nota de registro
- ✅ STATUS.md: Si es movimiento significativo (actualizar saldo, MRR, etc.)

**Formato AGENT_ACTIVITY.md**:
```markdown
### 30-Dic-2025 - Finn
- Registrado gasto: Cursor IDE - $19.000 CLP (Categoría: Fijo, Cuenta: 61.01.03)
- Comprobante archivado: invoice_cursor_2025-12.pdf
- Runway actualizado: X meses
```

---

### 8. Validación Final

**Checklist**:
- ✅ Monto coincide con extracto bancario
- ✅ Fecha correcta
- ✅ Clasificación FinOps correcta
- ✅ Cuenta contable correcta
- ✅ Comprobante archivado (o en seguimiento)
- ✅ IVA registrado (si aplica)
- ✅ Runway/P&L actualizados
- ✅ Documentación actualizada

**Si algo falta**:
```
"⚠️ Registro incompleto: [dato faltante]. 
Acción requerida: [qué hacer]"
```

---

## ✅ Criterios de Éxito

- ✅ Movimiento registrado en Google Sheet
- ✅ Comprobante archivado (o en seguimiento)
- ✅ Clasificación correcta (FinOps + Contable)
- ✅ Métricas actualizadas (Runway/P&L)
- ✅ IVA gestionado correctamente
- ✅ Documentación actualizada

---

## 🚨 Casos Especiales

### Préstamo del Socio

**Tratamiento especial**:
- Tipo: Préstamo (NO es ingreso operacional)
- Cuenta: 21.01 Préstamos de Socios (Pasivo)
- Registro: 11.02 Banco Chile (Débito) / 21.01 Préstamos de Socios (Crédito)
- Tracking: Actualizar Sheet de Préstamos del Socio

**Workflow**:
1. Registrar en Registro Diario (marcado como "Préstamo" o "PASIVO")
2. Actualizar Sheet "Préstamos_Socio" con fecha, monto, saldo acumulado
3. NO afecta P&L (no es ingreso operacional, es pasivo)
4. SÍ afecta Runway (aumenta saldo disponible en 11.02 Banco Chile)

**Referencia**: Ver [Plan de Cuentas](../../QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md) para detalles de cuenta 21.01.

---

### Gasto Pre-Inicio de Actividades

**Tratamiento**:
- ❌ NO se registra en contabilidad de QAI
- ✅ Se puede documentar como "Gasto Hundido" (histórico, no contable)
- ✅ Crear documento separado si se quiere referencia histórica

---

### Factura de Compra (Doc. 46) - Servicios Extranjeros

**Cuándo aplicar**:
- Servicios SaaS extranjeros (Cursor, Copilot, AWS, etc.)
- Suscripciones a nombre de QAI Company SpA

**Proceso**:
1. Registrar gasto normal en Registro Diario
2. Agregar nota: "Doc. 46 pendiente"
3. Agregar tarea INBOX: "Emitir Doc. 46 para [servicio]"
4. Cuando se emita Doc. 46:
   - Registrar IVA Crédito Fiscal
   - Actualizar registro original
   - Marcar como completo

---

### Boleta de Honorarios (con Retención) - Comisiones y Servicios Profesionales

**Cuándo aplicar**:
- Boletas de honorarios emitidas por personas naturales
- Ejemplos: Comisión Ligia, servicios de freelance, consultoría externa

**Características**:
- ❌ NO tiene IVA (boleta exenta)
- ❌ NO va al Libro de Compras (no genera crédito fiscal)
- ✅ SÍ es deducible para Impuesto a la Renta
- ⚠️ Requiere retención de 10,75% si es persona natural

**Proceso Paso a Paso**:

1. **Recibir Boleta de Honorarios**:
   - Verificar que esté a nombre de QAI Company SpA
   - Verificar monto y concepto

2. **Calcular Retención** (si el prestador es persona natural):
   - Retención: Monto Neto × 10,75%
   - Monto a pagar: Monto Neto - Retención
   
   Ejemplo (Comisión Ligia):
   - Monto Neto: $200.000
   - Retención: $200.000 × 10,75% = $21.500
   - Monto a pagar: $178.500

3. **Registrar en Google Sheets (Registro Diario)**:
   ```
   Fecha: [fecha de pago]
   Tipo: GASTO
   Concepto: Comisión Ligia - Invoice Match Enero 2026
   Categoría: Variable Proyecto (o según corresponda)
   Cuenta: 71.01 Comisiones Pagadas
   Monto Neto: $200.000
   IVA: $0 (boleta exenta)
   Monto Bruto: $200.000
   Retención: $21.500 (nueva columna, si la agregamos)
   Monto Pagado: $178.500
   Proyecto: Invoice Match
   Comprobante: boleta_honorarios_ligia_ene2026.pdf
   Notas: Retención 10,75% declarada en F29
   Estado: Comprobado
   ```

4. **Pagar al Prestador**:
   - Transferir el monto neto menos retención
   - Ejemplo: Pagar $178.500 a Ligia

5. **Declarar Retención en F29**:
   - La retención ($21.500) se declara en el F29 del mes correspondiente
   - Se paga al SII junto con el IVA del mes

6. **Registro Contable**:
   ```
   Débito:  71.01 Comisiones Pagadas   $200.000
   Crédito: 11.02 Banco Chile           $178.500
   Crédito: 21.02 Retenciones por Pagar $21.500

**Referencia**: Ver [Plan de Cuentas](../../QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md) para estructura de cuentas 71.01 y 21.02.
   ```

7. **Archivar Comprobante**:
   - Guardar boleta de honorarios en Google Drive
   - Carpeta: `/Empresa/03_ADMINISTRACION_FINANZAS/comprobantes/2026/[mes]/boletas_honorarios/`
   - Nombre: `YYYY-MM-DD_boleta_honorarios_[proveedor]_[concepto].pdf`

**Importante**:
- ✅ La boleta NO va al Libro de Compras (no tiene IVA)
- ✅ El gasto SÍ es deducible completo ($200.000) para Impuesto a la Renta (F22)
- ✅ La retención se declara en F29 mensual y se paga al SII
- ✅ Guardar boleta como respaldo (6 años para fiscalización)

---

## 📝 Notas para Finn

- **Consistencia**: Usar siempre las mismas categorías y cuentas
- **Trazabilidad**: Cada movimiento debe tener comprobante o justificación
- **Prontitud**: Registrar lo antes posible (idealmente el mismo día)
- **Validación**: Siempre verificar montos contra extractos bancarios
- **Dudas**: Si no estás seguro de clasificación, preguntar antes de registrar

---

**Referencias Relacionadas**:
- [Plan de Cuentas Completo](../../QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md)
- [Protocolo de Registro de Movimiento Bancario](registro_movimiento_bancario.md)
- [Protocolo de Conciliación Bancaria](conciliacion_bancaria.md)

**Versión**: 1.1  
**Creado**: 30-Dic-2025  
**Actualizado**: 10-Ene-2026 (Integración con Plan de Cuentas y protocolos bancarios)  
**Responsable**: Finn (Agente Financiero)

