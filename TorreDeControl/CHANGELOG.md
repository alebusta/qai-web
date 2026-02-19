# CHANGELOG - Bitácora de Decisiones Importantes

> Registro histórico de hitos, cambios de rumbo y decisiones estratégicas.

---

## 2026

### Febrero

#### [19-Feb-2026] - Hardening de Infraestructura & Primacía Corporativa (Nzero)
**Tipo**: Infraestructura / Protocolo / Arquitectura

**Contexto**: Se detectaron riesgos de duplicación de correos tras reinicios de sesión y desorden en la jerarquía de protocolos debido a la coexistencia de experimentos y normas corporativas.

**Decisión/Acción**:
- [QAICORE] **Idempotencia Local Gmail**: Implementación de `sent_registry.json` en `.qai/gmail/`. Las herramientas ahora verifican localmente antes de consultar la API, brindando protección instantánea y persistente.
- [QAICORE] **Consolidación de Memoria**: Auditoría y migración de ADRs traspapelados (ADR-018). Sincronización del Índice Maestro de Knowledge Base (44 archivos).
- [ARQUITECTURA] **ADR-019 (Primacía Corporativa)**: Establecida jerarquía suprema de la Torre de Control sobre experimentos en `QaiLabs`.
- [PROTOCOL] **Experimental Zone Notice**: Desplegado aviso preventivo en `QaiLabs/EXPERIMENTAL_ZONE_NOTICE.md` para evitar que los agentes adopten reglas locales de prototipos como normas globales.
- [INFRA] **Saneamiento Landing Zone**: Eliminación de carpetas temporales fuera de lugar y centralización de archivos operativos en la Landing Zone oficial.

**Impacto**: Sistema blindado contra fallos de red y errores de contexto. La memoria institucional es coherente y los agentes tienen guardrails claros para no confundir prototipos con la empresa.

---

#### [19-Feb-2026] - Indexación de Comprobantes y Flujos de Recuperación (Finn)
**Tipo**: Operativo / Finanzas / Memoria Institucional

**Contexto**: Se requería un diseño que facilitara la recuperación de información ("¿dónde está la factura de X del mes Y?") y que los flujos de nueva factura en landing zone y de detalle de gastos con link al comprobante quedaran explícitos y operativos.

**Decisión/Acción**:
- [FINANZAS] **INDICE_COMPROBANTES.md**: Índice único por período y proveedor con link a Drive; búsqueda por Ctrl+F. Tabla poblada con ene/feb 2026.
- [FINANZAS] **DISENO_RESPALDO_E_INDEXACION.md**: Estructura 01…05 por mes, reglas de ubicación, flujo al agregar comprobante, IDs de carpetas Drive, mantenimiento.
- [PROTOCOLO] **Landing Zone obligatoria**: Borradores y archivos operativos de Finn deben crearse solo en `/TorreDeControl/temp_files/` (profile, system_prompt, f29_template).
- [FINANZAS] **Flujos documentados**: "Nueva factura en landing zone" (leer → subir Drive → registrar sheet → índice → limpiar) y "Gastos mes X + ver comprobante" (listar desde sheet, link desde columna Comprobante o índice).
- [FINANZAS] **Cursor enero**: PDF movido a 04-Operaciones_Extranjeras_Doc46 vía `gdrive.py --move`; link en Registro_Diario (columna Comprobante); índice actualizado.
- [QAICORE] **gdrive.py**: Añadidos `move_file()` y CLI `--move` / `--to-folder` para mover archivos entre carpetas en Drive.
- [TRIBUTARIO] **Doc. 46 retroactivo**: Documentado en playbook emitir_doc46_extranjero que se pueden emitir Facturas de Compra por meses ya pagados; el crédito va al F29 del mes de emisión.
- [MEMORIA] **CONTROL_DIGITAL**: Sección "Recuperación de información" (comprobantes → índice; movimientos → Registro_Diario). Playbook registrar_gasto_ingreso: paso explícito para link + fila en índice.

**Impacto**: Recuperación de comprobantes en segundos (humano o agente). Flujos 1 y 2 operativos y documentados. PCA (ADR-010) cumplido al cierre de sesión.

---

#### [17-Feb-2026] - Optimización Masiva de Rendimiento QaiCore y Mantenimiento HQ
**Tipo**: Infraestructura / Operativo

**Contexto**: Se detectaron problemas de latencia crítica en las APIs de Google y errores de codificación/escape en el Inbox y herramientas de terminal durante el procesamiento contable real.

**Decisión/Acción**:
- [INFRA] **Caché de Discovery APIs**: Implementado sistema de caché local en `.qai/google_discovery/` para Sheets v4, Gmail v1 y Drive v3. Reducción de tiempo de warm-up de ~30s a <1s.
- [INFRA] **Lazy Imports Optimization**: Refactorizado `QaiCore/tools/__init__.py` para postergar la carga de dependencias pesadas (`openpyxl`, `google-api-python-client`), eliminando deadlocks y acelerando el arranque de scripts ligeros (como el de emails).
- [OPERATIVO] **Robustez PowerShell**: Habilitado soporte para `--data-file` en `gsheets.py` para evitar fallos de escape con caracteres especiales (paréntesis) en la línea de comandos de Windows.
- [MEMORIA] **Saneamiento INBOX**: Reparado archivo `INBOX.md` de errores de codificación UTF-8 (Mojibake fix) y reorganización táctica de prioridades.
- [PERFIL] **Finn v1.4**: Actualización del perfil del agente financiero para incorporar estas mejoras de rendimiento y protocolos de robustez.

**Impacto**: El Digital HQ alcanza su mayor nivel de fluidez técnica hasta la fecha. Operaciones que antes tomaban cerca de un minuto por las latencias de red ahora son virtualmente instantáneas.

#### [17-Feb-2026] - Automatización de Procesamiento Contable de Landing Zone (Finn)

**Tipo**: Procesamiento Operativo / Finanzas

**Contexto**: Se procesaron los primeros documentos reales depositados por el Founder en la Landing Zone (`TorreDeControl/temp_files/`) siguiendo el protocolo de procesamiento automático de Finn.

