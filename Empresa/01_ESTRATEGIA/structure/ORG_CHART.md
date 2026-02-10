# Organigrama Operativo: Human-Agent Interaction

> "No es una jerarquía de poder, es un flujo de orquestación."

Este documento es **complementario** a `TEAM_PROFILES.md`.
*   **Profiles:** Define *quiénes* son (sus habilidades y roles).
*   **Org Chart:** Define *cómo* se relacionan y fluye el trabajo.

## Diagrama de Orquestación (The QAI Topology)

```mermaid
graph TD
    %% Estilo del Nodo Humano
    Human[**FOUNDER / CEO**<br>Human-in-the-Loop]:::human
    
    %% Estilo de los Nodos Estructurales
    subgraph Structure [Estructura Trinitaria]
        direction TB
        
        %% Unidad TheQai
        subgraph Col1 [A. TheQai: Governance]
            direction TB
            Lex[Agente Legal<br>(Lex)]:::agent
            Finn[Agente Financiero<br>(Finn Bot)]:::agent
        end
        
        %% Unidad Labs
        subgraph Col2 [B. QaiLabs: Innovation]
            direction TB
            Research[Research Agent<br>(Curie)]:::agent
            Experiment[Data Science Agent<br>(DaVinci)]:::agent
        end
        
        %% Unidad Prod
        subgraph Col3 [C. QaiProd: Execution]
            direction TB
            PM[Product Manager<br>Assistant]:::agent
            Dev[Full-Stack Dev<br>(Builder)]:::agent
            Sales[Sales & Growth<br>(Rainmaker)]:::agent
        end
    end

    %% Relaciones de Flujo
    Human -->|Define Estrategia & Prompt| Col1
    Human -->|Plantea Hipótesis| Col2
    Human -->|Aprueba Specs & Roadmap| Col3

    %% Interacciones entre Agentes (Supervisadas)
    Research -.->|Informa nuevos trends| PM
    Lex -.->|Valida Contratos| Sales
    PM -->|Genera Tickets| Dev
    
    %% Output
    Dev -->|Deploy| Product[$$ Productos SaaS $$]:::output
    Sales -->|Vende| Product

    %% Clases de Estilo
    classDef human fill:#f96,stroke:#333,stroke-width:4px,color:black;
    classDef agent fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,color:black;
    classDef output fill:#8bc34a,stroke:#33691e,stroke-width:2px,color:white;
```

## Flujos de Trabajo (Workflows)

### 1. Flujo de Creación (Labs -> Prod)
1.  **Human** define una idea usando el `PRODUCT_REQ_TEMPLATE`.
2.  **PM Agent** analiza la idea y crea especificaciones (US).
3.  **Dev Agent** genera el boilerplate y código base en el IDE.
4.  **Human** revisa código, ajusta y valida (The Loop).
5.  **Dev Agent** ayuda a desplegar.

### 2. Flujo de Cumplimiento (TheQai)
1.  **Human** solicita revisión de un contrato o situación tributaria.
2.  **Lex/Finn** consultan su *Knowledge Base* (RAG).
3.  **Lex/Finn** generan borrador o reporte.
4.  **Human** valida y ejecuta.
