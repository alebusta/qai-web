# 04. LEGAL - El Escudo

> **Gestión**: Lex (Agente Legal)  
> **Última actualización**: 09-Feb-2026

---

## 🎯 Propósito

Esta carpeta contiene **documentos legales operativos y versionables** que pueden editarse, mejorarse y mantenerse en Git. No contiene PDFs pesados oficiales (esos están en Google Drive).

---

## 📁 Estructura Actual

```
/04_LEGAL/
├── README.md                                              ← Este archivo
├── PROTOCOLO_LIBROS_DIGITALES.md                          ← Marco legal libros corporativos
├── CHECKLIST_OPERATIVO_ACTAS.md                           ← Guía operativa para emisión de actas
├── ROADMAP_CONSTITUCION_QAI.md                            ← Plan de constitución (histórico)
├── ESTATUTOS_QAI_COMPANY.md                               ← Estatutos sociales
├── /actas/                                                ← Libro de actas digital
│   ├── INDICE.md                                          ← Registro correlativo de actas
│   ├── ACTA_TEMPLATE.md                                   ← Plantilla estándar
│   ├── 2026-02-07_ACTA_01_CONSTITUCION_LIBROS_DIGITALES.md
│   └── 2026-02-07_ACTA_01_CONSTITUCION_LIBROS_DIGITALES.pdf
│   └── 📁 Drive: https://drive.google.com/drive/folders/1Ieyd6PtP-3vooPePJ4nmxXR7E8Ieyf-O
├── /registros_oficiales/                                  ← Comprobantes de trámites oficiales
│   ├── INDICE.md                                          ← Registro de trámites
│   └── 2026-02-09_APERTURA_REGISTRO_ACCIONISTAS_RES.md
│   └── 📁 Drive: https://drive.google.com/drive/folders/1cxSL7Iz3j99yNsaLW6KRCrggBJKXHs3_
├── /contratos/                                            ← Templates de contratos
│   ├── template_nda.md
│   ├── template_servicios.md
│   └── template_confidencialidad.md
├── /politicas/                                            ← Políticas internas
│   ├── politica_privacidad.md
│   ├── politica_rrhh.md
│   └── codigo_conducta.md
└── /minutas/                                              ← Minutas de reuniones
    └── 2025/
        └── 2025-12-27_reunion_fundadores.md
```

---

## � Libro de Actas Digital (ACTIVO)

**Estado**: ✅ Operativo desde 07-Feb-2026  
**Marco Legal**: Ley N° 19.799 (Documentos Electrónicos y Firma Electrónica)

### Documentos Clave
- **[PROTOCOLO_LIBROS_DIGITALES.md](PROTOCOLO_LIBROS_DIGITALES.md)**: Marco legal y requisitos de validez
- **[CHECKLIST_OPERATIVO_ACTAS.md](CHECKLIST_OPERATIVO_ACTAS.md)**: Guía paso a paso para emisión de actas
- **[actas/INDICE.md](actas/INDICE.md)**: Registro correlativo de todas las actas

### Hitos Cumplidos
- [x] Acta N°1 firmada (07-Feb-2026): Constitución de Libros Digitales
- [x] Registro de Accionistas abierto en RES (09-Feb-2026)
- [x] Repositorio digital estructurado
- [x] Checklist operativo establecido
- [x] Respaldo en Google Drive configurado

