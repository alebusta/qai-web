# 🧠 Checkpoint — Misión Salida: QAI al Ciberespacio

> **Fecha:** 10-Feb-2026 | **Estado:** Análisis aprobado, preparando prerrequisitos

---

## Contexto

La misión es hacer que los agentes de QAI sean accesibles **fuera del entorno local** (IDE) para operar "on the go". El análisis completo está en [README.md](./README.md).

---

## Decisiones Tomadas (Q&A con Founder)

### ✅ D1: Lo local se mantiene intacto
- El IDE (Antigravity/Cursor) sigue siendo el centro de operaciones principal
- Lo remoto (Telegram) es un **canal adicional complementario**
- No reemplaza nada — solo agrega capacidad "on the go"

### ✅ D2: GitHub sí, CI/CD complejo no
- Necesitamos un repo privado en GitHub para backup + acceso cloud del bot
- **NO** necesitamos pipelines CI/CD — un `git push` (manual o auto-sync) es suficiente
- El bot lee del repo directamente, no necesita builds

### ✅ D3: Prerequisitos antes de GitHub
Antes de subir el HQ a GitHub hay que resolver:

1. **`.gitignore`** — Excluir productos con repo propio (invoice-match, gestion-zen)
2. **Auditoría de archivos pesados** — Mover PDFs/binarios a Drive, dejar solo código/texto
3. **Formalizar regla** — "Código en Git / Docs pesados en Drive" documentado
4. **`AGENT_TEMPLATE/`** — Template base en `QaiCore/agents/` para nuevos agentes
5. **Scan de secrets** — Verificar que no haya API keys expuestas en archivos

### ✅ D4: Estructura extensible para agentes
- La estructura `QaiCore/agents/` ya es extensible por diseño
- Crear un template base para facilitar la creación de nuevos agentes (UI, Marketing, etc.)
- No definir agentes nuevos ahora, solo asegurar que el molde esté listo

---

## Recomendación Estratégica Aprobada

| Prioridad | Canal | Score |
|:---|:---|:---|
| 🥇 Primario | **Telegram Bot** | 8.45/10 |
| 🥈 Futuro | **n8n como orquestador** | 7.55/10 |
| 🥉 Largo plazo | **UI Web propia** | 7.05/10 |
| ❌ Descartado (por ahora) | WhatsApp (restricciones Meta 2026) | 5.75/10 |

---

## Arquitectura Target (Fase 1)

```
PC Local (IDE) ──push──▶ GitHub Privado ◀──lee── Bot Telegram (Supabase Edge)
                              │
                              ▼
                         Supabase DB (state, logs, secrets)
                              │
                              ▼
                    Google APIs + Claude/Gemini API
```

---

## Roadmap de Alto Nivel

| Fase | Descripción | Duración |
|:---|:---|:---|
| **Fase 0** ← ESTAMOS AQUÍ | Preparar repo para GitHub | 1 sesión |
| **Fase 1** | Telegram MVP (/status, /inbox, /email) | 3 semanas |
| **Fase 2** | Agentes expandidos (Lex, Finn vía bot) | 3 semanas |
| **Fase 3** | Fortress Protocol (seguridad completa) | 4 semanas |
| **Fase 4** | Horizonte (n8n, UI Web, MCP remoto) | Evaluación Q2-2026 |

---

## Decisiones Pendientes (para resolver en Fase 1)

1. **Backend**: ¿Python (Cloud Function) o TypeScript (Supabase Edge)?
   - Recomendación: Python vía Railway/Render
2. **LLM**: ¿Gemini (gratis) o Claude (mejor razonamiento)?
   - Recomendación: Arrancar con Gemini, migrar si necesario
3. **Prioridad vs otros proyectos**: ¿Tiempo dedicado semanal?
4. **UI Web como producto comercial**: ¿Sí o no?

---

## Seguridad: "Fortress Protocol" (5 capas)

1. **Auth** — Whitelist chat_id + PIN para ops sensibles
2. **Secrets** — Supabase Vault, rotación 90 días, sin keys en código
3. **Sandbox** — Bot sin acceso directo a filesystem, whitelist de acciones
4. **Input Validation** — Sanitización + guardrails anti prompt injection
5. **Auditoría** — Logs completos + alertas automáticas

---

> **Próximo paso:** Ejecutar Fase 0 (preparar repo para GitHub).
> **Documento completo:** [README.md](./README.md)
