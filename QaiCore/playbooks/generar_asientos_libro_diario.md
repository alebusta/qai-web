# Playbook: Generar Asientos Formales - Libro Diario

> **Workflow para que Finn genere asientos contables formales desde el Registro Diario al Libro Diario**

---

## 🎯 Objetivo

Convertir los movimientos registrados en `Registro_Diario` (formato operativo) a asientos contables formales en `Libro_Diario` (formato contable), asegurando equilibrio contable y cumplimiento formal.

---

## 🔄 Trigger (Cuándo ejecutar)

- **Mensual**: Al finalizar el mes, antes de cerrar contabilidad
- **Quincenal**: Si hay muchos movimientos (futuro, cuando crezca)
- **Antes de F29**: Para validar equilibrio contable antes de declarar IVA
- **Usuario solicita**: "Genera los asientos formales del mes [mes]"

**Frecuencia Recomendada**:
- **Actual (movimientos mínimos)**: Mensual
- **Futuro (más movimientos)**: Quincenal según volumen

---

## 📋 Pre-requisitos

- Acceso a Google Sheets `QAI_Finanzas_2026`
- Movimientos registrados en pestaña `Registro_Diario` del período
- Plan de Cuentas disponible (referencia: `/QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md`)
- Comprobantes archivados (para referencia)

---

## 🛠️ Pasos del Workflow

### 1. Verificar Estructura de Libro_Diario

**Estructura de la Hoja** (crear si no existe):

```
| Asiento # | Fecha | Concepto | Cuenta | Débito | Crédito | Notas |
```

**Columnas**:
- **Asiento #**: Número correlativo (ej: AS-001, AS-002) - Mismo número para todas las filas de un mismo asiento
- **Fecha**: Fecha contable del movimiento
- **Concepto**: Descripción clara del movimiento (ej: "GitHub Copilot Pro - Suscripción Enero 2026")
- **Cuenta**: Código completo de cuenta (ej: `61.01.03 Suscripciones Tech`)
- **Débito**: Monto a débito (dejar vacío si es crédito)
- **Crédito**: Monto a crédito (dejar vacío si es débito)
- **Notas**: Info adicional (ej: "Doc. 46 pendiente", "Dólar obs. $896,89")

**Ubicación**: Google Sheet `QAI_Finanzas_2026` → Pestaña `Libro_Diario`

---

### 2. Leer Movimientos del Período desde Registro_Diario

**Desde Google Sheets `Registro_Diario`**:

```bash
# Leer movimientos del período desde Google Sheets
.\QaiCore\qrun.bat .\QaiCore\tools\gsheets.py --spreadsheet_id 1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw --read "Registro_Diario!A2:M100"
```

**Filtrar por**:
- Fecha del período a procesar (ej: enero 2026)
- Solo movimientos que no estén marcados como "Asiento generado" (columna adicional si es necesario)

---

### 3. Convertir cada Movimiento a Asiento Formal

**Regla de Oro**: Cada asiento debe balancear → **Suma Débitos = Suma Créditos**

#### Ejemplo 1: Gasto con IVA (Servicio Extranjero)

**Movimiento en Registro_Diario**:
```
| 09-Ene | GASTO | GitHub Copilot Pro | 61.01.03 | $9.250 | $1.704,09 | $10.954,09 | $9.250 | Doc. 46 pendiente |
```

**Asiento Formal en Libro_Diario** (AS-001):
```
| AS-001 | 09-Ene-2026 | GitHub Copilot Pro - Suscripción Enero 2026 | 61.01.03 Suscripciones Tech | $9.250,00 | | |
| AS-001 | 09-Ene-2026 | GitHub Copilot Pro - Suscripción Enero 2026 | 81.01 IVA Crédito Fiscal | $1.704,09 | | |
| AS-001 | 09-Ene-2026 | GitHub Copilot Pro - Suscripción Enero 2026 | 11.02 Banco Chile | | $9.250,00 | |
| AS-001 | 09-Ene-2026 | GitHub Copilot Pro - Suscripción Enero 2026 | 21.04 Proveedores Extranjeros | | $1.704,09 | |
```

**Validación**:
- Débitos: $9.250,00 + $1.704,09 = **$10.954,09**
- Créditos: $9.250,00 + $1.704,09 = **$10.954,09**
- ✅ **BALANCEADO**

