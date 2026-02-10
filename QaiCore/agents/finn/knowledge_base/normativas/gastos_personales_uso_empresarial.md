# Gastos Personales con Uso Empresarial - Chile

**Fuente**: Código Tributario Chile - SII  
**Fecha**: Enero 2026  
**Aplica a**: The QAI Company SpA

---

## Resumen Ejecutivo

**Pregunta**: ¿Se pueden deducir gastos que están a nombre personal pero se usan para la empresa?

**Respuesta**: **SÍ, con condiciones**. Los gastos personales con uso empresarial pueden ser deducibles para Impuesto a la Renta, PERO con limitaciones importantes en IVA.

---

## Reglas Generales

### 1. Para Impuesto a la Renta (F22)

**Gastos deducibles** si cumplen:
- ✅ Están relacionados con el giro de la empresa
- ✅ Pueden justificarse con uso empresarial
- ✅ No superan proporción razonable (ej: uso 80% empresarial, 20% personal)

**Ejemplos comunes**:
- Suscripciones SaaS (Google One, Cursor, etc.) usadas principalmente para trabajo
- Equipos informáticos (laptop, teléfono) usados para empresa
- Internet/telefonía con uso empresarial

**Limitaciones**:
- Debe poder justificarse proporción de uso empresarial
- Si es 100% uso empresarial, idealmente debería estar a nombre de la empresa
- Gastos completamente personales NO son deducibles

### 2. Para IVA (F29)

**Regla clave**: Solo gastos a nombre del RUT de la empresa generan crédito fiscal.

**Implicación**:
- ✅ Gasto personal con uso empresarial → **DEDUCIBLE** para Impuesto a la Renta
- ❌ Gasto personal con uso empresarial → **NO genera crédito fiscal de IVA**

**Ejemplo práctico**:
- Google One suscripción personal ($7.100/mes, VAT incluido $1.134)
- Uso: 100% empresarial (Antigravity)
- **Tratamiento**:
  - Deducible en F22: $7.100 CLP (o proporción justificada)
  - IVA no recuperable: $1.134 CLP perdido
  - No se puede emitir Doc. 46

---

## Caso Específico: Google One (Antigravity)

### Situación
- Suscripción: Google One (Antigravity) - $7.100 CLP/mes
- Perfil: Personal (Alejandro Bustamante)
- VAT cobrado por Google: $1.134 CLP/mes
- Uso: 100% empresarial (QAI)

### Tratamiento Contable

**Registro en Google Sheets**:
```
Fecha: [fecha de pago]
Tipo: GASTO
Concepto: Google One (Antigravity) - Suscripción mensual
Categoría FinOps: Fijo
Cuenta Contable: 61.01.03 Suscripciones Tech
Monto Neto: $5.966 CLP (descontando VAT)
IVA: $1.134 CLP (NO recuperable - a nombre personal)
Monto Bruto: $7.100 CLP
Proyecto: General
Notas: Suscripción a nombre personal, uso 100% empresarial. VAT no recuperable. Deducible en F22.
```

**Deducibilidad F22**:
- ✅ Monto total deducible: $7.100 CLP (si uso es 100% empresarial)
- ❌ IVA no recuperable: $1.134 CLP

**No se emite Doc. 46**:
- No aplica porque está a nombre personal, no empresarial

---

## Recomendaciones

### Corto Plazo
1. ✅ Registrar gasto como deducible en F22
2. ❌ Aceptar que VAT no es recuperable
3. 📝 Documentar uso 100% empresarial para justificación en F22

### Largo Plazo
1. **Migrar a servicios empresariales** cuando sea posible:
   - Google Workspace (si se necesita)
   - Servicios con facturación empresarial directa
2. **Verificar antes de suscribir** si permite facturación empresarial
3. **Priorizar servicios con Doc. 46** para recuperar IVA

---

## Casos Especiales

### Servicios Mixtos (Personal + Empresarial)

**Ejemplo**: Internet residencial usado 60% empresa, 40% personal

**Tratamiento**:
- Proporción deducible: 60% del gasto
- Documentar uso con justificación razonable
- IVA: No recuperable (a nombre personal)

### Equipos Informáticos

**Ejemplo**: Laptop comprada a nombre personal, uso empresarial

**Tratamiento**:
- Si uso es >50% empresarial → Proporción deducible
- Depreciación según vida útil (típicamente 3-5 años)
- IVA: No recuperable si compra fue personal

---

## Referencias Legales

- **Código Tributario Chile**: Art. 31 (Gastos deducibles)
- **Ley de Impuesto a la Renta**: Art. 31 (Gastos necesarios para producir renta)
- **SII**: Consultas telefónicas 223951111

---

## ⚠️ IMPORTANTE

Esta es una guía general. Para casos específicos:
1. **Consultar con contador** para confirmar deducibilidad
2. **Documentar uso empresarial** con evidencia (si aplica)
3. **Revisar normativa actualizada** en sii.cl

---

**Última actualización**: 07-Ene-2026  
**Responsable**: Finn  
**Revisado**: Caso Google One (Antigravity)

