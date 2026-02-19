---
description: Cómo procesar una reunión/transcripción desde temp_files hasta el HQ
---

# Workflow: Procesamiento de Reuniones y Transcripciones

Este workflow describe los pasos que debe seguir un agente para transformar un archivo crudo de reunión en inteligencia operativa.

## Pasos

1. **Revisión de Landing Zone**
   - Verificar archivos en `TorreDeControl/temp_files/`.
   - Identificar el contexto (Cliente, Proyecto, Fecha).

2. **Análisis de Contenido**
   - Leer el archivo completo.
   - Extraer:
     - **Perfiles**: Quiénes son y qué rol juegan.
     - **Requerimientos Técnicos**: Funcionalidades nuevas o cambios.
     - **Estrategia**: Afinidades, discrepancias y riesgos.
     - **Action Items**: Tareas concretas para el INBOX.

3. **Clasificación y Salida**
   - Crear (si no existe) carpeta del cliente en `Empresa/02_COMERCIAL/clientes/[NombreCliente]`.
   - Generar el análisis detallado: `YYYY-MM-DD_REUNION_ANALISIS_DETALLADO.md`.
   - **Archivo de Insumo**: Mover el archivo original a `[CarpetaCliente]/minutas/` (NO borrar si tiene valor histórico).

4. **Sincronización de Memoria**
   - **INBOX.md**: Agregar las tareas técnicas y de gestión.
   - **STATUS.md**: Actualizar el hito del proyecto y registrar la acción en el changelog.
   - **AGENT_ACTIVITY.md**: Registrar la ejecución de este workflow.

5. **Cierre (Zero InBox)**
   - Asegurarse de que `temp_files/` quede vacío una vez movidos los archivos.
