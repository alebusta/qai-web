# Ejemplo de Uso: Time Utils para Agentes

Este archivo muestra cómo los agentes pueden usar las utilidades de tiempo para priorizar tareas.

## Escenario: Lex procesando INBOX

```python
from qaicore.tools import (
    get_current_context,
    prioritize_tasks,
    calculate_task_urgency
)

# 1. Obtener contexto temporal
contexto = get_current_context()
print(f"🕐 {contexto}")
# Output: "Hoy es Jueves 26 de Diciembre de 2025, 13:15"

# 2. Leer tareas del INBOX (simulado)
tareas_inbox = [
    "- [ ] [Legal] Consultar con Lex sobre declaración IVA (hasta 15-Ene)",
    "- [ ] [Legal] Revisar contrato FedEx (deadline: 2025-12-28)",
    "- [ ] [Legal] Verificar patente municipal (para el 30/12)",
    "- [ ] [FedEx] Procesar ejemplos de Eduardo",  # Sin deadline
]

# 3. Priorizar tareas
tareas_priorizadas = prioritize_tasks(tareas_inbox)

# 4. Mostrar al usuario con urgencias
print("\n📋 TAREAS LEGALES PRIORIZADAS POR URGENCIA:\n")

for i, tarea_info in enumerate(tareas_priorizadas, 1):
    print(f"{i}. {tarea_info['urgency_text']}")
    print(f"   {tarea_info['task']}")
    
    if tarea_info['is_overdue']:
        print(f"   ⚠️  ATRASADA: {abs(tarea_info['days_remaining'])} días")
    elif tarea_info['days_remaining'] is not None:
        print(f"   ⏰ Quedan {tarea_info['days_remaining']} días")
    print()

# Output esperado:
"""
📋 TAREAS LEGALES PRIORIZADAS POR URGENCIA:

1. 🔴 URGENTE (2 días)
   - [ ] [Legal] Revisar contrato FedEx (deadline: 2025-12-28)
   ⏰ Quedan 2 días

2. 🟠 Alta (4 días)
   - [ ] [Legal] Verificar patente municipal (para el 30/12)
   ⏰ Quedan 4 días

3. 🟡 Media (20 días)
   - [ ] [Legal] Consultar con Lex sobre declaración IVA (hasta 15-Ene)
   ⏰ Quedan 20 días

4. Sin fecha límite definida
   - [ ] [FedEx] Procesar ejemplos de Eduardo
"""
```

## Escenario 2: Calcular urgencia de tarea individual

```python
from qaicore.tools import calculate_task_urgency

tarea = "Implementar Dashboard (deadline: 2025-12-28)"

urgencia = calculate_task_urgency(tarea)

print(f"Nivel: {urgencia['urgency_level']}")
print(f"Texto: {urgencia['urgency_text']}")
print(f"Días restantes: {urgencia['days_remaining']}")
print(f"Score de prioridad: {urgencia['priority_score']}")

if urgencia['is_overdue']:
    print("⚠️ ESTA TAREA ESTÁ ATRASADA!")
```

## Formatos de Fecha Soportados

La función `parse_date_from_task()` reconoce:

- `15-Dic` o `15-dic` → 15 de Diciembre del año actual
- `15/12/2025` o `15/12` → 15 de Diciembre
- `2025-12-15` → Formato ISO
- `hasta 15 de diciembre` → Lenguaje natural

## Integrando con Playbook

```python
# En process_inbox_task.md, agregar al inicio:

# PASO 0: Contexto Temporal
from qaicore.tools import get_current_context, prioritize_tasks

print(get_current_context())

# PASO 1: Leer y priorizar INBOX
inbox_tasks = read_inbox()
prioritized = prioritize_tasks(inbox_tasks)

# PASO 2: Alertar si hay urgencias
critical_tasks = [t for t in prioritized if t['urgency_level'] in ['overdue', 'today', 'critical']]

if critical_tasks:
    print(f"⚠️ ATENCIÓN: {len(critical_tasks)} tareas críticas!")
    for task in critical_tasks:
        print(f"  - {task['urgency_text']}: {task['task']}")

# PASO 3: Procesar en orden de prioridad
for task_info in prioritized:
    process_task(task_info['task'])
```

## Uso en STATUS.md

Los agentes pueden agregar sección de urgencias al STATUS:

```markdown
## ⏰ URGENCIAS (Actualizadas: 26-Dic-2025 13:15)

### Tareas Críticas (Próximos 3 días)
- [🔴 HOY] Tarea X
- [🔴 URGENTE - 2 días] Tarea Y

### Tareas Atrasadas
- [⚠️ ATRASADA - 5 días] Tarea Z (deadline era: 21-Dic)
```

---

**Creado**: 26-Dic-2025  
**Para**: Uso de agentes IA en QaiCore
