# Playbook: Facturar Cliente SaaS

> **Workflow completo: Desde Orden de Compra hasta Cobranza**

---

## 🎯 Objetivo

Emitir factura electrónica correcta, registrarla en contabilidad, y hacer seguimiento hasta cobranza.

---

## 🔄 Trigger (Cuándo ejecutar)

- Se recibe Orden de Compra (OC) firmada
- Inicio de servicio mensual (facturación recurrente)
- Usuario solicita: "Factura [Cliente] - [Período]"

---

## 📋 Pre-requisitos

- OC recibida y validada
- Cliente dado de alta en SII (si aplica)
- Autorización de Facturación Electrónica activa
- Template de factura disponible
- Datos del cliente completos (RUT, razón social, dirección, contacto)

---

## 🛠️ Pasos del Workflow

### 1. Validar OC y Datos del Cliente

**Verificar**:
- ✅ OC firmada recibida
- ✅ Datos del cliente correctos:
  - RUT
  - Razón Social
  - Dirección
  - Contacto (email, teléfono)
- ✅ Servicio/producto acordado
- ✅ Monto acordado (neto)
- ✅ Condiciones de pago (30 días, 60 días, etc.)
- ✅ Período facturado (mes/año)

**Si falta información**:
```
"⚠️ Faltan datos del cliente: [dato faltante]
Acción: Solicitar a [contacto] antes de facturar"
```

---

### 2. Calcular Montos

**Cálculo**:
```
Monto Neto: $[Acordado] CLP
IVA (19%): $[Neto × 0.19] CLP
Monto Bruto: $[Neto + IVA] CLP
```

**Ejemplo (Invoice Match - FedEx)**:
```
Monto Neto: $800.000 CLP
IVA (19%): $152.000 CLP
Monto Bruto: $952.000 CLP
```

**Notas**:
- Si el servicio es exento de IVA (verificar con Lex), entonces IVA = $0
- Monto neto siempre antes de IVA

---

### 3. Preparar Factura Electrónica

**Datos de la Factura**:
- **Número de Factura**: Secuencial (ej: 001, 002, 003...)
- **Fecha de Emisión**: Fecha actual
- **RUT Emisor**: RUT de The QAI Company SpA
- **Razón Social Emisor**: The QAI Company SpA
- **RUT Receptor**: RUT del cliente
- **Razón Social Receptor**: Razón social del cliente
- **Descripción**: Detalle del servicio/producto
- **Período**: Mes/año facturado (ej: "Enero 2026")
- **Monto Neto**: $X CLP
- **IVA**: $X CLP (19%)
- **Monto Bruto**: $X CLP
- **Condiciones de Pago**: (ej: "30 días")

**Template de Descripción**:
```
Suscripción Mensual - [Nombre Producto]
Período: [Mes] [Año]
Incluye: [Detalle de servicio]

Ejemplo:
Suscripción Mensual - The QAI Invoice Matcher
Período: Enero 2026
Incluye: Procesamiento de facturas y órdenes de compra, dashboard, soporte técnico
```

---

### 4. Emitir Factura en SII

**Proceso**:
1. Ingresar a `sii.cl` → Servicios Online → Factura Electrónica
2. Seleccionar: "Emitir Factura Electrónica"
3. Completar formulario con datos del paso 3
4. Revisar previsualización
5. **Enviar/Firmar** factura (con FEA)
6. Obtener PDF de la factura generada
7. Obtener número de folio/Timbre

**Verificación Post-Emisión**:
- ✅ Factura aparece en "Libro de Ventas"
- ✅ PDF generado correctamente
- ✅ Folio asignado
- ✅ Timbre electrónico presente

---

### 5. Enviar Factura al Cliente

**Método de Envío**:
- **Email**: Enviar PDF a contacto del cliente
- **Copia**: Guardar copia en Google Drive

**Email Template**:
```
Asunto: Factura N° [Número] - The QAI Company SpA - [Período]

Estimado/a [Nombre Contacto],

Adjunto encontrarás la Factura Electrónica N° [Número] correspondiente al período [Mes] [Año] por los servicios de [Producto/Servicio].

Detalle:
- Período: [Mes] [Año]
- Monto Neto: $[X] CLP
- IVA (19%): $[Y] CLP
- Total: $[Z] CLP
- Condiciones de Pago: [X días]

La factura fue emitida el [Fecha] y aparece registrada en el SII.

Para cualquier consulta, no dudes en contactarnos.

Saludos cordiales,
Alejandro Bustamante
The QAI Company SpA
```

