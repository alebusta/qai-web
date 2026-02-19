# ADR-018: Protocolo de Comunicaciones Seguras y Estabilidad SSL

## Estatus
Aceptado (13-Feb-2026)

## Contexto
Durante la Fase 4, se detectaron dos fallos críticos en el envío de correos:
1. **Interferencia SSL**: El terminal del IDE inyecta variables de entorno de proxy (`HTTP_PROXY`, etc.) que bloquean la conexión con las APIs de Google.
2. **Corrupción de Formato**: Pasar el cuerpo de un email como argumento de línea de comandos (`--body`) provoca que los caracteres de escape (`\n`) se traten como texto literal, arruinando el renderizado HTML.

## Decisiones
1. **Limpieza de Entorno**: Todas las herramientas que utilicen APIs externas (Gmail, Drive, Gemini) deben limpiar radicalmente cualquier variable de entorno que contenga la palabra "PROXY" al inicializarse.
2. **Input File-Only**: Los agentes tienen **prohibido** enviar cuerpos de email extensos mediante strings en CLI. Se debe utilizar siempre una entrada basada en archivos (`--body-md` o similar).
3. **Validación de Renderizado**: Antes de un envío final, el agente debe generar un preview local y verificar (vía lectura de archivo) que no existan caracteres de escape literales (`\n`, `\r`, `\t`) dentro del HTML.

## Consecuencias
- **Positivas**: Eliminación de re-procesos por errores de formato. Mayor estabilidad en redes restringidas o entornos de desarrollo (Cursor).
- **Negativas**: Ligero aumento en el uso de disco temporal (archivos `.md` efímeros).
