# Índice de Comprobantes – Drive y búsqueda rápida

> **Uso**: Respuesta a preguntas tipo *"¿dónde está la factura de Cursor de enero?"* o *"comprobante GitHub enero"*.  
> **Búsqueda**: Ctrl+F por **Proveedor** (Cursor, GitHub, E-Cert, Namecheap…) o por **Período** (2026-01, Enero, Febrero).

---

## Cómo usar este índice

| Si buscas… | Haz… |
|------------|------|
| Factura de un proveedor | Ctrl+F → nombre del proveedor (ej. `Cursor`, `GitHub`) |
| Comprobantes de un mes | Ctrl+F → `2026-01` (enero) o `2026-02` (febrero) o texto `Enero`/`Febrero` |
| Compras nacionales (IVA) | Filtra **Tipo** = Factura Chile o revisa carpeta `01-Compras_Chile_DTE` |
| SaaS / extranjero | Filtra **Tipo** = Receipt/Invoice extranjero o carpeta `04-Operaciones_Extranjeras_Doc46` |

**Mantenimiento**: Cada vez que subas un comprobante a Drive, agrega una fila a la tabla de abajo y guarda el link. Ver [Diseño Respaldo e Indexación](DISENO_RESPALDO_E_INDEXACION.md).

---

## Tabla de comprobantes (por período y proveedor)

| Período | Proveedor / Concepto | Tipo | Archivo | Link Drive | Carpeta (ruta lógica) |
|---------|----------------------|------|---------|------------|------------------------|
| 2026-01 | **Cursor** – Suscripción mensual | Invoice extranjero | Invoice-23T8JEF0-0002.pdf | [Abrir](https://drive.google.com/file/d/10_Fq2QtUWHo7q-rzDZyE02BZegmJ3L16/view?usp=drivesdk) | Contabilidad/2026/01-Enero/04-Operaciones_Extranjeras_Doc46 |
| 2026-01 | **GitHub** – Copilot Pro enero | Invoice extranjero | INV115166123.pdf | [Abrir](https://drive.google.com/file/d/1IkCaCrKLa2hSoUPWvjW_KI0ZZgbKFrZH/view?usp=drivesdk) | Contabilidad/2026/01-Enero/04-Operaciones_Extranjeras_Doc46 |
| 2026-01 | **Google One** / AI Pro | Receipt | GoogleOneReceipt_202601.pdf | [Abrir](https://drive.google.com/file/d/1tHzIPAFCteX0QxhbPqr07baRQHd_9Yew/view?usp=drivesdk) | Contabilidad/2026/01-Enero/04-Operaciones_Extranjeras_Doc46 |
| 2026-02 | **E-Cert Chile** – Certificado digital | Factura Chile (IVA) | factura_ecert.pdf | [Abrir](https://drive.google.com/file/d/18agXUziBJbBQJW6YgfufIloc-Jz118-G/view?usp=drivesdk) | Contabilidad/2026/02-Febrero |
| 2026-02 | **Cursor** – Feb-Mar | Invoice extranjero | Invoice-23T8JEF0-0003.pdf | [Abrir](https://drive.google.com/file/d/11nB1xhev81yLDpBB3LOUYdu1Tn8hziXz/view?usp=drivesdk) | Contabilidad/2026/02-Febrero/04-Operaciones_Extranjeras_Doc46 |
| 2026-02 | **Namecheap** – Dominio theqai.co | Invoice extranjero | namecheap-order-194911733.pdf | [Abrir](https://drive.google.com/file/d/1M4o_s4NUnsDZUkN19q89QhQznpcVnao4/view?usp=drivesdk) | Contabilidad/2026/02-Febrero/04-Operaciones_Extranjeras_Doc46 |
| 2026-02 | Cartola bancaria | Cartola | cartola (1).xls | [Abrir](https://docs.google.com/spreadsheets/d/1O1k6I67ACdNEri17fewLjTf4GmSAu85q/edit?usp=drivesdk) | Contabilidad/2026/02-Febrero/05-Bancos_Cartolas_y_Pagos |

*(IDs de archivo para integraciones: ver DISENO_RESPALDO_E_INDEXACION.md sección Referencia de IDs.)*

---

## Estructura de carpetas Drive (resumen)

```
Contabilidad (raíz)
└── 2026/
    ├── 01-Enero/
    │   ├── 01-Compras_Chile_DTE
    │   ├── 02-Ventas_Chile_DTE
    │   ├── 03-Gastos_Sin_Iva_y_Honorarios
    │   ├── 04-Operaciones_Extranjeras_Doc46   ← Cursor, GitHub, Google, SaaS
    │   └── 05-Bancos_Cartolas_y_Pagos
    └── 02-Febrero/
        └── (misma estructura)
```

**Regla**: Todo comprobante de **operación extranjera** (Cursor, GitHub, Namecheap, etc.) va en `04-Operaciones_Extranjeras_Doc46` del mes correspondiente.

---

**Última actualización**: 19-Feb-2026 (Finn – diseño indexación)  
**Responsable de mantener**: Quien suba comprobantes; Finn puede proponer filas al agregar registros.
