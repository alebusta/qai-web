# Índice Maestro de Knowledge Bases - QAI

> **Propósito**: Mapa centralizado del conocimiento distribuido entre agentes  
> **Última actualización**: 17-Feb-2026 (Infraestructura de Extracción Blindada)
> **Total de archivos**: 39 archivos de conocimiento

---

## 🎯 Cómo Usar Este Índice

### Para Agentes
- **Antes de crear nuevo contenido**: Busca aquí si ya existe
- **Para coordinación**: Identifica qué agente tiene el conocimiento que necesitas
- **Para referencias cruzadas**: Usa los links directos a archivos

### Para Humanos
- **Onboarding**: Mapa completo del conocimiento de QAI
- **Auditoría**: Identificar gaps o duplicaciones
- **Búsqueda rápida**: "¿Dónde está documentado X?"

---

## 📚 Por Tema

### Tributario y Compliance

#### IVA (Impuesto al Valor Agregado)
- **Finn** (Operativo): [iva_basico.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/normativas/iva_basico.md)
  - Cálculo de Débito y Crédito Fiscal
  - Flujo operativo para registrar ventas/compras
  - Alertas automáticas (7 días antes, 1 día antes)
  - Protocolo de cierre mensual F29
- **Lex** (Legal): [codigo_tributario_chile_resumen.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/lex/knowledge_base/codigo_tributario_chile_resumen.md)
  - Marco legal del Código Tributario
  - Régimen Pro Pyme General (14 D3)
  - Obligaciones legales, sanciones y multas

#### Servicios Digitales Extranjeros (SaaS)
- **Lex** (Legal): [guia_facturacion_saas_extranjero.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/lex/knowledge_base/guia_facturacion_saas_extranjero.md)
  - Factura de Compra Doc. 46
  - Requisitos B2B, titularidad
  - Tipo de cambio (Dólar Observado)
- **Finn** (Operativo): [iva_basico.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/normativas/iva_basico.md) (sección "Compras de Servicios Digitales")
  - Efecto "Suma Cero", registro en libros
  - Casos prácticos (GitHub, Cursor, AWS)

#### Gastos Personales vs Empresariales
- **Finn**: [gastos_personales_uso_empresarial.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/normativas/gastos_personales_uso_empresarial.md)
  - Deducibles en F22, no recuperan IVA
  - Criterios de separación patrimonial

---

### Contabilidad

#### Plan de Cuentas
- **Finn**: [plan_cuentas.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md)
  - Plan de cuentas completo (11.02 Banco Chile, 21.04 Proveedores Extranjeros, etc.)
  - Estructura minimalista pero escalable

#### Libro Diario
- **Finn**: [guia_implementacion_libro_diario.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/contabilidad/guia_implementacion_libro_diario.md)
  - Sistema dual: Registro Diario (operativo) + Libro Diario (formal)
  - Generación de asientos contables con validación

#### Diferencias de Cambio
- **Finn**: [explicacion_diferencias_cambio.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/contabilidad/explicacion_diferencias_cambio.md)
  - Manejo de diferencias de cambio (dólar observado SII vs monto banco)
  - Filosofía QAI: simplicidad + cumplimiento

---

### FinOps (Gestión de Costos)

#### Marco FinOps Maestro
- **Finn**: [marco_finops_master.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/finops/marco_finops_master.md)
  - Estructura de costos (Fijo/Proyecto/R&D)
  - Gestión agnóstica de costos (SaaS, Clouds, BaaS, AI APIs)

#### Google Cloud Billing
- **Finn**: [google_cloud_billing.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/finops/google_cloud_billing.md)
  - Configuración de billing
  - Free Tier activo ($300 USD)

#### Banco Chile
- **Finn**: [banco_chile_details.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/finops/banco_chile_details.md)
  - Detalles de cuenta bancaria principal
  - Digipass activado

---

### Proveedores

#### Google (One, Workspace, Support)
- **Finn**: [caso_google_one_2026.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/proveedores/caso_google_one_2026.md)
  - Caso de suscripción Google One
  - Decisión: Mantener en enero, evaluar Workspace
- **Finn**: [google_workspace_info.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/proveedores/google_workspace_info.md)
  - Info sobre Google Workspace
  - Comparación con Google One
- **Finn**: [contacto_google.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/proveedores/contacto_google.md)
  - Guía de contacto con Google Support
  - Caso ID: 7-7961000040538

---

### Arquitectura y Diseño (ADRs)

#### Design Decisions
- **Nzero**: [design_decisions/](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/)
  - **ADR-001**: [Torre de Control](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/001_torre_de_control.md)
  - **ADR-002**: [QaiCore Structure](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/002_qaicore_structure.md)
  - **ADR-003**: [Profile vs System Prompt](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/003_profile_vs_system_prompt.md)
  - **ADR-004**: [Criterios Graduación Labs → Prod](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/004_criterios_graduacion_labs_prod.md)
  - **ADR-005**: [Agent Naming Convention](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/005_agent_naming_convention.md)
  - **ADR-006**: [Setup Scripts Location](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/006_setup_scripts_location.md)
  - **ADR-007**: [Legal Documents Strategy](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/007_legal_documents_strategy.md)
  - **ADR-008**: [Temp Files Landing Zone](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/008_temp_files_landing_zone.md)
  - **ADR-009**: [FinOps Agnostic Strategy](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/009_finops_agnostic_strategy.md)
  - **ADR-010**: [Mission Closing Protocol](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/010_mission_closing_protocol.md)
  - **ADR-011**: [Separation of Memory KB vs HQ](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/011_separation_of_memory_kb_hq.md)
  - **ADR-012**: [Sistema Comunicación Corporativa](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/012_sistema_comunicacion_corporativa.md)
  - **ADR-013**: [Financial Data Integrity (Zero-Loss Finance)](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/013_financial_data_integrity.md)
  - **Template**: [template.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/template.md)

