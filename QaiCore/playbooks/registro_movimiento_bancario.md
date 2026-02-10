# Playbook: Registro de Movimiento Bancario

> **Workflow para que Finn registre movimientos de la cuenta corriente Banco Chile**

---

## 🎯 Objetivo

Registrar de forma consistente cada movimiento (cargo o abono) en la cuenta corriente `11.02 Banco Chile`, asegurando trazabilidad, correcta clasificación contable y actualización automática de métricas (Runway, P&L).

---

## 🔄 Trigger (Cuándo ejecutar)

- Alejandro recibe notificación de movimiento en cuenta Banco Chile
- Alejandro comparte extracto bancario (parcial o oficial) con movimientos pendientes
- Hay cargo automático de suscripción (ej: Cursor, Copilot)
- Hay abono de cobranza de factura
- Hay transferencia recibida o enviada
- Usuario solicita: "Registra este movimiento bancario"

**⚠️ IMPORTANTE - Cartolas Parciales vs Oficiales**:
- **Cartola Parcial**: Extracto bancario compartido durante el mes (ej: primera quincena). Se usa **solo para procesar movimientos individuales**, NO se archiva en Drive.
- **Cartola Oficial**: Extracto bancario oficial de fin de mes. Se archiva en Drive para conciliación y referencia tributaria.

---

## 📋 Pre-requisitos

- Acceso a Google Sheets (Registro Diario)
- Información del movimiento (fecha, monto, concepto, tipo)
- Acceso a Google Drive (para archivar comprobantes si existen)
- Plan de Cuentas disponible (referencia: `/QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md`)

---

## 🛠️ Pasos del Workflow

### 1. Identificar el Movimiento

**Información Requerida**:
- **Fecha**: ¿Cuándo ocurrió el movimiento?
- **Monto**: ¿Cuánto? (distinguir cargo vs abono)
- **Concepto/Glosa**: ¿Qué dice el extracto bancario?
- **Tipo**: ¿Es CARGO (salida de dinero) o ABONO (entrada de dinero)?
- **Comprobante**: ¿Hay PDF/factura asociada?

**Si falta información**:
```
"Necesito [dato faltante] para registrar correctamente este movimiento. 
¿Me lo proporcionas o revisamos el extracto bancario juntos?"
```

---

### 2. Clasificar el Tipo de Movimiento

#### Movimientos Típicos Actuales (Minimalistas)

**CARGOS (Salida de dinero - Gastos)**:
- Suscripciones recurrentes: Cursor ($20 USD), Copilot ($10 USD), Antigravity, Google One
- Pay-as-you-go de productos en Lab: APIs Gemini, Supabase, Cloudflare
- Gastos operacionales: Oficina virtual, Contador
- Transferencias de salida

**ABONOS (Entrada de dinero - Ingresos)**:
- Cobranza de facturas (ej: FedEx)
- Préstamos del socio
- Otros ingresos

---

### 3. Determinar Cuenta Contable (Según Plan de Cuentas)

**Para CARGOS (Gastos)**:

| Concepto en Extracto | Cuenta Contable | Subcuenta | Doc. 46? |
|:---|:---:|:---|:---:|
| "CURSOR" / "CURSOR IDE" | 61.01.03 | Suscripciones Tech | ✅ Sí |
| "GITHUB" / "COPILOT" | 61.01.03 | Suscripciones Tech | ✅ Sí |
| "ANTIGRAVITY" | 61.01.03 | Suscripciones Tech | ✅ Sí |
| "GOOGLE ONE" | 61.01.03 | Suscripciones Tech | ⚠️ Ver caso específico |
| "GOOGLE CLOUD" / "GCP" | 51.01.XX | Costos Directos [Proyecto] | ✅ Sí |
| "SUPABASE" | 51.01.XX | Costos Directos [Proyecto] | ✅ Sí |
| "CLOUDFLARE" | 51.01.XX | Costos Directos [Proyecto] | ✅ Sí |
| Oficina Virtual | 61.01.01 | Oficina Virtual | ❌ No |
| Contador | 61.01.02 | Contador | ❌ No |
| Transferencia a [nombre] | Según destinatario | - | - |

**Para ABONOS (Ingresos)**:

| Concepto en Extracto | Cuenta Contable | Subcuenta | IVA? |
|:---|:---:|:---|:---:|
| "FEDEX" / "INVOICE MATCH" | 41.01 | 41.01.01 Ventas Invoice Match | 19% |
| "PRESTAMO" / De Alejandro | 21.01 | Préstamos Socios | ❌ No |
| Transferencia de [cliente] | 41.01 | Según producto | 19% |

