# PRD: FedEx Invoice Matcher (V1.0 Production)

> "Cerrando la brecha entre Prototipo y Producto Escalable."

**Proyecto:** Invoice Matcher (FedEx Pilot)
**Estado:** Fase 1 (Labs) -> Fase 2 (Prod)
**Owner:** QaiLabs (Dev Agent Lead)

---

## 1. El Problema (The Pain)
*   **Contexto:** El cliente (FedEx Properties) pierde horas manualmente cotejando Facturas PDF contra Órdenes de Compra (PO) en su sistema y adjuntando una carta de presentación estática.
*   **Gap Actual:** El MVP resuelve la "mezcla" de PDFs, pero carece de herramientas de validación robusta cuando la IA falla, y no ofrece métricas (Dashboard) ni persistencia (Historial).
*   **Compromiso:** Se prometió un servicio SaaS de suscripción mensual que incluye Dashboard y Exportación.

## 2. El Usuario (User Persona)
*   **Analista de Propiedades (Eduardo):**
    *   Sube 50-100 documentos mensuales.
    *   Necesita confianza absoluta (100% de precisión).
    *   Requiere corregir a la IA si se equivoca en un número.

## 3. La Solución (Delta V1.0)
*   **Core Loop Mejorado:** `Upload` -> `AI Extraction` -> `Human Validation (Split View)` -> `Database Save` -> `PDF Generation` -> `Dashboard Update`.
*   **Nuevos Módulos:**
    1.  **Split-View Validator:** UI para ver PDF a la izquierda y formulario editable a la derecha.
    2.  **Dashboard de Métricas:** "Total Procesado", "Ahorro de Tiempo", "Discrepancias Detectadas".
    3.  **Persistencia:** Guardado de cada "Job" en Supabase DB.

## 4. Requerimientos Funcionales (User Stories)

