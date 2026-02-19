# INBOX - Buzón de Tareas Pendientes
 
> **Última actualización**: 19 de Febrero de 2026 (Búsqueda Híbrida & Saneamiento)  
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

### Gestión Zen - Joint Venture
- [ ] **Transcribir segunda parte de la reunión del 22 de diciembre** para identificar puntos pendientes
- [ ] **Consultar con SWS** sobre registro de prorrateo de gastos de gas y agua caliente común en cobros individuales
- [ ] **Configurar Prorrateo Estacional**: Reglas Invierno/Verano para Metrogás
- [ ] **Alertas de Consumo**: Implementar pre-auditoría de medidores (+10m3 warning)
- [ ] Agendar próxima reunión con socios (definir fecha)

### Legal & Compliance
- [ ] **Re-presentar Patente Municipal (Opción 1)** - Nueva solicitud con dirección del RL = Bucarest 17, Depto 58, Providencia (domicilio tributario).
- [ ] **Junta Ordinaria 2025 (Expedita)** - Semana del 16-Feb. Aprobación EEFF sin movimiento + ratificación administradores.

---

## 📋 IMPORTANTE (Este Mes)

### FedEx - Operaciones Comerciales
- [ ] **Seguimiento OC FedEx/Sempere**: Eduardo (FedEx) informa que Sempere debe emitir la OC a ellos primero. 🟡 (16-Feb)
- [x] **Enviar correo recordatorio a Eduardo (FedEx)**: Consultar si Sempere ya emitió la OC. ✅ **Enviado el 19-Feb**.
- [ ] **Facturación y Compliance - Documento 46 (Declaración Enero)**:
  - [ ] Emitir Factura de Compra (Doc. 46) para **GitHub** (Neto: 9.250) → **BLOQUEADO**
  - [ ] Emitir Factura de Compra (Doc. 46) para **Cursor** (Neto: 18.200) → **BLOQUEADO**

### Infraestructura & QaiCore
- [x] **Búsqueda Híbrida QMD & Saneamiento QaiLabs**: Implementados ADR-020 y ADR-021. El HQ ahora tiene motor de búsqueda de IA local y estructura README-only en labs. (19-Feb-2026)
- [x] **Auditoría de Alineación de Agentes**: Implementado **ADR-019** y `EXPERIMENTAL_ZONE_NOTICE.md`. (19-Feb)
- [ ] **Cloudflare**: Migrar cuenta a QAI (Tier Gratuito, migración técnica)
- [ ] **Graduación**: Crear criterios claros de "Graduación Labs → Prod"

---

## 💡 IDEAS / BACKLOG (Algún Día)

- [ ] **QAI-Parser (Open Source)**: Evaluar extraer y liberar el motor de extracción inteligente de documentos.
- [ ] **Misión Salida - Fase 5: Horizon**: Evaluación de n8n para soporte WhatsApp, Diseño de Dashboard Web.

---

## ✅ COMPLETADO (Historial Reciente)

- [x] **Búsqueda Híbrida QMD**: Integrado motor vectorial local (ADR-021).
- [x] **Saneamiento QaiLabs**: Repositorio README-only según ADR-020.
- [x] **Protocolo de cierre + Indexación comprobantes (Finn)**: INDICE_COMPROBANTES.md y DISENO_RESPALDO_E_INDEXACION.md creados. (19-Feb-2026)
- [x] **Optimización de Ejecución (Nzero)**: Caché de discovery para Google APIs. (17-Feb-2026)

---

## 🤖 Notas para Agentes

**REGLA DE ORO**: Si actualizas `STATUS.md`, DEBES marcar la tarea aquí en `INBOX.md`. La "Memoria Institucional" solo es válida si es consistente.

- `19-Feb-2026`: **Búsqueda Híbrida QMD & Saneamiento**. Implementado motor vectorial local (ADR-021) y finalizado saneamiento de QaiLabs (ADR-020). (Nzero)
- `19-Feb-2026`: **Cierre sesión Lex**. Patente #3026: revisión email y asesoría Opción 1. (Lex)
- `19-Feb-2026`: **Cierre sesión Finn (PCA)**. Indexación comprobantes y flujos landing zone. (Finn)
