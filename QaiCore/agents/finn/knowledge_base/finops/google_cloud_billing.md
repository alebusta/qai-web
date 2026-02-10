# Google Cloud Billing & FinOps Strategy

> **Última actualización**: 29-Dic-2025  
> **Responsable**: Finn (FinOps)

## 💳 Configuración de Pago
*   **Proveedor**: Google Cloud Platform / Google AI Studio
*   **Método de Pago**: Tarjeta de Débito Banco Chile (Cuenta SpA).
*   **Estado**: Afiliada y validada correctamente.

## 🎁 Créditos y Beneficios
*   **Free Tier**: $300 USD de crédito gratuito inicial.
*   **Vigencia**: 90 días o hasta agotar el monto (lo que ocurra primero).
*   **Acción**: Monitorear consumo para evitar cargos automáticos post-crédito.

## 📊 Estrategia de Monitoreo (Alineada con FinOps Master)
Para optimizar el uso y permitir el cobro cruzado:

1.  **Categorización**: 
    *   Este recurso se clasifica principalmente como **Variable R&D** (durante el crédito de $300) y pasará a **Variable por Proyecto** para `invoice-match` en producción.
2.  **Identificación por Proyecto**: 
    *   Uso de IDs de proyecto específicos (ej: `invoice-match`) para todas las APIs.
3.  **Alertas de Presupuesto**: 
    *   Configurar alertas al 50%, 75% y 90% del crédito de $300.

> Para más detalles sobre la clasificación general, ver [Marco Maestro de FinOps](./marco_finops_master.md).

## 🔗 Referencias
*   [STATUS.md](../../TorreDeControl/STATUS.md)
*   [AGENT_ACTIVITY.md](../../TorreDeControl/AGENT_ACTIVITY.md)