**Archivo en Drive**:
- Ruta: `/Empresa/03_ADMINISTRACION_FINANZAS/facturacion/2026/01-enero/`
- Nombre: `factura_001_[cliente]_[periodo].pdf`

---

### 6. Registrar en Contabilidad

**Registro en Google Sheets (Registro Diario)**:
```
Fecha: [Fecha de emisión]
Tipo: INGRESO
Concepto: [Cliente] - [Producto] - [Período]
Categoría: SaaS Recurrente (o según tipo)
Cuenta: 41.01.XX Ventas Servicios
Monto Neto: $[X] CLP
IVA: $[Y] CLP (Débito Fiscal)
Monto Bruto: $[Z] CLP
Proyecto: [Nombre Proyecto]
Comprobante: factura_001_[cliente]_[periodo].pdf
Notas: Facturado [fecha], cobranza a [X días], estado: Pendiente
```

**Asiento Contable (Al Emitir Factura)**:
```
Débito:  12.01 Cuentas por Cobrar          $[Bruto]
Crédito: 41.01.XX Ventas Servicios        $[Neto]
         81.02 IVA Débito Fiscal          $[IVA]
```

**Asiento Contable (Al Recibir Pago)**:
```
Débito:  11.02 Banco Chile                 $[Bruto]
Crédito: 12.01 Cuentas por Cobrar          $[Bruto]
```

**Estado Inicial**: Cuenta por Cobrar (12.01) hasta que se reciba el pago en 11.02 Banco Chile

**Referencia**: Ver [Plan de Cuentas](../../QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md) para estructura de cuentas 12.01, 11.02 y 41.01.

---

### 7. Actualizar Tracking de Facturación

**Sheet de Control de Facturación**:
```
| Número | Fecha Emisión | Cliente | Producto | Período | Neto | IVA | Bruto | Estado Cobranza | Fecha Pago | Notas |
```

**Estados de Cobranza**:
- **Pendiente**: Facturado, esperando pago
- **En Proceso**: Cliente confirmó recepción, procesando pago
- **Pagado**: Pago recibido en cuenta
- **Vencido**: Pasado plazo de pago sin recibir

---

### 8. Registrar en Libro de Ventas (SII)

**Nota**: La factura aparece automáticamente en Libro de Ventas al emitirse.

**Verificación**:
- ✅ Factura aparece en Libro de Ventas del SII
- ✅ Datos coinciden con lo emitido
- ✅ IVA Débito Fiscal registrado

---

### 9. Seguimiento de Cobranza

**Proceso**:
1. **Día 0 (Emisión)**: Factura enviada, estado "Pendiente"
2. **Día +7**: Seguimiento amigable (si no hay confirmación de recepción)
3. **Día +25 (si plazo 30 días)**: Recordatorio de vencimiento próximo
4. **Día +30**: Verificar pago en extracto bancario
5. **Si pagó**: Actualizar estado a "Pagado", registrar en contabilidad
6. **Si no pagó**: Seguimiento (email/llamada), considerar intereses si aplica

**Registro de Pago**:
Cuando se recibe el pago, seguir [Protocolo de Registro de Movimiento Bancario](registro_movimiento_bancario.md):

```
Fecha: [Fecha de pago]
Tipo: INGRESO (Pago Factura)
Concepto: Cobranza Factura N° [Número] - [Cliente]
Cuenta Débito: 11.02 Banco Chile (cuando se recibe el pago)
Cuenta Crédito: 12.01 Cuentas por Cobrar (cancela la cuenta por cobrar)
Monto: $[Bruto] CLP
Estado: Pagado
```

**Nota**: El movimiento de cobranza se registra como ABONO en 11.02 Banco Chile y cancela la cuenta 12.01 Cuentas por Cobrar.

---

### 10. Actualizar Métricas