**Decisión/Acción**:
- [FINANZAS] **Extracción y Conciliación**: Procesada factura Cursor Pro ($20 USD) y cartola bancaria Feb 2026.
- [INFRA] **GDrive Automation**: Los archivos fueron clasificados y subidos automáticamente a las carpetas correspondientes (`04-Operaciones_Extranjeras_Doc46` y `05-Bancos_Cartolas_y_Pagos`).
- [FINANZAS] **Runway Master**: Registro de 4 movimientos pendientes (Cursor, Github, Google, Namecheap) en el SSOT financiero (`QAI_Finanzas_2026`).
- [PROTOCOLO] **Zero Inbox**: Limpieza total de la Landing Zone tras el procesamiento.
- [PERFORMANCE] Identificación de cuellos de botella en el parsing de CLI (PowerShell) y latencia de inicialización de APIs de Google, documentados en INBOX para revisión de Nzero.

**Impacto**: Consolidación total de la contabilidad de Febrero hasta la fecha. El Founder recibe un resumen formal por email y el HQ queda sincronizado con el banco.

#### [16-Feb-2026] - Hardening Anti-Duplicados en Envíos Email (Finn)
**Tipo**: Infraestructura / Protocolo Operativo

**Contexto**: En una sesión operativa se detectaron reintentos de envío de correo por latencia/ambigüedad de estado en terminal, lo que provocó duplicados al enviar borradores a revisión.

**Decisión/Acción**:
- [QAICORE] `gmail.py` incorpora guardrail de deduplicación por defecto en `send` (destinatario + asunto + ventana temporal).
- [QAICORE] Se agrega bypass explícito `--allow-duplicate` para casos excepcionales con intención confirmada.
- [PROTOCOLO] Refuerzo en `finn/system_prompt.md`: usar `draft` cuando el usuario pide visualizar, y limitar reintentos ante estados ambiguos.
- [PLAYBOOK] `process_financial_inbox.md` incorpora guardrail de reintentos y prohibición de filas `TEST/DEBUG` en SSOT financiero.

**Impacto**: Reducción drástica del riesgo de envíos duplicados y de loops de reintento. Mayor seguridad operativa en sesiones con latencia alta.

#### [16-Feb-2026] - Optimización de Infraestructura QaiCore (Google API Local Discovery)
**Tipo**: Infraestructura / Rendimiento

**Contexto**: Se detectaron cuellos de botella críticos (hangs) al inicializar los servicios de Google Sheets y Gmail. La causa era la latencia en la descarga dinámica de los "discovery documents" vía red.

**Decisión/Acción**:
- [QAICORE] **Bypass de Red**: Refactorización de `gsheets.py` y `gmail.py` para utilizar `build_from_document` con archivos JSON locales.
- [QAICORE] **Inmunidad SSL/DNS**: Las herramientas financieras ahora operan de forma instantánea al no depender de handshakes externos para su construcción.

**Impacto**: Reducción del tiempo de respuesta de las herramientas de ~30s a <1s. Eliminación de fallos por timeout en entornos con redes restrictivas or inestables.

#### [16-Feb-2026] - Formalización de Rol Comercial Institucional (Iliana CGO)
**Tipo**: Gobierno Corporativo / Comercial

**Contexto**: Se requería estandarizar el título institucional de Iliana para firma y representación comercial en propuestas, prospección y dirección de equipos/agentes de crecimiento.

**Decisión/Acción**:
- [GOBIERNO] Se formaliza el uso de título: **Co-Founder & Chief Growth Officer (CGO)**.
- [COMERCIAL] Se alinea su uso para contexto de ventas, búsqueda de clientes, alianzas y liderazgo de growth.
- [MEMORIA] Actualización de `STATUS.md` para dejar el rol visible en la memoria operativa.

**Impacto**: Claridad de representación externa e interna en funciones comerciales. Se evita inconsistencia de cargos en documentos y comunicaciones.

#### [15-Feb-2026] - Refinamiento Arquitectural Web V3 ("The Hinge")
**Tipo**: Identidad / Producto

**Contexto**: Se completó el rediseño y refinamiento de la versión 3 de la web corporativa, estableciendo la base para futuras iteraciones de la identidad digital "Anti-Hype".

**Decisión/Acción**:
- [WEB] **Rediseño de Casos**: Implementación de tarjetas compactas con modales de baja fricción para una lectura más enfocada.
- [WEB] **Filosofía "Bisagra"**: Reestructuración del manifiesto para centrar la identidad de QAI como el conector entre dominio y tecnología.
- [WEB] **Cierre Premium**: Sustitución del CTA invasivo por un footer elegante y sobrio.
- [MEMORIA] **Checkpoint de Evolución**: Creación de archivo de histórico y preservación de insumos en `AREA_51/proyectos/web_evolution_2026/`.

**Impacto**: La identidad digital de QAI ahora refleja coherencia con su discurso: eficiencia, honestidad técnica y reducción de fricción. La V3 queda certificada como base de operación.

#### [11-Feb-2026] - Certificación Bot Telegram Nzero (Fase 1.5)
**Tipo**: Infraestructura / Producto (Experimental)

**Contexto**: Se completó la "Misión de Salida" para convertir el Bot de Telegram de un simple webhook a un agente inteligente (Nzero) capaz de gestionar la operativa diaria del HQ desde el móvil.

**Decisión/Acción**:
- [INFRA] **Deploy GCP**: Estabilización del pipeline de despliegue mediante `gcloud functions deploy` con variables de entorno robustas (`env.yaml`).
- [BOT] **Personalidad Nzero**: Implementación de la identidad conversacional de Nzero (CTO/COO style) y enrutador NLP.
- [BOT] **Gestión INBOX Fuzzy**: Implementación de algoritmo de búsqueda parcial para tareas, permitiendo marcar como hechas tareas con descripciones aproximadas.
- [BOT] **Comandos de Datos**: Acceso directo a RUT, Banco y datos corporativos mediante lenguaje natural.
- [BUGFIX] **Estabilización de Código**: Corrección de bug crítico de importación (`datetime`) y optimización de logging de errores de GitHub API (403 Forbidden resolution).

**Impacto**: El Founder ahora puede operar el HQ (agregar tareas, consultar datos, marcar hitos) 100% desde Telegram con un agente que entiende el contexto. El HQ se vuelve móvil y "siempre activo".

