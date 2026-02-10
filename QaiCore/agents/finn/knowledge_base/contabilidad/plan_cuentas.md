# Plan de Cuentas: The QAI Company SpA

> **Principio de Diseño**: Minimalista para el corto plazo, escalable para el mediano plazo.  
> **Última actualización**: 10-Ene-2026  
> **Responsable**: Finn (CFO QAI)

---

## 📋 Resumen Ejecutivo

Plan de cuentas diseñado para una startup bootstrapped que:
- **Ahora**: Opera con una cuenta bancaria (Banco Chile), movimientos mínimos (suscripciones, pay-as-you-go)
- **Futuro**: Estructura numérica permite escalar sin reestructurar (más bancos, más productos, más proyectos)

**Filosofía QAI**: Simple, claro, trazable. Solo lo necesario ahora, pero la senda abierta para crecer.

---

## 🏗️ Estructura de Cuentas

### ACTIVOS

#### 11. CUENTAS CORRIENTES Y BANCOS

| Código | Nombre | Estado | Notas |
|:---:|:---|:---:|:---|
| 11.02 | **Banco Chile** | ✅ Operativa | Cuenta Vista `00-001-24253-56`. Única cuenta con movimientos actualmente. |
| 11.03 | **BancoEstado** | 🔵 Reservada | Backup sin movimientos previstos (costo $0). Reservada para futura necesidad. |

**Decisión de Diseño**:
- No usamos `11.01 Caja/Banco` genérico. Preferimos cuentas específicas para trazabilidad.
- Reservamos `11.04`, `11.05`, etc. para futuros bancos sin necesidad de reestructurar.

#### 12. CUENTAS POR COBRAR

| Código | Nombre | Uso |
|:---:|:---|:---|
| 12.01 | **Cuentas por Cobrar Clientes** | Facturas emitidas pendientes de pago (ej: FedEx, otros SaaS) |

**Registro**: Se crea cuando se emite factura. Se cancela cuando se recibe pago en `11.02 Banco Chile`.

---

### PASIVOS

#### 21. PASIVOS CORRIENTES

| Código | Nombre | Uso | Notas |
|:---:|:---|:---|:---|
| 21.01 | **Préstamos Socios** | Préstamos del founder a QAI | Mutuo consensual sin documento de crédito (no gatilla Impuesto de Timbres). |
| 21.02 | **Retenciones por Pagar** | Retenciones de boletas honorarios (10,75%) | Se declara en F29 y se paga al SII. |
| 21.03 | **Comisiones por Pagar** | 🔵 Reservada | Para futuras comisiones (ej: Ligia u otros) |
| 21.04 | **Proveedores Extranjeros** | Deuda pendiente con proveedores en USD (ej: GitHub, Cursor) | Se registra al valor según dólar observado (SII). Se cancela con pago real del banco. La diferencia se ajusta en cuenta de diferencia de cambio. |

---

### INGRESOS

#### 41. VENTAS

| Código | Nombre | Uso | Ejemplo |
|:---:|:---|:---|:---|
| 41.01 | **Ventas Servicios** | Ventas principales de QAI | |
| 41.01.01 | Ventas Invoice Match | Ingresos recurrentes producto Invoice Match | FedEx: $800.000/mes |
| 41.01.02 | Ventas Consultoría | Servicios de consultoría puntuales | |
| 41.01.03 | Ventas Otros SaaS | 🔵 Escalable | Para futuros productos SaaS |

**Nota**: Estructura permite agregar subcuentas por producto sin modificar la estructura base.

---

### COSTOS

#### 51. COSTOS DIRECTOS (COGS)

| Código | Nombre | Uso | Tracking |
|:---:|:---|:---|:---|
| 51.01 | **Costos Directos por Proyecto** | Costos variables directamente asociados a productos | Por proyecto/producto |
| 51.01.XX | Costos Directos [Proyecto] | APIs, infraestructura específica del producto | Ej: 51.01.01 Invoice Match, 51.01.02 Gestión Zen |

**Ejemplos de Costos Directos**:
- APIs Gemini/Groq por proyecto
- Supabase por proyecto ($25 USD/proyecto)
- Cloudflare por proyecto
- Otros servicios pay-as-you-go asignados a producto específico

**Regla**: Si el costo es atribuible directamente a un producto/cliente, va aquí. Si es general (suscripciones), va a Gastos Fijos (61.01).

---

### GASTOS

#### 61. GASTOS OPERACIONALES

##### 61.01 Gastos Fijos

| Código | Nombre | Ejemplos | Notas |
|:---:|:---|:---|:---|
| 61.01.01 | **Oficina Virtual** | Alquiler oficina virtual | ~$50.000/mes |
| 61.01.02 | **Contador** | Honorarios contador | ~$80.000/mes |
| 61.01.03 | **Suscripciones Tech** | Cursor, Copilot, Antigravity, Google One | Requiere Doc. 46 si extranjero |

