# INBOX - Buzón de Tareas Pendientes
 
> **Última actualización**: 17 de Febrero de 2026 (Optimización de Ejecución QaiCore)  
> **Propietario**: Alejandro Bustamante

---

## 📥 ¿Qué es esto?

Tu **inbox personal** para capturar tareas rápidamente sin perder el contexto. Cuando piensas "tengo que hacer X después", lo dejas aquí.

**Reglas**:
1. ✅ Márcalo cuando lo hagas
2. 🗑️ Bórralo si ya no es relevante
3. 📌 Si crece mucho, archiva lo completado

---

## 🔥 URGENTE (Esta Semana)

### Infraestructura & Código
- [ ] **Habilitar acceso al bot para Iliana** (Whitelist de chat_id + modo restringido)
- [ ] **Rotar tokens del bot** (Telegram, GitHub PAT, Gemini API Key) — expuestos durante setup
- [ ] **Mover código de Gestión Zen** a `/QaiLabs/PROTOTIPOS/gestion-zen/` (estructura corporativa)
- [ ] **Crear GitHub Organization** "The QAI Company" (migrar repos personales)

### GestiÃ³n Zen - Joint Venture
- [ ] **Transcribir segunda parte de la reuniÃ³n del 22 de diciembre** para identificar puntos pendientes
- [ ] **Consultar con SWS** sobre registro de prorrateo de gastos de gas y agua caliente comÃºn en cobros individuales
- [ ] **Configurar Prorrateo Estacional**: Reglas Invierno/Verano para MetrogÃ¡s
- [ ] **Alertas de Consumo**: Implementar pre-auditorÃ­a de medidores (+10m3 warning)
- [ ] **uno de los demos para la web puede ser la captura de datos de imágenes de medidores** _(vía Telegram, 17-Feb-2026)_
- [ ] **Firmar MOU fundacional** con socios (basado en acuerdos de reuniÃ³n)
- [ ] Agendar prÃ³xima reuniÃ³n con socios (definir fecha)

### Legal & Compliance
- [ ] **Seguimiento Patente Municipal Nueva Solicitud #3026** - Enviada el 12-Feb-2026. Esperar confirmaciÃ³n de recepciÃ³n y fecha de evaluaciÃ³n (plazo 10 dÃ­as hÃ¡biles)
- [ ] **Junta Ordinaria 2025 (Expedita)** - Semana del 16-Feb. AprobaciÃ³n EEFF sin movimiento + ratificaciÃ³n administradores.

---

## 📋 IMPORTANTE (Este Mes)

### FedEx - Operaciones Comerciales
- [ ] **Seguimiento OC FedEx/Sempere**: Eduardo (FedEx) informa que Sempere debe emitir la OC a ellos primero. Se espera para esta semana. 🟡 (16-Feb)
- [ ] **Enviar correo recordatorio a Eduardo (FedEx)**: Consultar si Sempere ya emitió la OC. 📅 **Jueves 19-Feb**.
- [ ] **FacturaciÃ³n y Compliance - Documento 46 (DeclaraciÃ³n Enero)**:
  - [ ] Emitir Factura de Compra (Doc. 46) para **GitHub** (Neto: 9.250) → **BLOQUEADO** (Pendiente OC FedEx para habilitar facturaciÃ³n en SII)
  - [ ] Emitir Factura de Compra (Doc. 46) para **Cursor** (Neto: 18.200) → **BLOQUEADO** (Pendiente OC FedEx para habilitar facturaciÃ³n en SII)

### Infraestructura & QaiCore
- [ ] **Auditoría de Alineación de Agentes**: Verificar que Lex y Finn estén usando el motor de templates HTML correctamente en sus próximas tareas.
- [ ] **Cloudflare**: Migrar cuenta a QAI (Tier Gratuito, migración técnica)
- [ ] **Graduación**: Crear criterios claros de "Graduación Labs → Prod"