#### Ejemplo 2: Gasto sin IVA (Gasto Personal con Uso Empresarial)

**Movimiento en Registro_Diario**:
```
| 08-Ene | GASTO | Google One / Google AI Pro | 61.01.03 | $7.330 | $0 | $7.330 | $7.330 | VAT no recuperable |
```

**Asiento Formal en Libro_Diario** (AS-002):
```
| AS-002 | 08-Ene-2026 | Google One / Google AI Pro - Suscripción Enero 2026 | 61.01.03 Suscripciones Tech | $7.330,00 | | |
| AS-002 | 08-Ene-2026 | Google One / Google AI Pro - Suscripción Enero 2026 | 11.02 Banco Chile | | $7.330,00 | |
```

**Validación**:
- Débitos: $7.330,00
- Créditos: $7.330,00
- ✅ **BALANCEADO**

#### Ejemplo 3: Abono (Préstamo Socio)

**Movimiento en Registro_Diario**:
```
| 07-Ene | PRÉSTAMO | Préstamo socio - Alejandro | 21.01 | $50.000 | $0 | $50.000 | $50.000 | |
```

**Asiento Formal en Libro_Diario** (AS-003):
```
| AS-003 | 07-Ene-2026 | Préstamo socio - Alejandro Bustamante | 11.02 Banco Chile | $50.000,00 | | |
| AS-003 | 07-Ene-2026 | Préstamo socio - Alejandro Bustamante | 21.01 Préstamos de Socios | | $50.000,00 | |
```

**Validación**:
- Débitos: $50.000,00
- Créditos: $50.000,00
- ✅ **BALANCEADO**

#### Ejemplo 4: Ingreso con IVA (Factura Emitida - Futuro)

**Movimiento en Registro_Diario** (cuando facturemos):
```
| [Fecha] | INGRESO | Factura FedEx Invoice Match | 41.01.01 | $800.000 | $152.000 | $952.000 | $0 | Cobranza 30 días |
```

**Asiento Formal en Libro_Diario** (al emitir factura):
```
| AS-XXX | [Fecha] | Factura N°001 - FedEx Invoice Match Enero 2026 | 12.01 Cuentas por Cobrar | $952.000,00 | | |
| AS-XXX | [Fecha] | Factura N°001 - FedEx Invoice Match Enero 2026 | 41.01.01 Ventas Invoice Match | | $800.000,00 | |
| AS-XXX | [Fecha] | Factura N°001 - FedEx Invoice Match Enero 2026 | 81.02 IVA Débito Fiscal | | $152.000,00 | |
```

**Al cobrar** (asiento separado):
```
| AS-YYY | [Fecha] | Cobranza Factura N°001 - FedEx | 11.02 Banco Chile | $952.000,00 | | |
| AS-YYY | [Fecha] | Cobranza Factura N°001 - FedEx | 12.01 Cuentas por Cobrar | | $952.000,00 | |
```

---

### 4. Validar Equilibrio por Asiento

