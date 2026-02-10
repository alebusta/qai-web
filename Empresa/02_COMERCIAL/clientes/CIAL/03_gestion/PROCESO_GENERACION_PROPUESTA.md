# Protocolo de Generación de Propuestas Estratégicas QAI

## 1. Visión General
Este documento detalla el flujo de trabajo institucional para la creación, renderizado y entrega de propuestas comerciales de alto impacto, garantizando consistencia visual y técnica.

## 2. Flujo de Trabajo (Caso CIAL Alimentos)

### Fase A: Preparación de Insumos
1. **Briefing**: Notas de reuniones y análisis de tendencias almacenados en `TorreDeControl/temp_files`.
2. **Drafting Markdown**: Redacción técnica de la propuesta y el deck en archivos `.md`.

### Fase B: Desarrollo de Entregables (HTML/Aesthetics)
1. **Propuesta Estratégica**: Generación de HTML semántico con diseño premium y estilos de impresión (`@media print`) optimizados para A4.
2. **Deck Ejecutivo**: Sistema de slides interactivo en HTML con escalado automático y navegación.
3. **Mockup Funcional**: Dashboard de inteligencia (ECharts/Vanilla CSS) para tangibilizar la solución.

### Fase C: Generación de PDF (High Fidelity)
Para evitar los errores comunes de impresión de navegadores (cortes de tablas, logos perdidos), se utiliza un motor de renderizado basado en **Playwright**:
- **Herramienta**: `generate_pdfs.js`
- **Capacidades**:
    - Forzado de dimensiones exactas (A4 Portrait para propuesta, 1280x720 Landscape para Deck).
    - Inyección de rutas absolutas (`file:///`) para recursos locales.
    - Prevención de cortes de contenido mediante `break-inside: avoid`.

### Fase D: Entrega Corporativa (Gmail API)
La entrega se realiza mediante un script automatizado (`send_cial_email.py`) que:
1. Renderiza el cuerpo del mail con el **Base Template Corporativo QAI**.
2. Incrusta el logo institucional mediante **Content-ID (CID)**.
3. Adjunta los PDFs generados en la Fase C.
4. Soporta múltiples destinatarios.

## 3. Herramientas del Ecosistema
- **Frontend**: Vanilla CSS (Glassmorphism), ECharts, Material Icons.
- **Renderizado**: Node.js + Playwright (PDF Engine).
- **Envío**: Python + Google Discovery API (Gmail/Drive).
- **Storage Final**: `/Empresa/02_COMERCIAL/clientes/[CLIENTE]/entrega/`

## 4. Checklist de Validación Final
- [ ] PDFs sin contenido cortado o truncado.
- [ ] Paginación activa desde la página 2.
- [ ] Links externos operativos.
- [ ] Logo institucional visible en PDFs y Email body.
- [ ] Backups de archivos estáticos (`mockup/index.html`) para hosting.

---
*Documento de Memoria Institucional QAI | Enero 2026*
