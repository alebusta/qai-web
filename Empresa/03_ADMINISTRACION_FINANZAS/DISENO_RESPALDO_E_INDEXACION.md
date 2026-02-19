# Diseño: Respaldo en Drive e indexación de comprobantes

> **Objetivo**: Un solo lugar donde respaldar comprobantes, reglas claras de ubicación y un índice que permita responder en segundos *"¿dónde está la factura de X del mes Y?"* (humano o agente).

---

## 1. Principios del diseño

| Principio | Aplicación |
|-----------|------------|
| **Una estructura por mes** | Cada mes tiene las mismas 5 subcarpetas; no inventar carpetas nuevas. |
| **Un índice único** | [INDICE_COMPROBANTES.md](INDICE_COMPROBANTES.md) es la entrada de búsqueda: proveedor + período → link. |
| **Registro + Drive alineados** | Cada fila de Registro_Diario con comprobante debe tener link en columna Comprobante; el mismo documento debe estar en el índice. |
| **Sin duplicar** | El comprobante vive en **una** carpeta según tipo; el índice solo apunta. |

---

## 2. Estructura Drive (obligatoria por mes)

Cada año tiene carpeta `Contabilidad/AAAA/`. Dentro de cada mes (ej. `01-Enero`, `02-Febrero`):

| Carpeta | Contenido | Ejemplos |
|---------|-----------|----------|
| **01-Compras_Chile_DTE** | Facturas electrónicas locales (con IVA) | E-Cert, proveedores chilenos |
| **02-Ventas_Chile_DTE** | Facturas emitidas por QAI | DTE ventas a clientes Chile |
| **03-Gastos_Sin_Iva_y_Honorarios** | Boletas honorarios, tickets, exentos | Ligia, peajes, boletas exentas |
| **04-Operaciones_Extranjeras_Doc46** | Invoices/receipts SaaS y extranjeros + Doc 46 | Cursor, GitHub, Google One, Namecheap, AWS |
| **05-Bancos_Cartolas_y_Pagos** | Cartolas oficiales, comprobantes TEF | Cartola mensual, transferencias |

**Regla de ubicación**: Si el gasto/compra es con **proveedor extranjero** (SaaS, cloud, dominio), el PDF va en **04-Operaciones_Extranjeras_Doc46** del mes de la fecha del documento. Si es **factura chilena con IVA**, en **01-Compras_Chile_DTE**.

---

## 3. Índice de comprobantes (INDICE_COMPROBANTES.md)

### Qué es
- Un único archivo Markdown con una **tabla**: Período | Proveedor | Tipo | Archivo | Link Drive | Carpeta.
- Permite búsqueda por texto (Ctrl+F): proveedor o período.

### Dónde está
- `Empresa/03_ADMINISTRACION_FINANZAS/INDICE_COMPROBANTES.md`

### Cuándo actualizarlo
- **Cada vez** que se suba un comprobante a Drive: agregar una fila con el link.
- Al registrar un gasto/ingreso en Registro_Diario con comprobante: asegurar que el link esté en la columna Comprobante **y** que exista la fila en el índice (o agregarla).

### Búsqueda rápida (humanos y agentes)
- **Humano**: Abrir INDICE_COMPROBANTES.md, Ctrl+F por "Cursor", "enero", "2026-01", etc.
- **Finn / agente**: Leer el archivo (o la sección relevante) y filtrar por proveedor o período; devolver el link de la fila que coincida.

---

## 4. Flujo al agregar un comprobante

```text
1. Subir el PDF/archivo a la carpeta correcta del mes (según tabla de §2).
2. Copiar el link de “Compartir” o “Obtener enlace” de Drive.
3. En Registro_Diario (Google Sheet): en la fila del movimiento, pegar el link en columna Comprobante.
4. En INDICE_COMPROBANTES.md: agregar una fila a la tabla con Período, Proveedor, Tipo, nombre del archivo, Link, Carpeta.
5. Si el documento es de operación extranjera y quedó en la raíz del mes por error, moverlo a 04-Operaciones_Extranjeras_Doc46 y opcionalmente actualizar la fila del índice (el link de Drive no cambia al mover).
```

---

## 5. Acción de organización completada (19-Feb-2026)

- **Archivo**: `Invoice-23T8JEF0-0002.pdf` (Cursor enero 2026).  
- **Hecho**: Movido de Contabilidad/2026/01-Enero (raíz) a **01-Enero/04-Operaciones_Extranjeras_Doc46** vía `gdrive.py --move`. Índice actualizado.

---

## 6. Referencia de IDs de carpetas (Drive)

Para scripts o consultas por API (ej. `gdrive.py --list`):

| Ruta lógica | Folder ID |
|-------------|-----------|
| Contabilidad 2026 | `1Hw-fTHx6olO0s6ygqjs_kuZAu_4gukiM` |
| 2026/01-Enero | `1M_aOIOpEryla3vqXfmPttEuVhmgRGnse` |
| 2026/01-Enero/04-Operaciones_Extranjeras_Doc46 | `1hoHbJX4OgljPWtfWmpukel7-R9BBhre6` |
| 2026/02-Febrero | `1yw9WQmljA93-vajeIQ7s2ImpBdvg3Z3g` |
| 2026/02-Febrero/04-Operaciones_Extranjeras_Doc46 | `1ruEi0TRy9dqKYH_YqDkD9-TuzLMv_az0` |

*(Raíz Contabilidad en config: `contabilidad_id` en `.qai/config/gdrive_folders.json`.)*

---

## 7. Mantenimiento

- **Revisión mensual**: Al cerrar el mes, comprobar que todo comprobante del Registro_Diario tenga link en el Sheet y fila en el índice.
- **Nuevos meses**: Al crear la carpeta del mes (ej. 03-Marzo), replicar las 5 subcarpetas y seguir la misma convención.
- **Finn**: Al responder “¿dónde está la factura de [X] de [mes]?”, consultar primero INDICE_COMPROBANTES.md; si no hay fila, listar la carpeta Drive del mes (04 si es extranjero) y proponer agregar la fila al índice.

---

**Versión**: 1.0  
**Fecha**: 19-Feb-2026  
**Autor**: Finn (agente financiero), documentación operativa QAI
