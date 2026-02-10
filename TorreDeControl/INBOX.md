# INBOX - Buzón de Tareas Pendientes
 
> **Última actualización**: 10 de Febrero de 2026 (Sistema Libros Corporativos Operativo)  
> **Propietario**: Alejandro Bustamante

---

## 📥 ¿Qué es esto?

Tu **inbox personal** para capturar tareas rápidamente sin perder el contexto. Cuando piensas "tengo que hacer X después", lo dejas aquí.

**Reglas**:
1. ✅ Márcalo cuando lo hagas
2. 🗑️ Bórralo si ya no es relevante
3. 📝 Si crece mucho, archiva lo completado

---

## 🔥 URGENTE (Esta Semana)

### Infraestructura & Código
- [x] **Mover código de Invoice-Match** a `/QaiLabs/PROTOTIPOS/invoice-match/` (Confirmado en CHANGELOG 26-Dic) ✅
- [ ] **Mover código de Gestión Zen** a `/QaiLabs/PROTOTIPOS/gestion-zen/` (estructura corporativa)
- [ ] **Crear GitHub Organization** "The QAI Company" (migrar repos personales)

### FedEx - Invoice Matcher
- [x] **Procesar ejemplos de PDFs** que envió Eduardo (facturas + POs reales) ✅ 26-Dic-2025
- [x] **Desarrollar Dashboard** de métricas (Total procesado, Ahorro de tiempo, Discrepancias) ✅ 26-Dic-2025
- [x] **Infraestructura CI/CD** (Pipeline automático: staging, producción, previews PR) ✅ 26-Dic-2025
- [x] **Estabilización y Extracción** (Storage fix, fuzzy matching, normalización PO) ✅ 26-Dic-2025
- [x] **Mejoras al proceso de extracción** (basadas en procesamiento de ejemplos reales) ✅ 26-Dic-2025
- [x] **Split View Validator** (US-01, US-02, US-03) - Vista lado a lado, edición manual, botón aprobar ✅ 26-Dic-2025
- [x] **Historial de operaciones** (US-05) - Tabla con últimas 50 operaciones ✅ 26-Dic-2025
- [x] **Lógica de reintento Gemini** (US-08) - Implementada, monitorear en beta ✅ 26-Dic-2025
- [x] **Tabla jobs (US-07)** - Tabla `invoices` en Supabase cumple requisitos ✅ 26-Dic-2025
- [x] **Auditar código contra PRD_V1_PRODUCTION.md** (US-06: CSV Export verificado ✅ - Todos los user stories completados) ✅ 27-Dic-2025
- [x] **Compartir versión Beta** con equipo FedEx para testing (Enviado a Eduardo 30-Dic) ✅
- [x] **Completar Ficha Proveedor (Onboarding)** - Versión corregida enviada 02-Feb ✅ 03-Feb
- [x] **Revisar NDA FedEx** (Recibido 05-Feb por Eduardo Mejias) ✅ 07-Feb
- [x] **Firmar y Enviar NDA FedEx** - Firmado por Alejandro y enviado 10-Feb ✅
- [x] **Preparar documentación de uso** para cliente (`MANUAL_USUARIO.md` redactado) ✅ 26-Dic
- [x] **Generar y Enviar Cotización v3** a Sempere y Fernández (Rodrigo Fernández) ✅ 06-Feb
- [x] **Estandarizar estrucura de carpetas de clientes** (Protocolo 01/02/03) ✅ 06-Feb

### Gestión Zen - Joint Venture
- [x] **Procesar transcripción reunión 22-Dic-2025** (Análisis detallado creado) ✅ 28-Dic
- [ ] **Transcribir segunda parte de la reunión del 22 de diciembre** para identificar puntos pendientes
- [ ] **Consultar con SWS** sobre registro de prorrateo de gastos de gas y agua caliente común en cobros individuales
- [x] **Diseñar módulo de Egresos**: Implementar flujo de estados (Tránsito/Firmado/Pagado) ✅ 04-Ene-2026
- [ ] **Configurar Prorrateo Estacional**: Reglas Invierno/Verano para Metrogás
- [ ] **Alertas de Consumo**: Implementar pre-auditoría de medidores (+10m3 warning)
- [ ] **Firmar MOU fundacional** con socios (basado en acuerdos de reunión)
- [ ] Agendar próxima reunión con socios (definir fecha)


