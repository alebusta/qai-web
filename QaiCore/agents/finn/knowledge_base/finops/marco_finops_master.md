# Marco Maestro de FinOps QAI

> **Filosofía**: Agnosticismo total. No importa el proveedor (GCP, AWS, Supabase, OpenAI, Cursor), importa el impacto en el P&L y la asignación correcta del costo.

## 🗂️ Categorización de Costos

Para una visibilidad total y toma de decisiones, Finn clasifica todo gasto en tres baldes:

### 1. Costos Fijos (Infraestructura Base)
Gastos recurrentes necesarios para que la compañía opere, independientemente de la carga de proyectos.
*   **Ejemplos**: Suscripciones a IDEs (Cursor, Copilot), correo corporativo, oficina virtual, servicios de contabilidad.
*   **Meta**: Optimización por volumen o compromiso anual.

### 2. Variables por Proyecto (Billable/COGS)
Costos directamente vinculados a la ejecución de un producto o servicio para un cliente.
*   **Ejemplos**: Consumo de Gemini API para `invoice-match`, hosting de instancias específicas, almacenamiento de datos de clientes.
*   **Meta**: Mantener el margen bruto (Gross Margin) objetivo por cada producto.

### 3. Variables R&D (Investigación y Desarrollo)
Costos de experimentación, pruebas de nuevos modelos o prototipado Labs que aún no tienen un cliente asignado.
*   **Ejemplos**: Pruebas con nuevos modelos en AI Studio, suscripciones temporales a BaaS para pilotos de QaiLabs.
*   **Meta**: Controlar el burn rate de innovación sin asfixiar la experimentación.

## 📊 Protocolo de Monitoreo

1.  **Etiquetado (Tagging)**: Todo recurso en la nube o suscripción SaaS debe llevar un "Tag" o "Label":
    *   `type`: `fixed` | `project` | `rd`
    *   `project_id`: (ej: `gz`, `im`, `core`)
2.  **Revisión de Finn**: Mensualmente, Finn cruzará los reportes de facturación de todos los proveedores contra este marco.
3.  **Optimizaciones**: Finn sugerirá cambios de tier o cambio de proveedores basándose en el análisis de costo/beneficio agnóstico.

## 🔗 Enlaces Relacionados
*   [Google Cloud Billing](./google_cloud_billing.md)
*   [STATUS.md](../../../../TorreDeControl/STATUS.md)
