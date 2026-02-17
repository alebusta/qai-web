# Explicación: Diferencias de Cambio y Equilibrio Contable

> **Para Alejandro**: Explicación simple de cómo manejar diferencias de cambio manteniendo el equilibrio contable.

---

## 📚 La Ecuación Contable Fundamental

```
ACTIVO = PASIVO + CAPITAL + (INGRESOS - GASTOS)
```

**Traducido a QAI:**
- **ACTIVO**: Lo que tenemos (Banco Chile, Cuentas por Cobrar, etc.)
- **PASIVO**: Lo que debemos (Proveedores, Retenciones, etc.)
- **CAPITAL**: Lo que invirtieron los socios
- **(INGRESOS - GASTOS)**: La utilidad o pérdida del período

**Esta ecuación SIEMPRE debe balancearse.** Si aumenta el débito de un lado, debe aumentar el crédito del otro lado.

---

## 💰 El Problema: Dos Montos Diferentes

Cuando compras algo en USD, aparecen DOS valores:

1. **Monto para SII (Doc. 46)**: Usa dólar observado del Banco Central
   - Ejemplo: $10 USD × $896,89 = **$8.968,90 CLP**

2. **Monto Real del Banco**: Lo que realmente te cobraron
   - Ejemplo: **$9.250,00 CLP** (el banco puede usar un dólar diferente o agregar comisiones)

**La diferencia:** $9.250 - $8.968,90 = **$281,10 CLP**

---

## ✅ Solución Correcta: Mantener Equilibrio

### Opción 1: Método Completo (100% Preciso)

**Asiento 1: Registrar Gasto según Doc. 46 (Fecha emisión)**
```
Débito:  61.01.03 Suscripciones Tech    $8.968,90  (monto SII)
Débito:  81.01 IVA Crédito Fiscal       $1.704,09  (19% sobre monto SII)
Crédito: 21.04 Proveedores Extranjeros  $10.672,99 (total pendiente)
```

**Asiento 2: Registrar Pago Real del Banco (Fecha movimiento)**
```
Débito:  21.04 Proveedores Extranjeros  $9.250,00  (lo que pagamos)
Crédito: 11.02 Banco Chile              $9.250,00  (salió del banco)
```

**Estado de la Cuenta 21.04:**
- Debe: $10.672,99 (lo que registramos según SII)
- Haber: $9.250,00 (lo que pagamos)
- **Saldo Deudor: $1.422,99** (pendiente de ajustar)

**Asiento 3: Ajustar Diferencia de Cambio**
```
Débito:  61.03.01 Diferencia de Cambio  $281,10   (diferencia por tipo de cambio)
Débito:  61.01.03 Suscripciones Tech    $1.141,89 (diferencia de IVA - se ajusta en F29)
Crédito: 21.04 Proveedores Extranjeros  $1.422,99 (cierra la cuenta)
```

**Resultado Final:**
- Gasto total registrado: $8.968,90 + $281,10 = **$9.250,00** ✅ (coincide con banco)
- IVA registrado: $1.704,09 (para Doc. 46)
- Banco: -$9.250,00 ✅ (saldo correcto)
- **Equilibrio mantenido** ✅

---

### Opción 2: Método Simplificado (Pragmático para QAI)

**Para diferencias < $1.000 CLP**, podemos simplificar:

**Asiento Único:**
```
Débito:  61.01.03 Suscripciones Tech    $9.250,00  (monto real banco - incluye diferencia)
Débito:  81.01 IVA Crédito Fiscal       $1.757,50  (19% sobre $9.250 para balancear)
Crédito: 11.02 Banco Chile              $9.250,00  (monto real pagado)
Crédito: 21.04 Proveedores Extranjeros  $1.757,50  (IVA que se declarará en F29)
```

**⚠️ IMPORTANTE**: El IVA en este asiento ($1.757,50) es sobre el monto real. Para el Doc. 46 en SII, se usará el IVA calculado sobre monto SII ($1.704,09). La diferencia de $53,41 se ajusta al declarar en F29.

**En Notas del Registro:**
- "Doc. 46 base: $8.968,90 (dólar obs. $896,89)"
- "IVA Doc. 46: $1.704,09 (sobre monto SII)"
- "Diferencia cambio $281,10 absorbida en gasto"
- "IVA diferencia $53,41 se ajustará en F29"

**Resultado:**
- Gasto: $9.250,00 ✅ (coincide con banco)
- Banco: -$9.250,00 ✅ (saldo correcto)
- IVA registrado: $1.757,50 (se ajustará en F29 a $1.704,09)
- Proveedores: $1.757,50 (pendiente de ajustar en F29)
- **Equilibrio mantenido** ✅

---

## 🔢 Sobre Decimales en Pesos Chilenos

**Respuesta Corta**: En Chile **SÍ se usan decimales** en contabilidad, aunque las monedas físicas ya no existen.

**Regla de Redondeo (Solo para Pagos en Efectivo):**
- Desde Nov 2017: No hay monedas de $1 y $5
- **Para efectivo**: Se redondea a la decena más cercana ($1.234 → $1.230 o $1.240)
- **Para pagos electrónicos** (tarjetas, transferencias): **Monto exacto, con decimales**
- **Para contabilidad**: **Siempre usar decimales** para mantener precisión

**En nuestro caso:**
- El banco registró: $9.250,00 CLP (sin decimales visibles, pero existe el concepto)
- El dólar observado: $896,89 (tiene decimales)
- El cálculo: $10 × $896,89 = $8.968,90 (tiene decimales)

**Recomendación QAI:**
- Registrar con **1 decimal** cuando aplique (ej: $8.968,9)
- Redondear solo si es absolutamente necesario para pagos en efectivo
- En contabilidad y Excel/Sheets: **mantener decimales** para precisión

---

## 📋 Resumen para GitHub Copilot Pro

**Datos:**
- Factura: $10,00 USD (09-Ene-2026)
- Transacción Real: 09-Ene-2026 (mismo día que factura)
- Reflejo Banco: 12/01/2026 (próximo día hábil - solo reflejo contable)
- Dólar Observado (SII - 09-Ene): $896,89 CLP/USD
- Monto SII (Doc. 46): $8.968,90 CLP
- Monto Real Banco: $9.250,00 CLP (incluye spread/comisiones bancarias)
- Diferencia: $281,10 CLP (< $1.000, pequeña - se absorbe)

**Registro Recomendado (Método QAI: Simplicidad + Cumplimiento):**

| Fecha Contable | Concepto | Débito | Crédito | Notas |
|:---|:---|:---|---:|:---|
| 09-Ene-2026 | GitHub Copilot Pro - Enero 2026 | 61.01.03: $9.250,00<br>81.01: $1.704,09 | 11.02: $9.250,00<br>21.04: $1.704,09 | Fecha transacción: 09-Ene (reflejo banco: 12/01)<br>Doc. 46: $8.968,90 (dólar $896,89 del 09-Ene)<br>IVA Doc. 46: $1.704,09 (19% sobre monto SII)<br>Diferencia cambio: $281,10 absorbida<br>IVA se cancela en F29 (efecto suma cero) |

**Equilibrio Verificado:**
- Débitos: $9.250,00 + $1.704,09 = $10.954,09
- Créditos: $9.250,00 + $1.704,09 = $10.954,09
- **✅ BALANCEADO**

**Filosofía QAI Aplicada:**
- ✅ **Cumplimiento**: Doc. 46 usa dólar observado del día factura ($896,89 del 09-Ene)
- ✅ **Simplicidad**: Diferencia pequeña ($281,10) absorbida directamente en gasto
- ✅ **Realidad**: Banco refleja salida real de $9.250
- ✅ **Precisión**: Fecha contable es fecha real de transacción (09-Ene), no reflejo bancario (12/01)

---

## 🛡️ Protocolo de Conciliación Bancaria (QAI Zero-Loss)

> **Regla de Oro**: El saldo en el Runway Master (GSheets) es la "Única Fuente de Verdad" (SSOT) y DEBE coincidir al peso con el saldo real del banco al cierre de cada sesión.

### 1. El Ajuste de Realidad (Post-Transacción)
Cuando operamos con USD (Namecheap, Cursor, Google), el flujo es:
1.  **Registro Inicial**: Se usa el valor USD * Dólar Observado del día (estimado).
2.  **Conciliación**: Apenas el cargo aparece en la cartola bancaria, el monto en el GSheet **se sobreescribe** con el valor real en CLP cobrado por el banco.
3.  **Absorción**: La diferencia (spread bancario/comisión) se absorbe en el gasto principal si es < $1.000 CLP.

### 2. Lección Aprendida (Caso Namecheap Feb-2026)
*   **Estimado Inicial**: $5.161 CLP.
*   **Cargo Real Banco**: $5.274 CLP.
*   **Acción**: Se actualizó el GSheet para reflejar los $5.274, asegurando que el Runway Master proyecte el saldo bancario exacto.
*   **Por qué**: Evita que pequeños "goteos" de 100-200 pesos descalcen el saldo final después de 10-20 transacciones.

### 3. Checklist de Cierre para Finn
- [ ] ¿Todos los cargos USD en el GSheet coinciden con la cartola?
- [ ] Si hay diferencia, ¿se actualizó el monto bruto y pagado para igualar al banco?
- [ ] ¿Se generó el backup local tras la conciliación?

---

**Última actualización**: 17-Feb-2026  
**Responsable**: Finn (Financial Agent)
