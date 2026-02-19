---
description: Generación de entregables estratégicos con estética "QAI Executive Horizon"
---

# Workflow: Generación de Propuestas y Decks Premium

Este workflow blinda el proceso de creación de documentos de alto impacto para clientes, garantizando que el diseño "QAI Executive Horizon" se mantenga consistente y que las herramientas técnicas no se pierdan.

## 1. Identidad Visual: "QAI Executive Horizon"
Cualquier propuesta o deck debe seguir este patrón:
- **Portada**: Fondo "Deep Blue" (#0F172A), Título Blanco Masivo, Acento Turquesa (#14B8A6).
- **Contenido**: Fondo Blanco puro, Títulos en Azul QAI (#1976D2), Iconografía Material Design.
- **Relación de Aspecto (Decks)**: Siempre 16:9 (1280x720px) sin bordes blancos.
- **Formato (Propuestas)**: A4 con márgenes asimétricos (Izquierdo: 35mm, Derecho: 30mm).
- **Email**: Blanco bulletproof (tablas HTML), cuerpo #374151, negritas #5b5d61, acentos en #1976D2. Logo y firma a la izquierda.

## 2. Herramientas "Golden" (NO BORRAR)
Antes de crear scripts nuevos, el agente DEBE usar:
- **Motor de PDF**: `QaiCore/tools/generate_all_pdfs.py` (Sincroniza fuentes y fuerza dimensiones).
- **Servidor de Activos**: Servidor HTTP local en puerto `8585`.
- **Rutas de Logo**: Siempre via `http://localhost:8585/Empresa/01_ESTRATEGIA/IDENTIDAD_VISUAL/...` para evitar fallos de renderizado.

## 3. Pasos del Proceso

### Fase A: Mockup y Estructura
1.  **Markdown**: Redactar la narrativa en un archivo `.md`.
2.  **HTML Maestro**: Tomar el `MASTER_DESIGN.html` o la plantilla en `QaiCore/templates` y clonarla para el cliente.
3.  **Inspección**: Activar el servidor local y validar los iconos.

### Fase B: Producción de PDF
1.  **Pre-vuelo**: Asegurarse de que el servidor `python -m http.server 8585` esté corriendo en la **raíz del repo**.
2.  **Renderizado**: Ejecutar el motor desde la raíz usando el wrapper oficial (Regla TorreDeControl #8):
    - **Cliente CIAL** (default):  
      `QaiCore\qrun.bat QaiCore\tools\generate_all_pdfs.py`  
    - **Otro cliente** (ej. VinedosAustral):  
      `QaiCore\qrun.bat QaiCore\tools\generate_all_pdfs.py "<url_base>" "<path_base>" "<deck.html>" "<propuesta.html>"`
3.  **Troubleshooting (WinError 5 / Access Denied)**:
    - Si el IDE (Cursor/VSCode) bloquea la ejecución de Chromium, el script lanzará un aviso.
    - **Solución 1**: Ejecutar el comando en un terminal **externo** (CMD o PowerShell).
    - **Solución 2**: Ejecutar el IDE como Administrador.
    - **Solución 3**: Use la tarea de VS Code "Generar PDFs [Cliente]" que usualmente tiene permisos heredados distintos.
4.  **Control de Calidad**: Verificar que el PDF no tenga bordes blancos (sobrantes).


### Fase C: Despacho Premium
1.  **Render**: Usar `QaiCore/tools/render_email.py` con el cuerpo en Markdown.
2.  **Preview**: Validar en `email_preview.html`. Asegurar logo visible.
3.  **Envío**: Usar `QaiCore/tools/gmail.py` con `--attach` para ambos PDFs.

### Fase D: Limpieza Segura
- **Permitido**: Borrar archivos `.bak`, `.tmp` o versiones intermedias del HTML.
- **Prohibido**: Borrar scripts en `QaiCore/tools/` o archivos marcados como `MASTER_DESIGN`.

## 4. Cómo cambiar el Template
Si se desea actualizar la estética global:
1.  Modificar los archivos base en `Empresa/02_COMERCIAL/templates/executive_horizon/`.
2.  Actualizar la guía de estilo en este workflow.
3.  Probar el renderizado en formato A4, 16:9 y Email antes de considerar el template como "Validado".

---
*Protocolo de Continuidad Operativa QAI | Actualizado 23-Ene-2026*
