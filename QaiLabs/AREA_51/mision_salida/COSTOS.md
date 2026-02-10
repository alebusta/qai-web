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

---

## 🔗 Links de Monitoreo

| Qué monitorear | Link |
|:---|:---|
| **Billing Dashboard** | [console.cloud.google.com/billing](https://console.cloud.google.com/billing) |
| **Cloud Functions Métricas** | [console.cloud.google.com/functions](https://console.cloud.google.com/functions/details/us-central1/qai-hq-bot?project=qai-agents) |
| **Créditos restantes** | [console.cloud.google.com/billing](https://console.cloud.google.com/billing) → pestaña "Credits" |
| **Gemini API usage** | [aistudio.google.com](https://aistudio.google.com/apikey) → tu API key → "View metrics" |
| **Alertas de billing** | [console.cloud.google.com/billing/budgets](https://console.cloud.google.com/billing/budgets?project=qai-agents) |

---

## ⚠️ Recomendación: Crear Alerta de Billing

Para que nunca te sorprendan cargos, configura una alerta:

1. Ve a [Billing → Budgets & alerts](https://console.cloud.google.com/billing/budgets?project=qai-agents)
2. Click **"Create Budget"**
3. Budget: **$5 USD/mes** (muy por encima del uso esperado)
4. Alertas al **50%, 90%, 100%** del budget
5. Email: tu correo personal

Así recibes aviso si algo se dispara antes de que cueste.