#### [09-10-Feb-2026] - Operativización Sistema de Libros Corporativos Digitales
**Tipo**: Legal / Infraestructura

**Contexto**: Tras la firma del Acta N°1, se ejecutó el protocolo completo de puesta en marcha del sistema de libros corporativos digitales bajo la Ley 19.799, estableciendo la base legal y operativa para la gestión corporativa 100% digital de The QAI Company SpA.

**Decisión/Acción**:
- [LEGAL] **Registro de Accionistas RES**: Apertura oficial del libro electrónico (09-Feb). Composición 50/50 registrada. CVE: RA1UcsKaOvrD, N° Atención: 10294717.
- [LEGAL] **Repositorio Digital**: Estructura completa de carpetas `/actas/` y `/registros_oficiales/` con índices correlativos.
- [LEGAL] **Checklist Operativo**: Protocolo estandarizado para emisión de futuras actas (numeración, firma, custodia, respaldo).
- [INFRAESTRUCTURA] **Respaldo Google Drive**: Carpetas "Actas" y "Registros Oficiales" creadas bajo carpeta Legales. PDFs respaldados y config actualizada.
- [DOCUMENTACIÓN] **README 04_LEGAL**: Actualizado con estructura completa, links a Drive, instrucciones paso a paso.

**Impacto**: The QAI Company tiene ahora un sistema de libros corporativos legalmente válido, auditablemente impecable y operativamente simple. Próxima acta será N°02. Base legal sólida para operación de SpA.

#### [07-Feb-2026] - Cierre Legal: Acta N°1 + Seguimientos
**Tipo**: Legal / Operativo

**Contexto**: Se cerro el Acta N°1 de libros digitales y se estandarizo el template para futuras actas, manteniendo la compatibilidad del motor PDF con otros documentos.

**Decision/Accion**:
- [LEGAL] **Acta N°1**: PDF final generado y formateo calibrado (folio, portada, firmas, jerarquia). Pendiente firma simple y subida a Drive.
- [LEGAL] **Template Actas**: Nuevo template en Empresa/04_LEGAL/actas/ACTA_TEMPLATE.md.
- [QAICORE] **md_to_pdf (modo ACTA)**: Ajustes acotados solo a actas (margenes, salto de firmas, bullets estrictos).
- [LEGAL] **NDA FedEx**: NDA completado con datos legales de QAI.
- [LEGAL] **Patente Providencia**: Seguimiento enviado para Solicitud #1126-2026 (respuesta pendiente).

**Impacto**: Actas futuras quedan estandarizadas y el paquete legal queda listo para firma y archivo en Drive.

### Enero

#### [06-Feb-2026] - Refuerzo de Memoria Institucional (Nzero)
- **Falla detectada**: Omisión de actualización de `INBOX.md` y `AGENT_ACTIVITY.md` durante un protocolo de cierre de hito (FedEx v3).
- **Corrección**: Rediseño de la "Regla de Oro de los 4 Puntos" en `TorreDeControl/README.md`.
- **Nuevo Guardrail**: Bloqueo instruccional explícito: "Si no has actualizado el INBOX y la Actividad, NO tienes permiso para despedirte".
- **Aprendizaje**: La atomicidad de registros es la base de la confianza en agentes autónomos.

#### [03-Feb-2026] - Certificación Email Bulletproof v1.5
**Tipo**: Infraestructura QaiCore / Operativo / Marca

**Contexto**: Se realizó una prueba de estrés ("EcoPort Stress Test") para validar la modularidad del sistema de propuestas y el canal de despacho por email. Se detectaron y corrigieron fallos de visualización de logos y tipografías en clientes de correo (Gmail/Hotmail).

**Decisión/Acción**:
- [QAICORE] **Email Engine v1.2**: Implementación de la librería `markdown` para renderizado real y estructura `multipart/related` para incrustar el logo (`cid:logo_qai`) sin que Gmail lo marque como adjunto.
- [QAICORE] **Cross-Origin Preview**: Ajuste de `gmail_preview.py` para inyectar recursos desde `localhost:8585` eludiendo bloqueos del protocolo `file://` en navegadores.
- [IDENTIDAD] **Maestros Sanitizados**: Limpieza de los templates HTML maestros, reemplazando datos de clientes antiguos por placeholders técnicos `{{CLIENT_NAME}}`.
- [MEMORIA] **ADR-016**: Registro oficial de la arquitectura de despacho por correo de alta fidelidad.

**Impacto**: El workflow comercial de QAI es ahora agnóstico al cliente, técnicamente robusto y garantiza el 100% de consistencia visual en todas las bandejas de entrada. Certificado bajo prueba real con dirección Hotmail/Gmail.

#### 23-Ene: Blindaje de Entregables Premium (Executive Horizon)
**Tipo**: Infraestructura QaiCore / Identidad de Marca

**Contexto**: Tras una pérdida accidental de archivos por una limpieza excesiva, se reconstruyó el motor de renderizado y el diseño comercial, elevándolo a estándar institucional para evitar futuras regresiones de calidad.

**Decisión/Acción**:
- [QAICORE] **Golden Motor**: Implementación de `generate_all_pdfs.py` (Playwright) que fuerza dimensiones 16:9 Cinema y A4 asimétrico, sincronizando fuentes (`document.fonts.ready`).
- [BRAND] **Executive Horizon**: Formalización del estilo visual (Azul `#1976D2`) y creación de templates maestros en `Empresa/02_COMERCIAL/templates/executive_horizon/`.
- [MEMORIA] **ADR-015**: Documentación de la arquitectura de generación de alta fidelidad y el protocolo de protección `MASTER_DESIGN`.
- [WORKFLOW] **Generar Propuesta Premium**: Creación de un flujo agentic formalizado en `.agent/workflows/` para blindar la continuidad ante limpiezas.

**Impacto**: Recuperación total de la calidad premium para CIAL. QAI cuenta ahora con una "imprenta digital" infalible y una identidad visual inalterable por agentes.

#### 23-Ene: Capacidad de Envío Programado de Email (Windows Bridge)
**Tipo**: Infraestructura QaiCore / Operativo

**Contexto**: Se requería la capacidad de agendar envíos de correo sin una infraestructura de servidor 24/7. Se validó exitosamente mediante una prueba real a las 11:20 AM.

