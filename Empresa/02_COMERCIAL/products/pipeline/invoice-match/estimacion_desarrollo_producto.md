# Estimación de Desarrollo: Sistema de Automatización de Facturas FedEx

Este documento detalla la estimación de esfuerzo, costos y tiempos para el desarrollo del producto "Fact-Check / Invoice Automation".

> **Nota Aclaratoria:** Esta estimación se divide en dos secciones:
> 1.  **Esfuerzo Pendiente:** Lo necesario para terminar el proyecto desde hoy.
> 2.  **Esfuerzo Total:** La suma de lo ya desarrollado (Sunk Cost) más lo pendiente.

## 1. Análisis de Esfuerzo Pendiente (Gap Analysis)

Para llevar el prototipo actual (MVP) a producción, se requiere el siguiente trabajo:

### Áreas Pendientes
*   **Validación UI (Split-view):** Interfaz crítica para corrección humana.
*   **Backend & Persistencia:** Guardado de historial y datos en BD.
*   **Robustez:** Manejo de errores, reintentos y validaciones de negocio.
*   **Calidad:** Pruebas integrales con documentos reales.

### Estimación de Horas (Por Hacer)

| Módulo / Tarea | Rol Principal | Horas Estimadas |
| :--- | :--- | :--- |
| **Mejoras UI Validación (Split View)** | Frontend | 25 h |
| **Persistencia DB & Historial** | Backend | 12 h |
| **Gestión de Usuarios & Seguridad** | Fullstack | 10 h |
| **Lógica de Reintentos & Errores** | Fullstack | 10 h |
| **Pruebas y QA** | QA/Dev | 18 h |
| **Despliegue & DevOps** | DevOps | 6 h |
| **Refinamiento AI** | Prompt Eng. | 8 h |
| **Subtotal Pendiente** | | **~89 Horas** |

---

## 2. Esfuerzo Ya Realizado (Estado Actual)

Se estima que el desarrollo actual (MVP) representa una inversión de tiempo aproximada de **40-50 horas**, distribuida en:

*   **Infraestructura Base:** Configuración React, Vite, Tailwind, Supabase Auth (~8h).
*   **Motor de IA:** Integración Gemini, ingeniería de prompts, parsing JSON (~10h).
*   **Motor PDF:** Lógica compleja de generación (pdf-lib), mezcla de facturas/OC y carta presentación (~15h).
*   **Frontend Básico:** Dashboard, Drag & Drop, Rutas, State Management (~12h).

---

## 3. Resumen Consolidado (Total Proyecto)

Si se evalúa el proyecto en su totalidad (Desde Cero hasta Producción):

| Fase | Horas Estimadas | Estado |
| :--- | :--- | :--- |
| **Fase 1: MVP / Prototipo** | 45 h | ✅ Completado |
| **Fase 2: Productización (Pendiente)** | 89 h | ⏳ Por hacer |
| **TOTAL PROYECTO** | **~134 Horas** | |

---

## 4. Estimación Económica y Temporal

A continuación, se presenta un estimado de costos considerando tarifas de mercado para perfiles **Senior Fullstack Engineer** (necesario para velar por la arquitectura completa).

### Tarifas de Referencia (Promedio 2024/2025)
*   **Chile (CL):** ~35 USD/hora (Software Factory / Freelance Senior).
*   **Estados Unidos (US):** ~65 USD/hora (Freelance / Agency Mid-Level).

### Costo Total del Proyecto (134 Horas)
Calculado sobre el esfuerzo total (realizado + pendiente).

| Mercado de Desarrollo | Tarifa Hora | Costo Total Estimado |
| :--- | :--- | :--- |
| **Desarrollo en Chile** | $35 USD | **$4,690 USD** (~4.5M CLP) |
| **Desarrollo en USA** | $65 USD | **$8,710 USD** |

> *Nota: Estos valores pueden variar +/- 20% dependiendo de la modalidad de contratación (Freelance directo vs Agencia).*

### Tiempo de Ejecución (Time-to-Market)
Equivalencia del esfuerzo total en semanas calendario, asumiendo un desarrollador dedicado:

*   **Dedicación Full-time (40h/sem):** ~3.5 semanas.
*   **Dedicación Part-time (20h/sem):** ~7 semanas.

**Conclusión:** Un proyecto de esta envergadura típicamente se ejecuta en **1 mes** de trabajo intenso para llegar a una versión productiva v1.0.
