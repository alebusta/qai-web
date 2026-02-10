# Playbook: Coordinación de Inbox y Flujo de Landing Zone

Este protocolo define cómo QAI Company organiza su trabajo diario utilizando el IDE y las herramientas de IA.

## 1. El Ciclo de Vida del Dato
1. **Entrada**: Archivos crudos, transcripciones o capturas de pantalla llegan a `TorreDeControl/temp_files/`.
2. **Triage (Nzero)**: 
   - Nzero revisa el contenido.
   - Si es financiero -> Asigna a **Finn**.
   - Si es legal/contractual -> Asigna a **Lex**.
   - Si es desarrollo puro -> Asigna a **Builder**.
3. **Registro en INBOX**: La tarea se escribe en `TorreDeControl/INBOX.md` indicando el agente responsable.
4. **Ejecución y Preview**:
   - El agente genera la salida usando los `templates`.
   - Si es un email o documento externo, el agente **DEBE** generar un preview en `temp_files/`.
   - El agente solicita aprobación ("Human-in-the-loop").
5. **Envío/Finalización**: Solo tras el "OK" del usuario se procede al envío final.

## 2. Facultades por Agente

### Nzero (Control de Tráfico)
- Único agente con facultad para mover archivos de `temp_files` a carpetas finales de HQ.
- Auditor de consistencia de `STATUS.md`.

### Finn (Financiero)
- Facultad para redactar correos de cobranza y seguimiento de facturas.
- Edición directa del Runway en Google Sheets.

### Lex (Legal)
- Facultad para redactar minutas y memorándums de entendimiento (MOU).
- Revisión de cumplimiento tributario.

## 3. Cierre de Jornada (Zero Inbox)
Al finalizar el día, `temp_files/` debe estar vacío y todas las tareas en `INBOX.md` deben tener un estado claro.
