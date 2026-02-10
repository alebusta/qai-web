# 🤖 QAI HQ Bot — Telegram

> **Estado:** ✅ Operativo | **Desplegado:** 10-Feb-2026  
> **URL:** `https://us-central1-qai-agents.cloudfunctions.net/qai-hq-bot`

---

## ¿Qué es esto?

Un asistente en Telegram que permite acceder al HQ digital de QAI desde el celular. Lee los archivos importantes del repositorio (STATUS.md, INBOX.md), los resume con inteligencia artificial, y te los entrega en un mensaje de Telegram.

**Analogía simple:** Es como tener un junior que va a la oficina digital, lee los papeles, y vuelve a decirte "esto es lo importante". Todo desde tu celular, sin abrir el computador.

---

## Stack Tecnológico

| Pieza | Qué es | Por qué esta y no otra |
|:---|:---|:---|
| **Telegram Bot** | La interfaz — donde el usuario conversa | API abierta y gratuita. WhatsApp cobra y es más restrictivo |
| **Google Cloud Functions** | Servidor "serverless" que se activa solo cuando recibe un mensaje | Costo $0 si nadie lo usa. Un servidor tradicional cobra $5-20/mes 24/7 |
| **Python 3.12** | Lenguaje del backend | Compatible con las herramientas existentes de QAI (Invoice-Match, scripts internos) |
| **Gemini 2.0 Flash** | IA de Google que lee documentos y genera resúmenes | Créditos gratis disponibles. Diseño permite cambiar a Claude/GPT/Llama con 1 línea |
| **GitHub API** | Conexión al repositorio del HQ | Acceso read-only a los archivos del repo privado |

---

## ¿Qué PUEDE hacer hoy?

| Comando | Qué hace | Ejemplo real |
|:---|:---|:---|
| `/status` | Lee STATUS.md y genera resumen ejecutivo inteligente | "🟡 Patente pendiente, ✅ NDA FedEx ok, 🔴 SII bloqueado" |
| `/inbox` | Muestra solo tareas pendientes (ignora las completadas) | Lista organizada por sección y urgencia |
| `/pendientes` | Combina STATUS + INBOX, prioriza acciones urgentes con IA | "Lo más urgente: resolver OC de FedEx (bloqueado)" |
| `/help` | Menú de comandos disponibles | — |
| **Texto libre** | Escribe en lenguaje natural y Gemini interpreta tu intención | "¿cómo van los clientes?" → te muestra el status |

### Seguridad
- ✅ Solo el Founder tiene acceso (whitelist por `chat_id`)
- ✅ Rate limiting (máx 30 mensajes por minuto)
- ✅ Tokens en variables de entorno (nunca en el código)
- ✅ GitHub token de solo lectura

---

## ¿Qué NO puede hacer (todavía)?

| Limitación | Motivo técnico | Esfuerzo para habilitarlo |
|:---|:---|:---|
| ❌ Leer emails | Requiere Gmail OAuth (autorización con Google) | ~2-3 hrs |
| ❌ Enviar emails | Mismo requisito que leer emails | Junto con lo anterior |
| ❌ Editar archivos del repo | Token GitHub es read-only (a propósito, por seguridad) | ~1 hr, pero requiere cuidado |
| ❌ Recordar conversaciones | Cada mensaje es independiente, sin memoria | ~2 hrs (requiere base de datos) |
| ❌ Ejecutar código/scripts | El bot solo lee y resume | No aplica — eso es trabajo del IDE |
| ❌ Acceso a GDrive/GSheets | No conectado a Google Drive | ~2-3 hrs (OAuth similar a Gmail) |
| ❌ Múltiples usuarios | Solo 1 chat_id autorizado | ~5 min (agregar número al config) |

---

## Diferencia con el IDE

| | IDE (computador) | Bot Telegram (celular) |
|:---|:---|:---|
| **Inteligencia** | Nzero completo — acceso total al sistema | Nzero mini — lee y resume |
| **Puede editar archivos** | ✅ Sí | ❌ No |
| **Puede ejecutar código** | ✅ Sí | ❌ No |
| **Leer emails** | ✅ Sí | 🔜 Próxima iteración |
| **Conversación** | Completa, con memoria y contexto largo | Básica, sin memoria entre mensajes |
| **Cuándo usarlo** | Sesión de trabajo profundo | Revisión rápida "on the go" |

> **Resumen:** El bot de Telegram es un **dashboard inteligente de bolsillo**, el IDE sigue siendo el centro de operaciones con superpoderes.

---

## Estructura del Código

```
bot/
├── main.py                    # Entry point (webhook de Telegram)
├── config.py                  # Variables de entorno centralizadas
├── requirements.txt           # Dependencias Python
├── env.yaml                   # Tokens (NO en Git)
├── .env.example               # Template de tokens
├── commands/
│   ├── help.py                # /help
│   ├── status.py              # /status (resumen con IA)
│   ├── inbox.py               # /inbox (tareas pendientes)
│   ├── pendientes.py          # /pendientes (priorización con IA)
│   └── email_cmd.py           # /email (stub para Gmail)
├── services/
│   ├── github_reader.py       # Lee archivos de GitHub con cache
│   ├── llm_provider.py        # Capa LLM-agnostic (Gemini/Groq/Claude)
│   └── telegram_service.py    # Envía mensajes a Telegram
└── security/
    └── auth.py                # Whitelist + rate limiting
```

---

## Costos

Ver detalle completo en [`COSTOS.md`](../COSTOS.md).

**Resumen:** Con el uso actual (1 usuario, ~50 consultas/día), el costo es **$0 USD/mes**. Todo dentro del free tier de Google Cloud y Gemini API.

---

## Roadmap

- [ ] **Fase 1.5:** Gmail OAuth (leer/enviar emails desde Telegram)
- [ ] **Fase 1.5:** Landing zone (dejar tareas pendientes desde Telegram)
- [ ] **Fase 2:** Subdominio `bot.qai.cl`
- [ ] **Fase 2:** Memoria entre conversaciones
- [ ] **Fase 3:** Agregar a Iliana como segundo usuario
- [ ] **Fase 3:** Evaluar como producto "Backoffice-as-a-Service" para SMEs
