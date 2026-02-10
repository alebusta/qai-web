# Prompts de Inicio - Torre de Control QAI

> **Guía rápida para iniciar conversaciones con agentes IA que automáticamente activen el protocolo de Torre de Control**

---

## 🎯 Escenario 1: Inicio General (Cualquier Agente)

### **Prompt Básico** (Copy-Paste Ready)

```
Hola! Soy Alejandro, founder de The QAI Company.

ANTES de responder, lee estos archivos para tener contexto:
1. /TorreDeControl/STATUS.md (estado actual de la empresa)
2. /TorreDeControl/INBOX.md (tareas pendientes)

Luego dime:
- ¿Qué día es hoy?
- ¿Qué tareas tengo urgentes?
- ¿En qué debería trabajar primero?
```

**Qué logra este prompt**:
- ✅ Agente lee STATUS e INBOX automáticamente
- ✅ Usa time_utils para saber la fecha
- ✅ Prioriza tareas por urgencia
- ✅ Te da recomendación de qué hacer primero

---

## 🎯 Escenario 2: Invocar Agente Específico (Lex - Legal)

### **Prompt para Lex**

```
Hola! Soy Alejandro de The QAI Company.

Por favor carga tu system prompt desde:
/QaiCore/agents/lex/system_prompt.md

Luego, siguiendo el protocolo:
1. Lee STATUS.md e INBOX.md
2. Dame el contexto temporal actual
3. Revisa si hay tareas legales urgentes [Legal]

¿Qué consulta legal tengo pendiente?
```

**Qué logra**:
- ✅ Carga el system_prompt completo de Lex
- ✅ Activa protocolo legal específico
- ✅ Filtra tareas con tag `[Legal]`

---

## 🎯 Escenario 3: Mode "Daily Standup"

### **Prompt Standup Matutino**

```
Buenos días! Soy Alejandro.

Quiero mi daily standup. Lee:
- /TorreDeControl/STATUS.md
- /TorreDeControl/INBOX.md

Luego dame:
1. Fecha/hora actual
2. Top 3 tareas más urgentes (con días restantes)
3. Recordatorios críticos para HOY
4. Sugerencia de orden de trabajo

Formato: Conciso, bullet points.
```

**Qué logra**:
- ✅ Briefing rápido en <2 min
- ✅ Enfoque en lo crítico
- ✅ Plan del día priorizado

---

## 🎯 Escenario 4: Trabajar en Tarea Específica

### **Prompt Enfocado**

```
Hola! Necesito trabajar en una tarea específica.

1. Lee /TorreDeControl/INBOX.md
2. Busca: "Procesar transcripción reunión 22-Dic"
3. Ayúdame a completarla

Cuando termine:
- Marca como [x] en INBOX
- Actualiza STATUS.md
- Deja nota en el log
```

**Qué logra**:
- ✅ Foco en una tarea
- ✅ Agente sabe qué actualizar al terminar
- ✅ Mantiene sistema sincronizado

---

## 🎯 Escenario 5: Procesamiento Automático de INBOX

### **Prompt Batch Processing**

```
Hola! Vamos a procesar el INBOX.

Lee:
- /TorreDeControl/INBOX.md
- /QaiCore/playbooks/process_inbox_task.md

Ejecuta el playbook para tareas con tag [Legal].
Procesa en orden de urgencia.

Reporta progreso después de cada tarea.
```

**Qué logra**:
- ✅ Procesamiento automático por categoría
- ✅ Sigue playbook establecido
- ✅ Reporta progreso incremental

---

## 📋 Prompt Mínimo (Ultra-Corto)

Si quieres el **prompt más corto posible**:

```
Lee /TorreDeControl/STATUS.md e INBOX.md.
¿Qué día es hoy?
¿Qué tengo urgente?
```

---

## 🔧 Personalizaciones Útiles

### **Agregar Contexto de Proyecto**

```
...además, estoy trabajando en FedEx Invoice Matcher.
Prioriza tareas relacionadas con FedEx.
```

### **Pedir Análisis de Urgencias**

```
...además, usa /QaiCore/tools/time_utils.py
para calcular días restantes de cada tarea.
```

### **Solicitar Formato Específico**

```
...al final, dame el resumen en formato tabla Markdown.
```

---

## ✅ Checklist de Validación

Después de dar el prompt, verifica que el agente:

- [ ] Mencionó la fecha/hora actual
- [ ] Leyó STATUS.md (menciona info específica del estado)
- [ ] Leyó INBOX.md (lista tareas pendientes)
- [ ] Calculó urgencias (si pediste priorización)
- [ ] Sugirió siguiente acción

**Si NO cumple alguno**: Re-prompt con instrucción más explícita.

---

## 🎯 Recomendación de Uso

### **Primera vez del día**:
```
Usa: Prompt "Daily Standup" (Escenario 3)
```

### **Trabajar en algo específico**:
```
Usa: Prompt "Tarea Específica" (Escenario 4)
```

### **Consulta legal/financiera**:
```
Usa: Prompt "Agente Específico" (Escenario 2)
```

### **Revisar estado general**:
```
Usa: Prompt "Inicio General" (Escenario 1)
```

---

## 🚀 Ejemplo Real de Conversación

### **TÚ:**
```
Hola! Lee /TorreDeControl/STATUS.md e INBOX.md.
¿Qué día es hoy? ¿Qué tengo urgente?
```

### **AGENTE (ideal):**
```
Hoy es Viernes 27 de Diciembre de 2025, 09:30.

He revisado STATUS e INBOX. Tareas URGENTES:

🔴 HOY (quedan 0 días):
- Procesar transcripción reunión GZ (22-Dic)

🔴 URGENTE (quedan 1 día):
- Desarrollar Dashboard FedEx (deadline: 28-Dic)

🟠 Alta (quedan 3 días):
- Activar Digipass Banco Chile (Lunes 30-Dic)

Recomendación: Empezar por la transcripción GZ (más atrasada).
¿Quieres que te ayude con esa?
```

---

**Creado**: 26-Dic-2025  
**Para**: Testing de Torre de Control con agentes frescos  
**Próxima actualización**: Cuando agregues más agentes (Finn, Builder)