### Respaldo en Google Drive
- **Carpeta Actas**: [Ver en Drive](https://drive.google.com/drive/folders/1Ieyd6PtP-3vooPePJ4nmxXR7E8Ieyf-O)
- **Carpeta Registros Oficiales**: [Ver en Drive](https://drive.google.com/drive/folders/1cxSL7Iz3j99yNsaLW6KRCrggBJKXHs3_)
- **Carpeta Legales (Principal)**: [Ver en Drive](https://drive.google.com/drive/folders/165wBgQefhYiw49rGhVOQ_WE8OVWSxee2)

### Próximas Actas
Consultar [actas/INDICE.md](actas/INDICE.md) para ver el último N° correlativo. La próxima será **Acta N°02**.

---

## �🔍 ¿Qué VA aquí?

### ✅ SÍ va en `/04_LEGAL/` (Git)

1. **Templates de contratos** (markdown/docx editables):
   - NDAs, acuerdos de confidencialidad
   - Contratos de servicios profesionales
   - Acuerdos de Joint Venture
   - Contratos laborales tipo

2. **Políticas internas** (markdown):
   - Política de privacidad
   - Políticas de RRHH
   - Código de conducta
   - Política de uso de datos

3. **Libro de Actas Corporativas** (markdown + PDF firmados):
   - Actas de juntas de accionistas
   - Actas de directorio (si aplica)
   - Numeración correlativa obligatoria
   - Custodia digital con firma electrónica

4. **Templates de actas** (markdown):
   - Actas digitales con firmas
   - Formato calibrado para PDF

5. **Comprobantes de trámites oficiales** (markdown en `/registros_oficiales/`):
   - Apertura de Registro de Accionistas (RES)
   - Certificados de vigencia
   - Modificaciones estatutarias presentadas al RES
   - Otros trámites ante organismos públicos

6. **Índices markdown** que apuntan a Drive:
   - `_index_escrituras.md` → Links a PDFs oficiales
   - `_index_certificados.md` → Links a certificados SII
   - `_index_poderes.md` → Links a Poderes y Autorizaciones

### ❌ NO va aquí (va en Google Drive)

1. **PDFs oficiales firmados**:
   - Escritura de constitución (firmada, notariada)
   - Certificados SII (RUT, Inicio Actividades)
   - Patentes municipales
   - Contratos firmados (versión final con firmas)
   - Poderes notariales

**Ubicación**: Google Drive → `Documentos Legales/`  
**Acceso**: Ver `../03_ADMINISTRACION_FINANZAS/GOOGLE_DRIVE_STRUCTURE.md`

---

## 🤝 Coordinación con Finn

Existe overlap con `/03_ADMINISTRACION_FINANZAS/documentos_legales/`:

- **Lex gestiona**: Templates y políticas (aquí en `/04_LEGAL/`)
- **Finn gestiona**: PDFs oficiales en Drive + índice en `/03_ADMIN/documentos_legales/`
- **Colaboración**: Cuando Finn necesita referencia legal (ej: RUT para factura), consulta índice en `/03_ADMIN/`. Cuando Lex necesita subir PDF oficial, coordina con Finn para upload a Drive.

---

## 📝 Convenciones de Nombres

### Templates de contratos
```
template_[tipo]_[version].md
Ejemplo: template_nda_v1.md
```

### Políticas
```
politica_[area].md
Ejemplo: politica_privacidad.md
```

### Minutas
```
YYYY-MM-DD_[evento].md
Ejemplo: 2025-12-27_reunion_fundadores.md
```

### Actas
```
YYYY-MM-DD_ACTA_NN_[TEMA].md / .pdf
Ejemplo: 2026-02-07_ACTA_01_CONSTITUCION_LIBROS_DIGITALES.md
Nota: Numeración correlativa obligatoria (01, 02, 03...)
```

### Comprobantes de trámites
```
YYYY-MM-DD_[TIPO_TRAMITE]_[ORGANISMO].md
Ejemplo: 2026-02-09_APERTURA_REGISTRO_ACCIONISTAS_RES.md
```

---

## 🔄 Flujo de Trabajo

### Emitir nueva acta corporativa

1. **Lex** consulta [actas/INDICE.md](actas/INDICE.md) para obtener N° correlativo
2. **Lex** crea acta usando [actas/ACTA_TEMPLATE.md](actas/ACTA_TEMPLATE.md)
3. **Administradores** revisan y firman electrónicamente
4. **Lex** actualiza [actas/INDICE.md](actas/INDICE.md) con nueva entrada
5. **Finn** respalda en Google Drive (si aplica)
6. Si requiere acción en RES u otro organismo → seguir procedimiento específico

**Guía completa**: [CHECKLIST_OPERATIVO_ACTAS.md](CHECKLIST_OPERATIVO_ACTAS.md)

### Respaldar documentos en Google Drive

**Para actas nuevas:**
```powershell
.\QaiCore\qrun.bat .\QaiCore\tools\gdrive.py --upload "ruta\al\archivo.pdf" --folder "1Ieyd6PtP-3vooPePJ4nmxXR7E8Ieyf-O" --desc "Descripción del documento"
```

**Para registros oficiales:**
```powershell
.\QaiCore\qrun.bat .\QaiCore\tools\gdrive.py --upload "ruta\al\archivo.md" --folder "1cxSL7Iz3j99yNsaLW6KRCrggBJKXHs3_" --desc "Descripción del trámite"
```

Luego actualizar el INDICE correspondiente con el link de Drive.

### Crear nuevo contrato

1. **Lex** crea template en `/contratos/template_[tipo].md`
2. Cuando se firma → **Finn** sube PDF a Drive
3. **Finn** actualiza índice en `/03_ADMIN/documentos_legales/`

### Actualizar política interna

1. **Lex** edita markdown en `/politicas/`
2. Commit a Git con descripción clara
3. Si requiere comunicación a equipo → coordinar con Alejandro

### Archivar documento oficial

1. PDF llega a Alejandro (email, WhatsApp)
2. **Finn** sube a Google Drive → `Documentos Legales/[categoría]/`
3. **Finn** actualiza índice correspondiente
4. **Lex** puede referenciar desde `/04_LEGAL/` si es necesario

---

## 🧾 Template de Actas (PDF calibrado)

**Template oficial**: [actas/ACTA_TEMPLATE.md](actas/ACTA_TEMPLATE.md)

**Reglas clave del formato**
- El primer H1 debe contener la palabra "ACTA" para activar el modo acta del PDF.
- El nombre de la compania y el RUT van como dos lineas en negrita justo debajo del titulo.
- La linea "Firmas:" debe existir y gatilla nueva pagina para firmas.
- No agregues listas con guiones en la zona de firmas; las lineas de firma usan guiones bajos.

**Generacion del PDF**
```
python QaiCore/tools/md_to_pdf.py "Empresa/04_LEGAL/actas/2026-02-07_ACTA_01_LIBROS_DIGITALES.md" "Empresa/04_LEGAL/actas/2026-02-07_ACTA_01_LIBROS_DIGITALES.pdf"
```

**Parametros calibrados (modo ACTA)**
- Margenes: 30mm izquierdo, 20mm derecho
- Pie de pagina: "Folio N"
- Portada: titulo en negro, compania y RUT debajo
- Salto automatico a pagina de firmas

---

## 🚨 Importante

- **Git NO es para PDFs pesados**: Usar Drive
- **Sensibilidad**: Cuidado con información confidencial en Git (empresa es privada, pero mejor práctica)
- **Versionado**: Templates deben tener `_v1`, `_v2` al actualizarse
- **Índices siempre actualizados**: Si sube PDF a Drive, actualizar índice

---

## 📚 Referencias

- **Google Drive Structure**: `../03_ADMINISTRACION_FINANZAS/GOOGLE_DRIVE_STRUCTURE.md`
- **Índice de docs oficiales**: `../03_ADMINISTRACION_FINANZAS/documentos_legales/`
- **ADR sobre separación**: `/QaiCore/agents/nzero/knowledge_base/design_decisions/007_legal_documents_strategy.md`

---

**Creado**: 27-Dic-2025 (Nzero)  
**Actualizado**: 09-Feb-2026 (Lex - Implementación Libros Digitales)  
**Mantenedor**: Lex (Agente Legal)  
**Coordinación con**: Finn (para PDFs oficiales)