**Tabla de Decisión Rápida**:
- ¿Es suscripción tech? → `61.01.03 Suscripciones Tech`
- ¿Es costo de API/infraestructura de producto? → `51.01.XX Costos Directos [Proyecto]`
- ¿Es cobranza de factura? → `12.01 Cuentas por Cobrar` → `11.02 Banco Chile`
- ¿Es préstamo socio? → `21.01 Préstamos Socios`

---

### 4. Manejar Diferencia de Cambio (Si es Gasto en USD)

**Si el movimiento es un pago en moneda extranjera (ej: GitHub, Cursor, AWS):**

**⚠️ IMPORTANTE - Equilibrio Contable:**
La ecuación contable debe mantenerse: **ACTIVO = PASIVO + CAPITAL + (INGRESOS - GASTOS)**

**Filosofía QAI: Simplicidad + Cumplimiento**

Para gastos en USD hay DOS conceptos distintos:
1. **Doc. 46 (SII)**: Usa dólar observado del día de la factura (requisito tributario) ✅ **Cumplimiento**
2. **Pago Real Banco**: Usa el monto que realmente salió del banco (incluye spread/comisiones) ✅ **Realidad**

**Procedimiento QAI (Simplificado pero Correcto):**

**Paso 1: Identificar Fechas**
- **Fecha Factura**: Día que recibes la factura del proveedor (ej: 09-Ene-2026)
- **Fecha Transacción Real**: Día que realmente ocurre la transacción (normalmente mismo día que factura)
- **Fecha Reflejo Banco**: Día que aparece en cartola (puede ser siguiente día hábil) - **NO usar para registro contable**

**Paso 2: Calcular Monto SII (Doc. 46)**
- Obtener dólar observado del día de la factura (Banco Central)
- Calcular: `Monto USD × Dólar Observado = Monto CLP (SII)`
- IVA SII: `Monto SII × 19%`

**Paso 3: Registrar Asiento Único (Para diferencias < $1.000 CLP)**
- Usar monto real del banco como gasto (incluye diferencia)
- IVA calcular sobre monto SII (para Doc. 46)
- Fecha contable: Fecha transacción real (no reflejo bancario)
- Diferencia pequeña se absorbe directamente en el gasto ✅ **Simplicidad**

**Paso 4: Registrar Diferencia (Solo si diferencia ≥ $1.000 CLP)**
- Si diferencia es significativa, registrar en cuenta `61.03.01 Diferencia de Cambio`
- Esto requiere dos asientos separados (método completo)

**Ejemplo GitHub ($10 USD, Transacción 09-Ene-2026):**
- **Fecha Factura**: 09-Ene-2026
- **Fecha Transacción Real**: 09-Ene-2026 (mismo día)
- **Fecha Reflejo Banco**: 12/01/2026 (próximo día hábil, solo reflejo)
- **Dólar Observado (09-Ene)**: $896,89 CLP/USD
- **Monto SII (Doc. 46)**: $10 × $896,89 = **$8.968,90 CLP**
- **IVA SII (19%)**: $1.704,09 CLP
- **Monto Banco Real**: **$9.250,00 CLP** (incluye spread/comisiones bancarias)
- **Diferencia**: $9.250 - $8.968,90 = **$281,10 CLP** (< $1.000, pequeña)

**⚠️ IMPORTANTE - Filosofía QAI: Simplicidad y Cumplimiento**

El banco solo cobra el gasto ($9.250), NO el IVA. El IVA es un concepto contable que se maneja con el SII mediante el Doc. 46.

**Asiento Único (Método Pragmático QAI - Diferencia < $1.000):**
```
Débito:  61.01.03 Suscripciones Tech    $9.250,00  (monto real banco - incluye diferencia)
Débito:  81.01 IVA Crédito Fiscal       $1.704,09  (calculado sobre monto SII para Doc. 46)
Crédito: 11.02 Banco Chile              $9.250,00  (monto real pagado - fecha reflejo 12/01)
Crédito: 21.04 Proveedores Extranjeros  $1.704,09  (IVA pendiente que se declarará en F29)
```

**Equilibrio Verificado:**
- Débitos: $9.250,00 + $1.704,09 = $10.954,09 ✅
- Créditos: $9.250,00 + $1.704,09 = $10.954,09 ✅
- **BALANCEADO** ✅

