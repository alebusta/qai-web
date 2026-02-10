# ADR-016: Workflow de Correo Electrónico de Alta Fidelidad

## Estado
Aceptado (23 de enero de 2026)

## Contexto
Tras la formalización de los entregables PDF de alta gama (Executive Horizon), era imperativo que el vehículo de entrega (el correo electrónico) mantuviera la misma calidad estética y técnica. Las integraciones previas fallaban en encoding, renderizado de markdown y visualización de logos en previsualización local.

## Decisiones (Evolución)

1.  **Motor de Renderizado**: Se adoptó la librería `markdown` de Python (`render_email.py`). Permite jerarquías semánticas y links de marca.
2.  **Identidad Visual Inyectada**: El diseño no depende del input del agente, sino de la plantilla maestra `BASE_EMAIL_CORPORATIVO.md`.
3.  **Cross-Origin Preview**: Inyección de URLs de `localhost:8585` para previsualizar logos.
4.  **Protocolo Multi-Adjunto**: Soporte nativo para Propuesta + Deck en `gmail.py`.

### v1.5 (03-Feb-2026): Estética CIAL & Bulletproof Fix
Tras pruebas en Gmail y Hotmail, se detectaron inconsistencias de márgenes y colores por el filtrado de CSS de los clientes de correo.

1.  **Layout Bulletproof**: El template maestro migró de una estructura basada en `<div>` a una basada en **tablas HTML anidadas**. Esto blinda los márgenes y anchos en todas las plataformas.
2.  **Estética CIAL (SSOT)**: Se definió el look "CIAL Alimentos" como el estándar corporativo:
    *   **Cuerpo**: Gris pizarra premium (`#374151`).
    *   **Negritas**: Gris medio industrial (`#5b5d61`).
    *   **Alineación**: Logo y firma a la izquierda, footer minimalista centrado.
3.  **Color Inlining**: Implementación de inlining agresivo de colores y fuentes para eludir el filtrado de Gmail.

## Consecuencias
*   **Positivas**: Los clientes perciben una experiencia de marca unificada. Workflow "agnóstico" al cliente de correo.
*   **Atemporal**: Garantiza que el Digital HQ pueda operar de forma autónoma con total seguridad visual.
*   **Simplicidad**: El agente solo provee el cuerpo, el motor aplica la "Capa de Marca" automáticamente.
