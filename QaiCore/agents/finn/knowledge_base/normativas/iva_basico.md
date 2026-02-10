# IVA Básico - Chile

**Fuente**: Decreto Ley 825 (Ley de IVA) - SII  
**Vigencia**: Actualizado a Diciembre 2025  
**Última actualización**: 27-Dic-2025

---

## Resumen

El **IVA (Impuesto al Valor Agregado)** es un impuesto que grava las ventas y servicios en Chile. Para The QAI Company SpA:
- Tasa estándar: **19%**
- Declaración mensual obligatoria: **Formulario 29 (F29)**
- Plazo: Hasta día **12** del mes siguiente (o día **20** con F29 electrónico)

---

## 1. Conceptos Fundamentales

### Débito Fiscal
IVA que **debes pagar** al SII por tus ventas/servicios.

**Fórmula**: `Ventas Netas × 19% = Débito Fiscal`

**Ejemplo**:
- Ventas del mes: $1.000.000 neto
- Débito Fiscal: $190.000

### Crédito Fiscal
IVA que **puedes recuperar** por compras relacionadas con tu giro.

**Fórmula**: `Compras Netas × 19% = Crédito Fiscal`

**Ejemplo**:
- Compras del mes: $500.000 neto
- Crédito Fiscal: $95.000

### Diferencia a Pagar/Recuperar
```
Si Débito > Crédito → Pagas la diferencia al SII
Si Crédito > Débito → Remanente a favor (se arrastra al mes siguiente)
```

**Ejemplo**:
```
Débito:  $190.000
Crédito: $ 95.000
A Pagar: $ 95.000
```

---

## 2. Declaración Mensual (F29)

### Obligación
**Desde el mes en que se inicia actividades**, SIEMPRE declarar F29:
- **Con movimiento**: Declarar ventas y compras
- **Sin movimiento**: Declarar "sin movimiento" para evitar multas

### Para QAI Company
- **Inicio de actividades**: 19 de Diciembre 2025
- **Primera declaración**: Enero 2026 (por período diciembre 2025)
- **Tipo**: Declaración "sin movimiento" si no hay operaciones

### Plazos
- **Hasta día 12** del mes siguiente (F29 papel o web básico)
- **Hasta día 20** del mes siguiente (F29 electrónico con certificado digital)

**Ejemplo**:
- Ventas de enero 2026 → Declarar entre 1 y 20 de febrero 2026

---

## 3. Casos Especiales para QAI

### A. Servicios a Clientes Chilenos
**Factura Afecta a IVA (19%)**

```
Ejemplo:
- Servicio: $1.000.000 + IVA
- IVA (19%): $190.000
- Total: $1.190.000
```

Tu obligación:
- Emitir factura electrónica
- Registrar en Libro de Ventas
- Declarar $190.000 como Débito Fiscal en F29

### B. Servicios a Clientes Extranjeros
**Exportación de Servicios (Exento IVA)**

Requisitos:
- Cliente sin domicilio en Chile
- Servicio consumido fuera de Chile

Tu obligación:
- Emitir factura de exportación
- Declarar en F29 como "Exportación" (Código 103)
- **No cobras IVA**, pero **sí puedes recuperar** el IVA de tus compras

### C. Compras de Servicios Digitales Extranjeros (SaaS)
**Factura de Compra (Doc. 46)**

Ejemplos: GitHub, Cursor, AWS, OpenAI, Gemini API, Claude.

**Procedimiento**:
1. Proveedor envía Invoice sin IVA chileno
2. QAI emite **Factura de Compra (Doc. 46)** en el SII
3. Se retiene 19% de IVA
4. Ese IVA se usa como **Crédito Fiscal** en F29

**Efecto "Suma Cero"**:
- Débito: $X (por retención)
- Crédito: $X (por compra del giro)
- Resultado: $0 a pagar, pero gasto 100% deducible

Ver guía detallada: [Facturación SaaS Extranjero](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/lex/knowledge_base/guia_facturacion_saas_extranjero.md)

---

## 4. Régimen Simplificado vs General

