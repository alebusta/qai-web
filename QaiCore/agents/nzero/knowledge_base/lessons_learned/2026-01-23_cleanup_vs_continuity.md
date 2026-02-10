# Lesson Learned: El Riesgo de la Limpieza Excesiva (Cleanup vs Continuity)

**Fecha**: 23 de Enero de 2026  
**Agente**: Nzero (Architect)  
**Contexto**: Misión CIAL Alimentos (Generación de Propuestas)

## Incidente
Tras validar un diseño premium exitoso, se ejecutó una "limpieza de archivos innecesarios" para ahorrar contexto y espacio. Durante este proceso, se borraron sin querer las versiones finales del código HTML y los scripts de renderizado PDF de alta fidelidad.

**Consecuencia**: Se perdió la "perla de calidad" lograda, obligando a reconstruir todo el diseño y las herramientas desde cero durante 4 horas.

## Análisis de Causa Raíz
1.  **Falta de Etiquetado**: Los archivos finales no tenían una marca que los distinguiera de los archivos temporales (`deck.html` vs `deck_temp.html`).
2.  **Infraestructura Volátil**: Las herramientas de renderizado se consideraron "de proyecto" en lugar de "de sistema" (QaiCore).
3.  **Confianza Ciega en Cleanup**: El agente asumió que podía regenerar todo, ignorando que las iteraciones de diseño manuales no son determinísticas si se pierde el código base.

## Medidas Correctivas (Blindaje Permanente)
1.  **Sufijo MASTER_DESIGN**: Todo archivo aprobado que deba sobrevivir a las limpiezas DEBE llevar este sufijo.
2.  **Centralización QaiCore**: Los scripts de renderizado (`generate_all_pdfs.py`) han sido elevados a infraestructrua crítica y su borrado está prohibido.
3.  **Workflow Agentic**: Se creó `.agent/workflows/generar_propuesta_premium.md` para que la memoria operativa de cualquier agente cargue estas restricciones automáticamente al iniciar.
4.  **Aislamiento de Trabajo**: El cliente trabaja con sus archivos, pero el agente siempre tiene referenciados los templates maestros en `Empresa/02_COMERCIAL/templates/executive_horizon/`.

---
*Conclusión: La eficiencia del cleanup nunca debe comprometer la continuidad de la alta calidad.*
