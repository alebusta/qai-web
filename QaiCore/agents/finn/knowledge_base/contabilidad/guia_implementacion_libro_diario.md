# Guía: Implementación Libro Diario en Google Sheets

> **Propósito**: Guía rápida para crear y configurar la pestaña `Libro_Diario` en Google Sheets `QAI_Finanzas_2026`

---

## 🎯 Objetivo

Crear la estructura formal del Libro Diario en Google Sheets para registrar asientos contables completos con débito y crédito balanceados.

---

## 📋 Pre-requisitos

- Acceso a Google Sheets `QAI_Finanzas_2026`
- ID del Spreadsheet: `1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw`
- Pestaña `Registro_Diario` existente (ya existe)

---

## 🛠️ Pasos de Implementación

### 1. Crear Pestaña "Libro_Diario"

**En Google Sheets**:
1. Abrir: [QAI_Finanzas_2026](https://docs.google.com/spreadsheets/d/1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw/edit)
2. Hacer clic en el botón "+" (agregar pestaña) al final
3. Renombrar la nueva pestaña como: `Libro_Diario`

---

### 2. Configurar Estructura de Columnas

**Fila 1 (Encabezados)**:

| Columna | Encabezado | Formato | Notas |
|:---|:---|:---|:---|
| A | **Asiento #** | Texto | Ej: AS-001, AS-002 (mismo número para todas las filas de un asiento) |
| B | **Fecha** | Fecha (YYYY-MM-DD) | Fecha contable del movimiento |
| C | **Concepto** | Texto | Descripción clara (ej: "GitHub Copilot Pro - Suscripción Enero 2026") |
| D | **Cuenta** | Texto | Código completo (ej: `61.01.03 Suscripciones Tech`) |
| E | **Débito** | Número (CLP) | Monto a débito (dejar vacío si es crédito) |
| F | **Crédito** | Número (CLP) | Monto a crédito (dejar vacío si es débito) |
| G | **Notas** | Texto | Info adicional (ej: "Doc. 46 pendiente", "Dólar obs. $896,89") |

**Formato Recomendado**:
- **Fila 1**: Negrita, fondo gris claro, texto centrado
- **Columna E (Débito)**: Formato número chileno (punto para miles, coma para decimales)
- **Columna F (Crédito)**: Formato número chileno (punto para miles, coma para decimales)
- **Columnas A, B, D**: Texto alineado izquierda
- **Columna G**: Texto alineado izquierda, wrap text activado

---

### 3. Agregar Validaciones y Fórmulas

#### Validación de Equilibrio por Asiento

**Fila 2 en adelante** (en columna H, "Validación"):

**Fórmula sugerida** (columna H, fila 2):
```excel
=IF(
  SUMIF($A$2:$A$1000, A2, $E$2:$E$1000) = SUMIF($A$2:$A$1000, A2, $F$2:$F$1000),
  "✅ Balanceado",
  IF(
    SUMIF($A$2:$A$1000, A2, $E$2:$E$1000) = 0,
    "",
    "❌ Desbalanceado: " & TEXT(SUMIF($A$2:$A$1000, A2, $E$2:$E$1000) - SUMIF($A$2:$A$1000, A2, $F$2:$F$1000), "#,##0.00")
  )
)
```

**Explicación**:
- Suma todos los débitos del mismo Asiento #
- Suma todos los créditos del mismo Asiento #
- Si son iguales: "✅ Balanceado"
- Si son diferentes: "❌ Desbalanceado: $[diferencia]"

#### Resumen Total (Al final de la hoja)

**Agregar filas de resumen** (ej: después de fila 1000):

```
=== RESUMEN TOTAL ===
Total Débitos: =SUM(E:E)
Total Créditos: =SUM(F:F)
Diferencia: =SUM(E:E) - SUM(F:F)  (debe ser $0)
Estado: =IF(SUM(E:E) = SUM(F:F), "✅ EQUILIBRADO", "❌ DESBALANCEADO")
```

---

### 4. Configurar Lista de Cuentas (Opcional pero Recomendado)

**Validación de Datos en Columna D (Cuenta)**:

1. Seleccionar columna D (excepto encabezado)
2. Datos → Validación de datos
3. Criterios: Lista de un rango
4. Rango: Crear pestaña "Lista_Cuentas" con todas las cuentas del Plan de Cuentas

**O alternativa simple**: Permitir cualquier valor pero agregar nota en README sobre cuentas válidas.

---

### 5. Formato Condicional (Opcional)

**Para facilitar visualización**:

1. **Fila de encabezado**: Fondo gris, texto blanco, negrita
2. **Filas del mismo asiento**: Color de fondo alternado (blanco/gris muy claro)
3. **Validación**: 
   - Si "✅ Balanceado": Sin formato
   - Si "❌ Desbalanceado": Fondo rojo claro

**Formato condicional sugerido** (columna H):
- Si contiene "❌": Fondo rojo claro, texto rojo oscuro
- Si contiene "✅": Sin formato adicional

---

## 📝 Ejemplo de Estructura Completa

**Fila 1 (Encabezados)**:
```
| Asiento # | Fecha | Concepto | Cuenta | Débito | Crédito | Notas | Validación |
```

**Fila 2-5 (Ejemplo Asiento AS-001)**:
```
| AS-001 | 2026-01-09 | GitHub Copilot Pro - Suscripción Enero 2026 | 61.01.03 Suscripciones Tech | 9250,00 | | | |
| AS-001 | 2026-01-09 | GitHub Copilot Pro - Suscripción Enero 2026 | 81.01 IVA Crédito Fiscal | 1704,09 | | | |
| AS-001 | 2026-01-09 | GitHub Copilot Pro - Suscripción Enero 2026 | 11.02 Banco Chile | | 9250,00 | | |
| AS-001 | 2026-01-09 | GitHub Copilot Pro - Suscripción Enero 2026 | 21.04 Proveedores Extranjeros | | 1704,09 | Doc. 46 pendiente | ✅ Balanceado |
```

**Validación Automática** (columna H):
- Fórmula calculará: Débitos ($9.250,00 + $1.704,09 = $10.954,09) = Créditos ($9.250,00 + $1.704,09 = $10.954,09)
- Resultado: "✅ Balanceado"

---

## ✅ Criterios de Éxito

- ✅ Pestaña `Libro_Diario` creada en Google Sheets
- ✅ Estructura de columnas configurada (Asiento #, Fecha, Concepto, Cuenta, Débito, Crédito, Notas)
- ✅ Validación de equilibrio agregada (columna Validación)
- ✅ Resumen total agregado al final (Total Débitos, Total Créditos, Diferencia)
- ✅ Formato aplicado (negrita encabezados, formato número CLP)

---

## 🔗 Referencias Relacionadas

- **Plan de Cuentas**: [`plan_cuentas.md`](plan_cuentas.md)
- **Playbook Generación Asientos**: [`../../playbooks/generar_asientos_libro_diario.md`](../../playbooks/generar_asientos_libro_diario.md)
- **Registro Movimientos**: [`../../playbooks/registro_movimiento_bancario.md`](../../playbooks/registro_movimiento_bancario.md)

---

**Versión**: 1.0  
**Creado**: 10-Ene-2026  
**Responsable**: Finn (CFO QAI)  
**Revisión**: Cuando cambien necesidades de estructura contable

