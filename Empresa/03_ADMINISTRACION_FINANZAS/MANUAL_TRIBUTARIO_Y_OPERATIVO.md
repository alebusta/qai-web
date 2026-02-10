# Manual Tributario y Operativo: QAI Company

> **Visión Nzero**: Este manual es la guía de supervivencia administrativa. Define qué gastos acepta el SII, cómo preparar la renta y el plan de cuentas minimalista de la empresa.

---

## 1. Guía de supervivencia SII: Gastos Deducibles
**Regla de Oro**: Un gasto es deducible si es **necesario para producir renta** y está **relacionado con el giro** (Tecnología/Consultoría).

### Categorías Clave para QAI
- **Tecnología (100% SÍ)**: Cursor, Copilot, Antigravity, Supabase, APIs (IA).
- **Operación (SÍ)**: Oficina Virtual, Contador, Legal, Marketing Digital.
- **Activos (Depreciación)**: Computadores y muebles (<$2.5M puede ser gasto directo).
- **Exentos Justificados**: Sueldos, Honorarios (Ligia), Intereses de préstamos.

### Requisito Crítico (SaaS Extranjero)
Para servicios como Cursor o APIs, DEBES habilitar el **Documento 46 (Factura de Compra)** en el SII para recuperar el IVA. Las cuentas deben estar a nombre de **QAI Company SpA**.

---

## 2. Plan de Cuentas (Minimalista pero Escalable)

**Referencia Completa**: Ver [`/QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md`](../../../QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md)

**Estructura Principal**:
- **Activos**: 11.02 Banco Chile (operativa), 11.03 BancoEstado (reserva), 12.01 Cuentas por Cobrar
- **Pasivos**: 21.01 Préstamos Socios, 21.02 Retenciones por Pagar, 21.03 Comisiones (reserva)
- **Ingresos**: 41.01 Ventas Servicios (desglose por producto)
- **Costos COGS**: 51.01 Costos Directos por Proyecto (tracking dinámico)
- **Gastos OPEX**: 61.01 Gastos Fijos (61.01.01 Oficina, 61.01.02 Contador, 61.01.03 Tech), 61.02 R&D (Labs)
- **IVA**: 81.01 Crédito Fiscal, 81.02 Débito Fiscal

**Principio de Diseño**: Minimalista ahora (solo cuentas necesarias), escalable después (estructura numérica permite agregar subcuentas sin reestructurar).

---

## 3. Preparación de Renta (F22)
### Declaración Anual 2025 (Histórico)
- **Estado**: Sin Movimiento (13 días de operación).
- **Acción**: Declarar en "Cero" en Abril 2026. Obligatorio para evitar multas.

### Declaración Anual 2026 (Proyectada)
- **Fecha**: Abril 2027.
- **Tasa**: 25% sobre Renta Líquida Imponible (Régimen 14 D3).
- **Checklist**: Consolidar ingresos, restar gastos deducibles y depreciación.

---

## 4. Separación de Patrimonios (CRÍTICO)

> ⚠️ **Regla de Oro**: "La billetera de la empresa NO es la billetera del dueño"

### Riesgos Tributarios que Debes Evitar

1. **Gastos Personales**: Si QAI paga gastos personales → SII lo considera **retiro de utilidades** (afecto a Impuesto Global Complementario) o **gasto rechazado** (hasta 40%)

2. **Préstamos Informales**: Si prestas dinero de QAI a ti mismo sin contrato formal, intereses y timbraje → SII puede recalificarlo como **retiro encubierto**

3. **Uso de Activos Empresariales**:
   - Inmuebles: Presunción de beneficio = **11% avalúo fiscal anual**
   - Vehículos: Presunción de beneficio = **20% valor tributario**

### Protocolo de Protección QAI

✅ **SÍ puedes pagar con QAI**: Cursor, Copilot, Antigravity, Supabase, oficina virtual, contador, herramientas del giro  
❌ **NO puedes pagar con QAI**: Netflix personal, supermercado, servicios básicos del hogar, viajes personales

📖 **Guía Detallada**: Ver [SEPARACION_PATRIMONIOS_PYME.md](tributario/SEPARACION_PATRIMONIOS_PYME.md) para casos específicos y jurisprudencia

---

## 5. Protocolo de Registro Contable (Doble Nivel)

**⚠️ IMPORTANTE - Dos Niveles de Registro**:

### Nivel 1: Registro Diario (Operativo - Diario)

**Propósito**: Registro rápido diario de movimientos bancarios y clasificación FinOps.

**Ubicación**: Google Sheets `QAI_Finanzas_2026` → Pestaña `Registro_Diario`

