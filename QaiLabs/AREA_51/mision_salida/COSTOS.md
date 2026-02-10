# 💰 COSTOS — Bot Telegram QAI HQ
> **Creado:** 10-Feb-2026 | **Proyecto GCP:** `qai-agents`

---

## Estimación Mensual (Uso Normal: ~50 requests/día)

| Servicio | Free Tier | Uso Estimado | Costo |
|:---|:---|:---|:---|
| **Google Cloud Functions** | 2M invocaciones/mes | ~1,500/mes | **$0** ✅ |
| **GCF Compute** | 180K vCPU-sec/mes | ~1,500 sec/mes | **$0** ✅ |
| **GCF Memoria** | 360K GiB-sec/mes | ~6,000 sec/mes | **$0** ✅ |
| **Gemini 2.0 Flash (input)** | Free tier: 1,500 RPD | ~50 req/día × ~2K tokens | **$0** ✅ |
| **Gemini 2.0 Flash (output)** | — | ~50 req/día × ~500 tokens | **$0** ✅ |
| **GitHub API** | 5,000 req/hora | ~100/día | **$0** ✅ |
| **TOTAL MENSUAL** | | | **$0 USD** ✅ |

> 💡 Con el uso actual (1 usuario, ~50 consultas/día), **todo queda dentro del free tier**.

---

## ¿Cuándo empezaría a costar?

| Escenario | Invocaciones/mes | Costo GCF | Costo Gemini |
|:---|:---|:---|:---|
| Solo Founder (~50/día) | ~1,500 | $0 | $0 |
| +Iliana (~100/día total) | ~3,000 | $0 | $0 |
| 10 usuarios (~500/día) | ~15,000 | $0 | ~$0.15 |
| 100 usuarios (~5K/día) | ~150,000 | $0 | ~$1.50 |
| Punto de cobro GCF | >2,000,000 | $0.40/1M extra | — |

**Conclusión:** Con menos de 10 usuarios, el costo es **literalmente $0**. Incluso con 100 usuarios activos, serían ~$1.50/mes en la API de Gemini.

---

## Tarifas de Referencia (si se excede free tier)

### Google Cloud Functions (Gen2 / Cloud Run)
- Invocaciones: **$0.40/millón** (después de 2M gratis)
- CPU: **$0.00002400/vCPU-sec** (después de 180K gratis)
- Memoria: **$0.00000250/GiB-sec** (después de 360K gratis)
- Networking: 1 GB gratis, luego $0.12/GB

### Gemini 2.0 Flash API
- Input: **$0.10 / millón de tokens**
- Output: **$0.40 / millón de tokens**
- Free tier: 15 RPM, 1,500 RPD, 1M TPM

### GitHub API
- Gratis con autenticación (5,000 req/hora)
- Sin costo adicional

## 📋 Guía de Seguimiento Detallado de Costos

### Paso 1: Configurar Alerta de Billing (hacer una vez)

