# Checklist: Cierre de Proyecto (Para Nzero)

> **Propósito**: Asegurar que TODO se actualice cuando un proyecto se declara completado.

---

## 📋 Checklist Obligatorio

Cuando declares un proyecto como "100% completado" o "Beta-ready", **DEBES** realizar TODOS estos pasos:

### 1. Actualizar STATUS.md
- [ ] Marcar features como completadas (✅)
- [ ] Cambiar estado general del proyecto
- [ ] Si aplica: Declarar como "LISTO" o "100%"
- [ ] Actualizar sección de "Tareas Inmediatas" con próximos pasos

### 2. Actualizar CHANGELOG.md
- [ ] Crear entrada con fecha completa
- [ ] **Tipo**: "Hito Comercial / Cierre de Proyecto"
- [ ] **Contexto**: Qué se auditó/verificó
- [ ] **Decisión/Acción**: Listado de features verificadas
- [ ] **Impacto**: Qué se desbloquea ahora

### 3. Actualizar INBOX.md
- [ ] Marcar tareas del proyecto como `[x]` completadas
- [ ] Agregar entrada en "Log de Procesamiento" con resumen final
- [ ] Verificar que no queden tareas del proyecto sin marcar

### 4. Actualizar PRD (si existe)
- [ ] Marcar user stories como completados
- [ ] Actualizar estado del documento

### 5. Crear/Actualizar Walkthrough
- [ ] Documentar qué se hizo
- [ ] Screenshots/evidencia si aplica
- [ ] Próximos pasos sugeridos

### 6. Notificar Usuario
- [ ] Resumen claro de lo completado
- [ ] Links a documentos actualizados
- [ ] Confirmación explícita: "Proyecto X está 100% listo"

---

## ❌ Errores Comunes

### Error 1: "Dije que actualicé pero no lo hice"
**Síntoma**: Usuario pregunta dónde está la actualización que mencionaste.

**Causa**: Mencionaste que ibas a actualizar pero:
- El replace_file_content falló silenciosamente
- Olvidaste hacer el commit de la actualización
- Solo actualizaste STATUS pero no CHANGELOG

**Solución**:
1. SIEMPRE verificar que el tool call fue exitoso
2. NUNCA decir "actualicé X" sin confirmar que el archivo cambió
3. Usar este checklist

### Error 2: "Actualicé solo STATUS.md"
**Síntoma**: STATUS.md está actualizado pero CHANGELOG.md no tiene entrada.

**Causa**: Asumes que actualizar STATUS es suficiente.

**Solución**: CHANGELOG es **obligatorio** para hitos importantes. STATUS es estado actual, CHANGELOG es historial.

### Error 3: "No documenté en walkthrough"
**Síntoma**: Usuario no sabe qué se hizo exactamente.

**Causa**: Cerraste el proyecto sin crear artifact de resumen.

**Solución**: Walkthrough es la "prueba de trabajo". Siempre créalo al cerrar proyectos grandes.

---

## 🔍 Auto-Verificación

Antes de decir "Proyecto X está 100% listo", pregúntate:

1. **¿Actualicé STATUS.md con estado final?** → Sí/No
2. **¿Creé entrada en CHANGELOG.md con fecha de hoy?** → Sí/No
3. **¿Marqué tareas en INBOX.md como completadas?** → Sí/No
4. **¿Actualicé PRD si existía?** → Sí/No/N/A
5. **¿Creé walkthrough con evidencia?** → Sí/No
6. **¿Verifiqué que los cambios se guardaron (no fallaron)?** → Sí/No

Si alguna respuesta es "No", **NO DIGAS que el proyecto está listo**.

---

## 📝 Template de Entrada CHANGELOG

```markdown
#### [DD-Mes]: [Nombre Proyecto] - 100% Completado
**Tipo**: Hito Comercial / Cierre de Proyecto

**Contexto**: Se realizó auditoría final del código contra [documento de referencia].

**Decisión/Acción**:
- [PROYECTO] Verificación de [Feature 1]: ✅ [Evidencia]
- [PROYECTO] Verificación de [Feature 2]: ✅ [Evidencia]
- [PROYECTO] Actualización de [documento]: [Cambio específico]
- [PROYECTO] Actualización de STATUS.md: [Estado nuevo]

**Impacto**: [Proyecto] oficialmente listo para [próximo paso]. [Qué se desbloquea].
```

---

## 🚨 Si Olvidaste Algo

**Escenario**: El usuario te señala que falta una actualización.

**Respuesta correcta**:
1. Disculparse: "Tienes razón, faltó actualizar [X]"
2. Revisar qué falló
3. Corregir inmediatamente
4. Actualizar este checklist si descubres nuevo caso

**Respuesta INCORRECTA**:
- "Pero sí actualicé" (sin verificar)
- "Debe ser un error del sistema"
- Inventar excusas

---

**Creado**: 27-Dic-2025  
**Razón**: Prevenir que se repita el olvido de actualizar CHANGELOG al cerrar FedEx Invoice Matcher  
**Uso**: Consultar SIEMPRE antes de declarar proyecto completado