**Estructura**: 1 fila = 1 movimiento bancario
- Fecha, Tipo, Concepto, Categoría, Cuenta, Monto Neto, IVA, Monto Bruto, Monto Pagado, Proyecto, Comprobante, Notas

**Cuándo usar**: Diario, inmediatamente al ocurrir el movimiento bancario.

### Nivel 2: Libro Diario (Formal - Mensual)

**Propósito**: Registro contable formal con asientos completos (débito/crédito) para cumplimiento contable.

**Ubicación**: Google Sheets `QAI_Finanzas_2026` → Pestaña `Libro_Diario` (✅ ACTIVA)

**Estructura**: Múltiples filas = 1 asiento completo (Suma Débitos = Suma Créditos)
- Asiento #, Fecha, Concepto, Cuenta, Débito, Crédito, Notas

**Cuándo usar**: Mensual o quincenal, al finalizar el período contable.

**Flujo**:
```
Movimiento Bancario 
  → Registro Diario (inmediato, operativo) 
  → Al final de mes: Generar asientos formales en Libro Diario
  → Validar equilibrio contable (Suma Débitos = Suma Créditos)
```

**Playbooks Detallados**:
- **Registro de Gastos/Ingresos**: [`/QaiCore/playbooks/registrar_gasto_ingreso.md`](../../../QaiCore/playbooks/registrar_gasto_ingreso.md)
- **Registro de Movimientos Bancarios**: [`/QaiCore/playbooks/registro_movimiento_bancario.md`](../../../QaiCore/playbooks/registro_movimiento_bancario.md) (Registro Diario operativo)
- **Generar Asientos Formales**: [`/QaiCore/playbooks/generar_asientos_libro_diario.md`](../../../QaiCore/playbooks/generar_asientos_libro_diario.md) 🆕 (Libro Diario formal)
- **Conciliación Bancaria**: [`/QaiCore/playbooks/conciliacion_bancaria.md`](../../../QaiCore/playbooks/conciliacion_bancaria.md)

**Resumen del Proceso Operativo Diario**:
1. Identificar movimiento (gasto, ingreso o movimiento bancario)
2. Clasificar según Plan de Cuentas
3. Registrar en `Registro_Diario` (formato operativo, inmediato)
4. Archivar comprobante en Google Drive (si existe)
5. Actualizar métricas (Runway, P&L)

**Resumen del Proceso Formal Mensual**:
1. Revisar movimientos del período en `Registro_Diario`
2. Generar asientos formales en `Libro_Diario` (ver protocolo `generar_asientos_libro_diario.md`)
3. Validar equilibrio contable (Suma Débitos = Suma Créditos por asiento y total)
4. Marcar movimientos como "Asiento Generado" en `Registro_Diario`
5. Conciliar con extracto bancario oficial (mensual)

### Nivel 3: Integridad de Datos (Zero-Loss Finance) 🆕

**⚠️ PROTOCOLO DE SEGURIDAD (ADR-013)**:
Para evitar la pérdida o corrupción de datos financieros, se establece el protocolo de "Snapshot Local":
- **Backup Mandatorio**: Antes y después de cada sesión de registro en GSheet, los agentes deben ejecutar el tool `backup_finance.py`.
- **Almacenamiento**: Los backups se guardan localmente en el repositorio (`Empresa/03_ADMIN_FINANZAS/backups/`) en formato CSV.
- **SSOT**: El Google Sheet es el maestro, pero el repositorio local actúa como la caja negra de seguridad.

---

## 6. Estructura de Respaldo GDrive (Optimizado 2026)

Para facilitar auditorías (F22/F29), los respaldos de cada mes se organizan exclusivamente en estas 5 carpetas:

1.  **`01-Compras_Chile_DTE`**: Facturas electrónicas locales (IVA).
2.  **`02-Ventas_Chile_DTE`**: Facturas emitidas por QAI.
3.  **`03-Gastos_Sin_Iva_y_Honorarios`**: Boletas de honorarios (Ligia), tickets, peajes, boletas exentas.
4.  **`04-Operaciones_Extranjeras_Doc46`**: Receipts originales (Amazon/Google/Cursor) + sus Doc 46. Mantener vinculados.
5.  **`05-Bancos_Cartolas_y_Pagos`**: Cartolas bancarias oficiales y comprobantes TEF.

---
*Para la visión estratégica y valuación, ver [ESTRATEGIA_MAESTRA_FINANCIERA.md](file:///c:/Users/abustamante/TheQaiCo/Empresa/03_ADMINISTRACION_FINANZAS/ESTRATEGIA_MAESTRA_FINANCIERA.md)*
