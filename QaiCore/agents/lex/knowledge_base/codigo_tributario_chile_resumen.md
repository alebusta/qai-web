# Código Tributario de Chile - Resumen para QAI

**Fuente**: Servicio de Impuestos Internos (SII) - https://www.sii.cl  
**Fecha**: Diciembre 2025  
**Aplica a**: The QAI Company SpA (Pro Pyme General 14 D3)

---

## Resumen Ejecutivo

Este documento resume los aspectos clave del Código Tributario chileno relevantes para QAI:
- Declaración mensual IVA (Formulario 29)
- Régimen Pro Pyme General (14 D3)
- Obligaciones de facturación electrónica
- Plazos y sanciones

---

## 1. Declaración Mensual IVA (F29)

### ¿Qué es?
Formulario obligatorio para declarar IVA mensual y otros impuestos.

### ¿Cuándo se declara?
- **Plazo normal**: Hasta el día 12 del mes siguiente
- **Con Form 29 electrónico**: Hasta el día 20 del mes siguiente
- Ejemplo: Ventas de enero → Declarar hasta 12-feb (o 20-feb si es electrónico)

### ¿Qué se declara?
- IVA ventas (débito fiscal)
- IVA compras (crédito fiscal)
- PPM (Pago Provisional Mensual) si aplica
- Retenciones si corresponde

### Primera Declaración
La obligación de declarar el F29 nace **desde el mes en que se realiza el Inicio de Actividades**, independientemente de si hay ventas o compras.
- Si hay movimiento: Declarar ventas y compras.
- Si NO hay movimiento: Realizar "Declaración sin Movimiento" para evitar multas.
- Plazo: Mes siguiente al inicio (ej: Inicio en Dic → Declarar en Ene).

---

## 2. Régimen Tributario: Pro Pyme General (14 D3)

### Características
- **Tasa impuesto**: 25% sobre renta líquida imponible
- **Ventajas**:
  - Contabilidad simplificada
  - Diferimiento del impuesto al retiro de utilidades
  - Depreciación acelerada

### Requisitos
- Ingresos anuales < 75.000 UF (~$2.300M CLP aprox)
- Cumplir obligaciones tributarias al día

### Declaración Anual
- **Formulario 22**: Se declara en abril del año siguiente
- Ejemplo: Ingresos 2025 → Declarar en abril 2026

---

## 3. Facturación Electrónica

### Obligación
Todas las empresas deben facturar electrónicamente (Ley vigente).

### Tipos de Documentos
- **Factura Electrónica**: Ventas afectas a IVA
- **Factura Exenta**: Servicios exentos (ej: educación según casos)
- **Boleta Electrónica**: Ventas a consumidor final

### Activación
Solicitar autorización en SII (www.sii.cl) con:
- Certificado digital (firma electrónica)
- Timbraje electrónico

### Plazos
- Emitir factura: Mismo día de la prestación del servicio o entrega del bien
- Enviar al SII: Antes de medianoche del día de emisión

---

## 4. Patente Municipal

### ¿Qué es?
Permiso municipal para operar en una comuna específica.

### ¿Cuándo se necesita?
Depende de los giros:
- **Giros comerciales** (ej: venta de productos): SÍ requiere patente
- **Giros profesionales/servicios** (ej: consultoría, software): Depende de la comuna

### Para QAI (Giros: 620200, 620100, 631100)
**Consultar con municipalidad de domicilio** (Providencia en tu caso).
- Muchas comunas NO exigen patente para servicios profesionales/IT
- Si exigen, costo anual: 0,25% a 0,5% del capital (aprox $2.500 - $5.000 CLP/año)

### Cómo Tramitar
1. Ir a municipalidad de domicilio
2. Llevar: Inicio de Actividades SII, escritura de constitución
3. Pagar derecho (si aplica)

---

## 5. Libros Contables

### Obligatorios
- **Libro de Compras y Ventas**: Registro de facturas (IVA)
- **Libro Mayor**: Estado financiero mensual
- **Libro Diario**: Registro cronológico de operaciones

### Pro Pyme Simplificado
QAI (en Pro Pyme General) tiene obligaciones simplificadas:
- Puede usar software contable estándar
- No requiere legalizar libros físicos (todo electrónico)

---

