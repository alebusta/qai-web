# Documentos Legales - Índice para Finanzas

> **Propósito**: Índice de documentos legales oficiales relevantes para operaciones financieras.  
> **Gestión**: Finn (Agente Financiero)  
> **Última actualización**: 27-Dic-2025

---

## 🎯 ¿Qué es esto?

Este directorio NO contiene los documentos legales en sí (están en Google Drive), sino **índices markdown** que apuntan a ellos con links directos.

**¿Por qué separado de `/04_LEGAL/`?**
- `/04_LEGAL/`: Lex gestiona templates y políticas operativas
- Aquí: Finn gestiona PDFs oficiales (RUT, escrituras, certificados) necesarios para finanzas

---

## 📁 Estructura

```
/documentos_legales/
├── README.md                      ← Este archivo
├── _index_escrituras.md           ← Escrituras de constitución
├── _index_certificados_sii.md     ← RUT, Inicio Actividades, etc.
├── _index_patentes.md             ← Patentes municipales
└── _index_poderes.md              ← Poderes notariales y autorizaciones
```

---

## 📋 Índices Disponibles

### [_index_escrituras.md](_index_escrituras.md)
Escrituras de constitución, modificaciones societarias, aumento de capital.

**Útil para**: Verificar objeto social, representantes legales, capital social.

### [_index_certificados_sii.md](_index_certificados_sii.md)
Certificados del Servicio de Impuestos Internos.

**Útil para**: 
- RUT (para facturas, declaraciones)
- Inicio de Actividades (para validar giros)
- Certificados de cumplimiento tributario

### [_index_patentes.md](_index_patentes.md)
Patentes municipales.

**Útil para**: Verificar que la empresa puede operar legalmente en la comuna.

### [_index_poderes.md](_index_poderes.md)
Poderes notariales de representación.

**Útil para**: Validar quién puede firmar contratos, abrir cuentas bancarias, etc.

---

## 🔄 Flujo de Trabajo

### Cuando llega documento oficial nuevo

1. **Finn** recibe instrucción de archivar documento (vía Alejandro o Lex)
2. **Finn** sube PDF a Google Drive → `/Documentos Legales/[categoría]/`
3. **Finn** actualiza índice correspondiente aquí con:
   - Nombre del documento
   - Fecha de emisión
   - Link a Drive
   - Descripción breve

### Cuando Finn necesita documento legal

1. Consulta índice relevante (ej: `_index_certificados_sii.md` para RUT)
2. Obtiene link a Drive
3. Descarga si es necesario para procesamiento

---

## 🤝 Coordinación con Lex

| Escenario | Quién gestiona | Dónde |
|-----------|----------------|-------|
| Template de contrato | Lex | `/04_LEGAL/contratos/` |
| Contrato firmado (PDF) | Finn | Drive + índice aquí |
| Política interna | Lex | `/04_LEGAL/politicas/` |
| Certificado SII | Finn | Drive + índice aquí |
| Minuta de reunión | Lex | `/04_LEGAL/minutas/` |
| Escritura notariada | Finn | Drive + índice aquí |

---

## 📝 Formato de Índices

Cada archivo `_index_*.md` sigue este formato:

```markdown
# Índice: [Categoría]

| Documento | Fecha Emisión | Link Drive | Notas |
|-----------|---------------|------------|-------|
| [Nombre] | YYYY-MM-DD | [Ver PDF](https://drive.google.com/...) | [Descripción] |
```

---

## 🚨 Importante

- **Índices siempre actualizados**: Cuando sube PDF a Drive, actualizar índice inmediatamente
- **Links funcionando**: Verificar que links a Drive sean accesibles
- **No duplicar**: PDFs viven SOLO en Drive, no en Git
- **Seguridad**: Links de Drive deben tener permisos correctos (solo propietario)

---

## 📚 Referencias

- **PDFs en Drive**: Ver `../GOOGLE_DRIVE_STRUCTURE.md`
- **Templates legales**: Ver `/Empresa/04_LEGAL/`
- **ADR sobre estrategia**: `/QaiCore/agents/nzero/knowledge_base/design_decisions/007_legal_documents_strategy.md`

---

**Creado**: 27-Dic-2025 (Nzero)  
**Mantenedor**: Finn (Agente Financiero)  
**Coordinación con**: Lex (para documentos operativos)