**Decisión/Acción**:
- [QAICORE] **Windows Bridge**: Implementación de un flujo que utiliza el **Programador de Tareas de Windows** (`schtasks`) para invocar la herramienta `gmail.py` en el futuro.
- [QAICORE] **Script Auxiliar**: Creación de un `.bat` en `temp_files/` para estandarizar la ejecución y evitar errores de ruta en el scheduler.
- [MEMORIA] **ADR-014**: Documentación de la decisión técnica, alternativas y trade-offs (dependencia del host encendido).

**Impacto**: Los no-gentes de QAI ya pueden "viajar en el tiempo" para entregar comunicaciones, permitiendo una gestión de correos más profesional y menos inmediata.

#### 22-Ene: Entrega Final CIAL Alimentos y Memoria Institucional
**Tipo**: Comercial / Operativo

**Contexto**: Se realizó la entrega formal de la propuesta de Vigilancia Tecnológica a Iliana Alzurutt. Se requería una versión impecable de los documentos (PDF sin cortes) y un proceso de envío profesional.

**Decisión/Acción**:
- [COMERCIAL] **Entrega Formal**: Envío de email corporativo (Gmail API) con link al **Intelligence Hub (Mockup Vivo)** y adjuntos PDF (Propuesta + Deck).
- [OPERATIVO] **Generación de PDF High-Fidelity**: Implementación de un flujo vía Playwright (`generate_pdfs.js`) para garantizar renderizado exacto A4/Landscape sin cortes de tablas.
- [MEMORIA] **Protocolo Documentado**: Creación de `CIAL/PROCESO_GENERACION_PROPUESTA.md` como estándar institucional para futuras propuestas.
- [HIGIENE] **Zero Inbox Landing Zone**: Migración de insumos a `CIAL/insumos/` y limpieza total de archivos temporales en Torre de Control.

**Impacto**: CIAL cuenta con un paquete de entrega de nivel corporativo. QAI tiene ahora un proceso documentado y herramientas validadas para escalar ventas de servicios complejos.

#### 21-Ene: Sistema de Propuestas (Deck + PDF) institucionalizado
**Tipo**: Comercial / Infraestructura QaiCore

**Contexto**: Se necesitaba un workflow repetible y de calidad alta para generar propuestas con identidad QAI, soportando entrega por cliente en formato PDF, deck, ambos, y dejando preparado el camino para un “mockup vivo” (demo web).

**Decisión/Acción**:
- [COMERCIAL] **Workflow documentado (SSOT)** con inputs/outputs/modos de entrega y comandos CLI en `Empresa/02_COMERCIAL/templates/PROPOSAL_SYSTEM.md`.
- [QAICORE] **Renderer de deck**: Markdown (slides `---`) → HTML branded (preview) vía `tools.deck_html`.
- [QAICORE] **Renderer de propuesta PDF**: Markdown → HTML/CSS → PDF (Playwright) vía `tools.proposal_pdf`.
- [QAICORE] **Preview email (HITL)** reforzado vía `tools.gmail_preview` (independiente de Gmail auth).
- [BRAND] **Logo transparente** agregado para evitar “caja blanca” sobre fondos no blancos: `Empresa/01_ESTRATEGIA/IDENTIDAD_VISUAL/logoQAI_transparent.png` (fallback al logo original). Documentado en el Brand Kit.
- [DECK] **Componente de flujo** mejorado a infografía (`.flow`) para slides de proceso.
- [CONTROL] Issues pendientes anotados en `TorreDeControl/INBOX.md` (estructura estándar de contenido, orquestador por “evento”, agente dedicado, mockup vivo).

**Impacto**: Propuestas reproducibles, consistentes y fáciles de iterar estéticamente sin romper el proceso. Previews centralizados en `TorreDeControl/temp_files/` y entregables almacenados en carpeta del cliente.

#### 20-Ene: Patente Municipal y Protocolo de Libros Digitales
**Tipo**: Hito Legal / Operativo

**Contexto**: Se procesó la notificación de la Municipalidad de Providencia para la patente comercial y se investigó la viabilidad de prescindir de libros corporativos físicos en favor de una gestión 100% digital bajo la Ley 19.799.

**Decisión/Acción**:
- [LEGAL] **Archivo de Patente**: Procesado comprobante de solicitud #1126 de Providencia. Archivado en Drive bajo `Documentos Legales/Patente Comercial/`.
- [LEGAL] **Libros Digitales**: Investigación y formalización del **Protocolo de Libros Corporativos Electrónicos**. Se decidió no comprar libros físicos ni timbrar folios en notaría.
- [LEGAL] **Sustento Normativo**: Creación de `PROTOCOLO_LIBROS_DIGITALES.md` amparado en la Ley 19.799 (equivalencia de soporte y validez de FEA).
- [INFRA] **Reset de Token**: Se forzó la renovación del token de Gmail para asegurar acceso continuo de los agentes al inbox corporativo.

**Impacto**: Reducción de burocracia física. The QAI Company operará con libros corporativos inmateriales blindados por firma FEA. Seguimiento de patente centralizado con plazos de respuesta claros (10 días evaluación).

---

#### 20-Ene: Formalización de Domicilio y Herramientas PDF
**Tipo**: Decisión Técnica y Administrativa

**Contexto**: Se requería unificar la documentación que autoriza el uso de la oficina en Bucarest 17 para cumplimiento tributario y legal. Paralelamente, se detectó la falta de utilidades para manipulación de documentos PDF en el HQ.

**Decisión/Acción**:
- [ADMIN] **Unificación de Domicilio**: Fusión de Autorización de Domicilio y Poder de Representación en un solo archivo maestro: `Autorizacion_y_Poder_Bucarest_17.pdf`.
- [LEGAL] **Estandarización de Poderes**: Creación del índice `_index_poderes.md` para tracking de autorizaciones y poderes notariales en Drive.
- [QAICORE] **CLI Upgrade (gdrive.py)**: Mejora de la herramienta corporativa para permitir la creación de carpetas directamente desde la terminal (`--create-folder`).
- [QAICORE] **Utilidades PDF**: Implementación de `pdf_utils.py` para permitir a los agentes realizar fusiones (merge) de documentos de forma autónoma.

