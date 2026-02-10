# Soporte y Mantenimiento - Gestión Zen

> **Filosofía:** Soporte proactivo y humano, escalado con IA cuando sea posible.

---

## 1. Canales de Soporte

### WhatsApp Business (Canal Principal)
*   **Número:** +56 9 XXXX XXXX
*   **Horario:** Lunes a Viernes, 9:00 - 18:00 hrs
*   **SLA:** Respuesta en < 2 horas (horario laboral)
*   **Uso:** Consultas rápidas, bugs urgentes, onboarding

### Email (soporte@gestionzen.cl)
*   **SLA:** Respuesta en < 24 horas
*   **Uso:** Consultas complejas, solicitudes de features, documentación

### Zoom (Agendado)
*   **Calendly:** calendly.com/gestionzen/soporte
*   **Duración:** 30 min
*   **Uso:** Onboarding, capacitación, troubleshooting complejo

---

## 2. Clasificación de Incidentes

### 🔴 Crítico (P0)
**Definición:** El sistema está caído o hay pérdida de datos.
*   **Ejemplos:**
    *   No se puede acceder a la plataforma
    *   Error al guardar gastos (pérdida de información)
    *   Cálculos de nómina incorrectos
*   **SLA:** Respuesta inmediata (< 30 min)
*   **Responsable:** Desarrollador (tú) directamente

### 🟡 Alto (P1)
**Definición:** Funcionalidad importante no disponible, pero hay workaround.
*   **Ejemplos:**
    *   IA de extracción de gastos no funciona (se puede digitar manual)
    *   Reportes no se generan
    *   Prorrateo da error en un caso específico
*   **SLA:** Respuesta en < 2 horas, solución en < 24 horas
*   **Responsable:** Soporte (Economista o Admins) → Escala a Dev si es técnico

### 🟢 Normal (P2)
**Definición:** Consulta de uso, mejora sugerida, bug menor.
*   **Ejemplos:**
    *   "¿Cómo exporto el reporte a Excel?"
    *   "El botón está mal alineado"
    *   "Sería bueno tener un filtro por fecha"
*   **SLA:** Respuesta en < 24 horas
*   **Responsable:** Soporte

---

## 3. Protocolo de Escalamiento

```
Cliente → WhatsApp/Email
    ↓
¿Es P0 (Crítico)?
    SÍ → Notificar a Desarrollador inmediatamente
    NO → Soporte intenta resolver
        ↓
    ¿Se resolvió?
        SÍ → Cerrar ticket
        NO → Escalar a Desarrollador (con contexto completo)
```

---

## 4. Mantenimiento Preventivo

### Semanal
*   [ ] Revisar logs de errores en Supabase
*   [ ] Monitorear uso de API Gemini (costos)
*   [ ] Verificar uptime (objetivo: 99.5%)

### Mensual
*   [ ] Actualizar dependencias de seguridad (npm audit)
*   [ ] Backup manual de base de datos (además del automático)
*   [ ] Revisar feedback de clientes y priorizar mejoras

### Trimestral
*   [ ] Auditoría de performance (tiempos de carga)
*   [ ] Revisión de costos de infraestructura (Supabase, Vercel)
*   [ ] Actualización de documentación

---

## 5. Base de Conocimiento (FAQ)

### Preguntas Frecuentes
1.  **¿Cómo recupero mi contraseña?**
    *   Ir a login → "Olvidé mi contraseña" → Revisar email
2.  **¿Por qué la IA no reconoce mi factura?**
    *   Verificar que sea PDF o imagen clara
    *   Probar con foto en buena iluminación
3.  **¿Puedo tener más de un administrador?**
    *   Sí, en Configuración → Usuarios → Invitar

### Tutoriales en Video (Pendiente)
*   Cómo subir un gasto con IA (3 min)
*   Cómo hacer un prorrateo (5 min)
*   Cómo generar una nómina (7 min)

---

## 6. Herramientas de Soporte

### Sistema de Tickets (Futuro)
*   **Opción 1:** Notion (gratis, simple)
*   **Opción 2:** Linear (más profesional)
*   **Por ahora:** Excel con columnas:
    *   ID | Fecha | Cliente | Prioridad | Descripción | Estado | Responsable

### Monitoreo
*   **Uptime:** UptimeRobot (gratis, 50 monitores)
*   **Errores:** Sentry (gratis hasta 5k eventos/mes)
*   **Analytics:** Google Analytics o Plausible

---

## 7. Costos de Soporte (Estimado)

| Concepto | Costo Mensual |
|----------|---------------|
| WhatsApp Business | Gratis |
| Email (Google Workspace) | $6 USD |
| Calendly | Gratis |
| UptimeRobot | Gratis |
| Sentry | Gratis (tier básico) |
| **TOTAL** | **~$6 USD/mes** |

*Nota: El costo real es el tiempo humano (10-20 horas/mes en etapa inicial).*
