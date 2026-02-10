# Análisis Detallado: Reunión Gestión Zen (22-Dic-2025)

**Fecha**: 2025-12-28  
**Documento Fuente**: `reunionGZ_22122025-1.txt`  
**Participantes**: Anabel (SWS), Gerardo (SWS), Sandra (SWS), Ramón (Estratega), Alejandro (QAI).

---

## 1. Perfiles y Dinámica de la Reunión

*   **Anabel (Key User)**: La "mano derecha" operativa. Encargada de la carga de gastos. Valora el ahorro de tiempo y la precisión. Si ella adopta la herramienta, el proyecto tiene éxito garantizado.
*   **Ramón (Visionario/Digital)**: Empuja hacia la digitalización total (fotos, voz, automatización). A veces subestima la resistencia humana, pero marca el norte tecnológico.
*   **Gerardo/Sandra (Pragmáticos/Socios)**: Preocupados por la realidad del terreno (mayordomos con teléfonos malos, cheques que se pierden en el comité). Buscan trazabilidad y evitar errores humanos catastróficos.
*   **Alejandro (Puente/Arquitecto)**: Propone una evolución gradual ("A pie -> Twingo -> Ferrari"). Su rol es calmar la fricción adaptando el sistema al humano, no al revés.

---

## 2. Requerimientos Técnicos Prioritarios (Módulo de Gastos)

### A. Gestión de Servicios con Múltiples Cuentas (Agua/Luz)
*   **Problema**: Algunas comunidades tienen múltiples medidores/boletas para un mismo servicio (ej. 16 boletas de Aguas Andinas). Capturarlas una a una es tedioso.
*   **Solución Propuesta**: 
    - Permitir carga de un solo PDF con todas las boletas.
    - Generar un **"Reporte de Agua/Servicio"** que muestre el Gran Total para el gasto común, pero permita desglose (sub-cuentas) para transparencia de los copropietarios.

### B. Prorrateo Estacional (Metrogás/Calefacción)
*   **Problema**: La división de gastos entre "Gasto Común" e "Individual" cambia según el mes.
*   **Solución Propuesta**: Configurar reglas estacionales (Invierno: Mayo-Sep | Verano: Oct-Abril). El sistema debe detectar el mes automáticamente y aplicar el % correcto de división.

### C. Flujo de Egresos (Pagos)
*   **Requisito Crítico**: El proceso no termina con el registro del gasto. Se requiere un botón de **"Pagar/Generar Egreso"** inmediato.
*   **Estados de Pago**:
    1.  `En Proceso/Tránsito`: Egreso emitido, enviado al comité para firma.
    2.  `Aprobado`: Firmado por el comité (trazabilidad de quién tiene el documento).
    3.  `Pagado/Cobrado`: Conciliado con el banco.
*   **Formatos**: Capacidad de generar comprobantes de egreso (PDF) enviables por WhatsApp.

### D. Lectura de Medidores y Pre-Auditoría
*   **Captura**: Alternativas de Foto, Excel o incluso Notas de Voz (convertir audio a tabla).
*   **Alertas Inteligentes**: Si un consumo excede un parámetro (ej. +10m3 de agua o +10% del total en calefacción), el sistema debe lanzar un **Warning** antes de guardar para evitar errores de digitación (ej. confundir un 8 con un 5).

---

## 3. Puntos Estratégicos y Observaciones de Negocio

### 🤝 Afinidades
*   Todos coinciden en que la interfaz estilo "ChatGPT" para consultar datos (¿Cuánto pagamos de agua el mes pasado?) es una ventaja competitiva enorme.
*   La agrupación visual de Unidades + Estacionamientos por alícuota fue muy celebrada por su claridad.

### ⚠️ Discrepancias / Riesgos
*   **Legalidad en Nóminas**: Ramón advierte sobre la responsabilidad legal de generar nóminas (recursos humanos) dentro de la plataforma. Se sugiere que QAI solo actúe como "registrador", no como "elaborador responsable" para proteger la marca.
*   **Resistencia al Cambio**: Existe el miedo de que el personal de campo (mayordomos/conserjes) le haga "la guerra" al sistema si se les obliga a usar tecnología compleja. La solución debe ser multicanal (voz, foto o papel escaneado).

### 💡 Ideas de "Siguiente Nivel"
*   **IA de Soporte**: El chat no solo debe responder sobre datos del gasto, sino también sobre el **Reglamento de Copropiedad** de la comunidad específica y la Ley de Copropiedad General.

---

## 4. Próximos Pasos Propuestos

1.  [ ] Diseñar el prototipo de la pantalla de **Egreso/Pago** con estados de firma.
2.  [ ] Implementar la configuración de **Prorrateo Estacional**.
3.  [ ] Crear el "Landing Zone" para carga masiva de boletas de un mismo servicio.
4.  [ ] Validar con Lex (Agente Legal) los límites de responsabilidad en el módulo de nómina.

---
**Elaborado con amor por Nzero (con info de Alejandro)**  
*Misión: Vaciar temp_files y mover el conocimiento al HQ.*
