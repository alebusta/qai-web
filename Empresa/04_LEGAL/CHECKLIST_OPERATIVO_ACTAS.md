# Checklist Operativo: Emisión de Actas Corporativas
**THE QAI COMPANY SpA**

> **Gestión**: Lex (Agente Legal)  
> **Fecha de Creación**: 09-Feb-2026  
> **Propósito**: Garantizar correlatividad, validez legal y custodia de actas

---

## 📝 Proceso Estándar de Emisión de Actas

### **ANTES de la Junta/Sesión**

- [ ] Verificar último N° de acta en [INDICE.md](actas/INDICE.md)
- [ ] Asignar N° correlativo siguiente
- [ ] Preparar borrador usando [ACTA_TEMPLATE.md](actas/ACTA_TEMPLATE.md)
- [ ] Definir tipo de firma necesaria:
  - **Firma Simple**: Actas rutinarias (poderes menores, ratificaciones)
  - **FEA**: Actas críticas (cambios estatutarios, poderes amplios, traspasos de acciones)

### **DURANTE la Junta/Sesión**

- [ ] Registrar fecha, hora y lugar
- [ ] Listar asistentes con RUT y acciones
- [ ] Detallar acuerdos adoptados (con votación si aplica)
- [ ] Nombrar Presidente y Secretario de la sesión

### **DESPUÉS de la Junta/Sesión**

#### 1. Firma del Acta
- [ ] Exportar borrador a PDF
- [ ] Firmar electrónicamente (según nivel definido)
- [ ] Verificar que PDF tenga firma visible

#### 2. Custodia y Registro
- [ ] Guardar versiones en carpeta `/04_LEGAL/actas/`:
  - [ ] `YYYY-MM-DD_ACTA_NN_TITULO.md` (fuente editable)
  - [ ] `YYYY-MM-DD_ACTA_NN_TITULO.pdf` (firmado)
- [ ] Actualizar [INDICE.md](actas/INDICE.md) con nueva entrada
- [ ] Respaldar en Google Drive (`/Empresa/04_LEGAL/actas/`)

#### 3. Acciones Posteriores (si aplica)
- [ ] **Si aprueba cambio estatutario**: Modificar estatutos y presentar al RES
- [ ] **Si nombra nuevos administradores**: Actualizar registro en SII
- [ ] **Si traspasa acciones**: Registrar en Libro de Accionistas (RES)
- [ ] **Si otorga poderes amplios**: Considerar protocolización notarial

---

## 🔐 Niveles de Firma Electrónica

### Firma Simple (Válida para la mayoría de actas internas)
**Cuándo usar:**
- Ratificaciones de administración
- Aprobación de estados financieros rutinarios
- Autorizaciones de poderes menores (trámites bancarios, SII)

**Herramientas:**
- Adobe Acrobat Reader (firma básica)
- Foxit Reader
- Firma digital incluida en Windows

### Firma Electrónica Avanzada (FEA)
**Cuándo usar:**
- Cambios en estatutos sociales
- Aumento o disminución de capital
- Fusión, división, disolución
- Poderes amplios para venta de bienes raíces
- Traspasos de acciones con efectos ante terceros

**Proveedores en Chile:**
- e-Sign (ex Acepta)
- PrivadoID
- Firma Simple (FEA empresarial)

**Costo aproximado:** $2.000 - $8.000 CLP/año por persona

---

## ⚠️ Casos que Requieren Protocolización Notarial

Aunque la SpA permite libros digitales, algunos actos pueden requerir protocolización para ser oponibles ante:
- Conservador de Bienes Raíces (compra/venta de inmuebles)
- Bancos (créditos hipotecarios, líneas de crédito)
- Inversionistas institucionales (due diligence)

**Actas críticas para protocolizar:**
- Cambios en poderes de administración
- Modificación de objeto social
- Aumento de capital con entrada de nuevos socios

**Proceso:**
1. Llevar acta firmada digitalmente a Notaría Virtual (ej: Notaria.cl)
2. Solicitar "Protocolización de Documento Privado"
3. Obtener repertorio y copia autorizada
4. Presentar al RES si aplica modificación estatutaria

---

## 🛡️ Verificación de Correlatividad (Auditoría)

Antes de emitir una nueva acta:
1. Abrir [INDICE.md](actas/INDICE.md)
2. Confirmar último N° registrado
3. Verificar que no existan saltos en numeración
4. Asignar N° siguiente de forma correlativa

**❌ NO PERMITIDO:**
- Saltar números (Acta 1 → Acta 3)
- Repetir números
- Cambiar fechas retroactivas sin justificación legal

---

## 📋 Ejemplo Práctico: Emisión de Acta N°02

### Contexto: Aprobación de Estados Financieros 2025

**Paso a Paso:**
1. Consultar INDICE.md → Último N° = 01 → Siguiente = **02**
2. Copiar `ACTA_TEMPLATE.md` → Renombrar: `2026-03-15_ACTA_02_APROBACION_EEFF_2025.md`
3. Redactar acta con:
   - Fecha: 15-Mar-2026
   - Tipo: Junta Ordinaria
   - Asunto: Aprobación Balance 2025
4. Exportar a PDF y firmar (Firma Simple es suficiente)
5. Guardar ambos archivos en `/actas/`
6. Actualizar INDICE.md:
   ```
   | 02 | 15-Mar-2026 | Junta Ordinaria | Aprobación EEFF 2025 | ✅ Firmada | [Ver](2026-03-15_ACTA_02_APROBACION_EEFF_2025.md) |
   ```
7. Respaldar en Drive

---

## 📂 Respaldo en la Nube

**Política de Respaldo:**
- Todas las actas deben sincronizarse con Google Drive
- Ruta: `/Empresa/04_LEGAL/actas/`
- Frecuencia: Inmediata tras firma

**Herramientas:**
- Google Drive Desktop (sincronización automática)
- Manual: Subir PDF a Drive y compartir con administradores

---

## 🔗 Referencias

- [PROTOCOLO_LIBROS_DIGITALES.md](PROTOCOLO_LIBROS_DIGITALES.md): Marco legal
- [INDICE.md](actas/INDICE.md): Registro correlativo
- [ACTA_TEMPLATE.md](actas/ACTA_TEMPLATE.md): Plantilla estándar

---

**Mantenedor**: Lex (Agente Legal)  
**Próxima Revisión**: Trimestral o ante cambios normativos
