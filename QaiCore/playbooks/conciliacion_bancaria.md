# Playbook: Conciliación Bancaria

> **Workflow para que Finn concilie movimientos registrados vs extracto bancario de Banco Chile**

---

## 🎯 Objetivo

Asegurar que todos los movimientos de la cuenta corriente `11.02 Banco Chile` estén correctamente registrados en el sistema contable, identificando discrepancias y resolviéndolas para mantener integridad financiera.

---

## 🔄 Trigger (Cuándo ejecutar)

- Alejandro comparte cartola/extracto bancario (quincenal o mensual)
- Usuario solicita: "Haz la conciliación bancaria del [período]"
- Antes de cerrar mes contable
- Cuando hay diferencia significativa entre saldo contable y saldo bancario

**Frecuencia Recomendada**:
- **Actual (movimientos mínimos)**: Mensual
- **Futuro (más movimientos)**: Quincenal o semanal según volumen

---

## 📋 Pre-requisitos

- Cartola/extracto bancario en formato PDF o Excel
- Acceso a Google Sheets (Registro Diario)
- Acceso a Google Drive (para archivar extracto)
- Herramienta de extracción de documentos (`document_processor.py`)

---

## 🛠️ Pasos del Workflow

### 1. Obtener Extracto Bancario

**Formatos Soportados**:
- PDF (extracto descargado del banco)
- Excel/CSV (si el banco permite exportar)
- Imagen escaneada (requiere OCR)

**⚠️ IMPORTANTE - Tipo de Extracto**:

**Cartola Parcial** (durante el mes):
- **Propósito**: Solo para procesar movimientos individuales pendientes de registro
- **Acción**: Extraer movimientos, registrar en `Registro_Diario`, archivar comprobantes individuales
- **NO ARCHIVAR**: Las cartolas parciales NO se archivan en Drive (ver protocolo `registro_movimiento_bancario.md`)

**Cartola Oficial** (fin de mes):
- **Propósito**: Conciliación bancaria mensual y referencia tributaria
- **Acción**: Usar para comparar con registros contables y archivar en Drive
- **Archivar**: Sí, en `/Empresa/03_ADMINISTRACION_FINANZAS/comprobantes/2026/[MM]-[mes]/` con nombre `cartola_oficial_banco_chile_[mes]_[año].pdf`

**Ubicación del Archivo**:
- Si está en `/TorreDeControl/temp_files/`: 
  - Si es cartola parcial: Procesar movimientos, NO archivar, eliminar después
  - Si es cartola oficial: Procesar para conciliación, archivar en Drive, eliminar del landing zone
- Si usuario comparte directamente: Usar ruta proporcionada

---

### 2. Extraer Movimientos del Extracto

**Usando `document_processor.py`**:

```bash
# Si es PDF:
.\QaiCore\qrun.bat .\QaiCore\tools\document_processor.py "ruta/al/extracto.pdf"

# Si es Excel:
.\QaiCore\qrun.bat .\QaiCore\tools\document_processor.py "ruta/al/extracto.xlsx"
```

**Información a Extraer**:
- **Saldo Inicial**: Saldo al inicio del período
- **Saldo Final**: Saldo al final del período
- **Movimientos**: Para cada movimiento:
  - Fecha
  - Concepto/Glosa
  - Monto (distinguir cargo vs abono)
  - Saldo después del movimiento

**Si la extracción automática falla**:
```
"⚠️ No pude extraer automáticamente los movimientos del extracto.
¿Puedes proporcionarme los datos clave? (Saldo inicial, saldo final, y lista de movimientos principales)"
```

---

### 3. Obtener Movimientos Registrados en Sistema

**Desde Google Sheets `Registro_Diario`**:

```bash
# Leer movimientos del período desde Google Sheets
.\QaiCore\qrun.bat .\QaiCore\tools\gsheets.py --spreadsheet_id 1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw --read "Registro_Diario!A1:M100"
```

**Filtrar por**:
- Fecha del período a conciliar
- Solo movimientos que afectan `11.02 Banco Chile`
- Ordenar cronológicamente

**Estructura de Datos Esperada**:
```
| Fecha | Tipo | Concepto | Monto Bruto | Cuenta | Saldo Acumulado |
```

---

### 4. Comparar y Coincidir Movimientos

**Proceso de Matching**:

1. **Match Perfecto**:
   - Monto exacto
   - Fecha igual o muy cercana (±3 días)
   - Concepto similar

2. **Match por Monto y Fecha**:
   - Monto exacto
   - Fecha cercana (±5 días)
   - Concepto puede diferir (glosa bancaria vs concepto registrado)

3. **Match Parcial**:
   - Monto similar (dentro de ±1% tolerancia)
   - Fecha cercana
   - Requiere verificación manual