##### 61.02 Gastos Variables R&D

| Código | Nombre | Uso | Ejemplos |
|:---:|:---|:---|:---|
| 61.02.01 | **Experimentos IA** | Experimentación no asignada a producto específico | Testing de modelos, prototipos |

**Regla**: R&D solo si no es atribuible a un producto específico. Si ya es parte de un producto, va a Costos Directos (51.01).

##### 61.03 Gastos Financieros

| Código | Nombre | Uso | Notas |
|:---:|:---|:---|:---|
| 61.03.01 | **Diferencia de Cambio** | Diferencias entre dólar observado (SII) y tipo de cambio aplicado por banco | Se registra cuando hay discrepancia ≥ $1.000 CLP. Si es menor, se ajusta directamente en el gasto |

**Regla**: 
- **Dólar Observado**: Usar siempre para Factura de Compra (Doc. 46) según fecha de emisión
- **Registro Bancario**: Usar monto real cargado por el banco en `11.02 Banco Chile`
- **Diferencia**: Si la diferencia es significativa (≥ $1.000 CLP), registrar en `61.03.01`. Si es menor, ajustar directamente en el gasto original.

---

#### 71. COMISIONES Y HONORARIOS

| Código | Nombre | Uso | Tratamiento |
|:---:|:---|:---|:---|
| 71.01 | **Comisiones Pagadas** | Boletas de honorarios con retención | Ej: Comisión Ligia. Deducible F22, requiere retención 10,75% |

**Asiento Contable**:
```
Débito:  71.01 Comisiones Pagadas   $[Neto]
Crédito: 11.02 Banco Chile          $[Neto - Retención]
Crédito: 21.02 Retenciones por Pagar $[Retención]
```

---

### CUENTAS DE CONTROL IVA

#### 81. IVA

| Código | Nombre | Uso | Declaración |
|:---:|:---|:---|:---|
| 81.01 | **IVA Crédito Fiscal** | IVA recuperable de compras | Se declara en F29 como crédito |
| 81.02 | **IVA Débito Fiscal** | IVA cobrado en ventas | Se declara en F29 como débito |

**Regla**: 
- **Crédito**: IVA de Facturas de Compra (Doc. 46 para servicios extranjeros)
- **Débito**: IVA de facturas emitidas a clientes
- **Diferencia**: Crédito - Débito = IVA a pagar o remanente

---

## 📊 Tabla de Decisión Rápida

### Clasificación de Gastos

| Tipo de Gasto | Categoría FinOps | Cuenta Contable | Subcuenta | Doc. 46? | Notas |
|:---|:---:|:---:|:---:|:---:|:---|
| Suscripción Cursor/Copilot | Fijo | 61.01.03 | Suscripciones Tech | ✅ Sí | Usar dólar observado para Doc. 46, monto real banco para registro |
| Suscripción GitHub/Copilot | Fijo | 61.01.03 | Suscripciones Tech | ✅ Sí | Usar dólar observado para Doc. 46, monto real banco para registro |
| Oficina Virtual | Fijo | 61.01.01 | Oficina Virtual | ❌ No | |
| Contador | Fijo | 61.01.02 | Contador | ❌ No | |
| API Gemini (Invoice Match) | Variable Proyecto | 51.01.XX | Costos Directos [Proyecto] | ✅ Sí | |
| Supabase (Invoice Match) | Variable Proyecto | 51.01.XX | Costos Directos [Proyecto] | ✅ Sí | |
| Experimentación IA (Labs) | Variable R&D | 61.02.01 | Experimentos IA | ✅ Sí | |
| Diferencia de Cambio (≥ $1.000) | Fijo | 61.03.01 | Diferencia de Cambio | ❌ No | Solo si diferencia es significativa |
| Comisión Ligia | Variable Proyecto | 71.01 | Comisiones Pagadas | ❌ No | Boleta Honorarios |

### Clasificación de Ingresos

| Tipo de Ingreso | Cuenta Contable | Subcuenta | IVA |
|:---|:---:|:---:|:---:|
| Factura FedEx (Invoice Match) | 41.01 | 41.01.01 Ventas Invoice Match | 19% |
| Consultoría puntual | 41.01 | 41.01.02 Ventas Consultoría | 19% |
| Préstamo Socio | 21.01 | Préstamos Socios | ❌ No (Pasivo) |

---

## 🔄 Registro de Movimientos

### Movimiento de Banco Chile (11.02)

**Débitos** (Aumenta saldo):
- Cobranzas de facturas
- Préstamos de socio
- Otros ingresos en efectivo

**Créditos** (Disminuye saldo):
- Pagos de gastos
- Transferencias de salida
- Retiros de efectivo

**Regla de Oro**: Todo movimiento en `11.02 Banco Chile` debe tener contrapartida en otra cuenta.

