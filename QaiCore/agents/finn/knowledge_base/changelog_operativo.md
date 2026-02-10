# Changelog - Sistema Financiero QAI

> **Registro de cambios importantes en el sistema financiero**

---

## 30-Dic-2025 - Sistema Completo: Gastos Deducibles y Boletas Honorarios

### ✅ Nuevos Documentos

1. **`RUNWAY_RECOMENDADO.md`**
   - Análisis completo de capital mínimo recomendado
   - Capital sugerido: $600k-$800k CLP
   - Runway recomendado: 12 meses
   - Estrategias de préstamos documentadas

2. **`GASTOS_DEDUCIBLES_SII.md`**
   - Guía completa de gastos deducibles según giros QAI
   - Ejemplos prácticos de todos los tipos de gastos
   - Explicación de diferencia entre Libro de Compras y Gastos Deducibles
   - Casos específicos: boletas honorarios, depreciación, viáticos, etc.
   - Ejemplo completo de comisión Ligia

3. **`PREPARACION_F22_DECLARACION_ANUAL.md`**
   - Proceso completo para preparar F22 (declaración anual)
   - Timeline: abril 2027
   - Checklist de información necesaria
   - Template de consolidación
   - Cálculo de renta líquida imponible

4. **`RESUMEN_FLUJO_GASTOS_F22.md`**
   - Resumen ejecutivo del flujo de trabajo
   - Checklist de preparación
   - Referencias a documentos clave

### ✅ Documentos Actualizados

1. **`QaiCore/playbooks/registrar_gasto_ingreso.md`**
   - Agregado caso especial: Boleta de Honorarios (con Retención)
   - Proceso paso a paso para comisiones y servicios profesionales
   - Ejemplo completo de comisión Ligia
   - Instrucciones de cálculo de retención (10,75%)

2. **`PLANTILLAS_GOOGLE_SHEETS.md`**
   - Estructura actualizada de `Registro_Diario`
   - Agregadas columnas: Retención (H), Monto Pagado (J)
   - Reorganización de columnas (Monto Bruto ahora I, etc.)

3. **`GOOGLE_SHEETS_ID.md`**
   - Actualizado con nota de actualización de estructura

### ✅ Sistema Operativo Actualizado

1. **Google Sheet `QAI_Finanzas_2026`**
   - Hoja `Registro_Diario` actualizada con nuevas columnas:
     - Columna H: Retención
     - Columna J: Monto Pagado
   - Headers reorganizados según nueva estructura
   - Listo para registrar boletas de honorarios

### 📋 Impacto

**Para Operaciones Diarias**:
- Sistema completo para registrar boletas de honorarios (comisiones, servicios profesionales)
- Cálculo automático de retenciones
- Tracking correcto para deducciones F22

**Para Declaración Anual (F22 - Abril 2027)**:
- Proceso documentado y checklist completo
- Template de consolidación listo
- Guía clara de qué gastos son deducibles

**Documentación**:
- Base de conocimiento completa sobre gastos deducibles
- Ejemplos prácticos para todos los casos comunes
- Referencias cruzadas entre documentos

---

## 30-Dic-2025 - Sistema Financiero Operativo Inicial

### ✅ Sistema Google Sheets Creado
- Spreadsheet `QAI_Finanzas_2026` con 6 hojas
- Playbooks de registro y facturación
- Estructura documentada

---

## 07-Ene-2026 - Actualización Knowledge Base y Caso Google One

### ✅ Nuevos Documentos en Knowledge Base

1. **`normativas/gastos_personales_uso_empresarial.md`**
   - Guía sobre deducibilidad de gastos personales con uso empresarial
   - Tratamiento para Impuesto a la Renta (F22) vs IVA
   - Caso específico: Google One (Antigravity)
   - Instrucciones de registro contable

2. **`proveedores/google_workspace_info.md`**
   - Comparación Google One vs Google Workspace
   - Precios aproximados 2026
   - Recomendaciones para QAI

3. **`proveedores/contacto_google.md`**
   - Guía de contacto real con Google Support
   - Opciones verificadas que funcionan
   - Plantilla de consulta

### ✅ Caso Abierto con Google Support

**Problema**: Suscripción Google One asociada a perfil personal en lugar de empresarial QAI

**Acción**: Consulta enviada a Google One Support
- **ID de Caso**: 7-7961000040538
- **Fecha**: 07-Ene-2026
- **Estado**: Pendiente respuesta
- **Tiempo estimado**: 24-72 horas

**Documentación**: Consulta completa en `TorreDeControl/temp_files/consulta_google_payments.md`

### 📋 Impacto

- Knowledge base actualizada con información sobre gastos personales empresariales
- Caso Google documentado para seguimiento
- Guía de contacto Google actualizada con opciones reales

