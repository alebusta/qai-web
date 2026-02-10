# 🚀 Misión Salida: QAI al Ciberespacio

> **R&D — Exploración de alternativas para operar agentes fuera del entorno local**  
> Fecha: 10-Feb-2026 | Responsable: Nzero | Status: **Análisis Completo — Pendiente Revisión Founder**

---

## 📋 Índice

1. [Diagnóstico: Dónde Estamos Hoy](#1-diagnóstico-dónde-estamos-hoy)
2. [Landscape: Qué Existe Allá Afuera](#2-landscape-qué-existe-allá-afuera)
3. [Análisis Comparativo de Canales](#3-análisis-comparativo-de-canales)
4. [Análisis de Seguridad](#4-análisis-de-seguridad)
5. [Arquitectura Propuesta](#5-arquitectura-propuesta)
6. [Hoja de Ruta Recomendada](#6-hoja-de-ruta-recomendada)
7. [Estimación de Costos](#7-estimación-de-costos)
8. [Decisiones Pendientes](#8-decisiones-pendientes)

---

## 1. Diagnóstico: Dónde Estamos Hoy

### Arquitectura Actual

```
┌─────────────────────────────────────────────────┐
│              PC LOCAL (Alejandro)                │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ Antigrav. │  │  Cursor  │  │  VS Code │      │
│  │   (IDE)   │  │  (IDE)   │  │  (IDE)   │      │
│  └────┬──────┘  └────┬─────┘  └────┬─────┘      │
│       │              │             │              │
│       └──────────┬───┘─────────────┘              │
│                  │                                │
│         ┌────────▼────────┐                      │
│         │    QaiCore      │                      │
│         │  ├─ agents/     │    ┌──────────────┐  │
│         │  ├─ tools/      │───▶│ Google APIs   │  │
│         │  ├─ playbooks/  │    │ (Drive/Gmail/ │  │
│         │  └─ scripts/    │    │  Sheets)      │  │
│         └─────────────────┘    └──────────────┘  │
│                                                  │
│         ┌─────────────────┐                      │
│         │ TorreDeControl  │                      │
│         │  ├─ STATUS.md   │                      │
│         │  ├─ INBOX.md    │                      │
│         │  └─ temp_files/ │                      │
│         └─────────────────┘                      │
└─────────────────────────────────────────────────┘
```

### Fortalezas Actuales
- ✅ Perfiles de agentes bien definidos (Nzero, Lex, Finn)
- ✅ Herramientas Python funcionales (Gmail, GDrive, GSheets, extractores)
- ✅ Protocolo de Torre de Control como memoria compartida
- ✅ Playbooks estandarizados para flujos de trabajo
- ✅ Sistema de permisos por agente (`tools.json`)

### Debilidades / Riesgos Críticos
- 🔴 **Single Point of Failure**: Todo depende del PC local
- 🔴 **Operación limitada**: Solo se puede trabajar con el computador a la mano
- 🔴 **Sin respaldo cloud**: Si falla el hardware, se pierde conocimiento
- 🟠 **Sin acceso móvil**: Imposible operar "on the go"

---

## 2. Landscape: Qué Existe Allá Afuera

### 2.1 Frameworks Agénticos de Vanguardia

| Framework | Qué Es | Relevancia para QAI | Riesgo |
|:---|:---|:---|:---|
| **Claude Code** | Agente de Anthropic con MCP, cloud sessions, soporte Telegram/Slack/GitHub | ⭐⭐⭐ Alta — MCP muy alineado con nuestra arquitectura | Bajo |
| **OpenClaw** | Framework open-source (ex-Clawdbot) para agentes autónomos | ⭐ Baja — Graves vulnerabilidades de seguridad | 🔴 **Crítico** |
| **Nanobot** | Framework ligero que transforma MCP servers en agentes completos | ⭐⭐ Media — Concepto interesante para agentes livianos | Medio |
| **n8n** | Plataforma de automatización visual, self-hosted, con nodos para Telegram/WhatsApp | ⭐⭐⭐ Alta — Ideal como orquestador de workflows | Bajo |
| **CrewAI / LangGraph** | Frameworks multi-agente para orquestación compleja | ⭐⭐ Media — Útil si escalamos a más agentes | Bajo |

### 2.2 Similitudes con QAI

Lo que hemos construido artesanalmente en QaiCore tiene **paralelos directos** con estándares que la industria está adoptando:

| Concepto QAI | Equivalente Industria | Adopción |
|:---|:---|:---|
| `agents/nzero/system_prompt.md` | **Claude Skills** (bundles de instrucciones reutilizables) | Anthropic, Ene-2026 |
| `agents/*/tools.json` | **MCP Server** (herramientas expuestas vía protocolo estándar) | Estándar abierto |
| `TorreDeControl/` | **Shared Memory / Context Store** | Patrón "working memory" |
| `playbooks/` | **Agent Workflows / Runbooks** | n8n, LangGraph |
| `QaiCore/tools/` | **MCP Tools** (funciones invocables por agentes) | Cloudflare, AWS |

> **Insight Clave:** No necesitamos reemplazar nuestra estructura — necesitamos **exponerla** al mundo exterior mediante protocolos estándar como MCP.

### 2.3 OpenClaw: Lecciones Aprendidas (Qué NO Hacer)

> [!CAUTION]
> OpenClaw es un caso de estudio de todo lo que puede salir mal al desplegar agentes sin seguridad adecuada.

- **CVE-2026-25157**: Inyección de comandos OS vía SSH → ejecución remota de código
- **CVE-2026-25253**: Robo de tokens de autenticación → RCE con un solo clic
- **40,000+ instancias expuestas** en internet sin protección
- **63% de deployments vulnerables** a ataques RCE (SecurityScorecard)
- El marketplace de skills (ClawHub) fue infiltrado con cientos de paquetes maliciosos

**Conclusión para QAI:** Cualquier despliegue remoto DEBE priorizar seguridad desde el diseño. No podemos tomar atajos.

---

## 3. Análisis Comparativo de Canales

### 3.1 Telegram Bot

| Aspecto | Evaluación |
|:---|:---|
| **Facilidad de setup** | ⭐⭐⭐⭐⭐ — Bot en minutos con `python-telegram-bot` |
| **Costo** | 🟢 Gratis (API de Telegram es free) |
| **Acceso móvil** | ✅ Nativo iOS/Android/Desktop/Web |
| **Seguridad** | 🟢 Buena — Filtro por `chat_id`, HTTPS, E2E opcional |
| **Capacidad de agentes** | ⭐⭐⭐⭐ — Comandos, teclados inline, archivos, audio |
| **Integración con QaiCore** | ⭐⭐⭐⭐ — Python nativo, mismo stack |
| **Escalabilidad** | ⭐⭐⭐⭐ — Webhooks + serverless = auto-scale |
| **Limitaciones** | Sin llamadas VoIP nativas; UX limitada vs web app |

**Pros:**
- Stack 100% Python — se integra directo con nuestras tools existentes
- Bot privado con acceso restringido por `chat_id` del Founder
- Soporte nativo de archivos, imágenes, markdown
- Deploy serverless (Cloud Functions / Railway / Supabase Edge)

**Contras:**
- UX limitada para flujos complejos (no web forms)
- Sin soporte nativo para dashboards o visualizaciones ricas

---

### 3.2 WhatsApp (Business API)

| Aspecto | Evaluación |
|:---|:---|
| **Facilidad de setup** | ⭐⭐ — Requiere BSP, verificación de empresa, API de Meta |
| **Costo** | 🟠 Cobro por mensaje template (desde Jul-2025) |
| **Acceso móvil** | ✅ Nativo — la app más usada en LATAM |
| **Seguridad** | 🟢 E2E encryption por defecto |
| **Capacidad de agentes** | ⭐⭐⭐ — Botones, listas, flows, catálogos |
| **Integración con QaiCore** | ⭐⭐ — Requiere middleware / BSP |
| **Escalabilidad** | ⭐⭐⭐⭐ — Cloud API de Meta auto-escala |
| **Limitaciones** | Meta exige bots "task-specific" en 2026; más restricciones |

**Pros:**
- Canal más natural para comunicación en Chile/LATAM
- E2E encryption de fábrica
- WhatsApp Flows permite formularios dentro del chat

**Contras:**
- 🔴 Meta ya NO permite chatbots "general-purpose" (2026)
- Costo por mensaje template enviado
- Setup complejo: BSP + verificación Meta Business + número dedicado
- Menor flexibilidad que Telegram para agentes autónomos

---

### 3.3 UI Web Propia (Custom Dashboard)

| Aspecto | Evaluación |
|:---|:---|
| **Facilidad de setup** | ⭐⭐ — Requiere desarrollo frontend + backend |
| **Costo** | 🟠 Hosting + dominio + desarrollo |
| **Acceso móvil** | ✅ PWA responsive |
| **Seguridad** | 🟢 Control total — auth propia, Supabase RLS |
| **Capacidad de agentes** | ⭐⭐⭐⭐⭐ — Sin límites de UX |
| **Integración con QaiCore** | ⭐⭐⭐⭐⭐ — Backend propio = integración total |
| **Escalabilidad** | ⭐⭐⭐⭐ — Supabase + Edge Functions |
| **Limitaciones** | Mayor esfuerzo de desarrollo y mantenimiento |

**Pros:**
- Control total sobre UX, funcionalidad y branding QAI
- Puede servir como producto comercial futuro
- Dashboard + chat + visualizaciones en un solo lugar
- Supabase ya está en nuestro stack (MCP server activo)

**Contras:**
- Mayor inversión inicial de desarrollo
- Necesita mantenimiento continuo
- No tiene la inmediatez de un chat (notificaciones push requieren PWA)

---

### 3.4 Enfoque Híbrido con n8n (Orquestador)

| Aspecto | Evaluación |
|:---|:---|
| **Facilidad de setup** | ⭐⭐⭐ — Self-hosted o cloud, visual builder |
| **Costo** | 🟢 Open source self-hosted; cloud tiene tiers |
| **Capacidad** | ⭐⭐⭐⭐⭐ — Conecta todo: Telegram, WhatsApp, APIs, DBs |
| **Seguridad** | 🟢 Self-hosted = datos bajo tu control |
| **Integración** | ⭐⭐⭐⭐ — Nodos para LLMs, HTTP, Python code |

**Pros:**
- Funciona como "sistema nervioso" conectando todos los canales
- Visual builder = menos código, más rapidez
- Puede orquestar Telegram + WhatsApp + Email + Web simultáneamente
- Self-hosted = datos nunca salen de tu infraestructura

**Contras:**
- Otra pieza de infraestructura que mantener
- Curva de aprendizaje para workflows complejos
- Puede ser overkill si solo necesitamos un canal

---

### Matriz de Decisión Final

| Criterio (Peso) | Telegram | WhatsApp | UI Web | n8n Híbrido |
|:---|:---:|:---:|:---:|:---:|
| Rapidez de implementación (25%) | 🟢 9 | 🔴 4 | 🟠 5 | 🟡 7 |
| Costo operativo (20%) | 🟢 9 | 🟠 5 | 🟠 6 | 🟡 7 |
| Funcionalidad para agentes (20%) | 🟡 7 | 🟠 6 | 🟢 10 | 🟢 9 |
| Seguridad (20%) | 🟢 8 | 🟢 8 | 🟢 9 | 🟢 8 |
| Mantenimiento (15%) | 🟢 9 | 🟡 6 | 🟠 5 | 🟡 6 |
| **TOTAL PONDERADO** | **8.45** | **5.75** | **7.05** | **7.55** |

> **🏆 Recomendación:** Telegram como canal primario → n8n como orquestador futuro → UI Web como objetivo de largo plazo.

---

## 4. Análisis de Seguridad

### 4.1 Modelo de Amenazas para QAI Remoto

```
┌─────────────────────────────────────────────────────┐
│                 VECTORES DE ATAQUE                   │
│                                                      │
│  1. Prompt Injection    → Instrucciones maliciosas   │
│  2. API Key Exposure    → Filtración de credenciales │
│  3. Data Exfiltration   → Robo de datos empresa      │
│  4. Unauthorized Access → Acceso no autorizado       │
│  5. Man-in-the-Middle   → Intercepción de mensajes   │
└─────────────────────────────────────────────────────┘
```

### 4.2 Protocolo de Seguridad Propuesto: "Fortress Protocol"

#### Capa 1: Autenticación
- **Whitelist de `chat_id`**: Solo el Founder puede interactuar con el bot
- **PIN/Código de sesión**: Segundo factor para operaciones sensibles (enviar emails, mover dinero)
- **Timeout de sesión**: Auto-lock después de 30 min de inactividad

#### Capa 2: Gestión de Secrets
- **NUNCA** almacenar API keys en código fuente
- Usar **Supabase Vault** (ya disponible) o variables de entorno en el servidor
- Rotación automática de keys cada 90 días
- Keys separadas por ambiente (dev/staging/prod)

#### Capa 3: Sandboxing de Agentes
- El bot NO tiene acceso directo al filesystem del repo
- Todas las operaciones pasan por **funciones aprobadas** (whitelist de acciones)
- Operaciones destructivas (borrar archivos, enviar dinero) requieren confirmación explícita

#### Capa 4: Input Validation
- Sanitización de todos los inputs del usuario antes de enviarlos al LLM
- Guardrails contra prompt injection (prefijos de sistema, validación de output)
- Deny-list de patrones de ataque conocidos

#### Capa 5: Auditoría
- Log completo de todas las interacciones (quién, qué, cuándo)
- Alertas automáticas para operaciones anómalas
- Backup periódico de logs

---

## 5. Arquitectura Propuesta

### 5.1 Fase 1: "Nzero Mobile" (Telegram)

```
┌──────────────┐     ┌────────────────────────┐     ┌─────────────┐
│   Telegram   │     │   Backend Serverless    │     │  Servicios  │
│   (Founder)  │     │                         │     │  Externos   │
│              │     │  ┌──────────────────┐   │     │             │
│  📱 App     │────▶│  │  Supabase Edge   │   │────▶│ Google APIs │
│              │     │  │  Function        │   │     │ (Gmail,     │
│  Comandos:  │     │  │                  │   │     │  Drive,     │
│  /status    │◀────│  │  ┌────────────┐  │   │◀────│  Sheets)    │
│  /inbox     │     │  │  │ QAI Agent  │  │   │     │             │
│  /email     │     │  │  │ Logic      │  │   │     │ Anthropic   │
│  /pendientes│     │  │  └────────────┘  │   │     │ Claude API  │
│              │     │  └──────────────────┘   │     │             │
│              │     │                         │     │             │
│              │     │  ┌──────────────────┐   │     └─────────────┘
│              │     │  │  Supabase DB     │   │
│              │     │  │  (State, Logs,   │   │
│              │     │  │   Context,       │   │
│              │     │  │   Vault/Secrets) │   │
│              │     │  └──────────────────┘   │
│              │     └────────────────────────┘
└──────────────┘
```

### Funciones Iniciales del Bot

| Comando | Acción | Agente |
|:---|:---|:---|
| `/status` | Lee y devuelve `STATUS.md` | Nzero |
| `/inbox` | Lista tareas pendientes de `INBOX.md` | Nzero |
| `/pendientes` | Resumen priorizado de pendientes | Nzero |
| `/email <texto>` | Redacta y envía email corporativo | Nzero + Gmail |
| `/propuesta <cliente>` | Genera propuesta simple | Nzero + Templates |
| `/finanzas` | Resumen financiero del mes | Finn |
| `/legal <consulta>` | Consulta legal rápida | Lex |
| `/help` | Lista de comandos disponibles | Sistema |

### 5.2 Componentes Técnicos

| Componente | Tecnología | Justificación |
|:---|:---|:---|
| **Bot Framework** | `python-telegram-bot` | Mismo stack Python que QaiCore |
| **Backend** | Supabase Edge Functions (Deno/TS) o Cloud Function (Python) | Serverless, ya tenemos Supabase |
| **LLM** | Anthropic Claude API | Mejor razonamiento para agentes complejos |
| **Database** | Supabase PostgreSQL | State management, logs, contexto |
| **Secrets** | Supabase Vault + env vars | Gestión segura de API keys |
| **Archivos** | Supabase Storage o GDrive | Para propuestas, documentos |
| **Sync del HQ** | Git push periódico a repo privado | Backup + fuente de verdad cloud |

### 5.3 Fase 2 (Futuro): Orquestador n8n

```
┌──────────┐                              ┌──────────────┐
│ Telegram │──┐                       ┌──▶│ Google APIs   │
└──────────┘  │   ┌────────────────┐  │   └──────────────┘
              ├──▶│                │──┤   
┌──────────┐  │   │   n8n Server   │  │   ┌──────────────┐
│ WhatsApp │──┤   │  (Self-hosted) │  ├──▶│ Supabase DB  │
└──────────┘  │   │                │  │   └──────────────┘
              ├──▶│  ┌──────────┐  │  │   
┌──────────┐  │   │  │ AI Agent │  │  │   ┌──────────────┐
│  Web UI  │──┘   │  │  Nodes   │  │  └──▶│ Claude API   │
└──────────┘      │  └──────────┘  │      └──────────────┘
                  └────────────────┘
```

---

## 6. Hoja de Ruta Recomendada

### Fase 1: "Telegram MVP" (Semanas 1-3)

| Semana | Entregable | Esfuerzo |
|:---|:---|:---|
| **S1** | Setup bot Telegram + backend Supabase Edge Function + auth básica | 🔨 Alto |
| **S2** | Comandos básicos (`/status`, `/inbox`, `/pendientes`, `/help`) | 🔨 Medio |
| **S3** | Integración Gmail (`/email`) + pruebas de seguridad | 🔨 Medio |

**Criterio de éxito:** Poder consultar pendientes y enviar un email desde el celular.

### Fase 2: "Agentes Expandidos" (Semanas 4-6)

| Semana | Entregable | Esfuerzo |
|:---|:---|:---|
| **S4** | Integrar Claude API para consultas inteligentes (Lex, Finn) | 🔨 Alto |
| **S5** | Comando `/propuesta` con generación de PDF simple | 🔨 Medio |
| **S6** | Sync automático del HQ al repo cloud + backup periódico | 🔨 Medio |

**Criterio de éxito:** Operar con los 3 agentes (Nzero, Lex, Finn) desde Telegram.

### Fase 3: "Robustez y Escala" (Semanas 7-10)

| Semana | Entregable | Esfuerzo |
|:---|:---|:---|
| **S7-8** | Fortress Protocol completo (PIN, timeouts, auditoría) | 🔨 Alto |
| **S9** | Evaluación de n8n como orquestador multi-canal | 🔨 Medio |
| **S10** | Documentación y playbooks actualizados | 🔨 Bajo |

**Criterio de éxito:** Sistema seguro, auditado y documentado para producción.

### Fase 4: "Horizonte" (Q2-2026, evaluación)

- 🔮 UI Web propia (si se valida necesidad)
- 🔮 WhatsApp como canal secundario (si hay clientes que lo requieran)
- 🔮 MCP Server remoto exponiendo herramientas QaiCore al mundo
- 🔮 Multi-agente coordinado en cloud

---

## 7. Estimación de Costos

### Costos Mensuales Fase 1

| Componente | Costo Estimado (USD/mes) | Notas |
|:---|---:|:---|
| Supabase (Free tier) | $0 | 500MB DB, 1GB storage, 500K edge invocations |
| Telegram Bot API | $0 | API gratuita |
| Claude API (Anthropic) | ~$5-15 | ~100-300 consultas/mes estimadas |
| Dominio (opcional) | $1 | Solo si se necesita webhook custom |
| **TOTAL estimado** | **$5-16** | |

### Comparativa si escalamos

| Escenario | Costo/mes |
|:---|---:|
| Solo Telegram + Supabase Free | $5-16 |
| + Supabase Pro (más DB/storage) | $30-40 |
| + n8n Cloud (Starter) | $50-60 |
| + UI Web (hosting Vercel/Railway) | $55-70 |
| + WhatsApp BSP | $80-120 |

> **Nota:** Los costos son estimaciones conservadoras para un solopreneur. El uso real puede variar.

---

## 8. Decisiones Pendientes

> [!IMPORTANT]
> Las siguientes decisiones requieren input del Founder antes de proceder.

### 8.1 Decisiones Técnicas

1. **¿Backend Python o TypeScript?**
   - Python: Mismo stack que QaiCore, reutilización directa de tools
   - TypeScript/Deno: Nativo en Supabase Edge Functions, más ligero
   - **Recomendación Nzero:** Python vía Cloud Function externa (Railway/Render) + Supabase como DB

2. **¿Sync del HQ al cloud?**
   - Opción A: Push automático a GitHub privado (simple, gratis)
   - Opción B: Supabase Storage como mirror (más integrado)
   - **Recomendación Nzero:** GitHub privado como backup + Supabase para datos operativos

3. **¿Modelo LLM?**
   - Claude (Anthropic) — mejor razonamiento, más caro
   - Gemini (Google) — ya tenemos API key, gratis para bajo volumen
   - **Recomendación Nzero:** Arrancar con Gemini (costo $0) → migrar a Claude si se necesita

### 8.2 Decisiones de Negocio

4. **¿Prioridad de esta misión vs otros proyectos?**
   - ¿Se puede dedicar tiempo de desarrollo cada semana?
   - ¿O es un proyecto para ratos libres?

5. **¿La UI Web es un objetivo comercial?**
   - Si sí → Invertir en Fase 4 como producto
   - Si no → Telegram es suficiente a largo plazo

---

## Apéndice: Glosario

| Término | Definición |
|:---|:---|
| **MCP** | Model Context Protocol — estándar abierto (Anthropic) para conectar LLMs con herramientas |
| **Edge Function** | Función serverless ejecutada en el "borde" de la red, cerca del usuario |
| **BSP** | Business Solution Provider — intermediario autorizado de WhatsApp Business API |
| **Prompt Injection** | Ataque donde instrucciones maliciosas manipulan el comportamiento del LLM |
| **RLS** | Row Level Security — seguridad a nivel de fila en PostgreSQL/Supabase |

---

> **Próximo paso:** Revisión del Founder → Iteración → Plan de Acción detallado para Fase 1.  
> **Ubicación de este entregable:** `QaiLabs/AREA_51/mision_salida/` — elegido porque esta es una exploración R&D en fase de concepción, aún no un prototipo funcional.