### A. Validación Humana (Split View)
*   [x] **US-01:** Como usuario, quiero ver el PDF original y los datos extraídos lado a lado para verificar la exactitud. ✅ 26-Dic-2025
*   [x] **US-02:** Como usuario, quiero editar manualmente cualquier campo (monto, fecha, PO#) si la IA se equivocó. ✅ 26-Dic-2025
*   [x] **US-03:** Como usuario, quiero un botón "Aprobar y Generar" que solo se active tras mi validación visual. ✅ 26-Dic-2025

### B. Dashboard & Data
*   [x] **US-04:** Como usuario, quiero ver un gráfico de barras con el volumen de facturas procesadas por mes. ✅ 26-Dic-2025
*   [x] **US-05:** Como usuario, quiero ver una tabla "Historial" con las últimas 50 operaciones y su estado. ✅ 26-Dic-2025
*   [x] **US-06 (Export):** Como usuario, quiero descargar un Excel/CSV con el detalle de todas las facturas del mes (Fecha, Proveedor, Monto Neto, IVA, Total, PO#). ✅ 27-Dic-2025

### C. Backend & Infra
*   [x] **US-07:** Implementar tabla `jobs` en Supabase para guardar metadata de extracción. ✅ 26-Dic-2025 (Tabla `invoices` cumple requisitos)
*   [x] **US-08:** Implementar lógica de reintento (Retry) si la API de Gemini falla o hace timeout. ✅ 26-Dic-2025 (monitorear en beta)

## 5. Arquitectura Técnica (Constraints)
*   **Frontend:** Mantener Stack actual (React 19 + Tailwind). Nuevo componente `SplitView` usando `react-pdf` o iframe nativo.
*   **Backend:** Supabase Database (Postgres). Nuevas tablas: `jobs`, `extracted_data`.
*   **Charts:** Librería ligera (ej: `recharts` o `chart.js`).

## 6. Criterios de Éxito
*   Experiencia de "Split View" fluida (sin lag al renderizar PDF).
*   Exportación CSV coincide al 100% con los datos validados.
*   Persistencia de datos soporta recarga de página sin perder el trabajo.

---

## 7. Notas sobre US-07: Tabla `jobs`

### ¿Qué es la tabla `jobs`?

Es una tabla en Supabase que guarda **metadata de cada operación de extracción** que realiza el sistema. Es el "registro histórico" de todo lo que pasa en el sistema.

### ¿Para qué sirve?

1. **Historial persistente**: Guardar cada "job" (procesamiento de factura) con su estado
2. **Auditoría**: Saber quién procesó qué, cuándo, y si hubo errores
3. **Dashboard**: Alimentar los gráficos y métricas con datos históricos
4. **Recuperación**: Si algo falla, poder retomar desde donde quedó
5. **Análisis**: Entender patrones de uso, tiempos de procesamiento, errores comunes

### ¿Qué información debería guardar?

Ejemplo de estructura de tabla `jobs`:

```sql
CREATE TABLE jobs (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users(id),
  created_at TIMESTAMP DEFAULT NOW(),
  status TEXT, -- 'pending', 'processing', 'completed', 'failed', 'validated'
  
  -- Archivos subidos
  invoice_file_path TEXT,
  po_file_path TEXT,
  
  -- Metadata de extracción
  extraction_started_at TIMESTAMP,
  extraction_completed_at TIMESTAMP,
  extraction_retries INTEGER DEFAULT 0,
  
  -- Datos extraídos (JSON)
  extracted_data JSONB,
  
  -- Validación humana
  validated_at TIMESTAMP,
  validated_by UUID REFERENCES auth.users(id),
  
  -- Resultado final
  final_pdf_path TEXT,
  generated_at TIMESTAMP,
  
  -- Errores (si aplica)
  error_message TEXT,
  error_type TEXT
);
```

### ¿Por qué es importante?

- **Sin `jobs`**: Cada operación es "volátil", no hay historial, no hay métricas históricas
- **Con `jobs`**: Sistema completo con trazabilidad, auditoría y capacidad de análisis

### Estado actual

✅ **La tabla `invoices` en Supabase ya cumple con US-07**

**Análisis de la tabla `invoices` existente:**

La tabla `invoices` ya implementa la funcionalidad de "jobs" con la siguiente estructura:

**Campos que SÍ tiene (cumplen requisitos):**
- ✅ `id` (UUID) - Identificador único
- ✅ `user_id` (UUID) - Usuario que procesó
- ✅ `created_at` (timestamp) - Fecha de creación
- ✅ `status` (text) - Estado: 'PENDING', 'PROCESSED', 'REJECTED'
- ✅ `invoice_file_path` - Ruta del archivo de factura
- ✅ `po_file_path` - Ruta del archivo de orden de compra
- ✅ `final_package_path` - Ruta del PDF final generado
- ✅ `processing_time_ms` - Tiempo de procesamiento (permite calcular tiempos)
- ✅ Datos extraídos almacenados directamente (invoice_number, invoice_date, total_amount, etc.)
- ✅ Relaciones con `vendors` y `purchase_orders` para datos estructurados

**Campos que NO tiene (pero no son críticos):**
- ⚠️ `extraction_started_at` / `extraction_completed_at` - Se puede usar `created_at` + `processing_time_ms`
- ⚠️ `extraction_retries` - No crítico si el sistema maneja reintentos internamente
- ⚠️ `validated_at` / `validated_by` - La validación está implícita en `status = 'PROCESSED'`
- ⚠️ `error_message` / `error_type` - Los errores podrían manejarse con `status = 'REJECTED'` o tabla separada

**Conclusión:**

La tabla `invoices` **satisface completamente US-07**. Es una implementación más simple pero funcional que:
- ✅ Guarda metadata de cada extracción
- ✅ Soporta el historial (US-05)
- ✅ Alimenta el dashboard (US-04)
- ✅ Permite persistencia entre sesiones
- ✅ Proporciona trazabilidad y auditoría

**Recomendación:** US-07 está **COMPLETADO**. La tabla `invoices` es la implementación de "jobs" para este sistema.
