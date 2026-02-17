# Análisis de Caso: Ciclo Recrea Vía (Fundación)

> **Fecha**: 16-Feb-2026  
> **Autor**: Nzero (Arquitecto)  
> **Propósito**: Mapear dolores del potencial cliente con servicios que QAI puede ofrecer.

---

## 1. Resumen del Caso

**Cliente potencial**: Lina, Fundación Ciclo Recrea Vía (8 años como fundación).  
**Dolor central**: Falta absoluta de control y gestión profesional sobre recursos — lo que Lina llama "cáncer administrativo". Combina ceguera financiera, dependencia de personal ineficiente, irregularidades contables, riesgos laborales y pérdida de foco estratégico.

---

## 2. Mapa Dolor → Servicio QAI

| # | Dolor / Necesidad | Agente/Producto QAI | Servicio concreto posible |
|:--|:------------------|:--------------------|:---------------------------|
| 1 | **Ceguera financiera**: sin balances, sin historial, Excel manual ("El robo 123") | **Finn** + Google Sheets + Playbooks | **Sistema Financiero mínimo**: Registro Diario, Runway, P&L en Sheets + procesos documentados (playbooks). No reemplaza contador; da SSOT y visibilidad. |
| 2 | **Dependencia de Enrique** (admin ineficiente); no puede despedirlo por deuda 15–20M | **Finn** + automatización | **Reportes automatizados** y flujo de datos único. Reducir lo que “solo Enrique hace” para que Lina pueda eventualmente reemplazarlo por alguien part-time o sistema. |
| 3 | **Irregularidades contables**, contador anterior sin balances, sospecha de robo | **Finn** + **Lex** | **Ordenamiento contable** (estructura + clasificación) + **checklist de compliance** (SII, libros). Lex para marco legal; Finn para datos y procesos. |
| 4 | **Sin inventario en bodega**; robos de productos, nada de entradas/salidas | — (no producto actual) | **Oportunidad**: Control mínimo de inventario (entradas/salidas) en Sheets o módulo simple. Puede ser Fase 2 o paquete “control de bodega”. |
| 5 | **No puede emitir certificados de donación** (fundación 8 años) | **Lex** + **Finn** | **Ruta a certificados**: Ordenar contabilidad (Finn) + cumplir exigencias legales/tributarias para fundaciones (Lex). Servicio: “Roadmap contable-legal para habilitar donaciones”. |
| 6 | **Riesgos laborales**: ~30 personas en boletas cuando deberían tener contrato; ya pagó 15M por una demanda | **Lex** | **Diagnóstico laboral + plan de regularización**: Revisión de modalidades de contratación, checklist de riesgos, priorización (quién regularizar primero). Asesoría, no reemplazo de abogado laboral. |
| 7 | **Lina atada a tareas operativas** (pagar boletas a la 1am); quiere vender y buscar alianzas | **Finn** + procesos | **Automatización de lo repetitivo**: Registro de movimientos asistido (OCR de boletas si aplica), reportes automáticos, playbooks para que no dependa de una persona para “saber los números”. |

---

## 3. Servicios que QAI puede ofrecer hoy (sin nuevo producto)

- **Paquete “Ordenamiento Financiero”**  
  - Diseño e implementación de un Sistema Financiero mínimo (Sheets: Registro Diario, Runway, P&L, control de facturación).  
  - Playbooks de registro de gastos/ingresos y de cierre mensual.  
  - **Responsable**: Finn + Nzero (diseño).  

- **Paquete “Ruta a Certificados de Donación”**  
  - Diagnóstico contable y legal (qué falta para que la fundación pueda emitir certificados).  
  - Plan por fases: ordenar contabilidad → cumplir requisitos SII/legales → proceso de emisión.  
  - **Responsable**: Finn (contable) + Lex (legal/tributario fundaciones).  

- **Diagnóstico laboral y plan de regularización**  
  - Revisión de modalidades actuales (boletas vs contrato), identificación de riesgos y priorización.  
  - No sustituye abogado laboral ni firma de contratos; sí entrega claridad y roadmap.  
  - **Responsable**: Lex.  