**Ejemplos de Asientos**:

**Gasto con suscripción extranjera** (Formal - Libro Diario):
```
Débito:  61.01.03 Suscripciones Tech   $[Neto USD o Monto Real Banco]
Débito:  81.01 IVA Crédito Fiscal      $[IVA SII para Doc. 46]
Crédito: 11.02 Banco Chile             $[Monto Real Banco]
Crédito: 21.04 Proveedores Extranjeros $[IVA SII]  (si Doc. 46 pendiente)
Nota: Doc. 46 pendiente para recuperar IVA (si aplica)
```

**Ingreso por facturación** (Formal - Libro Diario):
```
Al emitir factura:
Débito:  12.01 Cuentas por Cobrar      $[Bruto]
Crédito: 41.01.01 Ventas Invoice Match $[Neto]
Crédito: 81.02 IVA Débito Fiscal       $[IVA]

Cuando cobra:
Débito:  11.02 Banco Chile             $[Bruto]
Crédito: 12.01 Cuentas por Cobrar      $[Bruto]
```

**⚠️ IMPORTANTE**: Estos son ejemplos formales para `Libro_Diario`. Para registro operativo diario, usar `Registro_Diario` (formato simplificado). Ver protocolo [`generar_asientos_libro_diario.md`](../../../../playbooks/generar_asientos_libro_diario.md) para proceso completo.

---

## 📈 Escalabilidad del Plan

### Agregar Nuevo Banco

**Cuando sea necesario**:
1. Asignar siguiente número disponible: `11.04`, `11.05`, etc.
2. Actualizar este documento
3. Registrar en changelog operativo

**Ejemplo futuro**: `11.04 Banco Santander` (si se abre cuenta)

### Agregar Nuevo Producto/Servicio

**Para Ingresos**:
- Agregar subcuenta: `41.01.04 Ventas [Nuevo Producto]`
- Mantener estructura base

**Para Costos Directos**:
- Crear subcuenta: `51.01.XX Costos Directos [Nuevo Producto]`
- Tracking por producto independiente

### Agregar Nuevo Tipo de Gasto

**Si es Fijo**:
- Agregar a `61.01.XX` si es nuevo tipo (ej: `61.01.04 Marketing`)
- O usar existente si cabe en categoría

**Si es Variable por Proyecto**:
- Ir a `51.01.XX` (Costos Directos)
- **NO** crear nueva categoría de Gastos Fijos

---

## ✅ Validaciones y Buenas Prácticas

### Al Registrar un Movimiento

**Registro Operativo (Registro Diario)**:
1. ✅ Verificar que la cuenta existe en este Plan
2. ✅ Confirmar que la clasificación es correcta (Fijo vs Variable vs R&D)
3. ✅ Asegurar que el movimiento bancario coincide con el extracto
4. ✅ Registrar comprobante y notas necesarias

**Registro Formal (Libro Diario)**:
1. ✅ Validar que el asiento contable tiene débito y crédito balanceados
2. ✅ Verificar que Suma Débitos = Suma Créditos por asiento
3. ✅ Asegurar que total período balancea (Suma Total Débitos = Suma Total Créditos)
4. ✅ Trazabilidad completa desde Registro Diario a Libro Diario

**Referencia**: Ver protocolo [`generar_asientos_libro_diario.md`](../../../../playbooks/generar_asientos_libro_diario.md) para proceso completo.

### Al Final de Mes

1. ✅ Verificar saldo de `11.02 Banco Chile` coincide con extracto bancario
2. ✅ Revisar que todas las cuentas por cobrar están actualizadas
3. ✅ Validar que IVA (81.01 y 81.02) suma correctamente para F29
4. ✅ Conciliar movimientos registrados vs extracto bancario

---

## 🔗 Referencias Relacionadas

- **Manual Tributario**: [`/Empresa/03_ADMINISTRACION_FINANZAS/MANUAL_TRIBUTARIO_Y_OPERATIVO.md`](../../../../../Empresa/03_ADMINISTRACION_FINANZAS/MANUAL_TRIBUTARIO_Y_OPERATIVO.md)
- **Protocolo Registro Bancario**: [`/QaiCore/playbooks/registro_movimiento_bancario.md`](../../../../playbooks/registro_movimiento_bancario.md)
- **Protocolo Conciliación**: [`/QaiCore/playbooks/conciliacion_bancaria.md`](../../../../playbooks/conciliacion_bancaria.md)
- **Playbook Gastos/Ingresos**: [`/QaiCore/playbooks/registrar_gasto_ingreso.md`](../../../../playbooks/registrar_gasto_ingreso.md)

---

**Versión**: 1.0  
**Creado**: 10-Ene-2026  
**Responsable**: Finn  
**Revisión**: Cuando se agreguen nuevas cuentas o cambien necesidades operativas

