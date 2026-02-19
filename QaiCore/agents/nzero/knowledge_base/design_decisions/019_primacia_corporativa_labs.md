# ADR-019: Primacía Corporativa y Aislamiento de Experimentos (QaiLabs)

**Fecha**: 2026-02-19  
**Estado**: Aceptado  
**Contexto**: Se detectó el riesgo de que los agentes (especialmente Finn o Builder) confundan archivos de configuración (.codacy, .env) o manuales de procedimientos encontrados dentro de proyectos en `QaiLabs` con directrices globales de la empresa.

## Problema
El desorden inherente a la fase de experimentación en `QaiLabs` puede generar "falsos positivos" de protocolos. Un agente que busca "cómo trabajar" podría encontrar un `PROTOCOLO_TRABAJO.md` dentro de un prototipo y adoptarlo erróneamente para toda la orquestación de QAI.

## Decisión: Primacía Ejecutiva (Executive Precedence)

Se establece una jerarquía estricta de "Verdad Corporativa":

1.  **Nivel 1 (Orden Suprema)**: `TorreDeControl/` (STATUS, INBOX, AGENT_ACTIVITY) y `QaiCore/` (Playbooks, Profile, Tools).
2.  **Nivel 2 (Estrategia)**: `Empresa/` (Legal, Comercial, Finanzas).
3.  **Nivel 3 (Datos/Código)**: `QaiLabs/` o `QaiProd/`.

### Reglas para Agentes (Guardrails):
- **Prohibición de Adopción**: Los agentes tienen prohibido adoptar protocolos, reglas o manuales encontrados en subcarpetas de `QaiLabs` como normas globales.
- **Aislamiento de Configuración**: Los agentes no deben editar archivos de configuración de herramientas (como `.codacy`, `.gitignore`, `.env`, `package.json`) dentro de `QaiLabs` pensando que afectan a la empresa. Solo se editan si la tarea específica es "Configurar el experimento X".
- **Advertencia de Zona**: Se implementará un archivo de aviso en la raíz de `QaiLabs` para señalizar el cambio de contexto.

## Consecuencias
- **Positivas**: Se evita la deriva operativa donde un agente cambia su comportamiento por un archivo residual de un experimento.
- **Negativas**: El agente requiere un poco más de contexto para saber si está trabajando "en" un experimento o "desde" la empresa.

---
**Autor**: Nzero  
**Aprobado por**: Alejandro (Founder)  
**Relacionado con**: ADR-002 (QaiCore Structure), ADR-004 (Graduación Labs -> Prod)