- **Reportes automatizados desde su Sistema Financiero**  
  - Una vez exista Registro Diario y estructura en Sheets: reportes de flujo de caja, resumen mensual, alertas básicas.  
  - **Responsable**: Finn (tools gsheets + scripts/playbooks).  

- **Propuesta comercial formal**  
  - Deck + PDF + email con alcance, fases y precios (Sistema de Propuestas Executive Horizon).  
  - **Responsable**: Nzero/Comercial + templates existentes.  

---

## 4. Servicios que requieren desarrollo o partners

- **Control de inventario / bodega**  
  - No hay producto listo. Opciones: módulo en Sheets (entradas/salidas) como proyecto acotado, o derivar a Gestión Zen si en el futuro hubiera módulo de inventarios.  

- **Reemplazo total de contador**  
  - QAI no es estudio contable. Podemos dejar la casa ordenada (datos, procesos, reportes) y recomendar contador externo para cierre oficial y declaraciones.  

- **Representación legal en demandas o fiscalización**  
  - Lex asesora y documenta; la representación ante tribunales o SII corresponde a abogado o contador titular.  

---

## 5. Enfoque recomendado (fases y quick wins)

1. **Quick win (Fase 0)**  
   - **Diagnóstico conjunto**: 1 sesión (o 2) con Lina: mapear todos los “Excels” y fuentes de verdad actuales, deuda con Enrique, estado real de contrataciones y de contador anterior.  
   - Entregable: documento “Estado actual y gaps” + propuesta de servicios por fases.  

2. **Fase 1 – Visibilidad financiera**  
   - Implementar Sistema Financiero mínimo (Registro Diario + Runway + P&L en Sheets).  
   - Migrar/estructurar lo que hoy está en “El robo 123” y definir reglas de clasificación.  
   - Objetivo: que Lina vea números reales y pueda tomar decisiones sin depender solo de Enrique.  

3. **Fase 2 – Compliance y donaciones**  
   - Ordenar contabilidad para cumplir requisitos legales/tributarios de la fundación.  
   - Ruta hacia emisión de certificados de donación (Lex + Finn).  

4. **Fase 3 – Riesgo laboral**  
   - Diagnóstico laboral (Lex) y plan de regularización priorizado, para reducir riesgo de nuevas demandas.  

5. **Opcional – Inventario**  
   - Si hay presupuesto y prioridad: diseño de control mínimo de bodega (entradas/salidas) en Sheets o herramienta simple.  

---

## 6. Límites y riesgos (transparencia con el cliente)

- **No somos contador ni reemplazo de abogado**: Ofrecemos ordenamiento, procesos, reportes y asesoría; las declaraciones formales y la representación legal siguen en manos de profesionales titulados.  
- **Deuda laboral (Enrique)**: No la resolvemos nosotros; sí podemos ayudar a que el resto de la operación sea más barata y clara para cuando pueda pagar el finiquito.  
- **Historial perdido**: Si no hay registros, no podemos “reconstruir” años atrás de forma confiable; el punto de partida es “desde ahora, bien hecho”.  

---

## 7. Alineación con Manifiesto QAI

- **Motor B (Misión)**: Democratizar IA y orden para organizaciones que no tienen acceso a estructura de clase mundial. Una fundación de 8 años sin control financiero encaja en este perfil.  
- **Human-in-the-loop**: Lina sigue tomando decisiones; QAI aporta datos, procesos y recomendaciones, no sustituye su criterio.  
- **Bisagra**: Unimos conocimiento de dominio (fundaciones, laboral, tributario) con herramientas (Sheets, playbooks, Lex/Finn) para resultados prácticos.  

---

## 8. Estimación de costos y opciones de cobro

*Referencia interna: FedEx piloto $990k neto; tarifas genéricas QAI consultoría ~$65k/h, desarrollo/setup ~$45k/h.*

### 8.1 Coste de referencia por fases (precio “mercado”)

| Fase | Alcance | Horas est. | Precio ref. (neto CLP) |
|:-----|:--------|-----------:|------------------------:|
| **Fase 0** | Diagnóstico (1–2 sesiones + informe + propuesta por fases) | 8–12 h | $400.000 – $500.000 |
| **Fase 1** | Sistema Financiero (Sheets + playbooks + migración “El robo 123”) | 25–35 h | $1.200.000 – $1.500.000 |
| **Fase 2** | Ruta compliance + certificados donación (Lex + Finn) | 15–22 h | $900.000 – $1.100.000 |
| **Fase 3** | Diagnóstico laboral + plan regularización (Lex) | 10–14 h | $550.000 – $700.000 |
| **Total proyecto (4 fases)** | | ~60–80 h | **$3.050.000 – $3.800.000** |

