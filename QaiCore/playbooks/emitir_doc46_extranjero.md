# Playbook: Emisión de Factura de Compra (Doc. 46) por Servicios Extranjeros

> **Workflow para que Finn formalice la recuperación de IVA en gastos SaaS internacionales**

---

## 🎯 Objetivo

Institucionalizar el proceso de emisión del **Documento 46 (Factura de Compra)** en el portal del SII para servicios SaaS extranjeros (GitHub, Cursor, AWS, OpenAI, etc.). Esto permite:
1. Registrar el gasto como gasto necesario para producir renta.
2. Recuperar el 19% de IVA (Crédito Fiscal) mediante la retención y pago del impuesto.

---

## 🔄 Trigger (Cuándo ejecutar)

- Se recibe un invoice de un proveedor extranjero (SaaS) a nombre de **The QAI Company SpA**.
- El invoice NO incluye el 19% de IVA chileno (VAT/Digital Services Tax).
- Se requiere descargar el IVA para la declaración mensual (F29).

---

## 📋 Pre-requisitos

1. **Invoice Original**: En PDF, a nombre de la empresa y con el RUT visible (`78.313.539-6`).
2. **Registro Contable**: El gasto ya debe estar en el **Registro Diario** con el monto neto pagado.
3. **Acceso al SII**: Credenciales del Representante Legal (Alejandro) o Certificado Digital (FEA).

---

## 🛠️ Pasos del Workflow

### 1. Preparación de Datos (Finn)

Antes de ir al portal del SII, consolidar la información:
- **Proveedor**: Nombre legal y país (ej: Anysphere Inc - USA, GitHub Inc - USA).
- **Monto Neto (CLP)**: Monto cargado en la tarjeta convertido a CLP (usar el dólar observado del día del cargo).
- **Tasa de Impuestos**: 
  - **IVA**: 19% (Retención total).
  - **Impuesto Adicional (IA)**: Generalmente exento para software/SaaS (verificar con Lex si hay dudas, pero usualmente 0% por tratados o exención específica de software).

### 2. Emisión en SII (Humano con asistencia de Finn)

1. Ingresar a `sii.cl` > Servicios Online > Factura Electrónica > Sistema de facturación gratuito del SII.
2. Seleccionar **Emisión de documentos tributarios electrónicos (DTE)**.
3. Elegir **Factura de Compra Electrónica (Código 46)**.
4. **Datos del Emisor**: (Automático - QAI SpA).
5. **Datos del Receptor**: Aquí se ingresan los datos del **Proveedor Extranjero**.
   - **RUT**: Se usa un RUT genérico para extranjeros: `55.555.555-5`.
   - **Razón Social**: Nombre del proveedor (ej: Cursor / Anysphere, Inc).
   - **Dirección**: Dirección del proveedor en el extranjero.
   - **Comuna/Ciudad**: (Extranjero).
6. **Detallado de Líneas**:
   - **Nombre**: "Servicios Digitales / Suscripción [Servicio] [Mes/Año]".
   - **Cantidad**: 1.
   - **Precio**: Monto Neto del invoice en CLP.
7. **Retenciones**:
   - Seleccionar **Retención de IVA (100%)**. 
   - El sistema calculará el 19% de IVA que la empresa *retiene* (y pagará en el F29).
8. **Referencia**: Adjuntar el Invoice ID original del proveedor en la sección de referencias si es posible.
9. **Firmar y Enviar**: Requiere FEA de Alejandro.

### 3. Registro Contable Post-Emisión (Finn)

Una vez emitido el Doc. 46:
1. **Descargar el PDF** del Doc. 46 del portal del SII.
2. **Archivar**: 
   - Subir a Drive: `/Empresa/03_ADMINISTRACION_FINANZAS/comprobantes/2026/[Mes]/03-SaaS_Extranjero_Doc46/`.
   - Nombre: `YYYY-MM-DD_Doc46_[Proveedor]_[Concepto].pdf`.
3. **Actualizar Registro Diario**:
   - Localizar la fila del gasto original.
   - Actualizar columna **IVA** con el monto calculado en el Doc. 46.
   - Actualizar columna **Monto Bruto** (Neto + IVA).
   - Agregar nota: "Doc. 46 emitido (Folio: [X])".
4. **Actualizar AGENT_ACTIVITY.md**: Registrar la formalización del IVA.

---

## 📅 Misión Enero 2026 (Pendientes)

| Proveedor | Monto Neto (USD) | Monto Neto (CLP) | Acción |
|:---|:---|:---|:---|
| **GitHub** | $10.00 (aprox) | $9.250 | Emitir Doc. 46 |
| **Cursor** | $20.00 | $18.200 | Emitir Doc. 46 |
| **Google** | $7.100 CLP | $7.100 CLP | **NO Doc. 46** (Personal). Registro solo F22. |

---

## ✅ Criterios de Éxito

- ✅ Documento 46 emitido en el SII y Folio obtenido.
- ✅ PDF archivado correctamente en Drive.
- ✅ Registro Diario actualizado con el Crédito Fiscal (IVA).
- ✅ Tarea en INBOX marcada como completada.

---

## 🚨 Caso Google (Importante)

- **Situación**: Suscripción personal de Alejandro.
- **Tratamiento**: 
  - NO genera Crédito Fiscal (no se puede emitir Doc. 46).
  - SÍ se registra como gasto para la Renta (F22) ya que es un insumo operativo para la IA de la empresa.
  - **Acción**: Mantener el registro actual sin IVA.

---

**Versión**: 1.0  
**Fecha**: 03-Feb-2026  
**Responsable**: Finn (Agente Financiero)