---

---

## 10-Ene-2026 - Sistema Contable Minimalista y Escalable

### ✅ Plan de Cuentas Completo Formalizado

**Documento Creado**: [`contabilidad/plan_cuentas.md`](contabilidad/plan_cuentas.md)

**Estructura Implementada**:
- **Cuenta Operativa**: `11.02 Banco Chile` (única cuenta con movimientos actualmente)
- **Cuenta Reservada**: `11.03 BancoEstado` (backup sin movimientos, reservada para futuro)
- **Estructura Escalable**: Sistema numérico permite agregar nuevas cuentas (11.04, 11.05, etc.) sin reestructurar

**Principio de Diseño**:
- **Minimalista ahora**: Solo cuentas necesarias (Banco Chile única operativa)
- **Escalable después**: Estructura permite crecimiento sin reestructurar
- **Consistente**: Unificación entre manual tributario, playbooks y práctica

**Cuentas Clave Definidas**:
- Activos: 11.02 Banco Chile, 11.03 BancoEstado (reserva), 12.01 Cuentas por Cobrar
- Pasivos: 21.01 Préstamos Socios, 21.02 Retenciones por Pagar, 21.03 Comisiones (reserva)
- Ingresos: 41.01.XX Ventas Servicios (desglose por producto)
- Costos: 51.01.XX Costos Directos por Proyecto (tracking dinámico)
- Gastos: 61.01.XX Fijos, 61.02.XX R&D
- IVA: 81.01 Crédito Fiscal, 81.02 Débito Fiscal

### ✅ Protocolos de Registro y Conciliación Bancaria

**Protocolos Creados**:
1. **`registro_movimiento_bancario.md`** 🆕
   - Workflow paso a paso para registrar movimientos de cuenta corriente
   - Flujo simplificado para movimientos mínimos actuales (suscripciones, pay-as-you-go)
   - Integración con Registro Diario de Google Sheets
   - Verificación de saldo bancario vs contabilidad

2. **`conciliacion_bancaria.md`** 🆕
   - Proceso quincenal/mensual de conciliación con extracto bancario
   - Comparación de movimientos registrados vs extracto bancario
   - Resolución de discrepancias
   - Generación de reporte de conciliación

### ✅ Actualizaciones de Documentación

**Documentos Actualizados**:
1. **`MANUAL_TRIBUTARIO_Y_OPERATIVO.md`**
   - Plan de Cuentas actualizado para usar `11.02 Banco Chile` específico (en lugar de genérico `11.01 Caja/Banco`)
   - Referencia a Plan de Cuentas completo y protocolos de registro/conciliación

2. **`registrar_gasto_ingreso.md`**
   - Referencia al Plan de Cuentas completo
   - Actualización de ejemplos para usar cuenta correcta (`11.02 Banco Chile`)
   - Referencias cruzadas con protocolos bancarios

3. **`facturar_cliente_saas.md`**
   - Actualización de asientos contables para reflejar flujo correcto (12.01 Cuentas por Cobrar → 11.02 Banco Chile)
   - Referencias al Plan de Cuentas y protocolos bancarios

4. **`knowledge_base/README.md`**
   - Nueva sección de Contabilidad y Plan de Cuentas
   - Documentación de protocolos y playbooks relacionados
   - Estructura escalable explicada

### ✅ Resolución de Inconsistencias

**Problema Resuelto**:
- **Inconsistencia anterior**: Manual mencionaba `11.01 Caja/Banco` genérico, pero playbooks usaban `11.02 Banco Chile` específico
- **Solución**: Plan de Cuentas formalizado usa `11.02 Banco Chile` específico (única cuenta operativa ahora), con estructura escalable para agregar más bancos después

### 📋 Impacto

**Para Operaciones Diarias**:
- Clasificación consistente de movimientos según Plan de Cuentas unificado
- Protocolo claro para registrar movimientos bancarios
- Verificación periódica de integridad contable mediante conciliación

**Para Escalabilidad**:
- Estructura numérica permite agregar nuevas cuentas bancarias (11.04, 11.05) sin reestructurar
- Sistema preparado para crecimiento sin cambios mayores
- Base sólida para cuando aumenten movimientos o se agreguen productos/proyectos

**Para Trazabilidad**:
- Cada movimiento tiene cuenta específica y trazable
- Saldo contable vs saldo bancario verificable periódicamente
- Discrepancias identificables y resolubles de forma sistemática

**Documentación**:
- Plan de Cuentas completo y referenciable
- Protocolos claros y ejecutables
- Consistencia entre todos los documentos financieros

---

**Última actualización**: 10-Ene-2026  
**Responsable**: Finn (Agente Financiero)