*Si suma inventario (bodega): +$400.000 – $600.000 según alcance.*

### 8.2 Precio “impacto” (fundación en crisis)

- Aplicar **~20–25% descuento** sobre el rango anterior, explícito como “precio impacto para organizaciones sociales”.
- **Total proyecto (4 fases) con descuento**: **$2.400.000 – $2.900.000** neto.
- **Fase 0 + Fase 1** (lo que más alivia ya): **$1.280.000 – $1.600.000** neto con descuento (~$1.400.000 como punto medio).

**Límite para no perder**: No bajar el paquete Fase 0 + Fase 1 por debajo de **~$1.100.000 – $1.200.000** neto (equivale a ~25–28 h a tarifa impacto). Por debajo de eso el margen es demasiado bajo para el valor entregado.

### 8.3 Formas de cobro que no ahoguen a Lina

1. **Pago por hitos (recomendado)**  
   - Cobrar al cierre de cada fase, no todo por adelantado.  
   - Ejemplo: Fase 0 → pago al entregar informe; Fase 1 → 50% al kickoff, 50% al entregar Sistema Financiero operativo.  

2. **Cuotas mensuales sin interés**  
   - Para Fase 1 (ej. $1.400.000): 3–4 cuotas de **$350.000 – $470.000**/mes.  
   - Condición: fechas fijas (ej. día 5 de cada mes); si se atrasa más de 15 días, suspender trabajo hasta regularizar (no embargar, solo pausar).  

3. **Fase 0 como compromiso bajo**  
   - Cobrar Fase 0 **$300.000 – $350.000** (por debajo de referencia).  
   - Si sigue con Fase 1, **descontar ese monto del total de Fase 1** (así el diagnóstico “no se pierde” para ella).  

4. **No cobrar todo el proyecto por adelantado**  
   - Evitar pedir 3M de una sola vez. Repartir en 4–6 meses según hitos o cuotas.  

5. **Opcional: pago en 2 partes en Fase 1**  
   - 40% al inicio (para compromiso y arranque).  
   - 60% a la entrega (Sistema Financiero en Sheets + playbooks + capacitación breve).  

### 8.4 Ejemplo de propuesta económica (para Lina)

**Opción A – Solo diagnóstico y visibilidad (recomendado para empezar)**  
- **Fase 0** (diagnóstico + informe + propuesta): **$350.000** neto (único).  
- **Fase 1** (Sistema Financiero mínimo): **$1.350.000** neto.  
  - Forma de pago: 40% ($540.000) al inicio; 60% ($810.000) a la entrega.  
  - O: 4 cuotas de **$337.500** (mes 1 a 4).  
- **Total Fase 0 + 1**: **$1.700.000** neto (+ IVA si aplica).  
- Si pagó Fase 0 y sigue con Fase 1: total **$1.700.000** (el $350k de Fase 0 ya contabilizado; no sumar de nuevo).

**Opción B – Proyecto completo (4 fases)**  
- **Total con precio impacto**: **$2.600.000** neto.  
- Forma de pago: por hitos (Fase 0: $350k | Fase 1: $1.050k | Fase 2: $750k | Fase 3: $450k).  
- Cada hito se cobra al entregar; no exige tener todo el efectivo al inicio.

**Resumen**: Cobrar por fases y/o en cuotas permite que no se ahogue; el precio impacto nos mantiene en margen razonable sin regalar el trabajo. El piso para no perder está en no bajar Fase 0+1 por debajo de ~$1.100.000–1.200.000 neto.

---

**Próximo paso sugerido**: Redactar propuesta comercial (deck + PDF) con alcance Fase 0 + Fase 1, precios y formas de pago anteriores, y opciones Fase 2 y 3, para enviar a Lina. Si Alejandro confirma, se puede generar con el Sistema de Propuestas y guardar en `clientes/CicloRecreaVia/` cuando se formalice la carpeta del cliente.