### Marketing & Presencia
- [ ] Primer post LinkedIn (tema: "Graduamos nuestro primer producto a Prod")
- [ ] Crear perfil LinkedIn corporativo (no existe actualmente)
- [ ] Decidir si crear página web `qai.cl` ahora o después
- [ ] Automatizar cartas y correos de ventas (templates + workflow)

### Finanzas (Futuro)
- [ ] **Finalizar Apertura Cuenta BancoEstado** (No urgente - Costo $0)
  - [ ] Pendiente: Firma presencial de socia (Esposa)
  - [ ] Retirar tarjetas/claves tras firma
- [ ] Implementar tracking automÃ¡tico de consumo de APIs (monitoreo Google Cloud)
- [ ] Crear reporte mensual automatizado (dashboard de mÃ©tricas)

---

## 💡 IDEAS / BACKLOG (Algún Día)

- [ ] **QAI-Parser (Open Source)**: Evaluar extraer y liberar el motor de extracción inteligente de documentos como librería independiente.
- [ ] **Misión Salida - Fase 5: Horizon**: Evaluación de n8n para soporte WhatsApp, Diseño de Dashboard Web (UI propia).
- [ ] **Sistema de Propuestas vNext**: "evento" por manifest (1 comando).
- [ ] **Seguridad**: Revisar políticas de acceso de agentes y protección de datos fuera del workspace.

---

## ✅ COMPLETADO (Historial Reciente)

- [x] **Optimización de Ejecución (Nzero)**: Implementado `--data-file` en `gsheets.py`, caché de discovery para Google APIs (30s → 1s) y desacople de `render_email.py`. (17-Feb-2026)
- [x] **Procesar Orden Namecheap (theqai.co)**: Dominio registrado en GSheets y Drive. (16-Feb-2026)
- [x] **Refinamiento Web V3 (The Hinge)**: Estética anti-hype certificada. (15-Feb-2026)
- [x] **Misión Latinarq: Prospección Inteligente v1.0**: Enriquecimiento de 68 registros de Circle Pack. (13-Feb-2026)
- [x] **Patente Providencia**: Documentación completa enviada el 12-Feb-2026 (Solicitud #3026).
- [x] **Gobernanza Mínima (Lex)**: Registro de Accionistas Digital y Acta N°1 operativa. (10-Feb-2026)
- [x] **NDA FedEx**: Firmado y enviado. (10-Feb-2026)
- [x] **Estandarización de Carpetas**: Protocolo 01/02/03 aplicado a clientes. (06-Feb-2026)
- [x] **Decisión Google Workspace**: Mantener Google One AI Pro + SMTP2GO. (05-Feb-2026)

---

## 🤖 Notas para Agentes

**REGLA DE ORO**: Si actualizas `STATUS.md`, DEBES marcar la tarea aquí en `INBOX.md`. La "Memoria Institucional" solo es válida si es consistente.

- `17-Feb-2026`: **Optimización Masiva QaiCore**. Se eliminó la latencia de 30s en APIs de Google mediante caché local de discovery. Se habilitó `--data-file` en GSheets para evitar errores con paréntesis en PowerShell. Se refactorizó `tools/__init__.py` con lazy imports para evitar deadlocks de dependencias pesadas. (Nzero)
- `16-Feb-2026`: **Namecheap & Zero-Loss**. Corregido monto de Namecheap para match exacto con banco ($5.274 CLP). SSOT financiero actualizado. (Finn)
- `13-Feb-2026`: **Misión Latinarq Finalizada**. Entrega de leads enriquecidos a Iliana. Proceso de cierre Zero-Footprint ejecutado. (Nzero)
- `10-Feb-2026`: **Hito Legal**. Libros digitales operativos y respaldados en Drive. QAI ya es legalmente "transparente" y auditable. (Lex)
- `06-Feb-2026`: **Hito FedEx Dispatch v3**. Propuesta enviada a Rodrigo Fernández. Estandarización comercial completada. (Nzero)
