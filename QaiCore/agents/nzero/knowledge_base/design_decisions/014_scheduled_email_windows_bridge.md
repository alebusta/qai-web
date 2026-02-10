# ADR-014: Capacidad de Envío Programado de Email (Windows Bridge)

**Fecha**: 2026-01-23  
**Estado**: Aceptado (Validado con prueba real 11:20 AM)  
**Contexto**: Se requería enviar correos electrónicos en una hora específica sin tener una infraestructura de servidor 24/7 o una cola de mensajería compleja.

## Problema
La herramienta `tools/gmail.py` solo soporta envíos inmediatos. Implementar un "cron" o un servicio de fondo permanente en el HQ representaba un costo de mantenimiento y complejidad innecesarios para la etapa actual.

## Alternativas Consideradas

### Opción 1: Implementar Worker/Producer en Supabase
- ✅ Tracción SaaS real, persistente.
- ❌ Requiere infraestructura de ejecución constante (Edge Functions o Servers) y monitoreo de colas.

### Opción 2: Windows Task Scheduler (Bridge) ⭐ ELEGIDA
- ✅ **Cero costo**: Usa el motor nativo del SO del host.
- ✅ **Confiable**: Maneja reintentos y logs de sistema.
- ✅ **Agnóstico**: Solo requiere un script `.bat` que invoque `qrun.bat`.
- ❌ **Trade-off**: Depende de que la máquina host esté encendida a la hora del envío.

## Decisión
Usar el **Programador de Tareas de Windows** como orquestador temporal de envíos programados. El agente debe:
1. Crear un script `.bat` en `temp_files/` que prepare el entorno y ejecute el comando.
2. Registrar la tarea usando `schtasks /create`.

## Consecuencias
- **Positivas**: Capacidad de programación inmediata disponible para todos los agentes sin cambios en el Core.
- **Negativas**: El humano debe estar consciente de que si apaga la laptop, el correo no sale hasta que se encienda y la tarea se dispare (según config).

## ☁️ Notas de Migración (Cloud)
Esta implementación es estrictamente **Local-First**. Si el Digital HQ se migra a un entorno de nube, esta decisión debe ser superseded por:
1. **Entorno Linux (VPS)**: Migrar de `schtasks` a `cron`.
2. **Entorno Serverless (Supabase)**: Migrar a Supabase Edge Functions invocadas por `pg_cron` o un servicio de colas persistente.
3. **GitHub Actions**: Uso de triggers `schedule` si el HQ opera vía CI/CD.

---
**Autor**: Nzero  
**Relacionado con**: ADR-012 (Comunicación Corporativa)