---

## 10-Ene-2026 (Tarde) - Protocolo Cartolas Parciales vs Oficiales

### ✅ Actualización de Protocolos de Archivado

**Decisión Operativa**: Solo archivar cartolas oficiales de fin de mes, NO cartolas parciales.

**Razones**:
- ✅ **Simplicidad**: Evita duplicados (parcial vs oficial)
- ✅ **Cumplimiento**: Solo la oficial tiene validez contable/tributaria
- ✅ **Trazabilidad**: Cada movimiento ya está registrado individualmente con su comprobante
- ✅ **Eficiencia**: Reduce trabajo duplicado y riesgo de inconsistencias

**Archivos Actualizados**:

1. **`playbooks/registro_movimiento_bancario.md`**
   - Nueva sección en Trigger: Distinción cartolas parciales vs oficiales
   - Nueva subsección 7: "REGLA ESPECIAL: Cartolas Bancarias (Extractos)"
   - Define cuándo archivar (solo oficiales fin de mes) y cuándo no (parciales durante el mes)
   - Excepciones documentadas: solo archivar parcial si hay discrepancia significativa

2. **`playbooks/conciliacion_bancaria.md`**
   - Sección 1 actualizada: Distinción clara entre cartola parcial y oficial
   - Sección 9 renombrada y reescrita: "Archivar Extracto Bancario Oficial"
   - Criterios de Éxito actualizados para reflejar nueva regla

**Acciones Realizadas**:
- ✅ Recibo Google One subido a Drive y verificado en registro
- ✅ Cartola parcial (cartola.xlsx) eliminada de Drive según nueva regla
- ✅ Protocolo documentado en ambos playbooks

**Impacto**:
- Sistema más limpio y ordenado (sin duplicados)
- Protocolo claro para futuras cartolas
- Alineado con filosofía QAI: simplicidad y cumplimiento

---

## 10-Ene-2026 (Noche) - Implementación Libro Diario Formal

### ✅ Sistema de Registro Contable Híbrido (Doble Nivel)

**Decisión Operativa**: Implementar sistema de registro contable con dos niveles: Registro Diario (operativo diario) y Libro Diario (formal mensual).

**Razones**:
- ✅ **Simplicidad Operativa**: Registro Diario permite registro rápido diario de movimientos bancarios
- ✅ **Formalidad Contable**: Libro Diario cumple con principios contables formales (asientos completos con débito/crédito)
- ✅ **Escalabilidad**: Sistema preparado para crecimiento sin cambios mayores
- ✅ **Cumplimiento**: Permite generar Balance y cumplir con obligaciones contables formales

**Archivos Creados**:

1. **`playbooks/generar_asientos_libro_diario.md`**
   - Workflow completo para generar asientos formales desde Registro Diario al Libro Diario
   - Ejemplos prácticos de conversión de movimientos a asientos formales
   - Validación de equilibrio contable (Suma Débitos = Suma Créditos)
   - Proceso mensual/quincenal según volumen de movimientos

**Archivos Actualizados**:

1. **`playbooks/registro_movimiento_bancario.md`**
   - Agregada sección sobre dos niveles de registro (Registro Diario vs Libro Diario)
   - Actualizados criterios de éxito para incluir registro formal mensual
   - Referencias al nuevo protocolo de Libro Diario

2. **`agents/finn/knowledge_base/contabilidad/plan_cuentas.md`**
   - Ejemplos de asientos actualizados para formato formal de Libro Diario
   - Sección de validaciones actualizada con dos niveles de registro
   - Referencias al protocolo de generación de asientos

3. **`Empresa/03_ADMINISTRACION_FINANZAS/MANUAL_TRIBUTARIO_Y_OPERATIVO.md`**
   - Sección 5 actualizada: "Protocolo de Registro Contable (Doble Nivel)"
   - Documentación completa de Registro Diario vs Libro Diario
   - Flujo de proceso operativo diario y formal mensual

**Estructura de Google Sheets (A Crear)**:

- **Pestaña `Libro_Diario`** (nueva, pendiente de crear en Google Sheets):
  - Columnas: `Asiento # | Fecha | Concepto | Cuenta | Débito | Crédito | Notas`
  - Propósito: Registro formal mensual con asientos completos (múltiples filas = 1 asiento)
  - Validación: Suma Débitos = Suma Créditos por asiento y total

**Impacto**:
- Sistema contable más robusto y formal sin perder simplicidad operativa
- Preparado para auditorías y cumplimiento contable formal
- Base sólida para generar Balance y Libro Mayor en el futuro
- Mantiene simplicidad diaria con Registro Diario operativo

---

**Última actualización**: 10-Ene-2026  
**Responsable**: Finn (Agente Financiero)

