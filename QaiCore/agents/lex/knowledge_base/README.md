# Knowledge Base - Lex (Legal)

Este directorio contiene la información legal de referencia que Lex consulta antes de responder.

## 📁 Estructura

```
knowledge_base/
├─ codigo_tributario_chile_resumen.md    → Normativa SII, IVA, Patentes
├─ ley_sociedades_spa.md                 → Ley 20.190 (SpA en Chile)
├─ casos/                                 → Casos históricos de QAI
│  └─ constitucion_qai_2025.md           → Proceso constitución The QAI Company
└─ plantillas/                            → Templates de documentos legales
   ├─ contrato_servicios_b2b.md          → Contrato tipo B2B
   └─ carta_autorizacion_domicilio.md     → Modelo autorización domicilio
```

## 📝 Cómo Usar

### Para Humanos:
1. Agregar nuevos documentos en formato Markdown
2. Usar nombres descriptivos (ej: `decreto_ley_XXX_resumen.md`)
3. Incluir siempre: Fecha, Fuente, Resumen ejecutivo

### Para Agentes (Lex):
```markdown
1. Buscar keywords en nombres de archivos
2. Leer archivo completo si es <50KB
3. Citar fuente al responder: "Según [nombre_archivo]..."
```

## ✅ Estándares de Documentación

Cada archivo debe tener:
```markdown
# [Nombre del Documento Legal]

**Fuente**: [URL oficial o referencia]
**Fecha**: [Última actualización]
**Aplica a**: [Chile/QAI/General]

## Resumen Ejecutivo
[3-5 líneas clave]

## Detalle
[Contenido estructurado]
```

## 🔄 Actualización

- **Frecuencia**: Cuando cambie normativa o surjan casos nuevos
- **Responsable**: Founder + Lex (sugerencias)
- **Validación**: Siempre contrastar con fuentes oficiales (SII, BCN)

---

**Creado**: 26-Dic-2025  
**Próxima revisión**: Cuando sea necesario
