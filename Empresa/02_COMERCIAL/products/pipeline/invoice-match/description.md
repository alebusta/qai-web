# Fact-Check / Invoice Automation

[![Deploy Frontend](https://github.com/alebusta/invoice-match/actions/workflows/deploy-frontend.yml/badge.svg)](https://github.com/alebusta/invoice-match/actions/workflows/deploy-frontend.yml)

## probando un cambio 

Sistema web automatizado para la extracción, validación y procesamiento de facturas y órdenes de compra de FedEx. Utiliza Inteligencia Artificial (Google Gemini) para extraer datos de documentos PDF e imágenes, y genera automáticamente paquetes de solicitud de pago estandarizados.

## 🚀 Características Principales

*   **Extracción IA:** Procesa facturas y OCs usando modelos *multimodal* (Gemini 2.5 Flash) para obtener RUT, montos, fechas y números de referencia.
*   **Generación de PDF:** Crea automáticamente una "Carta de Presentación" (Cover Letter) y la fusiona con los documentos originales en un solo archivo listo para enviar a Finanzas.
*   **Interfaz Moderna:** Dashboard construido con React 19 y TailwindCSS para una experiencia de usuario fluida.
*   **Seguridad:** Integración con Supabase para autenticación, gestión de sesiones y Edge Functions para proteger API keys.

## 🛠 Tech Stack

*   **Frontend:** [React 19](https://react.dev/), [Vite](https://vitejs.dev/), [TailwindCSS](https://tailwindcss.com/)
*   **AI:** [Google Gemini API](https://ai.google.dev/) (via Supabase Edge Functions)
*   **Backend / Auth:** [Supabase](https://supabase.com/) (Authentication + Edge Functions)
*   **PDF Processing:** `pdf-lib`

## 🔒 Arquitectura de Seguridad

La aplicación utiliza **Supabase Edge Functions** como proxy seguro para las llamadas a Gemini API:

- ✅ API key de Gemini almacenada en Supabase Secrets (nunca expuesta al cliente)
- ✅ Autenticación requerida (JWT automático vía Supabase)
- ✅ Sin dependencias de AI en el bundle del cliente

Ver [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md) para detalles de configuración y deployment.

## 📦 Instalación y Configuración

### Prerrequisitos
*   Node.js 18+
*   Cuenta en Supabase
*   Google Gemini API Key
*   Supabase CLI (`npm install -g supabase`)

### Pasos

1.  **Clonar el repositorio**
    ```bash
    git clone <repo-url>
    cd invoiceMatch
    ```

2.  **Instalar dependencias**
    ```bash
    npm install
    ```

3.  **Configurar Variables de Entorno**
    
    Copiar `.env.example` a `.env` y configurar:
    ```env
    VITE_SUPABASE_URL=your_supabase_project_url
    VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
    ```
    
    **Nota:** La API key de Gemini NO va en `.env` - se configura en Supabase Secrets (ver paso 4).

4.  **Configurar Supabase Edge Function**
    
    ```bash
    # Login y link al proyecto
    supabase login
    supabase link --project-ref your_project_ref
    
    # Configurar secret de Gemini API
    supabase secrets set GEMINI_API_KEY=your_gemini_api_key
    
    # Deploy Edge Function
    supabase functions deploy extract-document
    ```

5.  **Ejecutar en Desarrollo**
    ```bash
    npm run dev
    ```

## 📖 Documentación del Proyecto

La documentación detallada se encuentra en la carpeta `docs/`:
*   [`DEPLOYMENT.md`](docs/DEPLOYMENT.md) - Guía completa de deployment y configuración de Edge Functions
*   [Estimación de Desarrollo / Roadmap](docs/estimacion_desarrollo_producto.md) - Planificación, costos y tiempos
*   [Checklist de Tareas](docs/checklist_desarrollo.md) - Lista de seguimiento para el desarrollo restante

## 🚢 Deployment a Producción

### Cloudflare Pages

Variables de entorno requeridas:
```
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
```

**Importante:** NO incluir `VITE_GEMINI_API_KEY` - está protegida en Supabase Secrets.

Ver [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md) para instrucciones detalladas.

## 👥 Estado del Proyecto

Actualmente en fase **MVP (Prototipo Funcional)** con seguridad de producción implementada.

Para ver el plan de trabajo hacia la versión de producción, revisar el [Checklist de Desarrollo](docs/checklist_desarrollo.md).

---

## 🔄 CI/CD Pipeline

Este proyecto utiliza **GitHub Actions** para deployment automático:

### Frontend (Cloudflare Pages)
- **Trigger:** Push a `main` branch
- **Deploy:** Automático a Cloudflare Pages
- **Workflow:** [`.github/workflows/deploy-frontend.yml`](.github/workflows/deploy-frontend.yml)

### Supabase Edge Functions
- **Trigger:** Push a `main` con cambios en `supabase/functions/`
- **Deploy:** Automático vía Supabase CLI
- **Workflow:** [`.github/workflows/deploy-supabase-functions.yml`](.github/workflows/deploy-supabase-functions.yml)

### Secrets Requeridos

Configurar en **GitHub Settings → Secrets and variables → Actions**:

**Frontend:**
- `CLOUDFLARE_API_TOKEN` - Token de API de Cloudflare
- `CLOUDFLARE_ACCOUNT_ID` - ID de cuenta de Cloudflare
- `VITE_SUPABASE_URL` - URL del proyecto Supabase
- `VITE_SUPABASE_ANON_KEY` - Anon key de Supabase

**Supabase Functions:**
- `SUPABASE_ACCESS_TOKEN` - Personal access token de Supabase
- `SUPABASE_PROJECT_ID` - Project reference ID (ej: `rlpmpizwxntwdpolsayn`)

Ver [`.github/workflows/README.md`](.github/workflows/README.md) para más detalles.