**En Notas del Registro:**
- "Fecha transacción: 09-Ene-2026 (reflejo banco: 12/01)"
- "Doc. 46: $8.968,90 (dólar obs. $896,89 del 09-Ene)"
- "IVA Doc. 46: $1.704,09 (19% sobre monto SII)"
- "Diferencia cambio/comisiones: $281,10 absorbida en gasto"
- "IVA pendiente se cancelará al declarar F29 (efecto suma cero)"

**Regla QAI (Simplicidad + Cumplimiento):**
1. **Para Doc. 46**: Usar siempre dólar observado del día de la factura (09-Ene-2026: $896,89) ✅ **Cumplimiento**
2. **Para registro bancario**: Usar monto real que salió del banco ($9.250) ✅ **Realidad**
3. **Para diferencias < $1.000**: Absorber directamente en el gasto ✅ **Simplicidad**
4. **Para IVA**: Calcular sobre monto SII para Doc. 46, se cancela en F29 (efecto suma cero) ✅ **Cumplimiento**
5. **Fecha contable**: Usar fecha de transacción real (09-Ene), no fecha de reflejo bancario (12/01) ✅ **Precisión**

---

### 5. Registrar en Google Sheets (Registro Diario)

**⚠️ IMPORTANTE - Dos Niveles de Registro**:

**Nivel 1 - Registro Diario (Operativo)**:
- Registro rápido diario de movimientos bancarios
- Formato operativo: 1 fila = 1 movimiento
- Propósito: Seguimiento diario de caja y clasificación FinOps

**Nivel 2 - Libro Diario (Formal)**:
- Registro contable formal con asientos completos (débito/crédito)
- Formato contable: Múltiples filas = 1 asiento completo
- Propósito: Cumplimiento contable formal y generación de Balance
- **Frecuencia**: Mensual o quincenal (ver protocolo `generar_asientos_libro_diario.md`)

**Flujo**:
```
Movimiento Bancario 
  → Registro Diario (inmediato, operativo) 
  → Al final de mes: Generar asientos formales en Libro Diario
```

---

### 5.1. Registrar en Registro_Diario (Operativo)

**Estructura de la Hoja** (verificar columnas actuales):
```
| Fecha | Tipo | Concepto | Categoría | Cuenta | Monto Neto | IVA | Monto Bruto | Retención | Monto Pagado | Proyecto | Comprobante | Notas |
```

**Pasos**:
1. Abrir Google Sheet: `QAI_Finanzas_2026` → Pestaña `Registro_Diario`
2. Insertar nueva fila después del último movimiento
3. Completar campos según clasificación del paso 3:
   - **Fecha**: Fecha del movimiento bancario
   - **Tipo**: `GASTO` o `INGRESO`
   - **Concepto**: Descripción clara (ej: "Cursor IDE - Suscripción Enero 2026")
   - **Categoría**: Fijo / Variable Proyecto / Variable R&D
   - **Cuenta**: Código completo (ej: `61.01.03 Suscripciones Tech`)
   - **Monto Neto**: Monto sin IVA (para gastos USD: usar monto real banco si diferencia < $1.000, o monto SII si diferencia ≥ $1.000)
   - **IVA**: Si aplica, monto del IVA (calculado sobre monto Neto)
   - **Monto Bruto**: Monto Neto + IVA (o igual si sin IVA)
   - **Retención**: Si aplica (ej: boleta honorarios)
   - **Monto Pagado**: Monto real cargado/recibido en banco (debe coincidir con extracto)
   - **Proyecto**: Invoice Match / Gestión Zen / General / R&D
   - **Comprobante**: Link o nombre de archivo (si existe)
   - **Notas**: Info adicional (ej: "Doc. 46 pendiente", "Diferencia cambio: $X", "Dólar obs.: $896,89")

4. Validar fórmulas automáticas:
   - Verificar que `Monto Bruto = Monto Neto + IVA`
   - Verificar que categorización es consistente

5. Verificar coincidencia con extracto bancario:
   - Monto registrado debe coincidir exactamente con extracto
   - Fecha debe ser la misma o muy cercana (diferencias de días por procesamiento son normales)

---

### 6. Actualizar Saldo de Banco Chile (11.02)

**Saldo Contable**:
- Calcular: `Saldo Anterior + Abonos - Cargos = Saldo Nuevo`
- Verificar que coincide con saldo del extracto bancario (o muy cercano, considerando movimientos pendientes)

