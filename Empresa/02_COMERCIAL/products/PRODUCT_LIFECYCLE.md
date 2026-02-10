# Ciclo de Vida del Producto QAI (The Pipeline)

> "De idea mental a producto escalable, sin burocracia pero con disciplina."

Definimos tres estados claros para cualquier iniciativa. Cada estado tiene requisitos de entrada y salida.

## Fase 0: La Incubadora Mental (Backlog)
*   **Estado:** Idea / Concepto.
*   **Donde vive:** En `docs/empresa/products/ideas.md` o Notion.
*   **Requisito de Entrada:**
    *   Pasar el filtro "Low-End Disruptor": ¿Es útil? ¿Es barato de hacer? ¿Hay un nicho desatendido?
*   **Ejemplos:** *"Tus 6 ideas sin demandante aún".*

## Fase 1: QaiLabs (Validación & Piloto)
*   **Estado:** Prototipo Funcional / Custom Solution.
*   **Donde vive:** Repositorio en GitHub (`qai-labs-nombreproyecto`).
*   **Enfoque:** Resolver el problema de **UN** cliente real (o un problema propio).
*   **Requisito de Salida:**
    *   El cliente paga o usa intensivamente el producto.
    *   Identificamos que el código es generalizable a otros clientes (SaaS potential).
*   **Limitaciones:** No tiene SLA de soporte, UI "tosca", despliegue manual.
*   **Ejemplo Actual:** *Automatización Facturas vs PO (Early Adopter).*

## Fase 2: QaiProd (Producto SaaS)
*   **Estado:** Live / Ready-to-Market.
*   **Donde vive:** Repositorio SaaS (`qai-prod-nombreapp`) + Landing Page.
*   **Enfoque:** Escalar ventas a "Desconocidos".
*   **Requisitos:**
    *   Onboarding automatizado (o semi-automatizado).
    *   Pricing definido (Stripe/Reveniu).
    *   Soporte Nivel 1 (Agente/Docs).
*   **Ejemplo Actual:** *Gestión Zen.*

---

## Flujo de Trabajo (The Factory)

1.  **Identificación:**
    *   Tú detectas una necesidad.
    *   Escribes un breve "Product Brief" en Notion usando el *Product Blueprint* (`docs/templates/PRODUCT_REQ_TEMPLATE.md`).
2.  **Experimentación (Fase 1):**
    *   Clonas el `qai-saas-template`.
    *   Agentes construyen el MVP.
    *   Se despliega en URL de prueba.
3.  **Graduación (Fase 2):**
    *   Si el experimento tracciona, se "pule" el código.
    *   Se conecta pasarela de pago.
    *   Se lanza comercialmente.