**Impacto**: Memoria institucional blindada con el respaldo del domicilio oficial. Aumento de la autonomía de los agentes para gestionar documentos complejos sin intervención manual del usuario.

---

#### 15-Ene: Optimización de Infraestructura QaiCore (Latencia & UX Agente)
**Tipo**: Mejora Técnica / UX Agente

**Contexto**: Se identificaron tiempos de espera excesivos (latencia de inicialización) en la herramienta `gdrive.py`, lo que provocaba falsos positivos de "timeout" y abortos preventivos por parte de los agentes (Finn). El script cargaba pesadamente el cliente de Google API y realizaba handshakes SSL incluso para tareas simples como `--help` o `--show-folders`.

**Decisión/Acción**:
- [QAICORE] **Implementación de Lazy Loading**: El servicio de Google Drive ya no se inicializa en el constructor (`__init__`), sino al primer uso real (`@property service`).
- [QAICORE] **Feedback Visual (stderr)**: Se agregaron mensajes de progreso (`[-]`, `[+]`) a la salida de error estándar para que el agente vea actividad durante la fase de handshake y no asuma que el proceso se colgó.
- [FINN] **Actualización de Protocolo de Espera**: Se ajustó el `system_prompt.md` de Finn para esperar hasta 30s si hay actividad en stderr, evitando re-intentos innecesarios.
- [QAICORE] **CLI Fast-Path**: Refactorización del entry point para que el parsing de argumentos sea instantáneo.

**Impacto**: Reducción del 60% en el tiempo de carga para comandos de configuración. Mejora drástica en la fiabilidad de las operaciones de subida/bajada de documentos financieros. Eliminación de la fricción "Digital HQ vs Agente".

---

#### 04-Ene: Módulo de Egresos Completado - Gestión Zen
**Tipo**: Hito Técnico / Producto

**Contexto**: Tras la reunión con socios del 22-Dic-2025, se identificó como requisito crítico implementar un sistema completo de gestión de pagos que cerrara el ciclo desde "Gasto Registrado" hasta "Proveedor Cobró". El problema principal era la falta de trazabilidad en los pagos (cheques perdidos, documentos sin firmar, no saber quién tiene qué).

**Decisión/Acción**:
- [GESTION-ZEN] **Arquitectura de Datos**: Implementación de 3 tablas en Supabase:
  - `expense_disbursements`: Tabla principal de egresos
  - `expense_disbursement_history`: Auditoría completa de cambios de estado
  - `expense_disbursement_signers`: Registro de firmantes y aprobaciones
- [GESTION-ZEN] **Seguridad**: Políticas RLS (Row Level Security) y triggers automáticos para numeración correlativa
- [GESTION-ZEN] **API**: Servicio completo `disbursementsAPI` con patrón "Manual Join" para garantizar visibilidad de datos
- [GESTION-ZEN] **Flujo de Estados**: Implementación de máquina de estados (En Tránsito → Firmado → Pagado)
- [GESTION-ZEN] **Frontend**: Módulo completo con componentes:
  - `DisbursementList`: Tabla interactiva con filtros
  - `DisbursementDetail`: Panel lateral (Drawer) para gestión
  - `DisbursementModal`: Formulario crear/editar
  - `DisbursementStatusBadge`: Componente visual de estados
- [GESTION-ZEN] **UX**: Sistema de tabs para alternar entre Gastos y Egresos, semáforo visual de estados (🟡 En Tránsito, 🔵 Firmado, 🟢 Pagado)
- [GESTION-ZEN] **Features Avanzadas**:
  - Generación de PDF con comprobantes profesionales
  - Exportación a Excel/CSV
  - Timeline de auditoría visual
  - Resumen financiero inteligente (tarjetas de estadísticas)
- [GESTION-ZEN] **Documentación**: Manual técnico en `docs/MANUAL_EGRESOS.md`

**Impacto**: Cierre del ciclo completo de pagos con trazabilidad total. Los administradores ahora pueden saber en tiempo real el estado de cada pago, quién tiene el documento, quién firmó, y cuándo se pagó. Eliminación del riesgo de pagos duplicados o documentos perdidos. Producto listo para validación con socios.

---

#### 05-Ene: Incorporación de Guía Tributaria y Deuda Simple
**Tipo**: Hito de Conocimiento / Estrategia Financiera Pragmática

**Contexto**: Artículo de Emol (Portal PYME) advierte sobre riesgos tributarios graves en PYMEs por mezclar gastos personales con empresariales. Se evaluó formalizar mediante Cuenta Corriente Mercantil (CCM) vs Deuda Simple.

**Decisión/Acción**:
- [FINN] Creación de `SEPARACION_PATRIMONIOS_PYME.md` en `/Empresa/03_ADMINISTRACION_FINANZAS/tributario/`.
- [FINN] **Estrategia Definida**: Para montos bajos (<$1M) y corto plazo, se opta por **"Deuda con Socio Simple"** (sin contrato, respaldo contable + transferencias) en lugar de estructuras complejas (CCM o Mutuos).
- [FINN] Validación Legal: Al ser mutuo consensual sin documento de crédito, no gatilla Impuesto de Timbres (Art. 1 N°3 DL 3475).
- [FINN] Actualización de Plan de Cuentas: `21.01 Deuda con Socio` en `MANUAL_TRIBUTARIO_Y_OPERATIVO.md`.

**Impacto**: Protocolo ultra-eficiente implementado. Se asegura cumplimiento tributario sin burocracia innecesaria. "La billetera de la empresa NO es la billetera del dueño", pero el mecanismo de financiamiento es ágil.


---

## 2025

### Diciembre

#### 20-Ene: Propuesta VT CIAL y herramienta md_to_pdf
**Tipo**: Comercial / Infraestructura QaiCore

**Contexto**: Se preparó propuesta de vigilancia tecnológica para CIAL Alimentos con enfoque en sistema vivo (dashboard, alertas, fichas) y pricing 20% bajo la oferta competidora (IALE). Se necesitaba capacidad propia para emitir PDFs desde Markdown para los no-gentes.

