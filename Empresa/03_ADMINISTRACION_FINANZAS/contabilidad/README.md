# Contabilidad

> **Libros contables e índices de facturas**

---

## 📋 Contenido

Esta carpeta contiene:
- **Libros contables mensuales** (CSV, git-friendly):
  - `libro_compras_AAAAMM.csv`
  - `libro_ventas_AAAAMM.csv`
  - `conciliacion_AAAAMM.csv`

- **Índices de facturas** (Markdown con links a Drive):
  - `_index_facturas.md` (por mes)

---

## 🗂️ Organización

```
contabilidad/
├── 2025/
│   ├── 01-enero/
│   │   ├── libro_compras_202501.csv
│   │   ├── libro_ventas_202501.csv
│   │   └── _index_facturas.md
│   └── 12-diciembre/
│       └── (misma estructura)
└── 2026/
    └── (misma estructura)
```

---

## 📄 Formato de Libros Contables

### libro_compras_AAAAMM.csv

```csv
Fecha,RUT,Proveedor,Factura,Neto,IVA,Total,Categoria,Archivo_Drive
2025-12-05,12.345.678-9,Hosting ABC,123,100000,19000,119000,Tecnología,https://drive.google.com/...
2025-12-15,98.765.432-1,Software XYZ,456,200000,38000,238000,Tecnología,https://drive.google.com/...
```

**Columnas**:
- `Fecha`: AAAA-MM-DD
- `RUT`: Con puntos y guión
- `Proveedor`: Nombre del proveedor
- `Factura`: Número de factura
- `Neto`: Monto sin IVA
- `IVA`: Monto del IVA (19%)
- `Total`: Neto + IVA
- `Categoria`: Clasificación contable
- `Archivo_Drive`: Link al PDF en Google Drive

### libro_ventas_AAAAMM.csv

```csv
Fecha,RUT,Cliente,Factura,Neto,IVA,Total,Proyecto,Archivo_Drive
2025-12-10,11.222.333-4,Cliente 001,1,1000000,190000,1190000,FedEx,https://drive.google.com/...
```

**Columnas**: Similar a libro_compras, pero con `Cliente` y `Proyecto`

### conciliacion_AAAAMM.csv

```csv
Fecha,Descripcion,Debito,Credito,Saldo,Conciliado
2025-12-01,Saldo inicial,0,0,500000,SI
2025-12-05,Pago hosting,-119000,0,381000,SI
2025-12-10,Cobro cliente,0,1190000,1571000,SI
```

---

## 📝 Índice de Facturas

Ver template en: `/QaiCore/agents/finn/knowledge_base/templates/` (crear próximamente)

**Ejemplo básico**:
```markdown
# Índice de Facturas - Diciembre 2025

**Carpeta Google Drive**: [📁 Ver carpeta](https://drive.google.com/...)

## Facturas Recibidas
| Fecha | Proveedor | Monto | Archivo |
|-------|-----------|-------|---------|
| 2025-12-05 | Hosting ABC | $119.000 | [PDF](https://drive.google.com/...) |
```

---

## 🤖 Protocolo de Finn

### Al registrar compra:
1. Subir PDF a Drive (carpeta `AAAA/MM-mes/Facturas Recibidas/`)
2. Agregar línea a `libro_compras_AAAAMM.csv`
3. Actualizar `_index_facturas.md`

### Al registrar venta:
1. Subir PDF a Drive (carpeta `AAAA/MM-mes/Facturas Emitidas/`)
2. Agregar línea a `libro_ventas_AAAAMM.csv`
3. Actualizar `_index_facturas.md`

### Al final del mes:
1. Consolidar libros
2. Generar conciliación bancaria
3. Cerrar mes (marcar como conciliado)

---

## 📊 Categorías Contables

Ver `plan_cuentas.md` (pendiente de crear con Finn)

**Ejemplos básicos**:
- Tecnología (hosting, software, APIs)
- Marketing (publicidad, branding)
- Legal (abogados, notarías)
- Administrativo (oficina, servicios)
- Financiero (bancos, intereses)

---

**Responsable**: Finn (Agente Financiero)  
**Última actualización**: 27-Dic-2025
