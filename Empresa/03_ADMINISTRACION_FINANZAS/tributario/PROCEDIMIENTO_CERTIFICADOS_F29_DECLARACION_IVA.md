# Procedimiento: Certificados de declaración F29 (IVA mensual)

> **Alcance**: PDFs descargados del SII que acreditan la presentación de la declaración de IVA mensual (F29).  
> **No aplica a**: RUT, Inicio de Actividades, Certificado de Cumplimiento u otros documentos SII que van en Documentos Legales / Certificados.

---

## 1. Dónde se guardan

| Dónde | Ruta en Drive |
|-------|----------------|
| **Documentos tributarios** | **Tributario** → año (ej. `2025`, `2026`) → mes (ej. `12-diciembre`, `01-enero`) |
| **No** en Documentos Legales | Los certificados de declaración F29 no van en `/Documentos Legales/Certificados/`. Esa carpeta es para RUT, Inicio de Actividades, etc. |

---

## 2. Formato de nombre del archivo (obligatorio)

**Patrón:** `YYYY-MM_F29_Declaracion_IVA.pdf`

| Período declarado | Nombre del archivo |
|-------------------|--------------------|
| Diciembre 2025 | `2025-12_F29_Declaracion_IVA.pdf` |
| Enero 2026 | `2026-01_F29_Declaracion_IVA.pdf` |
| Febrero 2026 | `2026-02_F29_Declaracion_IVA.pdf` |

- **YYYY**: año del período declarado (4 dígitos).  
- **MM**: mes del período declarado (2 dígitos, 01–12).  
- El resto del nombre es fijo: `_F29_Declaracion_IVA.pdf`.

Si el PDF se descarga con otro nombre (ej. `2026_01_IVA.pdf`), **renombrar** antes de subir o al subir (vía herramienta `gdrive.py --rename` después de subir).

---

## 3. IDs de carpetas Drive (Tributario)

Para uso con `gdrive.py` (config en `.qai/config/gdrive_folders.json` o `--show-folders`):

| Ruta lógica | Uso |
|-------------|-----|
| `tributario_id` | Raíz Tributario |
| `tributario_2025_id` | Tributario/2025 |
| `tributario_2025_12_id` | Tributario/2025/12-diciembre |
| Tributario/2026 | Crear si no existe (`--create-folder "2026" --parent tributario_id`) |
| Tributario/2026/01-enero | Crear si no existe; ID creado 19-Feb-2026: `15jFTaIipB03FwgEjPGlTTCMBbXb3beJK` |

Al abrir un **nuevo mes/año**, crear la carpeta correspondiente bajo Tributario y documentar el ID aquí o en DISENO_RESPALDO si se centraliza.

---

## 4. Flujo para Finn (paso a paso)

1. **Tras declarar el F29 en el SII**  
   - Descargar el comprobante/certificado de declaración (PDF).

2. **Nombre del archivo**  
   - Si no viene como `YYYY-MM_F29_Declaracion_IVA.pdf`, renombrar localmente o en Drive después de subir.

3. **Subir a Drive**  
   - Carpeta destino: **Tributario / AAAA / MM-mes** (ej. Tributario/2026/01-enero).  
   - Ejemplo CLI:
     ```bash
     ./QaiCore/qrun.bat ./QaiCore/tools/gdrive.py --upload "ruta/local/2026-01_F29_Declaracion_IVA.pdf" --folder "ID_CARPETA_TRIBUTARIO_MES" --desc "Comprobante F29 IVA Enero 2026"
     ```

4. **Si el archivo se subió con otro nombre**  
   - Renombrar en Drive:
     ```bash
     ./QaiCore/qrun.bat ./QaiCore/tools/gdrive.py --rename "FILE_ID" --name "2026-01_F29_Declaracion_IVA.pdf"
     ```

5. **Actualizar índice local**  
   - En `Empresa/03_ADMINISTRACION_FINANZAS/tributario/AAAA/MM-mes/_index_declaraciones.md`:  
     - Agregar o completar la fila del período con el **link de Drive** al PDF y, si aplica, folio SII.

6. **No registrar** este PDF en `documentos_legales/_index_certificados_sii.md`.  
   - Ese índice es solo para certificados SII de tipo “legal” (RUT, Inicio de Actividades, etc.).

---

## 5. Resumen de reglas

| Regla | Detalle |
|-------|---------|
| **Ubicación** | Solo en **Tributario** (por año y mes), nunca en Documentos Legales / Certificados. |
| **Nombre** | Siempre `YYYY-MM_F29_Declaracion_IVA.pdf`. |
| **Índice** | Solo en `tributario/.../_index_declaraciones.md` del mes correspondiente. |
| **Duplicados** | Si por error se subió a Certificados, mover a Tributario (y renombrar si aplica) y enviar el duplicado a la papelera. |

---

**Versión**: 1.0  
**Fecha**: 19-Feb-2026  
**Autor**: Finn (agente financiero), corrección de ruta y procedimiento