**Categorización de Resultados**:
- ✅ **Coincidencia**: Movimiento del extracto tiene correspondencia en registro
- ⚠️ **Posible Coincidencia**: Monto/fecha similar pero requiere verificación
- ❌ **Sin Coincidencia**: Movimiento en extracto NO está registrado
- 🔴 **Pendiente**: Movimiento registrado NO aparece en extracto (puede ser pendiente de procesar)

---

### 5. Identificar Discrepancias

**Tipos de Discrepancias Comunes**:

| Tipo | Causa Posible | Acción |
|:---|:---|:---|
| Movimiento en extracto no registrado | Olvido o movimiento nuevo | Registrar movimiento faltante |
| Movimiento registrado no en extracto | Pendiente de procesar o fecha futura | Verificar fecha y estado |
| Monto diferente | Error de registro o comisión no considerada | Corregir monto registrado |
| Saldo no coincide | Movimientos faltantes o error acumulado | Revisar todos los movimientos del período |

**Cálculo de Diferencias**:

```
Saldo Final (Extracto) - Saldo Final (Contable) = Diferencia
```

**Si diferencia > $1.000 CLP**:
- Investigar movimientos no coincidentes
- Verificar cálculos acumulados
- Revisar movimientos del período anterior

---

### 6. Resolver Discrepancias con Usuario

**Para cada discrepancia identificada**:

**Movimiento en Extracto NO Registrado**:
```
"Encontré un movimiento en el extracto que no está registrado:
- Fecha: [fecha]
- Concepto: [concepto]
- Monto: $[X]

¿Qué es este movimiento? ¿Debo registrarlo como [clasificación sugerida]?"
```

**Monto Diferente**:
```
"Hay diferencia en el monto de este movimiento:
- Registrado: $[X] en [fecha] - [concepto]
- Extracto: $[Y] en [fecha] - [concepto]

¿Hay comisión o ajuste que no consideré? ¿Corrijo el registro a $[Y]?"
```

**Movimiento Registrado NO en Extracto**:
```
"Tengo registrado un movimiento que no aparece en el extracto:
- Fecha: [fecha]
- Concepto: [concepto]
- Monto: $[X]

¿Este movimiento ya se procesó o está pendiente? ¿Mantengo el registro o lo marco como pendiente?"
```

---

### 7. Actualizar Registros y Saldos

**Acciones Correctivas**:

1. **Registrar movimientos faltantes**:
   - Seguir protocolo de `registro_movimiento_bancario.md`
   - Usar información del extracto bancario
   - Confirmar clasificación con usuario si es necesario

2. **Corregir montos erróneos**:
   - Actualizar fila en Google Sheet `Registro_Diario`
   - Recalcular saldos acumulados
   - Agregar nota explicando corrección

3. **Marcar movimientos pendientes**:
   - Si movimiento registrado aún no aparece en extracto:
     - Agregar nota: "Pendiente de procesar - Extracto [fecha]"
     - Verificar en próxima conciliación

4. **Actualizar saldo contable**:
   - Recalcular saldo final del período
   - Verificar que coincide con saldo final del extracto
   - Si aún hay diferencia pequeña (<$1.000): Investigar redondeos o comisiones menores

---

### 8. Generar Reporte de Conciliación

**Formato del Reporte**:

```markdown
# Conciliación Bancaria - Banco Chile - [Mes] [Año]

## Período
- Inicio: [fecha] - Saldo: $[X]
- Fin: [fecha] - Saldo: $[Y]
- Diferencia de Período: $[Z]

## Resumen de Movimientos
- Total Movimientos en Extracto: [N]
- Total Movimientos Registrados: [M]
- Coincidencias: [X] ✅
- Discrepancias Resueltas: [Y] ⚠️
- Pendientes: [Z] 🔴

## Saldos Finales
- Saldo Extracto Bancario: $[A]
- Saldo Contable (11.02 Banco Chile): $[B]
- Diferencia: $[C] (✅ Conciliado / ⚠️ Pendiente)

## Movimientos Pendientes (si hay)
1. [Descripción del movimiento pendiente]
   - Fecha Registro: [fecha]
   - Monto: $[X]
   - Estado: Pendiente de procesar
```

**Guardar Reporte**:
- Ubicación: `/Empresa/03_ADMINISTRACION_FINANZAS/contabilidad/2026/[MM]-[mes]/conciliacion_[AAAAMM].md`
- Actualizar índice de contabilidad si existe

---

### 9. Archivar Extracto Bancario Oficial

**⚠️ IMPORTANTE - Solo Archivar Cartola Oficial de Fin de Mes**:

**Filosofía QAI: Simplicidad y Cumplimiento**