**Regla**: Cada asiento (#) debe tener **Suma Débitos = Suma Créditos**

**Validación en Google Sheets**:
- Agregar columna "Total Débito" que sume todos los débitos del mismo Asiento #
- Agregar columna "Total Crédito" que sume todos los créditos del mismo Asiento #
- Agregar columna "Diferencia" que calcule: `Total Débito - Total Crédito`
- **Debe ser $0 para cada asiento**

**Fórmula sugerida** (en Google Sheets):
```excel
=IF(SUMIF($A$2:$A$1000, A2, $E$2:$E$1000) = SUMIF($A$2:$A$1000, A2, $F$2:$F$1000), "✅ Balanceado", "❌ Desbalanceado")
```

---

### 5. Registrar Asientos en Libro_Diario

**Pasos**:
1. Abrir Google Sheet: `QAI_Finanzas_2026` → Pestaña `Libro_Diario`
2. Generar siguiente número de asiento (ej: si último es AS-003, siguiente es AS-004)
3. Insertar filas para cada línea del asiento (mismo Asiento #, diferentes cuentas)
4. Completar columnas según estructura del paso 1
5. Validar equilibrio del asiento antes de continuar con el siguiente

**Orden Recomendado**:
- Débitos primero (arriba)
- Créditos después (abajo)
- Agrupar por Asiento # para claridad

---

### 6. Validar Equilibrio Total del Período

**Al finalizar todos los asientos del período**:

**Validación Total**:
- Suma Total Débitos del período = Suma Total Créditos del período
- Si hay diferencia, revisar cada asiento hasta encontrar el error

**Fórmula en Google Sheets**:
```excel
Total Débitos: =SUM(E:E)
Total Créditos: =SUM(F:F)
Diferencia: =SUM(E:E) - SUM(F:F)  // Debe ser $0
```

---

### 7. Marcar Movimientos como "Asiento Generado"

**En Registro_Diario**:
- Agregar columna "Asiento #" (si no existe)
- Registrar el número de asiento generado (ej: "AS-001")
- Esto permite evitar duplicar asientos en próximas ejecuciones

---

### 8. Generar Resumen del Período

**Crear resumen en hoja separada o al final de Libro_Diario**:

```
=== RESUMEN MENSUAL - ENERO 2026 ===

Total Asientos Generados: [N]
Total Débitos: $[X]
Total Créditos: $[Y]
Diferencia: $0 ✅

Movimientos Procesados:
- GitHub Copilot Pro (AS-001)
- Google One (AS-002)
- Préstamo Socio (AS-003)
```

---

## ✅ Criterios de Éxito

- ✅ Todos los movimientos del período convertidos a asientos formales
- ✅ Cada asiento balancea (Suma Débitos = Suma Créditos)
- ✅ Total período balancea (Suma Total Débitos = Suma Total Créditos)
- ✅ Movimientos marcados como "Asiento Generado" en Registro_Diario
- ✅ Resumen mensual generado y documentado

---

## 🚨 Casos Especiales

### Movimientos con Diferencias de Cambio Significativas (≥ $1.000)

**Si la diferencia es ≥ $1.000 CLP**, se registra en cuenta `61.03.01 Diferencia de Cambio`:

**Ejemplo** (diferencia $1.200):
```
| AS-XXX | [Fecha] | [Concepto] | 61.01.03 Suscripciones Tech | $[Monto SII] | | |
| AS-XXX | [Fecha] | [Concepto] | 61.03.01 Diferencia de Cambio | $1.200,00 | | |
| AS-XXX | [Fecha] | [Concepto] | 81.01 IVA Crédito Fiscal | $[IVA SII] | | |
| AS-XXX | [Fecha] | [Concepto] | 11.02 Banco Chile | | $[Monto Real] | |
| AS-XXX | [Fecha] | [Concepto] | 21.04 Proveedores Extranjeros | | $[IVA SII] | |
```

### Movimientos Pendientes de Comprobante

**Si falta comprobante**: Registrar asiento igualmente, agregar nota "Comprobante pendiente" y seguimiento en INBOX.

---

## 📝 Notas para Finn

- **Consistencia**: Usar siempre las mismas cuentas para el mismo tipo de movimiento según Plan de Cuentas
- **Validación**: Siempre validar equilibrio antes de continuar con siguiente asiento
- **Orden**: Mantener orden cronológico en Libro_Diario
- **Trazabilidad**: Cada asiento debe poder rastrearse al movimiento original en Registro_Diario
- **Documentación**: Mantener notas claras sobre asientos complejos (diferencias de cambio, IVA, etc.)

---

## 🔗 Referencias Relacionadas

- **Plan de Cuentas**: [`/QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md`](../agents/finn/knowledge_base/contabilidad/plan_cuentas.md)
- **Registro Movimientos**: [`registro_movimiento_bancario.md`](registro_movimiento_bancario.md)
- **Conciliación**: [`conciliacion_bancaria.md`](conciliacion_bancaria.md)
- **Diferencias Cambio**: [`/QaiCore/agents/finn/knowledge_base/contabilidad/explicacion_diferencias_cambio.md`](../agents/finn/knowledge_base/contabilidad/explicacion_diferencias_cambio.md)

---

**Versión**: 1.0  
**Creado**: 10-Ene-2026  
**Responsable**: Finn (CFO QAI)  
**Revisión**: Cuando cambien patrones de movimientos o estructura contable

