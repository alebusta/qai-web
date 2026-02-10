# ADR-007: Estrategia de Documentos Legales (Git vs Drive)

**Fecha**: 2025-12-27  
**Estado**: Aceptado  
**Contexto**: Overlap entre `/Empresa/04_LEGAL/` y Google Drive "Documentos Legales" generaba confusión

---

## Problema

Tras implementar Google Drive para documentos financieros, se creó una carpeta "Documentos Legales" en Drive. Esto generó overlap con la carpeta `/Empresa/04_LEGAL/` existente en Git.

**Preguntas que surgieron**:
- ¿Qué documentos van en Git vs Drive?
- ¿Quién gestiona qué? (Lex vs Finn)
- ¿Dónde busco un certificado SII? ¿Y un template de contrato?
- ¿Cómo evitamos duplicación?

---

## Alternativas Consideradas

### Opción 1: Todo en Git
**Pros**: Versionado completo, un solo lugar  
**Contras**: PDFs pesados en Git (mala práctica), dificulta sincronización con Drive

### Opción 2: Todo en Drive
**Pros**: PDFs centralizados, fácil acceso  
**Contras**: Pérdida de versionado de templates, no es git-friendly

### Opción 3: Separación clara por tipo (ELEGIDA) ✅

**Criterio**:
- **Templates/Operativos** → Git (`/04_LEGAL/`)
- **PDFs Oficiales e Inmutables** → Drive
- **Índices** → Git (`/03_ADMIN/documentos_legales/`)

---

## Decisión

### Documentos en `/Empresa/04_L EGAL/` (Git)

**Gestión**: Lex (Agente Legal)

**Contenido**:
1. Templates de contratos (markdown/docx editables)
2. Políticas internas (markdown)
3. Minutas de directorio (markdown)
4. Índices markdown que apuntan a Drive

**Justificación**:
- Versionables (se actualizan frecuentemente)
- Necesitan Git para track de cambios
- Livianos (markdown, no PDFs)

### Documentos en Drive `/Documentos Legales/`

**Gestión**: Finn (upload/download) + Lex (cuando necesita)

**Contenido**:
1. Escrituras notariadas (PDFs firmados)
2. Certificados SII (RUT, Inicio Actividades)
3. Patentes municipales
4. Contratos firmados (versión final con firmas)
5. Poderes notariales

**Justificación**:
- Inmutables (no se editan, son documentos oficiales)
- Pesados (PDFs escaneados, firmas digitales)
- Necesitan backup automático de Google
- Accesibles desde cualquier lugar

### Índices en `/03_ADMIN/documentos_legales/` (Git)

**Gestión**: Finn

**Contenido**:
- `_index_escrituras.md`
- `_index_certificados_sii.md`
- `_index_patentes.md`
- `_index_poderes.md`

**Justificación**:
- Finn necesita acceso rápido a documentos para operaciones financieras
- Índices livianos (markdown con links)
- Separación de responsabilidades: Lex gestiona templates, Finn gestiona PDFs oficiales

---

## Flujo de Trabajo

### Crear nuevo contrato

1. **Lex** crea template en `/04_LEGAL/contratos/template_[tipo].md`
2. Alejandro/Cliente firma → PDF
3. **Finn** sube PDF a Drive → `/Documentos Legales/Contratos Firmados/`
4. **Finn** actualiza `/03_ADMIN/documentos_legales/_index_contratos.md`

### Recibir certificado oficial (ej: RUT)

1. Alejandro recibe PDF del SII
2. **Finn** sube a Drive → `/Documentos Legales/Certificados/`
3. **Finn** actualiza `/03_ADMIN/documentos_legales/_index_certificados_sii.md`
4. **Lex** puede referenciar desde `/04_LEGAL/` si necesita

### Actualizar política interna

1. **Lex** edita `/04_LEGAL/politicas/politica_privacidad.md`
2. Commit a Git con mensaje descriptivo
3. NO se sube a Drive (es template operativo, no oficial)

---

## Consecuencias

### Positivas

- ✅ **Claridad**: Está claro qué va dónde (operativo/versionable vs oficial/inmutable)
- ✅ **Separación de responsabilidades**: Lex cuida templates, Finn cuida PDFs oficiales
- ✅ **Git limpio**: No se llena de PDFs pesados
- ✅ **Backup automático**: Documentos oficiales en Drive con backup de Google
- ✅ **Acceso rápido**: Finn tiene índices para finanzas, Lex tiene templates para legal

### Negativas

- ⚠️ **Coordinación requerida**: Lex y Finn deben comunicarse cuando documento pasa de template a oficial
- ⚠️ **Dos lugares para "legal"**: Humano debe saber buscar según tipo de documento

### Neutras

- 📝 Requiere READMEs claros en ambas ubicaciones
- 📝 Índices deben mantenerse actualizados

---

## Implementación

1. ✅ Crear `/Empresa/04_LEGAL/README.md` con guía completa
2. ✅ Crear `/03_ADMIN/documentos_legales/README.md` explicando propósito
3. ✅ Crear templates de índices (`_index_*.md`)
4. ✅ Actualizar `/Empresa/README.md` con descripción clara de `/04_LEGAL/`
5. ✅ Actualizar `/03_ADMIN/README.md` con sección de `documentos_legales`
6. ✅ Crear este ADR

---

## Criterios de Decisión

**Pregunta**: ¿Dónde va este documento?

```
¿Es un template o política operativa?
  → SÍ → /04_LEGAL/ (Git, Lex gestiona)
  → NO → Continuar

¿Es un PDF oficial firmado/certificado?
  → SÍ → Drive (Finn gestiona) + índice en /03_ADMIN/
  → NO → /04_LEGAL/ si es legal, otro lugar si no lo es
```

---

## Lecciones Aprendidas

1. **Separar por mutabilidad**: Documentos que cambian (templates) vs documentos inmutables (PDFs oficiales)
2. **Separar por rol**: Lex cuida lo operativo-legal, Finn cuida lo oficial-financiero
3. **Índices son clave**: Permiten acceso rápido sin duplicar PDFs
4. **READMEs exhaustivos**: Evitan confusión futura

---

**Revisiones**:
- 2025-12-27: Creado (Nzero + Alejandro)

**Referencias**:
- `/Empresa/04_LEGAL/README.md`
- `/Empresa/03_ADMINISTRACION_FINANZAS/documentos_legales/README.md`
- `ADR-006`: Ubicación de scripts de setup