**Si hay diferencia significativa**:
```
"⚠️ Diferencia detectada entre saldo contable y extracto bancario: $[X].
¿Hay movimientos pendientes por registrar o revisamos la conciliación?"
```

---

### 7. Archivar Comprobante (si existe)

**Si hay documento asociado** (facturas, recibos, comprobantes individuales):
1. Subir a Google Drive:
   - Carpeta: `/Empresa/03_ADMINISTRACION_FINANZAS/comprobantes/2026/[MM]-[mes]/`
   - Nombre: `YYYY-MM-DD_[tipo]_[concepto].pdf` 
   - Ejemplo: `2026-01-07_invoice_cursor_ene.pdf`, `2026-01-08_receipt_google_one.pdf`

2. Actualizar columna "Comprobante" en Google Sheet con:
   - Link de Drive, O
   - Nombre del archivo si ya está en Drive

3. **⚠️ IMPORTANTE**: Si el archivo estaba en `/TorreDeControl/temp_files/` (landing zone):
   - **Eliminarlo** después de subirlo a Drive
   - Mantener la landing zone limpia (protocolo Zero Inbox)

**Si NO hay documento individual**:
- Nota en columna "Notas": "Comprobante pendiente" o "Extracto bancario solo"
- No crear recordatorio a menos que sea necesario (gastos significativos)

---

**📋 REGLA ESPECIAL: Cartolas Bancarias (Extractos)**

**Filosofía QAI: Simplicidad y Cumplimiento**

1. **Cartolas Parciales** (extractos durante el mes):
   - **Propósito**: Procesar movimientos individuales para registro inmediato
   - **Acción**: Extraer movimientos, registrar en `Registro_Diario`, archivar comprobantes individuales
   - **NO ARCHIVAR**: Las cartolas parciales NO se archivan en Drive (evita duplicados y confusión)
   - **Excepciones**: Solo archivar si hay discrepancia significativa que requiere investigación posterior

2. **Cartola Oficial de Fin de Mes**:
   - **Propósito**: Conciliación bancaria mensual y referencia tributaria
   - **Acción**: 
     - Archivar en Drive: `/Empresa/03_ADMINISTRACION_FINANZAS/comprobantes/2026/[MM]-[mes]/`
     - Nombre: `cartola_oficial_banco_chile_[mes]_[año].pdf` o `cartola_oficial_banco_chile_[mes]_[año].xlsx`
     - Usar para conciliación bancaria (ver protocolo `conciliacion_bancaria.md`)
   - **Cuándo**: Al finalizar el mes, cuando el banco emite el extracto oficial

3. **Razones**:
   - ✅ **Simplicidad**: Evita duplicados (parcial vs oficial)
   - ✅ **Cumplimiento**: Solo la oficial tiene validez contable/tributaria
   - ✅ **Trazabilidad**: Cada movimiento ya está registrado individualmente con su comprobante
   - ✅ **Eficiencia**: Reduce trabajo duplicado y riesgo de inconsistencias

---

### 8. Actualizar Métricas Impactadas

**Si es GASTO**:
- ✅ Actualizar Runway (recalcular saldo disponible)
- ✅ Actualizar categoría de costo (Fijo vs Variable)
- ✅ Actualizar costo por proyecto (si aplica a 51.01.XX)
- ✅ Actualizar P&L del período

**Si es INGRESO**:
- ✅ Actualizar MRR (si es recurrente, ej: FedEx)
- ✅ Actualizar Runway (aumenta saldo disponible)
- ✅ Actualizar P&L del período
- ✅ Si es cobranza: Actualizar estado de factura de "Pendiente" a "Pagado"

**Actualización Runway**:
```
Runway (meses) = Saldo Actual en 11.02 Banco Chile / Burn Rate Mensual
```

---

### 9. Verificar IVA (si aplica)

**Para GASTOS con IVA (Servicios Extranjeros)**:
- ✅ Verificar si requiere Factura de Compra (Doc. 46)
- ✅ Si sí: Agregar nota "Doc. 46 pendiente" y crear recordatorio en INBOX si es significativo
- ✅ Si ya existe Doc. 46: Registrar IVA como Crédito Fiscal (81.01)

**Para INGRESOS con IVA**:
- ✅ IVA Débito Fiscal (81.02) ya debe estar registrado en la factura original
- ✅ Verificar que el ingreso coincide con factura emitida
- ✅ Si hay diferencia, investigar y ajustar

---

### 10. Validación Final

