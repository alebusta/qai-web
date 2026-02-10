# 🧠 Checkpoint — Misión Salida: QAI al Ciberespacio

> **Fecha:** 10-Feb-2026 | **Estado:** ✅ Fase 1 completada — Bot Telegram OPERATIVO
>
> **URL Cloud Function:** `https://us-central1-qai-agents.cloudfunctions.net/qai-hq-bot`
> **Proyecto GCP:** `qai-agents` | **Runtime:** Python 3.12 | **Region:** us-central1

---

## Contexto

La misión es hacer que los agentes de QAI sean accesibles **fuera del entorno local** (IDE) para operar "on the go". El análisis completo está en [README.md](./README.md).

---

## Decisiones Tomadas (Q&A con Founder)

### ✅ D1: Lo local se mantiene intacto
- El IDE (Antigravity/Cursor) sigue siendo el centro de operaciones principal
- Lo remoto (Telegram) es un **canal adicional complementario**

### ✅ D2: GitHub sí, CI/CD complejo no
- Repo privado: `github.com/qai-labs/TheQaiCo` ← **YA OPERATIVO**
- Solo `git push` manual, sin pipelines
- Credential Manager configurado con PAT (rotado)

### ✅ D3: Prerequisitos completados
- [x] `.gitignore` comprehensivo
- [x] API key redactada en `PROTOCOL_API_KEYS.md`
- [x] `AGENT_TEMPLATE/` creado
- [x] Push inaugural exitoso (345 objetos)

### ✅ D4: Backend → Python + Google Cloud Functions
- Python para consistencia con tools existentes (Gmail, GDrive)
- Google Cloud Functions: **gratis** (2M invocaciones/mes), ecosistema conocido
- Descartados: Railway/Render (pago, desconocido), Cloudflare (no soporta Python), Supabase Edge (TypeScript)

### ✅ D5: LLM → Gemini para arrancar, arquitectura LLM-agnostic
- Gemini con $300 de crédito existente
- Capa de abstracción `LLMProvider` para swap fácil a Claude/Groq/open source
- Evaluar **Groq** (modelos open source, Llama/Mixtral) como alternativa

### ✅ D6: Prioridad → Activa, en paralelo con otros proyectos
- Arranca ya, Fase 1 en las próximas 3 semanas

### ✅ D7: Usuarios → Solo Founder por ahora
- Whitelist con `chat_id` de Alejandro
- Futuro: agregar Iliana (socia, marketing/ventas/gestión)

### ✅ D8: Comandos MVP + Landing Zone
- `/status`, `/inbox`, `/pendientes`, `/email`, `/help`
- **Landing zone**: dejar cosas para ejecutar (leer, archivar, contabilizar, pendientes)
- Lectura + escritura con **human-in-the-loop** (ej: borrador de email → aprobación → envío)

### ✅ D9: Dominio → Subdominio de qai.cl
- Usar `api.qai.cl` o `bot.qai.cl` (dominio propio existente)

### ✅ D10: Visión comercial → Backoffice-as-a-Service para PYMEs
- Si el experimento interno funciona, potencial producto comercial
- Backoffice inteligente como servicio para empresas pequeñas

---

## Arquitectura Target (Fase 1) — ACTUALIZADA

```
PC Local (IDE) ──push──▶ GitHub Privado ◀──lee── Google Cloud Function (Python)
                              │                          │
                              │                    Bot Telegram
                              │                          │
                              ▼                          ▼
                    Google APIs (Gmail/Drive)    Gemini API (LLM-agnostic)
```

---

## Roadmap

| Fase | Descripción | Estado |
|:---|:---|:---|
| **Fase 0** | Preparar repo para GitHub | ✅ Completada |
| **Fase 1** ← SIGUIENTE | Telegram MVP (Python + Cloud Functions) | 🔜 3 semanas |
| **Fase 2** | Agentes expandidos + Iliana | ⏳ |
| **Fase 3** | Fortress Protocol completo | ⏳ |
| **Fase 4** | Horizonte (n8n, UI Web, Backoffice SaaS) | ⏳ |

---

## Seguridad: "Fortress Protocol" (5 capas)

1. **Auth** — Whitelist chat_id + PIN para ops sensibles
2. **Secrets** — Variables de entorno, rotación 90 días, sin keys en código
3. **Sandbox** — Bot sin acceso directo a filesystem, whitelist de acciones
4. **Human-in-the-loop** — Escrituras requieren aprobación explícita
5. **Auditoría** — Logs completos + alertas automáticas

---

> **Próximo paso:** Iniciar Fase 1 — Setup Telegram Bot + Google Cloud Function
> **Documento completo:** [README.md](./README.md)