1. Ve a [Billing → Budgets & alerts](https://console.cloud.google.com/billing/budgets?project=qai-agents)
2. Click **"Create Budget"**
3. **Nombre:** `QAI Bot - Alerta mensual`
4. **Projects:** Selecciona `qai-agents`
5. **Amount:** `$5 USD` (muy por encima del uso esperado)
6. **Threshold rules:** `50%`, `90%`, `100%`
7. **Notifications:** Tu email personal + email QAI
8. **Guardar**

> 💡 Esto te envía un email automático si tus costos se acercan a $5 en cualquier mes.

---

### Paso 2: Revisión Semanal (~5 min)

Abre estos 3 links y verifica que todo esté en $0:

**1️⃣ Google Cloud — Billing overview**
- Link: [Billing Dashboard](https://console.cloud.google.com/billing?project=qai-agents)
- Qué buscar: El gráfico de "Cost this month" debería mostrar **$0.00**
- Si ves algún costo > $0, revisa qué servicio lo genera

**2️⃣ Cloud Functions — Métricas de uso**
- Link: [Cloud Functions Metrics](https://console.cloud.google.com/functions/details/us-central1/qai-hq-bot?project=qai-agents&tab=metrics)
- Qué buscar:
  - **Invocations/sec**: cuántas veces se llama al bot
  - **Execution time**: cuánto tarda cada ejecución (debería ser <5 seg)
  - **Memory usage**: cuánta RAM usa (configuramos 256MB)
  - **Active instances**: cuántas instancias se crean (normalmente 0-1)

**3️⃣ Gemini API — Consumo de tokens**
- Link: [Google AI Studio](https://aistudio.google.com/apikey)
- Click en tu API key → **"View metrics"**
- Qué buscar:
  - **Requests per day**: debería ser <100 para uso normal
  - **Tokens consumed**: input + output tokens usados
  - **Error rate**: si hay fallos (quota exceeded = llegaste al límite free)

---

### Paso 3: Revisión Mensual (~15 min)

Al cierre de cada mes, completa esta tabla en el registro:

**Checklist mensual:**
- [ ] Revisar billing total del mes
- [ ] Anotar invocaciones totales del bot
- [ ] Verificar créditos GCP restantes ($300 iniciales)
- [ ] Verificar que no haya servicios huérfanos (Cloud Run, Cloud Build, etc.)
- [ ] Actualizar tabla de registro (abajo)

**¿Dónde revisar créditos restantes?**
1. [Billing Dashboard](https://console.cloud.google.com/billing?project=qai-agents)
2. Click en tu cuenta de billing
3. Pestaña **"Credits"**
4. Verás: créditos totales, usados, y fecha de vencimiento

---

### Paso 4: Limpieza de Servicios Fantasma

Google Cloud puede crear servicios auxiliares durante el deploy. Verifica que solo existan los necesarios:

**Servicios que SÍ deben estar activos:**
- `Cloud Functions` (el bot)
- `Cloud Run` (backing de Gen2)
- `Cloud Build` (builds del deploy)
- `Artifact Registry` (containers)

**Servicios que NO deberían tener costo:**
- Si ves cargos de `Cloud Storage`, `Compute Engine`, `Cloud SQL` → algo se creó de más
- Acción: desactivar o eliminar el recurso

**Cómo revisar servicios activos:**
1. [APIs & Services](https://console.cloud.google.com/apis/dashboard?project=qai-agents)
2. Revisa la lista de APIs habilitadas
3. Si hay algo que no reconoces, desactívalo

---

## 🔗 Links de Monitoreo Rápido

| Qué monitorear | Link | Frecuencia |
|:---|:---|:---|
| **Billing total** | [Billing Dashboard](https://console.cloud.google.com/billing?project=qai-agents) | Semanal |
| **Cloud Function métricas** | [Function Details](https://console.cloud.google.com/functions/details/us-central1/qai-hq-bot?project=qai-agents&tab=metrics) | Semanal |
| **Créditos restantes** | [Credits](https://console.cloud.google.com/billing?project=qai-agents) → Credits tab | Mensual |
| **Gemini API usage** | [AI Studio Keys](https://aistudio.google.com/apikey) → View metrics | Semanal |
| **Alertas configuradas** | [Budgets & Alerts](https://console.cloud.google.com/billing/budgets?project=qai-agents) | Una vez |
| **Servicios activos** | [APIs Dashboard](https://console.cloud.google.com/apis/dashboard?project=qai-agents) | Mensual |
| **Logs del bot** | [Cloud Logging](https://console.cloud.google.com/logs?project=qai-agents) | Si hay problemas |

---

## 📊 Registro de Costos Mensual

| Mes | Invocaciones | Costo GCF | Costo Gemini | Costo Total | Créditos Restantes | Notas |
|:---|:---|:---|:---|:---|:---|:---|
| Feb-2026 | — | $0 | $0 | **$0** | ~$300 | Lanzamiento, solo Founder |
| Mar-2026 | | | | | | |
| Abr-2026 | | | | | | |
| May-2026 | | | | | | |
| Jun-2026 | | | | | | |

> 📝 **Instrucción para Finn:** Al cierre de cada mes, completar esta tabla con los datos reales del billing dashboard. Esto alimenta el reporte financiero mensual.

---

## 🚨 ¿Qué hacer si aparece un costo inesperado?

1. **No entres en pánico** — Los créditos de $300 absorben cualquier error
2. Revisa [Billing Reports](https://console.cloud.google.com/billing/reports?project=qai-agents) → filtra por servicio
3. Identifica qué servicio genera el costo
4. Si es Cloud Functions: revisa si hay un loop o error que dispara invocaciones masivas
5. Si es otro servicio: probablemente se creó durante el deploy y puede eliminarse
6. **Acción inmediata:** Puedes pausar el bot con:
   ```
   gcloud functions delete qai-hq-bot --region us-central1 --project qai-agents
   ```
   (Esto no borra el código, solo detiene la ejecución)
