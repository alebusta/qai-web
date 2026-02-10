# Torre de Control - QAI Company

> "La memoria colectiva de la empresa. El punto de partida de todo agente."

## 🎯 Propósito

Este directorio contiene el **estado operativo en tiempo real** de The QAI Company. A diferencia de `/Empresa/` (estrategia estática), aquí vive la **operación día a día**.

## 📂 Archivos Clave

### [`STATUS.md`](STATUS.md) - El Dashboard (Estado Actual)
**¿Qué es?** El estado actual de TODOS los proyectos, clientes y procesos. **SÓLO contiene hechos consumados y estados vigentes**, no tareas pendientes.

**¿Cuándo leerlo?** SIEMPRE al iniciar una conversación con un agente.

**¿Quién lo actualiza?** El Founder (Ale) o cualquier agente que complete una tarea importante.

---

### [`INBOX.md`](INBOX.md) - Fuente Única de Verdad (SSOT)
**¿Qué es?** La única fuente oficial de tareas pendientes, urgencias y próximos pasos.

**¿Cuándo usarlo?** Cuando tengas una idea o tarea pero no tiempo de ejecutarla ahora.

**Ejemplo:**
```markdown
- [ ] Procesar transcripción reunión GZ 22-dic
- [ ] Verificar con Lex próximos pasos legales
```

---

### [`CHANGELOG.md`](CHANGELOG.md) - Bitácora de Decisiones
**¿Qué es?** Log histórico de decisiones importantes y cambios de rumbo.

**¿Cuándo usarlo?** Para registrar hitos que quieras recordar en 6 meses.

---

### [`AGENT_ACTIVITY.md`](AGENT_ACTIVITY.md) - Log de Actividad de Agentes
**¿Qué es?** Registro cronológico de acciones significativas realizadas por agentes (Finn, Lex, Nzero).

---

### [`DISCOVERY_LOG.md`](DISCOVERY_LOG.md) - Bitácora de Hallazgos
**¿Qué es?** "Eurekas" y aprendizajes metodológicos (ej: estrategias FinOps o nuevas formas de trabajar).

---

### [`temp_files/`](temp_files/) - Landing Zone (Zona de Aterrizaje) 🆕

**¿Qué es?** Carpeta para archivos que el Founder sube para ser procesados o archivos temporales generados por agentes.

**🚨 REGLA DE ORO 🚨**: 
1. **SSOT**: Esta es la ÚNICA carpeta autorizada para archivos temporales. Está estrictamente **PROHIBIDO** crear carpetas `temp_files` o archivos sueltos en el root del proyecto o cualquier otra ubicación no oficial.
2. **LIMPIEZA**: Debe quedar VACÍA después de que el agente complete la acción (los archivos se mueven a su destino final o se borran).
3. **ZERO FOOTPRINT**: No dejes rastro de scripts auxiliares una vez cumplida su misión.

---

## 🤖 Protocolo para Agentes (INSTRUCCIONES)

Si eres un agente de IA trabajando con Alejandro, **SIEMPRE** sigue este flujo:

### 1️⃣ AL INICIAR UNA CONVERSACIÓN
```markdown
1. Lee `STATUS.md` para entender el contexto actual
2. Lee `INBOX.md` para ver tareas pendientes
3. Revisa `temp_files/` para ver si hay archivos nuevos para procesar 🆕
4. Lee `AGENT_ACTIVITY.md` para ver últimas acciones de agentes
5. (Solo Nzero) Lee `DISCOVERY_LOG.md` para ver hallazgos recientes
6. Menciona al usuario: "He revisado el STATUS..."
```

### 2️⃣ DURANTE EL TRABAJO
```markdown
- Si completas una tarea de INBOX → Marca como [x] y actualiza STATUS
- Si realizas acción significativa → Registra en AGENT_ACTIVITY.md
  (uploads, reportes, índices, declaraciones)
- Si descubres algo NUEVO e IMPORTANTE (regla, decisión):
  - Crea/Actualiza un documento en tu knowledge_base o en TorreDeControl/
  - Agrega UN resumen al archivo `DISCOVERY_LOG.md`
  - **NO** guardes logs de chat crudos
```

### 3️⃣ AL FINALIZAR (PROTOCOLO DE CIERRE AUTÓNOMO)
**Regla**: Ningún agente debe dar por terminada una tarea sin completar estos pasos proactivamente. No esperes a que el usuario lo pida.