## 6. Plazos Críticos

| Obligación | Frecuencia | Plazo |
|:---|:---:|:---|
| F29 (IVA mensual) | Mensual | 12 o 20 del mes siguiente |
| F22 (Renta anual) | Anual | Abril del año siguiente |
| Declaración Jurada (DJ) | Anual | Marzo del año siguiente |
| Pago PPM | Mensual | Junto con F29 |

---

## 7. Sanciones Comunes

### Declaración fuera de plazo
- Multa: 10% del impuesto adeudado (mínimo 1 UTM)
- Intereses moratorios: 1,5% mensual

### No emitir factura
- Multa: 2 UTM a 40 UTM por cada factura no emitida

### No llevar libros contables
- Multa: 1 UTM a 15 UTM

---

## 8. Casos Específicos para QAI

### Servicios a Clientes Extranjeros
- **Exportación de servicios**: Exento de IVA
- Requisitos: Cliente sin domicilio en Chile, servicio consumido fuera de Chile
- Declarar en F29 como "Exportación" (Código 103)

### Facturación en USD
- Permitido si el contrato lo especifica.
- Convertir a CLP al tipo de cambio del día de facturación (SII).

---

## 9. IVA Servicios Digitales Extranjeros (SaaS)

> [!NOTE]
> Para un flujo detallado paso a paso diseñado para agentes (Finn/Lex), ver: [Guía de Facturación SaaS Extranjero](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents\lex\knowledge_base\guia_facturacion_saas_extranjero.md).

### ¿Se puede recuperar el IVA?
**SÍ**, se puede utilizar como crédito fiscal, pero no es automático.

### Requisitos Críticos
1. **Titularidad**: Las suscripciones (Cursor, Copilot, AWS, etc.) deben estar a nombre de **The QAI Company SpA** y su RUT. Las boletas a nombre personal (Alejandro) NO sirven para crédito fiscal de la empresa.
2. **Notificación al Proveedor**: Informar al proveedor (ej: Google, AWS) que eres "IVA Taxpayer" en Chile. Esto evita que ellos te cobren el 19% (régimen simplificado).

### Procedimiento (B2B)
1. El proveedor emite factura sin IVA (Invoice internacional).
2. QAI debe emitir una **Factura de Compra (Doc. 46)** en el SII.
3. Se retiene el 19% de IVA en dicha factura.
4. Ese IVA retenido se declara en el F29 (Código 57) y se utiliza como **Crédito Fiscal**.

### Tipo de Cambio (USD a CLP)
- Se debe utilizar el **Dólar Observado** publicado por el Banco Central.
- La fecha a considerar es la **fecha de emisión de la Factura de Compra**.
- El SII dispone de una tabla diaria con estos valores para facilitar la conversión.

### Registro en Libros
- **Libro de Compras**: La Invoice de Cursor NO se sube directamente; lo que se registra en el Libro de Compras es la **Factura de Compra (Doc. 46)** que tú emitiste.
- **Respaldo**: Debes guardar la Invoice original del proveedor (PDF) junto con la Factura de Compra como respaldo ante una fiscalización.

### El "Efecto Suma Cero" (Netting)
Al declarar la Factura de Compra en el F29, el 19% de IVA aparece como **Débito** (impuesto a pagar por retención) y simultáneamente como **Crédito** (impuesto a favor por compra del giro). 
- **Resultado en caja**: $0 a pagar al SII por ese concepto.
- **Beneficio**: Permite deducir el 100% del gasto para el Impuesto a la Renta y evita pagar el recargo del 19% al proveedor extranjero.

### Proveedores Comunes
- GitHub, Cursor, OpenAI, AWS, Google Cloud, Claude.ai, Meta Ads.

---

## 🚨 IMPORTANTE

Esta es información resumida y orientativa. Ante dudas:
1. **Consultar con contador** (siempre recomendado)
2. **Revisar SII directamente**: www.sii.cl
3. **Llamar teléfono SII**: 223951111 (consultas gratuitas)

---

**Última actualización**: 26-Dic-2025  
**Fuentes**:
- https://www.sii.cl/normativa_legislacion/codigos/codigo_tributario.pdf
- https://www.sii.cl/preguntas_frecuentes/  
**Próxima revisión**: Cuando surjan cambios normativos