**Decisión/Acción**:
- [COMERCIAL] Propuesta lista (one-pager + deck + comparativa) y PDF generado: [propuesta_vt_cial.pdf](file:///c:/Users/abustamante/TheQaiCo/Empresa/02_COMERCIAL/clientes/CIAL/propuesta_vt_cial/propuesta_vt_cial.pdf).
- [QAICORE] Nueva utilidad `md_to_pdf` expuesta en `QaiCore.tools` para convertir Markdown a PDF (usa fpdf2, bullets ASCII) habilitando a los agentes a emitir PDFs sin depender de terceros.
- [DOCS] Archivo combinador para exportar: [for_pdf.md](file:///c:/Users/abustamante/TheQaiCo/Empresa/02_COMERCIAL/clientes/CIAL/propuesta_vt_cial/for_pdf.md).

**Impacto**: Propuesta lista para envío con diferenciadores claros (sistema vivo vs informe estático). Los agentes ahora pueden producir PDFs directamente desde el HQ.


#### 26-Dic: Creación de Torre de Control
**Decisión**: Implementar sistema de "memoria compartida" para agentes IA.

**Contexto**: Como solopreneur trabajando con múltiples agentes (Antigravity, Claude, etc.) en diferentes sesiones, se perdía contexto entre conversaciones.

**Solución**: Directorio `/TorreDeControl/` con:
- `STATUS.md`: Dashboard del estado actual
- `INBOX.md`: Buzón de tareas pendientes
- Protocolo para que todo agente lea/actualice estos archivos

**Impacto esperado**: Memoria persistente entre sesiones, menos tiempo explicando contexto.

---

#### 26-Dic (tarde): Infraestructura QaiCore + Temporal Awareness
**Decisión**: Implementar biblioteca compartida de herramientas para agentes IA.

**Contexto**: Los agentes necesitaban:
1. Extraer información de documentos (PDF, Word, Excel, imágenes)
2. Saber qué día es y calcular urgencias de tareas
3. Tener perfiles especializados (Legal, Financiero, etc.)

**Solución Implementada**:
- `/QaiCore/tools/`: 7 extractors de documentos + OCR con Gemini
- `/QaiCore/tools/time_utils.py`: Gestión temporal y priorización automática
- `/QaiCore/agents/lex/`: Primer agente (Legal) completo con knowledge base
- Playbooks para workflows estandarizados

**Impacto**: Agentes pueden procesar docs automáticamente, saber deadlines, y priorizar tareas.

---

#### 26-Dic (noche): Manual de Usuario y Migración de Código
**Tipo**: Hito Comercial / Cambio de Producto

**Contexto**: Preparación para la entrega del producto Invoice Matcher a FedEx y consolidación de la infraestructura de desarrollo.

**Decisión/Acción**:
- [FEDEX] Redacción y finalización del **Manual de Usuario** (`MANUAL_USUARIO.md`) con capturas de pantalla reales y flujos de validación.
- [FEDEX] Migración técnica del repositorio `invoiceMatch` a la estructura corporativa oficial en `/QaiLabs/PROTOTIPOS/`.
- [QAICORE] Implementación de **Memoria Institucional** (`DISCOVERY_LOG.md`) y actualización de protocolos de agentes.

**Impacto**: Producto listo para entrega, infraestructura de desarrollo organizada, mejora en la gestión del conocimiento interno.

---

#### 27-Dic (madrugada): Auditoría Final FedEx Invoice Matcher - 100% Completado
**Tipo**: Hito Comercial / Cierre de Proyecto

**Contexto**: Se realizó auditoría final del código contra PRD V1 Production antes de declarar el proyecto como "Beta Corporativo".

**Decisión/Acción**:
- [FEDEX] Verificación de CSV Export (US-06): ✅ `HistoryView.jsx` + `csvExport.js` operativos
- [FEDEX] Verificación de Dashboard (US-04): ✅ KPIs, gráficos, filtros funcionando
- [FEDEX] Verificación de Historial (US-05): ✅ Tabla con operaciones procesadas
- [FEDEX] Actualización de `PRD_V1_PRODUCTION.md`: Todos los user stories marcados como completados
- [FEDEX] Actualización de `STATUS.md`: Proyecto marcado como "100% LISTO - Auditoría final completada"

**Impacto**: FedEx Invoice Matcher oficialmente listo para despliegue beta. Producto pasa de prototipo a SaaS corporativo. Pendiente: entrega de manual y link a Eduardo.

---

#### 26-Dic (noche): Agente Nzero + Memoria Institucional Operativa
**Decisión**: Crear Nzero como "No-gente Cero" - agente arquitecto con knowledge_base propia.

**Contexto**: El conocimiento y decisiones de diseño se perdían entre sesiones (ej: análisis inicial de empresa, por qué elegimos X sobre Y).

**Solución Implementada**:
- `/QaiCore/agents/nzero/`: Agente arquitecto completo
- `knowledge_base/design_decisions/`: ADRs (Architecture Decision Records)
- `knowledge_base/company_analysis/`: Para evaluaciones trimestrales
- `knowledge_base/lessons_learned/`: Aprendizajes por sesión
- `knowledge_base/context_for_ai/`: Contexto de empresa para otros agentes

**ADRs Retroactivos Creados**:
- ADR-001: Torre de Control (por qué y cómo)
- ADR-002: QaiCore Structure (modular vs monolítico)
- ADR-003: Profile vs System Prompt (separación de audiencias)
- ADR-004: Criterios Graduación Labs → Prod

**Impacto**: Decisiones arquitecturales preservadas, no se pierde contexto entre sesiones.

---

#### 26-Dic: Información Bancaria Asegurada
**Hito**: Datos bancarios corporativos completos y protegidos.

**Logros**:
- Cuenta Banco Chile activa: `00-001-24253-56` (puede recibir pagos)
- RUT empresarial: `78.313.539-6`
- Email corporativo: `alebusta@qai.cl`
- Cuenta BancoEstado lista para retiro (próxima semana)
- Archivo seguro creado con `.gitignore`

**Pendiente**: Retirar cuenta BancoEstado (02-Ene) (Digipass activado el 30-Dic ✅)

---

#### 22-Dic: Reunión Socios Gestión Zen
**Evento**: Primera reunión formal con socios administradores del JV.

**Acuerdos** (pendiente procesar transcripción completa):
- Ajustes requeridos en módulo "Pagos de Egresos"
- Definir timeline para constitución NewCo
- [Agregar más detalles al procesar transcripción]

---

#### 22-Dic: Cotización Enviada a FedEx
**Hito**: Primera cotización formal como The QAI Company SpA.

**Producto**: Invoice Matcher SaaS  
**Valor**: $800.000 CLP/mes + IVA  
**Estado**: Esperando respuesta / Orden de Compra

---

#### Dic-2025: Empresa Constituida ✅
**Hito Mayor**: The QAI Company SpA legalmente operativa.

**Logros**:
- RUT obtenido
- Inicio de Actividades (SII) con giros tecnológicos
- Cuenta bancaria Banco Chile abierta
- Oficina virtual registrada
- Firma Electrónica Avanzada (FEA) activa

**Pendiente**: Autorización facturación (esperando primera OC)

---

#### 27-Dic (noche): Creación de Finn (Agente Financiero)
**Tipo**: Hito Técnico / Expansión de Agentes

**Contexto**: Tras finalizar el proyecto FedEx Invoice Matcher y establecer la estructura de Nzero, se crea el tercer agente de QAI: Finn, especializado en finanzas operativas y tributarias.

**Decisión/Acción**:
- [QACORE] Creación de `/QaiCore/agents/finn/` con estructura estándar (profile.md, system_prompt.md, knowledge_base/)
- [QACORE] Definición clara de fronteras entre Finn (finanzas) y Lex (legal) con zona de colaboración
- [QACORE] Énfasis en rol operativo: registro de gastos, P&L, balance, declaraciones SII

**Impacto**: QAI ahora tiene capacidad para gestionar finanzas operativas + compliance tributario internamente.

---

#### 27-Dic (noche): Creación de Landing Zone (temp_files)
**Tipo**: Decisión Técnica / Infraestructura

**Contexto**: Los agentes necesitan un lugar seguro y temporal para dejar archivos antes de procesarlos o moverlos a su destino final. Esto evita que los archivos se dispersen o se pierdan.

**Decisión/Acción**:
- [TORREDECONTROL] Creación de `/TorreDeControl/temp_files/` como Landing Zone oficial (Zero InBox).
- [QACORE] Actualización de `system_prompt` de agentes para usar `temp_files` como punto de entrada/salida temporal.
- [QACORE] ADR-008 documenta la decisión y el protocolo de uso.

**Impacto**: Centralización de archivos temporales, mejora la organización y reduce el riesgo de pérdida de información durante el procesamiento de agentes.

---

#### 27-Dic (noche): Google Drive API Configurado para Finn
**Tipo**: Hito Técnico / Infraestructura

**Contexto**: Finn necesita almacenar documentos financieros (fact uras, declaraciones tributarias, comprobantes) en Google Drive con acceso programático.

**Decisión/Acción**:
- [QACORE] Proyecto "QAI-Agents" creado en Google Cloud Console con OAuth2
- [QACORE] Herramienta `/QaiCore/tools/gdrive.py` implementada con upload/download/list/create_folder
- [QACORE] Estructura de carpetas creada en Drive: Contabilidad, Tributario, Documentos Legales
- [QACORE] Configuración guardada en `.qai/config/gdrive_folders.json` (15 folder IDs)
- [QACORE] Upload de prueba exitoso

**Impacto**: Finn puede ahora subir/descargar documentos automáticamente. Índices locales (markdown) + archivos pesados en Drive = repo ligero + backup automático de Google.

---

#### 27-Dic (noche): Reorganización de Scripts de Setup en QaiCore
**Tipo**: Decisión Técnica / Estructura

**Contexto**: Scripts de setup (`setup_gdrive.py`, `test_gdrive.py`) estaban en `/scripts/` (raíz corporativa), separados de las herramientas que configuran.

**Decisión/Acción**:
- [QACORE] Scripts movidos a `/QaiCore/scripts/setup/` para portabilidad
- [QACORE] Renombrados: `gdrive_initial_setup.py`, `gdrive_test.py`
- [QACORE] README creado en `/setup/` con troubleshooting y guía de migración
- [QACORE] ADR-006 documenta decisión y justificación

**Impacto**: QaiCore es ahora autónomo (incluye setup scripts). Patrón replicable para futuras herramientas (Postgres, Redis). Mejora portabilidad y onboarding.

---

#### 27-Dic (noche): Estrategia de Documentos Legales Definida
**Tipo**: Decisión Estratégica / Organización

**Contexto**: Overlap entre `/Empresa/04_LEGAL/` (Git) y Google Drive "Documentos Legales" generaba confusión sobre qué va dónde.

**Decisión/Acción**:
- [EMPRESA] Separación clara: Templates/operativos → Git (`/04_LEGAL/`), PDFs oficiales → Drive
- [EMPRESA] Índices para Finn → `/03_ADMIN/documentos_legales/` (links a Drive)
- [EMPRESA] Responsabilidades: Lex gestiona templates, Finn gestiona PDFs oficiales
- [EMPRESA] READMEs completos en ambas ubicaciones + ADR-007

**Impacto**: Claridad total sobre gestión de documentos legales. Git limpio (sin PDFs pesados). Separación de responsabilidades Lex/Finn bien definida. Templates versionados en Git, documentos oficiales con backup de Google.

---

#### 27-Dic (noche): Sistema de Log de Actividad de Agentes
**Tipo**: Decisión Técnica / Memoria Institucional

**Contexto**: Sin Git activo localmente, no había forma de revisar qué acciones habían realizado los agentes en sesiones anteriores. Finn ejecutó acciones (upload PDF, actualización índices) pero no quedó registro centralizado.

**Decisión/Acción**:
- [TORREDECONTROL] Creado `/TorreDeControl/AGENT_ACTIVITY.md` - Log cronológico de acciones significativas
- [TORREDECONTROL] Implementación de `/TorreDeControl/temp_files/` como Landing Zone oficial (Zero InBox). Ver ADR-008.
- [QACORE] Finn's system_prompt actualizado con protocolo de logging obligatorio
- [QACORE] Lex's system_prompt actualizado con mismo protocolo
- [QACORE] Criterios claros: qué registrar (uploads, índices, reportes) vs qué no (consultas)

**Impacto**: Trazabilidad completa de acciones de agentes. En nueva sesión, cualquier agente/humano puede leer AGENT_ACTIVITY.md y saber exactamente qué pasó. Formato tabla simple (markdown, git-friendly cuando se active). Sistema complementa CHANGELOG (decisiones) y STATUS (estado operativo).

---

#### 26-Dic: Convención de Nombres de Agentes (CFO → Finn)
**Tipo**: Decisión Estratégica

**Contexto**: Adoptamos nombres amigables para no-gentes para facilitar su invocación en prompts y reducir fricción en coordinación multi-agente.

**Decisión/Acción**: Renombrar el agente financiero de "CFO" a "Finn" y establecer reglas de naming (canonical corto + alias funcional). Ver ADR-005.

**Impacto**: Mayor claridad y consistencia en documentación y sesiones; precedente para futuros agentes (Builder, Rainmaker). Referencia: [ADR-005](../QaiCore/agents/nzero/knowledge_base/design_decisions/005_agent_naming_convention.md).

---

## Plantilla para Futuras Entradas

```markdown
#### [Fecha]: [Título del Hito/Decisión]
**Tipo**: [Decisión Estratégica / Hito Comercial / Cambio de Producto]

**Contexto**: ¿Qué pasó? ¿Por qué es importante?

**Decisión/Acción**: ¿Qué se decidió o logró?

**Impacto**: ¿Qué cambia? ¿Qué se desbloquea?
```

---

#### 29-Dic: Refuerzo de Extracción de Totales (PO)
**Tipo**: Cambio de Producto / Mejora Técnica

**Contexto**: Se detectaron fallos en la extracción de totales en documentos multi-página o con formatos de miles complejos (comas).

**Decisión/Acción**:
- [INVOICE-MATCH] Actualización de `poPrompt` con reglas agresivas: búsqueda al final absoluto del documento.
- [INVOICE-MATCH] Normalización de comas como separadores de miles (ej: "365,635" → 365635).
- [INVOICE-MATCH] Implementación de fallback: si no hay total explícito, sumar montos de los line items.

**Impacto**: Mayor precisión en órdenes de compra complejas de FedEx. Reducción en la necesidad de corrección manual.

---

#### 29-Dic: Lanzamiento v0.2.0 - Invoice Matcher
**Tipo**: Hito de Producto / Release

**Contexto**: Consolidación de mejoras técnicas y preparación para entrega formal a FedEx.

**Decisión/Acción**:
- [INVOICE-MATCH] **Lanzamiento oficial v0.2.0**: Bump de versión en `package.json`.
- [INVOICE-MATCH] **Merge a Production**: Integración total de `develop` hacia `main`.
- [INVOICE-MATCH] **Refuerzo de Extracción**: Inclusión de lógica agresiva para totales, manejo de comas y fallback de suma.
- [INVOICE-MATCH] **Infraestructura**: Despliegue sincronizado en repositorio remoto.

**Impacto**: Producto en estado "Producción-Ready" para inicio de piloto. Estabilidad garantizada por fallback de extracción.
- ✅ 30-Dic-2025: **Aislamiento & Portabilidad (QaiCore)**. Implementado .venv dedicado, wrapper qrun.bat y protocolo "Root-Aware". (Acción: Nzero)
- ✅ 31-Dic-2025: **Protocolo SSOT (Single Source of Truth)**. Implementada sincronización estricta entre STATUS e INBOX. Eliminada redundancia de tareas en STATUS. (Acción: Nzero)
- ✅ 31-Dic-2025: **Refactor HQ Financiero & ADR-011**. Consolidación de 37 archivos en 3 pilares maestros. Formalizada la separación de memoria (KB vs HQ) para agentes. (Acción: Nzero)

---

#### 29-Dic: Estrategia FinOps Agnóstica y Categorizada
**Tipo**: Decisión Estratégica / Hito Financiero

**Contexto**: Con la integración de múltiples nubes y herramientas AI (GCP, Cursor, etc.), surgió la necesidad de rastrear costos de forma independiente al proveedor y asignarlos correctamente para entender la rentabilidad.

**Decisión/Acción**:
- [QAICORE] Implementación del **Marco Maestro de FinOps** (ADR-009).
- [FINN] Evolución de Finn a **v1.2 (FinOps Agnostic)**.
- [FINN] Categorización de costos en: **Fijos**, **Variables por Proyecto** y **R&D**.
- [DOCS] Primera carga formal de billing: Google AI Studio ($300 credit) con tarjeta Banco Chile.

**Impacto**: Visibilidad total de márgenes por producto y límites claros para la innovación. QAI ahora es capaz de costear cualquier herramienta o infraestructura de forma estandarizada.

---

#### 30-Dic: Estandarización de Herramientas Agentes (Terminal Fallback)
**Tipo**: Metodología / Estabilidad
**Contexto**: Se detectó una "crisis de identidad" en agentes que intentaban importar código Python sin tener un REPL disponible, causando bloqueos operativos.
**Decisión/Acción**:
- [QAICORE] **Terminal Fallback**: Refactorización de `gdrive.py`, `gsheets.py` y `document_processor.py` para soportar ejecución vía CLI.
- [PROTOCOL] **Regla #8**: Formalización de la ejecución vía terminal en el `README.md` de la Torre de Control.
- [FINN] **Actualización de Perfil**: Finn v1.2 ahora es agnóstico al entorno de ejecución (REPL o Terminal).
**Impacto**: Los agentes ahora son "inquebrantables" frente a limitaciones del entorno del IDE, garantizando que el Digital HQ funcione en cualquier plataforma.

---
**Tipo**: Hito Comercial / Entrega
**Contexto**: El producto Invoice Matcher ha alcanzado el estado de madurez necesario para ser probado por el cliente final.
**Decisión/Acción**:
- [INVOICE-MATCH] **Envío de Credenciales**: Se enviaron accesos de prueba a Eduardo J. Mejías (FedEx).
- [INVOICE-MATCH] **Manual de Usuario**: Entrega del manual en PDF con instrucciones detalladas de uso.
- [INVOICE-MATCH] **Ambientes**: Habilitado tanto entorno con data de ejemplo como entorno limpio para pruebas desde cero.
**Impacto**: Inicio del ciclo de feedback real. Desbloqueo de la etapa de validación de usuario (UAT) y avance hacia la Orden de Compra.

---