**Actualizar**:
- ✅ **MRR**: Si es suscripción recurrente, actualizar MRR mensual
- ✅ **Runway**: Recalcular cuando se reciba el pago
- ✅ **P&L**: Actualizar ingresos del período
- ✅ **Estado de Cliente**: Actualizar tracking de facturación

---

### 11. Registrar IVA para Declaración F29

**Nota**: La factura ya está en Libro de Ventas, pero debe incluirse en preparación de F29.

**Para F29**:
- ✅ IVA Débito Fiscal: Sumar a total de ventas del mes
- ✅ Se declara en F29 del mes correspondiente

---

### 12. Documentación Final

**Actualizar**:
- ✅ Google Sheet: Registro Diario
- ✅ Google Sheet: Control de Facturación
- ✅ Google Drive: Factura PDF archivada
- ✅ AGENT_ACTIVITY.md: Nota de facturación
- ✅ STATUS.md: Actualizar MRR si es significativo

**Formato AGENT_ACTIVITY.md**:
```markdown
### 05-Ene-2026 - Finn
- Factura emitida: N° 001 - FedEx - Invoice Match - Enero 2026
- Monto: $800.000 neto + $152.000 IVA = $952.000 bruto
- Estado: Pendiente de cobranza (plazo 30 días)
- MRR actualizado: $800.000 CLP
```

---

## ✅ Criterios de Éxito

- ✅ Factura emitida correctamente en SII
- ✅ PDF generado y enviado al cliente
- ✅ Factura archivada en Google Drive
- ✅ Registrada en contabilidad (Registro Diario)
- ✅ Tracking de cobranza actualizado
- ✅ IVA registrado para F29
- ✅ Métricas actualizadas (MRR, Runway)
- ✅ Documentación completa

---

## 🚨 Casos Especiales

### Facturación Recurrente (SaaS Mensual)

**Proceso Automatizado**:
- Crear recordatorio mensual en calendario/INBOX
- Facturar el día X de cada mes
- Usar mismo template, cambiar solo período
- Secuencia de números consecutiva

**Ejemplo**:
- Factura 001: Enero 2026
- Factura 002: Febrero 2026
- Factura 003: Marzo 2026
- ...

---

### Factura con Comisión (Ej: Ligia 25%)

**Proceso**:
1. Facturar monto completo al cliente ($800k neto)
2. Calcular comisión ($800k × 25% = $200k)
3. Registrar comisión como gasto cuando se pague
4. **No** descontar comisión del monto facturado al cliente

**Registro de Comisión**:
```
Cuando se pague la comisión:
Fecha: [Fecha pago]
Tipo: GASTO
Concepto: Comisión Ligia - Invoice Match - [Período]
Cuenta: 71.01 Comisiones Pagadas
Monto: $200.000 CLP
Notas: 25% de facturación neta
```

---

### Factura Exenta de IVA

**Cuándo aplicar**:
- Servicios de educación/capacitación (código 855000)
- Exportación de servicios (cliente extranjero)
- Otros casos según normativa (consultar con Lex)

**Proceso**:
- Marcar factura como "Exenta" en SII
- IVA = $0
- Monto Neto = Monto Bruto
- Descripción debe indicar motivo de exención

---

## 📝 Notas para Finn

- **Numeración**: Mantener secuencia consecutiva de números de factura
- **Prontitud**: Facturar a tiempo (inicio de período o según acuerdo)
- **Seguimiento**: No olvidar seguimiento de cobranza
- **Archivo**: Siempre guardar PDF en Drive organizadamente
- **IVA**: Verificar siempre si es afecto o exento antes de facturar
- **Dudas**: Si hay duda sobre monto, condiciones, o IVA, consultar antes de emitir

---

**Referencias Relacionadas**:
- [Plan de Cuentas Completo](../../QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md)
- [Protocolo de Registro de Movimiento Bancario](registro_movimiento_bancario.md)
- [Protocolo de Conciliación Bancaria](conciliacion_bancaria.md)
- [Playbook Registrar Gasto/Ingreso](registrar_gasto_ingreso.md)

**Versión**: 1.1  
**Creado**: 30-Dic-2025  
**Actualizado**: 10-Ene-2026 (Integración con Plan de Cuentas y protocolos bancarios)  
**Responsable**: Finn (Agente Financiero)

