# Análisis de Costos Base: Proyecto Invoice Matcher (FedEx/Sempere)

**Destinatario**: Finn (Agente Financiero QAI)  
**Propósito**: Entrega de estructura de costos para seguimiento y afinamiento de márgenes.

## 1. Estructura de Ingresos
- **Monto Neto Piloto**: $990.000 CLP.
- **Forma de Pago**: Pago único anticipado via Sempere y Fernández Arquitectos.

## 2. Estimación de Costos Directos (OpEx)
Este piloto requiere el monitoreo de los siguientes ítems para calcular el margen real:

| Ítem | Proveedor | Cantidad | Costo Est. | Frecuencia |
| :--- | :--- | :--- | :--- | :--- |
| **Infraestructura Cloud** | AWS | Tier 1 compute | Variable (est. $5-10 USD) | Mensual |
| **Token IA (Procesamiento)** | Google/OpenAI | 500 procesos | Variable (depende de densidad de tokens) | Por cuota |
| **Almacenamiento Seguro** | AWS S3 | Cifrado AES-256 | Bajo (est. <$1 USD) | Mensual |

## 3. Costo de Implementación (CapEx/Horas)
- **Horas Agente (Nzero)**: ~4-6 horas de refinamiento de layout y estandarización.
- **Iteraciones**: 3 ciclos de ajuste fino corporativo incluidos en el precio.

## 4. Notas para Finn
- **Seguimiento de Márgenes**: Es crítico monitorear el consumo real de tokens de IA por cada uno de los 500 procesos para definir el precio de la fase post-piloto.
- **Sempere y Fernández**: Verificar la recepción de la OC y la emisión de la factura correspondiente para gatillar la operación.

---
*Este documento es una base de planificación. Finn debe actualizar los valores reales una vez que el servicio esté en producción.*
