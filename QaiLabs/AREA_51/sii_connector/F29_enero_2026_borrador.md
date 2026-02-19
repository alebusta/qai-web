# F29 Enero 2026 – Borrador y plan de declaración

**Período:** Enero 2026  
**Vencimiento:** 20-Feb-2026 (declaración electrónica)  
**Estado:** Borrador listo para aprobación y envío (corregido 19-Feb-2026)  
**Origen datos:** Registro_Diario – QAI_Finanzas_2026 (consulta 19-Feb-2026)

---

## 1. Resumen ejecutivo

| Concepto | Monto (CLP) |
|----------|--------------|
| **IVA a pagar (91)** | **0** |
| **PPM (151)** | **0** |
| **Total a pagar (93)** | **0** |
| **Remanente a favor (para Feb)** | **0** |

Declaración **sin movimiento** en IVA: no ventas afectas en enero, no se utiliza aún crédito por facturas extranjeras (Doc. 46). La única factura en pesos (compras nacionales) es E-Cert y es de **febrero**; por eso no entra en este F29 (enero).

---

## 2. Criterios aplicados (revisión)

- **Facturas extranjeras / Doc. 46:** Hoy **no** se está aprovechando el IVA de facturas de compra (Doc. 46) de servicios extranjeros. Por tanto, en este F29 **no** se declara crédito en código 57. Los gastos GitHub Copilot, Cursor, etc. siguen en Registro_Diario para F22 y control; no generan crédito fiscal en el F29 hasta que se habilite el uso de Doc. 46.
- **Única factura en pesos (compras nacionales afectas):** E-Cert Chile – Certificado Digital (03-Feb-2026). Es **compra nacional** en CLP con IVA (neto $15.990, IVA $3.038). Corresponde al **período febrero 2026** y se declarará en el **F29 de febrero**, no en el de enero. Por eso no aparece en este borrador.

---

## 3. Movimientos del mes (enero 2026) – base del F29

### Ingresos / ventas
- **Ninguno** con IVA en enero 2026.

### Compras nacionales afectas (código 30/31)
- **Ninguna en enero.** La única compra nacional en pesos con IVA registrada es E-Cert (fecha 03-Feb-2026 → F29 febrero).

### Gastos sin IVA para F29 (solo F22)
- 2026-01-08 – Google One / Google AI Pro – $7.330 (a nombre personal; sin Doc. 46)
- 2026-01-19 – Cursor Pro – $18.200
- 2026-01-09 – GitHub Copilot Pro – $9.250 (Doc. 46 no utilizado como crédito fiscal por ahora)

### No afectan IVA
- 2026-01-07 – Préstamo socio – $50.000 (cuenta 21.01)

---

## 4. Códigos F29 – Valores a declarar

### SECCIÓN A: Débito fiscal
| Código | Concepto | Valor (CLP) |
|--------|----------|------------|
| 15 | Ventas y/o servicios del giro (neto) | 0 |
| 103 | Exportaciones | 0 |
| **27** | **Débito fiscal total (15 × 19%)** | **0** |

### SECCIÓN B: Crédito fiscal
| Código | Concepto | Valor (CLP) |
|--------|----------|------------|
| 30 | Compras nacionales afectas (neto) | 0 |
| 31 | Crédito por compras nacionales (30 × 19%) | 0 |
| 57 | IVA retenido (Doc. 46) | **0** (no se utiliza aún) |
| **37** | **Total crédito fiscal (31 + 57)** | **0** |

### SECCIÓN C: Determinación del IVA
| Código | Concepto | Valor (CLP) |
|--------|----------|------------|
| 89 | Diferencia (27 − 37) | 0 |
| 90 | Remanente mes anterior (dic-2025) | 0 |
| **91** | **IVA a pagar** | **0** |

### SECCIÓN D: PPM
| Código | Concepto | Valor (CLP) |
|--------|----------|------------|
| 150 | Base imponible PPM (15 + 103) | 0 |
| 151 | PPM (0,25% sobre 150) | 0 |

### TOTAL
| Código | Concepto | Valor (CLP) |
|--------|----------|------------|
| **93** | **Total a pagar** | **0** |

---

## 5. Plan de ejecución (pasos a seguir)

### Antes del 20-Feb-2026
1. [ ] **Revisar borrador** – Confirmar criterio: sin uso de Doc. 46; E-Cert solo en F29 febrero.
2. [ ] **Aprobación** – Alejandro aprueba montos (todo en 0).
3. [ ] **Entrar a SII** – Portal MIPYME / sii.cl con certificado digital.
4. [ ] **Completar F29 electrónico** – Período 01/2026; todos los códigos en 0 (sin movimiento).
5. [ ] **Declarar** – Enviar declaración y descargar comprobante.
6. [ ] **Guardar** – Comprobante F29 en carpeta respaldo.

### Para F29 febrero 2026
- **Compras nacionales (30/31):** Incluir E-Cert Chile (03-Feb): neto $15.990, IVA $3.038 (crédito fiscal).
- **Código 57 (Doc. 46):** Mantener en 0 hasta que se habilite el uso de IVA de facturas extranjeras.
- **Remanente (90):** 0.

---

**Generado por:** Finn (agente financiero QAI)  
**Fecha:** 19-Feb-2026  
**Ubicación:** Landing Zone `/TorreDeControl/temp_files/` (protocolo HQ limpio)  
**Fuente:** Registro_Diario – spreadsheet 1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw
