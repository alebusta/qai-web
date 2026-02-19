# Template: Formulario 29 (F29) - Declaración Mensual IVA

**Propósito**: Guía de llenado del Formulario 29 para The QAI Company SpA  
**Tipo de Empresa**: Pro Pyme General (14 D3)  
**Frecuencia**: Mensual  
**Última actualización**: 27-Dic-2025

---

## 📋 Información General

### Datos del Contribuyente
```
RUT: [RUT de QAI]
Razón Social: The QAI Company SpA
Giro: Consultoría en Informática y Tecnología
Régimen: Pro Pyme General (14 D3)
```

### Período a Declarar
```
Mes: [MM]
Año: [AAAA]
Ejemplo: 12/2025 (Diciembre 2025)
```

---

## 🧮 Secciones del F29

### SECCIÓN A: IVA DÉBITO FISCAL (Lo que debes pagar)

#### Código 15: Ventas y/o Servicios del Giro (Neto)
**Qué incluir**:
- Todas las ventas de servicios afectas a IVA
- Monto SIN IVA (neto)

**Ejemplo**:
```
Factura 1: $1.000.000 neto
Factura 2: $500.000 neto
Total Código 15: $1.500.000
```

#### Código 103: Exportaciones
**Qué incluir**:
- Servicios prestados a clientes extranjeros (sin IVA)
- Monto total en CLP

**Ejemplo**:
```
Cliente USA - Invoice $1,000 USD × $950 = $950.000 CLP
Total Código 103: $950.000
```

#### Código 27: Débito Fiscal Total
**Cálculo automático**: Código 15 × 19%

**Ejemplo**:
```
$1.500.000 × 19% = $285.000
```

---

### SECCIÓN B: IVA CRÉDITO FISCAL (Lo que puedes recuperar)

#### Código 30: Compras Nacionales Afectas a IVA (Neto)
**Qué incluir**:
- Facturas de proveedores chilenos con IVA
- Monto SIN IVA (neto)

**Ejemplo**:
```
Compra hosting local: $100.000 neto
Compra software local: $200.000 neto
Total Código 30: $300.000
```

#### Código 31: Crédito Fiscal por Compras Nacionales
**Cálculo automático**: Código 30 × 19%

**Ejemplo**:
```
$300.000 × 19% = $57.000
```

#### Código 57: IVA Retenido Total (Retenciones Totales)
**Qué incluir**:
- IVA de Facturas de Compra (Doc. 46) por SaaS extranjero
- IVA de servicios con retención total

**Ejemplo** (SaaS extranjero):
```
Cursor: $50 USD × $950 = $47.500 neto → IVA: $9.025
GitHub: $100 USD × $950 = $95.000 neto → IVA: $18.050
Total Código 57: $27.075
```

**IMPORTANTE**: Este código genera débito Y crédito simultáneo (efecto suma cero).

#### Código 37: Total Crédito Fiscal del Mes
**Cálculo**: Código 31 + Código 57

**Ejemplo**:
```
$57.000 + $27.075 = $84.075
```

---

### SECCIÓN C: DETERMINACIÓN DEL IVA

#### Código 89: Diferencia Débito - Crédito
**Cálculo**: Código 27 - Código 37

**Ejemplo**:
```
Débito: $285.000
Crédito: $84.075
Diferencia: $200.925 (a pagar)
```

**Si es negativo**: Remanente a favor (se arrastra al mes siguiente)

#### Código 90: Remanente del Mes Anterior
Si tuviste crédito fiscal mayor que débito en el mes anterior, ese saldo se arrastra aquí.

**Ejemplo**:
```
Remanente nov: $50.000
Diferencia dic: $200.925
A pagar: $200.925 - $50.000 = $150.925
```

#### Código 91: IVA a Pagar
**Cálculo**: Código 89 - Código 90 (si es positivo)

**Si es negativo**: Remanente para próximo mes (declarar $0 a pagar)

---

### SECCIÓN D: PAGO PROVISIONAL MENSUAL (PPM)

#### Código 150: Base Imponible PPM
**Para Pro Pyme General**:
- Ingresos del mes (ventas netas + exportaciones)

**Ejemplo**:
```
Código 15: $1.500.000
Código 103: $950.000
Total: $2.450.000
```

#### Código 151: PPM (0,25% sobre Code 150)
**Cálculo**: Código 150 × 0,25%

**Ejemplo**:
```
$2.450.000 × 0,25% = $6.125
```

**Exención**: Si ingresos anuales proyectados \< 50 UF/mes → PPM exento (verificar)

---

### SECCIÓN FINAL: RESUMEN DE PAGO

#### Código 93: Total a Pagar
**Cálculo**: Código 91 (IVA) + Código 151 (PPM)

**Ejemplo**:
```
IVA: $150.925
PPM: $6.125
Total a Pagar: $157.050
```

---

## 📊 Ejemplo Completo: Diciembre 2025

### Movimientos del Mes
**Ventas**:
- Cliente Chile - Factura afecta: $1.000.000 neto
- Cliente USA - Exportación: $1,000 USD (TC: $950) = $950.000

**Compras**:
- Hosting nacional: $100.000 neto + IVA
- Cursor (SaaS): $50 USD = $47.500 neto

### Formulario 29

```
═══════════════════════════════════════════════════════
SECCIÓN A: DÉBITO FISCAL
═══════════════════════════════════════════════════════
[15] Ventas y/o Servicios del Giro    $1.000.000
[103] Exportaciones                    $  950.000
[27] Débito Fiscal Total (15 × 19%)   $  190.000

═══════════════════════════════════════════════════════
SECCIÓN B: CRÉDITO FISCAL
═══════════════════════════════════════════════════════
[30] Compras Nacionales                $  100.000
[31] Crédito por Compras (30 × 19%)   $   19.000
[57] IVA Retenido (Cursor Doc. 46)    $    9.025
[37] Total Crédito Fiscal              $   28.025

═══════════════════════════════════════════════════════
SECCIÓN C: DETERMINACIÓN IVA
═══════════════════════════════════════════════════════
[89] Diferencia (27 - 37)              $  161.975
[90] Remanente mes anterior            $        0
[91] IVA a Pagar                       $  161.975

═══════════════════════════════════════════════════════
SECCIÓN D: PPM
═══════════════════════════════════════════════════════
[150] Base Imponible PPM               $1.950.000
[151] PPM (0,25%)                      $    4.875

═══════════════════════════════════════════════════════
TOTAL A PAGAR
═══════════════════════════════════════════════════════
[93] TOTAL                             $  166.850
```

---

## 🔧 Proceso de Declaración (Para Finn)

### 1. Preparación (Día 1 al 15 del mes)
```markdown
- Consolidar Libro de Ventas
- Consolidar Libro de Compras
- Verificar Facturas de Compra (Doc. 46) emitidas
- Calcular todos los códigos
```

### 2. Borrador (Día 15)
```markdown
- Crear borrador de F29 en /TorreDeControl/temp_files/ (Landing Zone obligatoria; nunca en raíz de TorreDeControl).
- Revisar cálculos
- Verificar que no falten facturas
- Calcular monto a pagar
```

### 3. Aprobación (Día 16-18)
```markdown
- Presentar borrador a Alejandro:
  "📊 F29 [Mes]:
  - Débito: $X
  - Crédito: $Y
  - A pagar: $Z
  ¿Apruebas declaración?"
```

### 4. Declaración (Día 18-20)
```markdown
- Ingresar a sii.cl
- Completar F29 electrónico
- Validar montos
- Enviar declaración
- Guardar comprobante
```

### 5. Pago (Mismo día o siguiente)
```markdown
- Generar línea de pago en SII
- Pagar vía transferencia bancaria
- Guardar comprobante de pago
- Actualizar registros
```

---

## ⚠️ Casos Especiales

### Declaración "Sin Movimiento"
Si NO hubo ventas NI compras en el mes:

```
[15] Ventas: $0
[27] Débito: $0
[30] Compras: $0
[37] Crédito: $0
[91] A Pagar: $0
[93] TOTAL: $0
```

**IMPORTANTE**: Igual debes declarar, aunque sea en $0.

### Remanente a Favor
Si Crédito \> Débito:

```
Ejemplo:
Débito: $50.000
Crédito: $100.000
Remanente: $50.000 (se arrastra al próximo mes)
```

No pagas nada, pero **sí debes declarar**.

### Corrección de F29
Si cometiste un error:
1. F29 rectificatorio (mismo mes/año)
2. Marca: "Rectificatoria"
3. Completa TODOS los campos nuevamente (no solo el error)

---

## 📎 Documentos de Respaldo

Guardar por 6 años (plazo legal):
- Libro de Compras y Ventas del mes
- Facturas emitidas (respaldo automático en SII)
- Facturas recibidas (PDFs)
- Facturas de Compra Doc. 46 (SaaS extranjero)
- Comprobante de declaración F29
- Comprobante de pago

---

## 🚨 Errores Comunes (y cómo evitarlos)

### ❌ No declarar facturas de SaaS extranjero
**Solución**: Siempre emitir Doc. 46 el mismo mes del pago.

### ❌ Olvidar remanente del mes anterior
**Solución**: Finn debe llevar registro acumulado de remanentes.

### ❌ Declarar fuera de plazo
**Solución**: Alarmas automáticas 7 días antes del vencimiento.

### ❌ Sumar IVA incluido en vez de neto
**Solución**: Siempre trabajar con montos NETOS, el sistema calcula el 19%.

---

**Próxima revisión**: Cuando cambie normativa del F29 o tasa de IVA  
**Uso**: Consulta obligatoria de Finn al preparar declaración mensual
