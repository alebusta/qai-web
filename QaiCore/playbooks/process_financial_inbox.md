# Playbook: Procesar Documentos en Landing Zone (Finn)

> **Workflow para que Finn procese automáticamente facturas y boletas desde la Landing Zone.**

---

## 🎯 Objetivo

Eliminar la fricción manual de registro. Pasar de un archivo PDF/Imagen a una fila en el Runway Master y el archivo organizado en Drive en un solo paso.

---

## 🔄 Trigger (Cuándo ejecutar)

- Hay archivos nuevos en `/TorreDeControl/temp_files/`
- Usuario solicita: "Finn, procesa los nuevos documentos" o "Registra este gasto"

---

## 📋 Pre-requisitos

- Finn agent cargado con acceso a `gsheets.py` y `gdrive.py`
- Existencia del archivo `Runway Master` en Google Sheets (si no existe, Finn debe crearlo)
- Estructura de carpetas en Google Drive configurada

---

## 🛠️ Pasos del Workflow

### 1. Detección y Extracción
```markdown
ACCIÓN: 
- Listar archivos en `/TorreDeControl/temp_files/`
- Para cada archivo:
  1. Usar `extract_content` para obtener Fecha, Monto, Proveedor e Items.
  2. Determinar si es Gasto o Ingreso.
```

### 2. Clasificación FinOps (ADR-009)
```markdown
ACCIÓN: 
- Clasificar el ítem en una de las tres categorías maestras:
  - **Fijos**: Suscripciones, oficina, sueldos.
  - **Proyecto**: APIs o recursos usados para un cliente específico (ej: FedEx).
  - **R&D**: Innovación, pruebas de nuevas IAs.
```

### 3. Organización en Drive
```markdown
ACCIÓN: 
- Subir el archivo original a la carpeta correspondiente según el impacto tributario:
  - `01-Compras_Chile_DTE`: DTE locales.
  - `03-Gastos_Sin_Iva_y_Honorarios`: Honorarios y tickets exentos.
  - `04-Operaciones_Extranjeras_Doc46`: SaaS Internacional.
  - `05-Bancos_Cartolas_y_Pagos`: TEF y cartolas.
- Carpeta base: `/Empresa/03_ADMINISTRACION_FINANZAS/comprobantes/[Año]/[Mes]/`
```

### 4. Registro en Master Sheet (GSheets)

**⚠️ PROTOCOLO ZERO-LOSS FINANCE (CRÍTICO)**:
- **ANTES**: `.\QaiCore\qrun.bat .\QaiCore\tools\backup_finance.py`
- **DESPUÉS**: `.\QaiCore\qrun.bat .\QaiCore\tools\backup_finance.py`

**ACCIÓN**: 
- Usar `gsheets.py` para abrir el GSheet Master (`QAI_Finanzas_2026`).
- Agregar fila con: [Fecha] | [Tipo] | [Concepto] | [Categoría FinOps] | [Cuenta] | [Monto Neto] | [IVA] | [Retención] | [Monto Bruto] | [Monto Pagado] | [Proyecto] | [Link a Drive].

### 5. Actualización de Memoria (Torre de Control)
```markdown
ACCIÓN: 
- Registrar en `AGENT_ACTIVITY.md`: "Procesado documento [X] -> Registrado en Runway".
- Actualizar `STATUS.md`: Reflejar balance actual si es significativo.
- **LIMPIAR**: Borrar el archivo de `/TorreDeControl/temp_files/`.
```

---

## ✅ Criterios de Éxito

- `temp_files/` está vacía.
- El archivo vive en Google Drive organizado.
- Hay una nueva fila detallada en el Google Sheet del Runway.
- El log de actividad registra la operación.

---

**Versión**: 1.0  
**Fecha**: 29-Dic-2025  
**Autor**: Nzero (Arquitecto)