1. **Sincronizar INBOX**: Marca como [x] todas las tareas completadas en `INBOX.md`.
2. **Actualizar STATUS**: Refleja el avance en `STATUS.md` (debe coincidir con INBOX y CHANGELOG). Actuliza la fecha de encabezado.
3. **Registrar Actividad**: Agrega fila a `AGENT_ACTIVITY.md` con las acciones significativas del día.
4. **Resumir Hallazgos**: Si hubo cambios metodológicos o decisiones técnicas (ADRs), actualiza `DISCOVERY_LOG.md`.
5. **Verificación de Limpieza**: Asegúrate de que `temp_files/` esté vacío si se procesaron archivos.
6. **Notificar**: CUALQUIER mensaje final que incluya "Hito completado" o "Cierre de sesión" DEBE ser precedido por la verificación de los puntos 1-5. **Si no has actualizado el INBOX y la Actividad, NO tienes permiso para despedirte.**

---

## 🚨 Reglas de Oro (Anti-Burocracia)

1. **Brevedad Radical**: STATUS.md debe leerse en <3 minutos. Si crece demasiado, archiva lo viejo en CHANGELOG.
2. **Sin Duplicación**: Si algo ya está en `/Empresa/` (docs estratégicos), NO lo copies aquí. Solo enlaza.
3. **Prohibida la Duplicación**: NO listes tareas pendientes en `STATUS.md`. Toda tarea, idea o pendiente debe vivir únicamente en `INBOX.md`. `STATUS.md` solo enlaza al INBOX para el detalle de pendientes.
4. **Acción > Perfección**: Mejor un STATUS "feo pero actualizado" que un documento perfecto desactualizado.
5. **Metadatos Obligatorios**: CUALQUIER agente que edite STATUS.md DEBE actualizar la fecha de "Última actualización" en el encabezado.
6. **Explicitud de Ramas**: Si se menciona un despliegue, DEBE especificarse si `main` y `develop` están sincronizados para evitar discusiones improductivas entre agentes.
7. **🚨 LA REGLA DE LOS 4 PUNTOS (ATOMICIDAD)**: Cada hito o tarea completada **DEBE** impactar simultáneamente en: `STATUS.md`, `INBOX.md`, `CHANGELOG.md` y `AGENT_ACTIVITY.md`. Si falta uno solo de estos archivos, la memoria institucional se considera ROTA y el agente ha fallado en su misión.
10. **Separación de Memoria (KB vs HQ)**: NO guardes archivos teóricos, metodológicos o borradores en `/Empresa/`. Estos deben ir a tu `knowledge_base` interna. Solo publica en `/Empresa/` entregables finales y consolidados.
8. **Regla de Ejecución de Tools (Terminal Fallback)**: Los agentes que utilicen herramientas de `/QaiCore/tools/` DEBEN ejecutarlas vía **Terminal** usando el wrapper oficial:
   `c:/Users/abustamante/TheQaiCo/QaiCore/qrun.bat <script.py> <argumentos>`
   *Esto garantiza que se use el entorno virtual aislado (.venv) con todas las librerías necesarias.*
9. **No Alucinar Rutas**: Antes de ejecutar un comando, verificar que los archivos existen usando `list_dir` o similares.

---

## 🔗 Integración con el HQ Digital

```
/TheQaiCo/
├─ /TorreDeControl/     ← TÚ ESTÁS AQUÍ (operación viva)
│  ├─ temp_files/       ← Landing Zone (InBox de archivos) 🆕
├─ /Empresa/            ← Estrategia, Legal, Docs estáticos
├─ /QaiLabs/            ← Productos en validación
├─ /QaiProd/            ← Productos en producción
└─ /QaiCore/            ← Agentes y herramientas (futuro)
```

**Flujo típico:**
1. Agente lee `TorreDeControl/STATUS.md` → Entiende qué se está haciendo HOY
2. Agente consulta `/Empresa/` → Contexto estratégico si necesita
3. Agente trabaja en `/QaiLabs/` o `/QaiProd/` → Ejecuta tareas
4. Agente actualiza `TorreDeControl/STATUS.md` → Deja registro para el próximo

---

**Última actualización**: 10 de Febrero de 2026 (Sync Protocol v1.1 - Zero Footprint)
**Mantenedor**: Alejandro Bustamante (Founder) / Nzero (Arch.)