**Checklist de Validación**:
- ✅ Monto coincide exactamente con extracto bancario
- ✅ Fecha correcta (mismo día o diferencia razonable por procesamiento)
- ✅ Tipo correcto (GASTO vs INGRESO)
- ✅ Cuenta contable correcta según Plan de Cuentas
- ✅ Clasificación FinOps correcta (Fijo vs Variable)
- ✅ Saldo contable actualizado
- ✅ Comprobante archivado (o en seguimiento)
- ✅ IVA gestionado correctamente
- ✅ Métricas actualizadas (Runway/P&L)

**Si algo falta o está incorrecto**:
```
"⚠️ Registro incompleto o con error: [dato/problema].
Acción requerida: [qué hacer para corregir]"
```

---

## ✅ Criterios de Éxito

**Registro Operativo (Inmediato)**:
- ✅ Movimiento registrado en Google Sheet `Registro_Diario`
- ✅ Cuenta contable correcta según Plan de Cuentas
- ✅ Saldo de `11.02 Banco Chile` actualizado y verificado
- ✅ Monto coincide con extracto bancario
- ✅ Comprobante archivado (si existe) o en seguimiento
- ✅ Métricas actualizadas (Runway, P&L)
- ✅ IVA gestionado correctamente (si aplica)

**Registro Formal (Mensual)**:
- ✅ Asientos formales generados en `Libro_Diario` (ver protocolo `generar_asientos_libro_diario.md`)
- ✅ Equilibrio contable validado (Suma Débitos = Suma Créditos)
- ✅ Movimientos marcados como "Asiento Generado" en Registro_Diario

---

## 🚨 Casos Especiales

### Movimiento sin Concepto Claro

**Si el extracto bancario tiene glosa confusa o genérica**:
1. Preguntar a Alejandro: "¿Qué es este movimiento de $[X] del [fecha]?"
2. Una vez aclarado, registrar con concepto claro
3. Si no se puede aclarar: Registrar como "Movimiento pendiente clasificación" y agregar a INBOX para seguimiento

### Diferencia de Fechas

**Si la fecha del extracto difiere de la fecha del movimiento**:
- **Normal**: Diferencia de 1-3 días por procesamiento bancario es común
- **Usar**: Fecha del extracto bancario (fecha contable)
- **Nota**: Si la diferencia es >5 días, investigar

### Movimientos Pendientes

**Si hay movimientos en extracto que no se han registrado aún**:
1. Registrar todos los movimientos del período
2. Marcar como "Conciliado" una vez que todos estén registrados
3. Si hay movimientos que requieren más información: Agregar nota y seguimiento

### Suscripciones Recurrentes

**Para suscripciones automáticas (Cursor, Copilot, etc.)**:
- Registrar cada mes cuando aparece en extracto
- Concepto claro: "Cursor IDE - Suscripción [Mes] [Año]"
- Si el monto cambia, agregar nota explicando cambio
- Doc. 46: Emitir una vez al mes consolidando todas las suscripciones del período (si es más eficiente)

---

## 📝 Notas para Finn

- **Consistencia**: Usar siempre las mismas cuentas y conceptos para el mismo tipo de movimiento
- **Prontitud**: Registrar lo antes posible (idealmente el mismo día que aparece en extracto)
- **Validación**: Siempre verificar montos contra extracto bancario antes de marcar como "Completado"
- **Trazabilidad**: Cada movimiento debe poder rastrearse desde extracto → Registro → Comprobante
- **Dudas**: Si no estás seguro de clasificación, preguntar antes de registrar

---

## 🔗 Referencias Relacionadas

- **Plan de Cuentas**: [`/QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md`](../agents/finn/knowledge_base/contabilidad/plan_cuentas.md)
- **Libro Diario Formal**: [`generar_asientos_libro_diario.md`](generar_asientos_libro_diario.md) 🆕
- **Playbook Gastos/Ingresos**: [`registrar_gasto_ingreso.md`](registrar_gasto_ingreso.md)
- **Protocolo Conciliación**: [`conciliacion_bancaria.md`](conciliacion_bancaria.md)
- **Banco Chile Detalles**: [`/QaiCore/agents/finn/knowledge_base/finops/banco_chile_details.md`](../agents/finn/knowledge_base/finops/banco_chile_details.md)

---

**Versión**: 1.0  
**Creado**: 10-Ene-2026  
**Responsable**: Finn (CFO QAI)  
**Revisión**: Cuando cambien patrones de movimientos o agreguen nuevas cuentas bancarias

