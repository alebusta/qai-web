# ADR-010: Protocolo de Cierre Autónomo (PCA)

## Estado
Aceptado

## Contexto
Los agentes (especialmente Nzero) estaban fallando en sincronizar la documentación institucional (`STATUS.md`, `AGENT_ACTIVITY.md`, etc.) de forma proactiva al finalizar una misión, esperando a que el usuario lo preguntara. Esto rompe la confianza en la "Memoria Institucional" y genera burocracia innecesaria.

## Decisión
Se establece el **PCA (Protocolo de Cierre Autónomo)** como una pre-condición obligatoria para cualquier agente antes de reportar el fin de una tarea.

### Requisitos del PCA:
1. **Sincronización Atómica**: Toda tarea completada debe reflejarse simultáneamente en `INBOX.md`, `STATUS.md` y `CHANGELOG.md`.
2. **Log de Actividad**: Cada sesión debe dejar una huella clara en `AGENT_ACTIVITY.md`.
3. **Log de Hallazgos**: Las decisiones técnicas o metodológicas deben resumirse en `DISCOVERY_LOG.md`.
4. **Limpieza de Landing Zone**: `temp_files/` debe quedar vacío si se procesaron archivos.
5. **Autonomía**: No se debe esperar confirmación o pregunta del usuario para realizar estas sincronizaciones.

## Consecuencias
- **Positivas**: Memoria institucional siempre al día, mayor confianza del usuario, reducción de ciclos de preguntas/respuestas.
- **Negativas**: Ligero aumento en el consumo de tokens por sesión debido a las escrituras finales obligatorias.
