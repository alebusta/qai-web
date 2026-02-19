# ADR-021: Implementación de Motor de Búsqueda Híbrido (QMD)

**Fecha**: 2026-02-19  
**Estado**: Afectado  
**Contexto**: A medida que el Digital HQ de QAI crece en volumen de documentos (KIs, ADRs, Actas, Minutas), la búsqueda lineal mediante `grep` se vuelve ineficiente para los agentes. Se requiere una solución que mejore la recuperación de información mediante búsqueda semántica y re-ranking, sin comprometer la privacidad local.

## Problema
Los agentes pueden sufrir de "ceguera de contexto" o amnesia selectiva si no encuentran el documento exacto que define una regla o antecedente. Las herramientas estándar de búsqueda por palabras clave fallan cuando el usuario (o el agente) usa términos sinónimos o conceptos relacionados pero no exactos.

## Decisión: Integración de QMD (Quick Markdown Search)
Se integra la herramienta `qmd` como una "skill" de arquitectura dentro del núcleo de QaiCore:

1.  **Instalación Aislada**: El motor se aloja en `QaiCore/bin/qmd/` (vía node_modules) para no depender de instalaciones globales.
2.  **Arquitectura Híbrida**: Se utiliza BM25 para velocidad y Vector Search (Embeddings locales via Gemma) para precisión semántica.
3.  **Localidad Total**: Los modelos (Gemma 300M, Qwen3 Reranker) se ejecutan localmente en la máquina del host, manteniendo la privacidad de QAI.
4.  **Estructura de Cache**: La base de datos de búsqueda se almacena en `.qai/cache/qmd/`, la cual ha sido añadida al `.gitignore` para evitar redundancia en el repositorio.
5.  **Variables de Entorno**: Se utiliza `XDG_CACHE_HOME` para centralizar los metadatos dentro de la estructura corporativa `.qai`.

## Consecuencias
- **Positivas**: 
    - Búsqueda instantánea e inteligente en todo el HQ (incluyendo experimentos en QaiLabs).
    - Capacidad de "entender" intenciones de búsqueda (ej: buscar "impuestos" encontrará "IVA" y "F29").
    - Menor consumo de tokens al filtrar solo los documentos realmente relevantes antes de pasarlos al contexto de la LLM.
- **Negativas**: 
    - Consumo de espacio en disco inicial (~1.6 GB) para los modelos locales.
    - Requiere ejecución periódica de `qmd update` para mantener el índice fresco.

## Contingencia y Evaluación de Performance
Se establece un periodo de prueba de 7 días. Si el impacto en el tiempo de respuesta de los agentes o la carga de CPU en el entorno local degrada la experiencia de usuario o la agilidad operativa, **esta decisión será revertida** (eliminando `QaiCore/bin/qmd` y el cache en `.qai/cache`). La simplicidad y la agilidad tienen prioridad sobre la sofisticación técnica.

---
**Autor**: Nzero  
**Aprobado por**: Alejandro (Founder)  
**Relacionado con**: ADR-002 (QaiCore Structure), ADR-019 (Primacía Corporativa)
