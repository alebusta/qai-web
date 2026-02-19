# Knowledge Base (Finn): Teoría y Procesamiento

> **Propósito**: Este es el cerebro interno de Finn. Contiene la investigación y los procesos técnicos que NO necesitan saturar el HQ de Alejandro.

---

## 1. Contabilidad y Plan de Cuentas
- **[Plan de Cuentas Completo](contabilidad/plan_cuentas.md)** 🆕 - Estructura jerárquica completa de cuentas contables (minimalista pero escalable)
  - Cuenta específica: `11.02 Banco Chile` (operativa)
  - Reserva: `11.03 BancoEstado` (backup sin movimientos)
  - Tabla de decisión rápida para clasificación
  - Estructura escalable para futuras cuentas
- **[Explicación Diferencias de Cambio](contabilidad/explicacion_diferencias_cambio.md)** 🆕 - Manejo de diferencias entre dólar observado (SII) y tipo de cambio bancario, y uso de decimales en CLP
- **[Guía Implementación Libro Diario](contabilidad/guia_implementacion_libro_diario.md)** 🆕 - Guía rápida para crear y configurar la pestaña `Libro_Diario` en Google Sheets

---

## 2. Normativas y Regulaciones
- [IVA Básico - Chile](normativas/iva_basico.md)
- [Gastos Personales con Uso Empresarial](normativas/gastos_personales_uso_empresarial.md)

---

## 3. Información de Proveedores
- [Google Workspace - Información](proveedores/google_workspace_info.md)
- [Contacto Soporte Google](proveedores/contacto_google.md)
- [Caso Google One - Suscripción Perfil Incorrecto](proveedores/caso_google_one_2026.md)

---

## 4. FinOps y Costos
- [Marco FinOps Master](finops/marco_finops_master.md) - Categorización agnóstica de costos (Fijo/Proyecto/R&D)
- [Google Cloud Billing](finops/google_cloud_billing.md)
- [Banco Chile - Detalles Cuenta](finops/banco_chile_details.md)

---

## 5. Protocolos y Playbooks

**Registro Financiero**:
- [Registro de Gastos/Ingresos](../../playbooks/registrar_gasto_ingreso.md) - Workflow completo para registrar operaciones diarias
- [Registro de Movimientos Bancarios](../../playbooks/registro_movimiento_bancario.md) 🆕 - Protocolo específico para movimientos de cuenta corriente (Registro Diario operativo diario)
- [Generar Asientos Formales - Libro Diario](../../playbooks/generar_asientos_libro_diario.md) 🆕 - Workflow para generar asientos contables formales desde Registro Diario al Libro Diario (mensual/quincenal)
- [Conciliación Bancaria](../../playbooks/conciliacion_bancaria.md) 🆕 - Proceso quincenal/mensual de conciliación con extracto bancario

**Facturación**:
- [Facturación Cliente SaaS](../../playbooks/facturar_cliente_saas.md) - Flujo completo desde OC hasta cobranza

**Referencias**:
- Todos los playbooks referencian el [Plan de Cuentas](contabilidad/plan_cuentas.md) para clasificación consistente

**Búsqueda de comprobantes (Drive)**:
- Para preguntas tipo *"¿dónde está la factura de [proveedor] de [mes]?"*: consultar primero el **Índice de comprobantes** en el HQ: `Empresa/03_ADMINISTRACION_FINANZAS/INDICE_COMPROBANTES.md` (búsqueda por proveedor o período). Si no hay fila, listar la carpeta Drive del mes (p. ej. `04-Operaciones_Extranjeras_Doc46`) y proponer agregar la fila al índice. Diseño completo: `Empresa/03_ADMINISTRACION_FINANZAS/DISENO_RESPALDO_E_INDEXACION.md`.

---

## 6. Templates
- [Template F29](templates/f29_template.md) - Plantilla para declaración IVA

---

## 7. Bitácora de Operaciones
- [Changelog Operativo Finn](changelog_operativo.md) - Historial de decisiones y aprendizajes

---

## 📚 Estructura Escalable

**Principio de Diseño**: 
- **Minimalista ahora**: Solo cuentas necesarias (11.02 Banco Chile operativa)
- **Escalable después**: Estructura numérica permite agregar nuevas cuentas sin reestructurar (ej: 11.04, 11.05 para otros bancos)

**Cuando agregar nuevas cuentas**:
1. Asignar siguiente número disponible
2. Actualizar Plan de Cuentas
3. Registrar en Changelog Operativo
4. Actualizar playbooks si es necesario