### QAI está en **Régimen General** (Pro Pyme General 14 D3)
- Facturación electrónica obligatoria
- Libro de compras y ventas
- Declaración mensual F29
- Declaración anual F22 (Impuesto a la Renta)

---

## 5. Registro en Libros

### Libro de Ventas
Todas las facturas emitidas (afectas y exentas).

**Campo clave**: Monto Neto, IVA, Total

### Libro de Compras
Todas las facturas recibidas + Facturas de Compra Doc. 46.

**Campo clave**: Crédito Fiscal (solo facturas afectas)

---

## 6. Sanciones

### Declaración fuera de plazo
- **Multa**: 10% del impuesto adeudado (mínimo 1 UTM ≈ $67.000)
- **Intereses**: 1,5% mensual sobre monto adeudado

### No declarar (aunque sea "sin movimiento")
- **Multa automática**: 1 UTM por mes sin declarar

### No emitir factura
- **Multa**: 2 UTM a 40 UTM por cada factura

---

## 7. Flujo Operativo para Finn

### Al registrar una venta:
```markdown
1. Emitir factura electrónica (mismo día)
2. Registrar en Libro de Ventas
3. Sumar al Débito Fiscal del mes
4. Actualizar proyección de F29
```

### Al registrar una compra:
```markdown
1. Verificar que factura esté a nombre de QAI (RUT correcto)
2. Verificar que sea afecta a IVA (19%)
3. Registrar en Libro de Compras
4. Sumar al Crédito Fiscal del mes
5. Si es SaaS extranjero: Emitir Doc. 46
```

### Al cerrar el mes:
```markdown
1. Consolidar Libro de Ventas → Total Débito
2. Consolidar Libro de Compras → Total Crédito
3. Calcular diferencia
4. Preparar borrador F29
5. Solicitar aprobación a Alejandro
6. Declarar en SII (antes del día 20)
7. Pagar si corresponde
```

---

## 8. Alertas Automáticas (para Finn)

### 7 días antes del vencimiento:
```
📅 Recordatorio: F29 de [mes] vence [fecha].
Estado actual: 
- Débito: $X
- Crédito: $Y
- A pagar: $Z (o remanente: $Z)
¿Preparamos la declaración?
```

### 1 día antes:
```
🚨 URGENTE: F29 vence mañana.
¿Ya declaraste o lo hacemos ahora?
```

### Si hay remanente acumulado por 3+ meses:
```
💡 Tienes $X en remanente IVA desde hace [N] meses.
Opciones:
1. Esperar a compensar con futuras ventas
2. Solicitar devolución al SII
¿Qué prefieres?
```

---

## 9. Preguntas Frecuentes

### ¿Qué pasa si no tengo ventas en un mes?
Igual debes declarar F29 "sin movimiento". No pagas IVA, pero evitas multas.

### ¿Puedo recuperar IVA de compras personales?
**NO**. Solo compras relacionadas con el giro de la empresa y a nombre del RUT de QAI.

### ¿Y si mi cliente no paga la factura?
Igual debes declarar el IVA (Débito Fiscal). El IVA se genera al emitir la factura, no al cobrar.

### ¿Puedo pagar el F29 en cuotas?
Sí, solicitando convenio de pago en el SII. Pero genera intereses.

---

## 10. Recursos Útiles

- **SII Web**: https://www.sii.cl
- **Portal MIPYME SII**: https://mipyme.sii.cl
- **Consultas telefónicas**: 223951111 (lunes a viernes, 9-18h)
- **Facturación gratuita SII**: https://www4.sii.cl/siiWSPublico/

---

## 🚨 IMPORTANTE

Esta es información resumida. Ante casos complejos:
1. Consultar con contador externo
2. Llamar al SII (consultas gratuitas)
3. Revisar normativa actualizada en sii.cl

**No inventar interpretaciones** en casos ambiguos.

---

**Próxima actualización**: Cuando cambie la tasa de IVA o normativa relevante  
**Responsable**: Finn (bajo supervisión de Alejandro)