1. **Cartola Oficial de Fin de Mes** (SÍ ARCHIVAR):
   - **Propósito**: Referencia tributaria y conciliación mensual
   - **Cuándo**: Al finalizar el mes, cuando el banco emite el extracto oficial
   - **Acción**: 
     - Subir a Google Drive: `/Empresa/03_ADMINISTRACION_FINANZAS/comprobantes/2026/[MM]-[mes]/`
     - Nombre: `cartola_oficial_banco_chile_[mes]_[año].pdf` (o `cartola_oficial_banco_chile_[mes]_[año].xlsx`)
     - Descripción: "Cartola oficial Banco Chile [Mes] [Año] - Conciliada [fecha]"
   - **⚠️ IMPORTANTE**: Si el archivo estaba en `/TorreDeControl/temp_files/`:
     - **Eliminarlo** después de subirlo a Drive
     - Mantener landing zone limpia (protocolo Zero Inbox)
   - Actualizar referencia en reporte de conciliación con link de Drive

2. **Cartolas Parciales** (NO ARCHIVAR):
   - **Propósito**: Solo para procesar movimientos individuales durante el mes
   - **Acción**: Extraer movimientos, registrar en `Registro_Diario`, archivar comprobantes individuales
   - **NO ARCHIVAR**: Las cartolas parciales NO se archivan en Drive (evita duplicados)
   - **Excepciones**: Solo archivar si hay discrepancia significativa que requiere investigación posterior
   - **⚠️ IMPORTANTE**: Si el archivo estaba en `/TorreDeControl/temp_files/`:
     - **Eliminarlo** después de procesar movimientos (NO subir a Drive)
     - Mantener landing zone limpia

**Razones de esta Regla**:
- ✅ **Simplicidad**: Evita duplicados (parcial vs oficial)
- ✅ **Cumplimiento**: Solo la oficial tiene validez contable/tributaria
- ✅ **Trazabilidad**: Cada movimiento ya está registrado individualmente con su comprobante
- ✅ **Eficiencia**: Reduce trabajo duplicado y riesgo de inconsistencias

---

### 10. Actualizar Estado de Conciliación

**En Google Sheets `Registro_Diario`**:
- Agregar columna "Conciliado" (si no existe)
- Marcar movimientos conciliados con "✅ [fecha conciliación]"
- O crear pestaña separada "Conciliacion_[AAAAMM]" con resumen

**En STATUS.md o INBOX.md** (si aplica):
- Registrar: "✅ Conciliación bancaria [mes] completada - Sin discrepancias" o "⚠️ Conciliación [mes] - [X] discrepancias resueltas"

---

## ✅ Criterios de Éxito

- ✅ Todos los movimientos del extracto están registrados o identificados
- ✅ Saldo contable coincide con saldo bancario (o diferencia explicada)
- ✅ Discrepancias resueltas o documentadas
- ✅ **Cartola oficial de fin de mes archivada en Drive** (NO cartolas parciales)
- ✅ Reporte de conciliación generado y guardado
- ✅ Movimientos marcados como "Conciliado" en sistema
- ✅ Landing zone limpia (archivos eliminados después de procesar)

---

## 🚨 Casos Especiales

### Diferencia Pequeña (<$1.000 CLP)

**Si hay diferencia pequeña y no se encuentran movimientos faltantes**:
- **Causas comunes**: Redondeos, comisiones menores no registradas, diferencias de cambio
- **Acción**: Documentar en reporte como "Diferencia menor - Aceptada" con explicación
- **Nota**: Si la diferencia se acumula en períodos siguientes, investigar

### Movimientos de Períodos Anteriores

**Si aparecen movimientos de meses anteriores**:
- Registrar en el período correcto (mes original)
- Ajustar saldos acumulados desde ese período
- Documentar en reporte como "Ajuste de período anterior"

### Extracto con Errores del Banco

**Si hay error evidente en el extracto**:
- Documentar error
- Contactar banco si es necesario
- Mantener registro contable correcto
- Registrar ajuste cuando banco corrija

---

## 📝 Notas para Finn

- **Frecuencia**: Conciliar mensualmente mientras movimientos sean mínimos. Ajustar a quincenal o semanal cuando volumen aumente.
- **Automatización Futura**: Si volumen aumenta, considerar automatizar extracción y matching inicial
- **Documentación**: Siempre documentar discrepancias y su resolución para trazabilidad
- **Prudencia**: Si hay duda sobre un movimiento, preguntar antes de ajustar

---

## 🔗 Referencias Relacionadas

- **Plan de Cuentas**: [`/QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md`](../QaiCore/agents/finn/knowledge_base/contabilidad/plan_cuentas.md)
- **Protocolo Registro Bancario**: [`registro_movimiento_bancario.md`](registro_movimiento_bancario.md)
- **Herramienta Extracción**: [`/QaiCore/tools/document_processor.py`](../tools/document_processor.py)
- **Banco Chile Detalles**: [`/QaiCore/agents/finn/knowledge_base/finops/banco_chile_details.md`](../QaiCore/agents/finn/knowledge_base/finops/banco_chile_details.md)

---

**Versión**: 1.0  
**Creado**: 10-Ene-2026  
**Responsable**: Finn (CFO QAI)  
**Revisión**: Cuando cambien patrones de movimientos o se automatice parcialmente