#### Sistema de Emails
- **Nzero**: [012_sistema_comunicacion_corporativa.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/012_sistema_comunicacion_corporativa.md)
  - Gmail API, templates corporativos
  - Protocolo Human-in-the-Loop

---

### Análisis de Empresa

- **Nzero**: [company_analysis/](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/company_analysis/)
  - Análisis de fortalezas y debilidades
  - Evaluaciones trimestrales

---

### Contexto para AI

- **Nzero**: [context_for_ai/](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/context_for_ai/)
  - Contexto de empresa para otros agentes
  - Background de QAI

---

### Lecciones Aprendidas

- **Nzero**: [lessons_learned/](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/lessons_learned/)
  - Aprendizajes metodológicos
  - Estrategias FinOps

---

## 🤖 Por Agente

### Finn (Financiero) - 14 archivos

**Contabilidad** (3):
- [plan_cuentas.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md)
- [guia_implementacion_libro_diario.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/contabilidad/guia_implementacion_libro_diario.md)
- [explicacion_diferencias_cambio.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/contabilidad/explicacion_diferencias_cambio.md)

**FinOps** (3):
- [marco_finops_master.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/finops/marco_finops_master.md)
- [google_cloud_billing.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/finops/google_cloud_billing.md)
- [banco_chile_details.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/finops/banco_chile_details.md)

**Normativas** (2):
- [iva_basico.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/normativas/iva_basico.md)
- [gastos_personales_uso_empresarial.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/normativas/gastos_personales_uso_empresarial.md)

**Proveedores** (3):
- [caso_google_one_2026.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/proveedores/caso_google_one_2026.md)
- [google_workspace_info.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/proveedores/google_workspace_info.md)
- [contacto_google.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/proveedores/contacto_google.md)

**Changelog** (1):
- [changelog_operativo.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/changelog_operativo.md)

**Documentación** (2):
- [README.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/finn/knowledge_base/README.md)
- templates/ (1 subcarpeta)

---

### Lex (Legal) - 3 archivos

- [codigo_tributario_chile_resumen.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/lex/knowledge_base/codigo_tributario_chile_resumen.md)
- [guia_facturacion_saas_extranjero.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/lex/knowledge_base/guia_facturacion_saas_extranjero.md)
- [README.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/lex/knowledge_base/README.md)

---

### Nzero (Arquitecto) - 20 archivos

**Design Decisions** (14):
- ADRs 001-013 + template (ver sección "Arquitectura y Diseño" arriba)

**Company Analysis** (2):
- Análisis de fortalezas y debilidades

**Context for AI** (2):
- Contexto de empresa para agentes

**Lessons Learned** (2):
- Aprendizajes metodológicos

**Otros** (2):
- [012_sistema_comunicacion_corporativa.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/design_decisions/012_sistema_comunicacion_corporativa.md)
- [README.md](file:///c:/Users/abustamante/TheQaiCo/QaiCore/agents/nzero/knowledge_base/README.md)

---

## 🔍 Búsqueda Rápida por Palabra Clave

| Palabra Clave | Archivos Relacionados |
|:---|:---|
| **IVA** | Finn (`iva_basico.md`), Lex (`codigo_tributario_chile_resumen.md`) |
| **F29** | Finn (`iva_basico.md`), Lex (`codigo_tributario_chile_resumen.md`) |
| **SaaS Extranjero** | Lex (`guia_facturacion_saas_extranjero.md`), Finn (`iva_basico.md`) |
| **Doc. 46** | Lex (`guia_facturacion_saas_extranjero.md`) |
| **Plan de Cuentas** | Finn (`plan_cuentas.md`) |
| **Libro Diario** | Finn (`guia_implementacion_libro_diario.md`) |
| **FinOps** | Finn (`marco_finops_master.md`), Nzero (ADR-009) |
| **Google Cloud** | Finn (`google_cloud_billing.md`) |
| **Banco Chile** | Finn (`banco_chile_details.md`) |
| **ADR** | Nzero (`design_decisions/`) |
| **Landing Zone** | Nzero (ADR-008) |
| **Gastos Deducibles** | Finn (`gastos_personales_uso_empresarial.md`) |
| **Excel/CSV/PDF** | Finn/Lex/Nzero (Herramientas Core mejoradas Feb 2026) |
| **Google Drive** | Finn/Lex/Nzero (Integración E2E certificada) |

---

## 📊 Estadísticas

| Agente | Total Archivos | Categorías |
|:---|:---:|:---|
| **Finn** | 14 | Contabilidad (3), FinOps (3), Normativas (2), Proveedores (3), Otros (3) |
| **Lex** | 3 | Tributario (2), Documentación (1) |
| **Nzero** | 22 | Design Decisions (14), Company Analysis (2), Context (2), Lessons (2), Otros (2) |
| **TOTAL** | **39** | **11 categorías** |

---

## 🔄 Mantenimiento

**Responsable**: Nzero (actualización trimestral o cuando se agregue nuevo conocimiento)

**Protocolo**:
1. Al crear nuevo archivo en knowledge_base → Agregar a este índice
2. Al mover/renombrar archivo → Actualizar links
3. Al eliminar archivo → Remover del índice

**Última actualización**: 10-Ene-2026

---

**Creado por**: Nzero  
**Propósito**: Facilitar búsqueda de conocimiento y coordinación entre agentes
