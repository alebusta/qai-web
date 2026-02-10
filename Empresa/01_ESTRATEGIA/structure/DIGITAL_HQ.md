# Digital HQ & Tech Stack: La Oficina es el IDE

> "Hoy nuestra oficina no es un edificio ni un servidor de Discord con bots hablando solos. Nuestra oficina es el IDE y nuestra sala de reuniones es el Chat Contextual."

Este documento define la infraestructura tecnológica y operativa actual de **The QAI Company**, priorizando el pragmatismo "Bootstrapped" sobre la complejidad innecesaria.

## 1. Filosofía Operativa
*   **The IDE is the Office:** Todo el trabajo real sucede dentro del entorno de desarrollo (VS Code, Cursor, Windsurf, Antigravity).
*   **Human-Centric Orchestration:** A diferencia de modelos teóricos donde los agentes "viven" y "deciden" solos, aquí los agentes viven *bajo demanda* en el contexto del proyecto. El humano orquesta; el agente ejecuta.
*   **Stack Agnostic (Labs):** No nos casamos con tecnologías. Usamos lo que funciona hoy, pero estamos siempre probando mañana.

## 2. Infrastructure Stack (La Realidad Actual)

### A. Gestión del Conocimiento (Brain)
*   **Estratégico & Ideas:** **Notion**. Para roadmaps de alto nivel, brain-dumping y organización de tareas abstractas.
*   **Técnico & Procedimental:** **Markdown (Repo)**. La documentación viva (como este archivo) vive junto al código.
*   **Memoria:** Discos Locales + GitHub. Estructura de directorios simple pero disciplinada.

### B. "The Factory" (Desarrollo)
*   **Interfaces:** Antigravity (Google), VS Code, Cursor, Windsurf.
*   **Flujo:** `Instrucción Humana` -> `Directorio Local` -> `Generación IA` -> `Iteración en IDE` -> `Push a GitHub`.
*   **Repositorios Centralizados (QAI Corp):**
    *   **GitHub Org:** `The QAI Company` (Propiedad de la empresa, no personal).
    *   **Convención Naming:**
        *   `qai-labs-[proyecto]`: Para experimentos y pilotos.
        *   `qai-prod-[producto]`: Para SaaS en producción.
        *   `qai-core-[infra]`: Para templates y configs comunes.
*   **Modelos (The Engines):**
    *   **Propietarios:** Gemini, Claude, OpenAI (para tareas de razonamiento pesado).
    *   **Open Source / Small:** Gemma 270M, Llama (para experimentos de fine-tuning y costos bajos).

### C. Despliegue (Production)
*   **Filosofía:** Serverless & Edge. Costo cero si no hay tráfico.
*   **Frontend:** **Cloudflare Pages** (Rapidez, seguridad, costo bajo).
*   **Backend / Database:** **Supabase** (Auth, DB, Realtime).
*   **Otros:** Vercel, Netlify (según el caso de uso del producto).

## 3. Modelo de Agentes: Nivel de Autonomía
Actualmente operamos en **Nivel 2: Asistencia Supervisada**.

*   **Lo que NO hacemos:**
    *   Agentes conversando entre ellos sin supervisión (riesgo de alucinación).
    *   Agentes tomando decisiones de gasto o despliegue autónomo.
*   **Lo que SÍ hacemos:**
    *   Agentes generando el 80% del código base ("Boilerplate & Logic").
    *   Agentes refactorizando y explicando código.
    *   Agentes analizando documentos (RAG local).

## 4. Análisis Crítico & Riesgos (Self-Audit)
Reconocemos las debilidades actuales de nuestro modelo minimalista:
*   **"Bus Factor = 1":** Dependencia excesiva de la presencia física del Founder. Riesgo de "silorización" local.
*   **Fragilidad de Contexto:** Los agentes son efímeros (por sesión). Si no se inyecta el contexto correcto, su calidad baja.

## 5. Estrategia de Mitigación y Futuro
Para escalar sin rompernos, implementaremos:

### A. Persistencia de "Expertise" (RAG Local)
Para los perfiles complejos (Lex, Finn Bot), no confiaremos solo en el entrenamiento base del modelo.
*   **Acción:** Creación de `knowledge-bases` específicas (bases de datos vectoriales ligeras o Markdown estructurado) con:
    *   Leyes y Normativas (Texto formal).
    *   Experiencias y Casos (Relatos informales y aprendizajes).
*   **Objetivo:** Que el agente "Lex" siempre consulte esta base antes de responder, simulando una memoria experta persistente.

### B. Estandarización (Templates)
*   Creación de un `qai-saas-template`: Un repositorio semilla con el stack configurado y, crucialmente, los **System Prompts** de los agentes ya definidos en la carpeta `/docs`.

### C. Roadmap de Evolución de Autonomía
1.  **Fase Actual:** Human-in-the-loop estricto (100% supervisión).
2.  **Fase Próxima (Semi-Autonomous):** Agentes con RAG para consultas especializadas.
3.  **Fase Futura (Autonomous Tasking):** Agentes de Soporte Nivel 1.

## 6. Seguridad & Estandarización
Para operar con IA de forma responsable y escalable.

### A. Protocolo de Seguridad ("The Shield")
*   **Regla de Oro:** Datos Personales Identificables (PII), Claves API y Secretos Comerciales críticos **NUNCA** se envían al contexto de un LLM público sin anonimizar.
*   **Local First:** Para datos sensibles, preferimos modelos locales (Gemma/Llama) o instancias Enterprise con política de "Zero-Retention".

### B. El "Molde" de Producto (Product Blueprint)
Para evitar la "hoja en blanco", estandarizamos cómo pedimos software a los agentes.
*   **Template Maestro:** `docs/templates/PRODUCT_REQ_TEMPLATE.md`.
*   **Estructura:**
    1.  Problem Statement (El "Dolor").
    2.  User Stories (El "Quién").
    3.  Technical Constraints (El "Stack").
    4.  Success Metrics (El "Éxito").

### C. Protocolo de Organización de Clientes
Estandarización obligatoria para todas las carpetas en `Empresa/02_COMERCIAL/clientes/`.
*   `01_insumos/`: Material base y requerimientos.
*   `02_entregas/`: Productos finales certificados.
*   `03_gestion/`: Documentación interna y costos.
*   **Referencia:** [Protocolo de Organización de Clientes](file:///c:/Users/abustamante/TheQaiCo/Empresa/02_COMERCIAL/PROTOCOLO_ORGANIZACION_CLIENTES.md)

*Nota: Sin este molde completo, no se tira una línea de código ni se procesa un nuevo cliente.*
