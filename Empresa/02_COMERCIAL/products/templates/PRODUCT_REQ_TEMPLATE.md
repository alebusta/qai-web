# Product Requirement Document (PRD) - The Blueprint

> "Todo gran software empieza con una definición clara, no con código."

**Proyecto:** [Nombre del Proyecto]
**Estado:** Fase 0 (Idea) | Fase 1 (Labs) | Fase 2 (Prod)
**Owner:** [Tu Nombre o Agente Responsable]

---

## 1. El Problema (The Pain)
*¿Qué dolor estamos resolviendo? ¿Por qué esto debería existir?*
*   **Contexto:** (Describe la situación actual)
*   **El Dolor:** (Qué le duele al usuario hoy. Ej: "Pierden 4 horas a la semana comparando excels").
*   **La Oportunidad:** (Por qué nosotros podemos resolverlo mejor/más barato. Low-End Disruptor thesis).

## 2. El Usuario (User Persona)
*¿Quién va a usar esto?*
*   **Persona:** (Ej: "Juan, el administrador de edificio de 50 años").
*   **Motivación:** (Quiere irse temprano a casa).
*   **Nivel Tecnológico:** (Bajo/Medio/Alto).

## 3. La Solución (High Level)
*¿Qué vamos a construir?*
*   **Concepto:** (Pitch de 1 frase).
*   **Core Loop:** (Qué hace el usuario repetidamente).
*   **Output Esperado:** (Un reporte, una alerta, una acción automática).

## 4. Requerimientos Funcionales (User Stories)
*Detalle para los Agentes Dev.*
*   [ ] **US-01:** Como [usuario], quiero [acción], para [beneficio].
*   [ ] **US-02:** ...
*   [ ] **US-03:** ...

## 5. Arquitectura Técnica (Constraints)
*   **Frontend:** (Cloudflare Pages / Vite / React).
*   **Backend:** (Supabase / Edge Functions).
*   **AI Models:** (Gemini 2.0 para razonamiento, Haiku para clasificación rápida).
*   **Datos Sensibles:** (¿Maneja PII? ¿Requiere RAG local?).

## 6. Criterios de Éxito (KPIs)
*¿Cómo sabemos si funcionó?*
*   **Fase Labs:** El cliente piloto lo usa 3 veces por semana sin quejarse.
*   **Fase Prod:** 10 usuarios pagados.

---
*Usa este documento como prompt inicial para el Agente "Product Manager".*