### Legal & Compliance
- [x] **Consultar con Lex**: ¿Cuándo debo hacer primera declaración IVA? (Confirmado: enero 2026 mensual)
- [x] **Activar Digipass Banco Chile** (Digipass activado 30-Dic) ✅
- [x] **Declarar IVA (F29) - Sin Movimiento DIC 2025** (Completado 15-Ene - Archivado en Drive) ✅
- [x] **🔥 Seguimiento Patente Providencia**: PLAZO VENCIDO (04-Feb). Seguimiento enviado (07-Feb). Respuesta pendiente.
- [ ] **Esperar respuesta Municipalidad Providencia** (Solicitud #1126-2026)
- [ ] **Junta Ordinaria 2025 (Expedita)** - Antes de fin de febrero. Aprobación EEFF sin movimiento + ratificación administradores.
- [x] **Apertura de Registro de Accionistas Digital**: Portal RES - Completado 09-Feb. CVE: RA1UcsKaOvrD ✅
- [x] **Implementar Libro de Actas Digital**: ✅ 09-10-Feb
  - [x] Redactar Acta N°1 (Constitución y Adopción de Libros Electrónicos). ✅ 07-Feb
  - [x] Firmar con firma simple y archivar (Firmada por ambos socios, respaldada en Drive). ✅ 10-Feb
  - [x] Crear repositorio digital completo (índices, checklist, respaldo Drive). ✅ 10-Feb
- [ ] **Consultar con Lex**: ¿Qué otros trámites faltan post-constitución? (Ver checklist en AGENT_ACTIVITY)
- [x] **Renovación Certificado Firma Electrónica**: Recibida factura E-Cert Folio 3286323 (04-Feb). ✅ 05-Feb-2026

---

## 📋 IMPORTANTE (Este Mes)

### Prioridades (próximas acciones)
- [ ] **Sistema de Propuestas vNext: “evento” por manifest** (1 comando)
  - Objetivo: `proposal_manifest.(yml|json)` + orquestador que genere según modo: `pdf`, `deck`, `both`, `both+mock`.
  - Contexto: priorización definida 21-Ene (Nzero). Mantenerlo visible.
- [x] **Estandarizar estructura de contenido (deck+pdf)**
  - Objetivo: un esqueleto reusable por servicio (sin depender de un cliente específico).
- [x] **Legal: gobernanza mínima** ✅ 09-10-Feb-2026 (Lex)
  - [x] Registro de Accionistas Digital abierto (RES) ✅
  - [x] Acta N°1 firmada + Libro de Actas Digital operativo ✅
  - [x] Sistema completo de libros corporativos con respaldo Drive ✅
  - Opción B: Acta N°1 + Libro de Actas Digital

### Infraestructura & Código
- [ ] Cloudflare: Migrar cuenta a QAI (Tier Gratuito, migración técnica)
- [ ] Crear criterios claros de "Graduación Labs → Prod"

### Marketing & Presencia
- [ ] Primer post LinkedIn (tema: "Graduamos nuestro primer producto a Prod")
- [ ] Crear perfil LinkedIn corporativo (no existe actualmente)
- [ ] Decidir si crear página web `qai.cl` ahora o después
- [ ] Automatizar cartas y correos de ventas (templates + workflow)
  - [x] Crear **Brand Kit** mínimo (SSOT) para propuestas y emails ✅ 21-Ene
  - [x] Crear **Sistema de Propuestas** (bloques + guía de estilo + render PDF/Deck) ✅ 23-Ene
  - [x] **Email Engine High-Fidelity**: Renderizado Markdown + Logo inline (Multipart/Related). ✅ 24-Ene

### Tech Debt (QaiCore)
- [ ] Barrido final: eliminar rutas absolutas / comandos legacy en docs/knowledge_base

### Finanzas

- [x] **Crear Google Sheet: Sistema Financiero QAI 2026** ✅ 30-Dic-2025
  - [x] Pestaña: Registro Diario (estructura completa con fórmulas) ✅
  - [x] Pestaña: Runway (flujo de caja mensual) ✅
  - [x] Pestaña: P&L (pérdidas y ganancias) ✅
  - [x] Pestaña: Préstamos_Socio (tracking de préstamos) ✅
  - [x] Pestaña: Control_Facturacion (tracking de facturas) ✅
  - [x] Pestaña: Costos_Proyecto (desglose FinOps) ✅
  - **URL**: [QAI_Finanzas_2026](https://docs.google.com/spreadsheets/d/1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw/edit)
  - **ID**: `1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw`
  - **Referencia**: Playbooks en `/QaiCore/playbooks/registrar_gasto_ingreso.md` y `facturar_cliente_saas.md`
- [x] **Configurar fórmulas y validaciones** en Google Sheets (listas desplegables, fórmulas automáticas) ✅ 30-Dic
- [x] **Actualizar estructura Registro_Diario** con columnas Retención y Monto Pagado para boletas honorarios ✅ 30-Dic
- [x] **Probar sistema**: Registrar primer movimiento de prueba ✅ 10-Ene-2026
- [x] **Evaluar migración Google One → Google Workspace** (Mesas de trabajo Enero 2026) ✅ 05-Feb
  - **Decisión actual**: Mantener Google One AI Pro (Permanente).
  - **Razón**: Acceso a Antigravity AI Pro (Claude/Gemini) con límites altos es vital. La fachada profesional se resuelve vía SMTP2GO.
  - **Referencia**: Ver discusion en `/QaiCore/agents/finn/knowledge_base/proveedores/caso_google_one_2026.md`

#### 🟡 IMPORTANTE - Operaciones Bancarias
- [ ] **Finalizar Apertura Cuenta BancoEstado** (No urgente - Costo $0)
  - [ ] Pendiente: Firma presencial de socia (Esposa)
  - [ ] Retirar tarjetas/claves tras firma

- [x] **📅 Seguimiento Google Workspace**:
  - [x] **Decisión Final**: Mantener Google One AI Pro + SMTP2GO. Se prioriza el acceso a modelos avanzados (Antigravity AI Pro) y el ahorro de costos operativos sobre la automatización del token de 7 días. ✅ 07-Feb.
  - [x] Objetivo: Mantener setup híbrido funcional. Profesionalismo vía SMTP2GO validado. ✅

#### 🟡 IMPORTANTE - Migración y Optimización
- [x] **Migrar suscripciones a nombre de QAI** (Cursor, Copilot, Antigravity, etc.) para crédito fiscal. ✅ 07-Ene-2026
  - [x] **Antigravity**: Cuenta corporativa creada con `alebusta.qai@gmail.com`, billing a nombre QAI ✅ 7-Ene-2026
  - [x] **Cursor**: Billing migrado a QAI SpA (Renueva 17-Ene) ✅
  - [x] **GitHub Copilot**: Billing migrado a QAI SpA (Renueva 09-Ene) ✅
  - [ ] **🔥 Facturación y Compliance - Documento 46 (Declaración Enero)**:
  - [ ] Emitir Factura de Compra (Doc. 46) para **GitHub** (Neto: 9.250) → **BLOQUEADO** (Pendiente OC FedEx para habilitar facturación en SII)
  - [ ] Emitir Factura de Compra (Doc. 46) para **Cursor** (Neto: 18.200) → **BLOQUEADO** (Pendiente OC FedEx para habilitar facturación en SII)
  - [x] **Google (Personal)**: Registrar solo para Renta (F22). **NO emitir Doc. 46**. ✅ (Contabilizado contablemente)
  - [ ] Cloudflare: Migrar cuenta a QAI (Nota: Actualmente Tier Gratuito, es migración técnica)
  - **Nota**: Cada migración requiere emitir Doc. 46 para crédito fiscal
  - **Estrategia**: Migración híbrida pragmática (billing primero, repos después en Q1 2026)

### Operaciones
- [x] **Crear playbooks financieros** en `/QaiCore/playbooks/`:
  - [x] `registrar_gasto_ingreso.md` (registro diario de operaciones) ✅ 30-Dic
  - [x] `facturar_cliente_saas.md` (flujo completo de facturación) ✅ 30-Dic
- [ ] **Crear playbooks técnicos** en `/QaiCore/playbooks/`:
  - `deploy_prod.md` (cómo hacer deploy)
  - `onboarding_cliente_saas.md` (activar nuevo cliente)
- [ ] Documentar proceso de revisión legal de contratos (para Lex)

#### 🟢 NICE TO HAVE - Sistema Financiero (Futuro)
- [ ] Implementar tracking automático de consumo de APIs (monitoreo Google Cloud)
- [ ] Definir límites de suscripción (qué incluye el precio base vs consumo adicional)
- [ ] Crear sistema de alertas de consumo (Finn puede monitorear)
- [ ] Automatizar reconciliación bancaria (proceso manual por ahora)
- [ ] Crear reporte mensual automatizado (dashboard de métricas)

---

## 💡 IDEAS / BACKLOG (Algún Día)

- [ ] **QAI-Parser (Open Source)**: Evaluar extraer y liberar el motor de extracción inteligente de documentos como librería independiente.
- [ ] Definir estrategia de contenido (blog técnico?)
- [ ] Investigar integraciones con otros sistemas (ERP, contabilidad)
- [ ] Crear "QAI SaaS Template" reutilizable para futuros productos
- [ ] **Seguridad**: Revisar políticas de acceso de agentes y protección de datos fuera del workspace (Algún día)

---

## ✅ COMPLETADO (Último Mes)

- [x] Constituir The QAI Company SpA
- [x] Abrir cuenta bancaria (Banco Chile)
- [x] Obtener Inicio de Actividades (SII)
- [x] Enviar cotización a FedEx
- [x] Reunión con socios Gestión Zen (22-Dic)
- [x] Crear estructura Torre de Control
- [x] **Certificación E2E Delivery Comercial v1.2** (Executive Horizon) ✅ 24-Ene-2026

---

## 🤖 Notas para Agentes

**REGLA DE ORO**: Si actualizas `STATUS.md`, DEBES marcar la tarea aquí en `INBOX.md`. La "Memoria Institucional" solo es válida si es consistente.

Si procesaste alguna tarea de este INBOX:
1. Márcala como `[x]`
2. Actualiza el `STATUS.md` con el resultado
3. Deja una nota abajo tipo: "✅ [Fecha]: Completé [tarea] - [Resultado]"

- `06-Feb-2026`: **Hito FedEx Dispatch v3 & Estandarización Comercial**. Generado PDF v3 para Sempere y Fernández Arquitectos. Despachado formalmente a Rodrigo Fernández via Gmail. Implementado y aplicado el **Protocolo de Organización de Clientes (01/02/03)** en todo el departamento comercial (CIAL, FedEx, GestionZen). DIGITAL_HQ.md actualizado. (Nzero)
- `07-Feb-2026`: **Acta N°1 lista** (PDF final) y template creado. Pendiente firma FEA + upload a Drive. Seguimiento patente Providencia enviado. NDA FedEx completado. (Lex)
- `03-Feb-2026`: **Certificación Final Email Bulletproof v1.5**. Implementada estructura de tablas HTML para blindar márgenes y colores en Gmail/Hotmail. Estética "CIAL" (Gris #374151 / Negritas #5b5d61) estandarizada como SSOT corporativo. Landing zone limpia y mock de Viñedos Austral eliminado. (Nzero)
- `24-Ene-2026`: Certificación E2E exitosa del Sistema de Propuestas v1.2...
- `22-Ene-2026`: CIAL Alimentos - **ENTREGA FINAL COMPLETADA** 🚀. Envío de propuesta (+ INTERACTIVO) a Iliana Alzurutt. PDFs generados con Playwright para fidelidad total. Landing zone 100% limpia. Proceso institucionalizado en `PROCESO_GENERACION_PROPUESTA.md`. (Nzero)
- `21-Ene-2026`: Comercial - Documentado workflow end-to-end del Sistema de Propuestas (inputs/outputs/modos de entrega) y anotados issues pendientes: estructura estándar de contenido, orquestador por evento, agente dedicado y mockup vivo. (Nzero)
- `10-Ene-2026`: Finanzas & Gobernanza - Ejecutada auditoría y consolidación de SSOT para Google Sheets. Implementado protocolo **Zero-Loss Finance (ADR-013)** con backups locales mandatorios. Estandarizada estructura de GDrive 2026 con 5 carpetas optimizadas por impacto tributario. Corregido extractor de Excel para cartolas y documentos complejos. Finn Brain actualizado con lógica dual (Registro Diario + Libro Diario). Landing Zone limpia. (Nzero)
- `07-Ene-2026`: QaiCore - Upgrade de `gmail.py` a v2.0. Implementada lectura, búsqueda y gestión de inbox (trash/read). Documentación creada en `README_GMAIL.md`. Proceso validado con éxito. (Nzero)
