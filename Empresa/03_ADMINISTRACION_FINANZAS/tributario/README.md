# Tributario

> **Declaraciones tributarias e índices de comprobantes**

---

## 📋 Contenido

Esta carpeta contiene:
- **Cálculos previos** de declaraciones (CSV):
  - `f29_AAAAMM_calculos.csv`
  
- **Índices de declaraciones** (Markdown con links a Drive):
  - `_index_declaraciones.md` (por mes)
  - `_index_renta.md` (anual)

---

## 🗂️ Organización

```
tributario/
├── 2025/
│   ├── 01-enero/
│   │   ├── f29_202501_calculos.csv
│   │   └── _index_declaraciones.md
│   ├── 12-diciembre/
│   │   └── (misma estructura)
│   └── anual/
│       └── _index_renta.md
└── 2026/
    └── (misma estructura)
```

---

## 📄 Formato de Cálculos F29

### f29_AAAAMM_calculos.csv

```csv
Codigo,Descripcion,Monto
15,Ventas y/o Servicios del Giro,1000000
103,Exportaciones,950000
27,Débito Fiscal Total,190000
30,Compras Nacionales,100000
31,Crédito por Compras,19000
57,IVA Retenido Total,9025
37,Total Crédito Fiscal,28025
89,Diferencia Débito-Crédito,161975
90,Remanente mes anterior,0
91,IVA a Pagar,161975
150,Base Imponible PPM,1950000
151,PPM (0.25%),4875
93,TOTAL A PAGAR,166850
```

**Uso**: Este CSV sirve como borrador antes de declarar en el SII.

---

## 📝 Índice de Declaraciones

### Ejemplo: _index_declaraciones.md

```markdown
# Índice de Declaraciones Tributarias - Diciembre 2025

**Carpeta Google Drive**: [📁 Ver carpeta](https://drive.google.com/...)

## Declaraciones Mensuales (F29)

| Período | Fecha Declaración | Débito | Crédito | A Pagar | Comprobante | Pago |
|---------|-------------------|--------|---------|---------|-------------|------|
| Dic 2025 | 2026-01-15 | $190.000 | $28.025 | $166.850 | [PDF](link) | [PDF](link) |

## Estado
- ✅ Declarado
- ✅ Pagado
- 📄 Comprobantes guardados en Drive
```

### Ejemplo: _index_renta.md (Anual)

```markdown
# Declaración de Renta - 2025

**Carpeta Google Drive**: [📁 Ver carpeta](https://drive.google.com/...)

## Formulario 22 (F22)

| Año Tributario | Fecha Declaración | Ingresos | Gastos | Renta Líquida | Impuesto | Comprobante |
|----------------|-------------------|----------|--------|---------------|----------|-------------|
| 2025 | 2026-04-15 | $X | $Y | $Z | $W | [PDF](link) |

## Documentos de Respaldo
- Balance anual: [PDF](link)
- Estado de resultados: [PDF](link)
- Certificados de retención: [PDF](link)
```

---

## 🤖 Protocolo de Finn

### Al preparar F29 mensual:

1. **Consolidar datos** (del libro de compras/ventas del mes)
2. **Crear cálculos previos**: `f29_AAAAMM_calculos.csv`
3. **Presentar borrador** a Alejandro
4. **Al aprobar**:
   - Declarar en SII
   - Descargar comprobante de declaración
   - Subir PDF a Drive
   - Pagar
   - Subir comprobante de pago a Drive
   - Actualizar `_index_declaraciones.md`

### Al preparar F22 anual:

1. **Consolidar año completo**
2. **Generar balance** y estado de resultados
3. **Presentar borrador** a Alejandro
4. **Al aprobar**:
   - Declarar en SII
   - Subir comprobantes a Drive
   - Actualizar `_index_renta.md`

---

## 📊 Plazos Críticos

### F29 (IVA Mensual)
- **Plazo**: Hasta día **20** del mes siguiente (F29 electrónico)
- **Ejemplo**: Dic 2025 → Declarar hasta 20-Ene-2026

### F22 (Renta Anual)
- **Plazo**: **Abril** del año siguiente
- **Ejemplo**: Año tributario 2025 → Declarar en Abril 2026

---

## 🚨 Alertas de Finn

Finn enviará recordatorios automáticos:
- **7 días antes**: "F29 de [mes] vence [fecha]"
- **1 día antes**: 🚨 "F29 vence mañana"

---

## 📎 Respaldo Legal

**Retención**: 6 años (obligatorio SII)

**Guardar**:
- Comprobantes de declaración
- Comprobantes de pago
- Cálculos previos
- Libros contables asociados

---

**Responsable**: Finn (Agente Financiero)  
**Coordinación con**: Lex (en casos complejos)  
**Última actualización**: 27-Dic-2025
