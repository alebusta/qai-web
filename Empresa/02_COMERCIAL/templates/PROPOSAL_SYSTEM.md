# Sistema de Propuestas QAI — Executive Horizon

## Propósito
Estandarizar la generación de entregables comerciales de altísimo impacto mediante ingeniería de diseño que garantice consistencia visual radical y excelencia técnica.

## 1. Identidad Visual: "QAI Executive Horizon"
Este estilo es el estándar oficial para propuestas que requieren posicionar tecnología y vanguardia.

### Paleta de Colores (Brand Kit Oficial)
- **Primario**: `#1976D2` (Azul QAI) - Títulos y énfasis.
- **Portada**: `#0F172A` (Azul Profundo) - Fondos de impacto.
- **Acento**: `#14B8A6` (Turquesa) - Highlights y gradientes.
- **Operación**: `#16A34A` (Verde) - Iconografía de éxito.

### Tipografía e Iconos
- **Fuente**: Inter / System Stack (San Serif).
- **Iconografía**: **Material Design Icons** (solo via motor Playwright para PDF).

---

## 2. Tooling (Motor Golden 💎)

### Generación de Alta Fidelidad
Cualquier propuesta DEBE generarse usando el motor unificado:
`QaiCore/tools/generate_all_pdfs.py`

**Por qué este motor es obligatorio:**
1.  **Race conditions**: Sincroniza la descarga de fuentes externas antes del renderizado.
2.  **Formatos**: Fuerza el Deck a 1280x720px (16:9) y la Propuesta a A4 sin bordes blancos.
3.  **Local Assets**: Se conecta al servidor interno (`port 8585`) para cargar logos sin fallos de ruta.

---

## 3. Workflow Maestro (Agent Friendly)

### Paso 1: Preparación
1.  Servidor activo: `python -m http.server 8585` en la raíz.
2.  Insumos: `Propuesta_ESTR_[CLIENTE].html` y `Deck_[CLIENTE].html`.

### Paso 2: Producción
Ejecutar el script desde `QaiCore`:
`python QaiCore/tools/generate_all_pdfs.py`

### Paso 3: Protección "Master Design" (Fuerza de Ley)
Una vez que el diseño es aprobado por el usuario, **clonar** los HTMLs como:
- `Deck_[CLIENTE]_MASTER_DESIGN.html`
- `Propuesta_ESTR_[CLIENTE]_MASTER_DESIGN.html`
Estos archivos están exentos de limpiezas rutinarias y sirven como "fuente de verdad" absoluta. **Borrarlos se considera un fallo técnico grave.**

### Paso 4: Despacho (Email Premium)
Para el envío del paquete comercial, es mandatorio usar la cadena de herramientas de alta fidelidad:

1.  **Renderizado**: `QaiCore/tools/render_email.py`
    *   Usa el motor `markdown` real (librería python).
    *   Inyecta automáticamente la estética **Executive Horizon**.
2.  **Vista Previa (HITL)**: Validar en `TorreDeControl/temp_files/email_preview.html` (vía http://localhost:8585 para visualización de logos).
3.  **Envío**: `QaiCore/tools/gmail.py` con el argumento `--attach` para incluir los PDFs finales.

---

## 4. Estructura de Salida (Digital HQ)
Los archivos finales se centralizan en la carpeta de entrega del cliente:
`Empresa/02_COMERCIAL/clientes/[CLIENTE]/entrega/`

---
*Este documento invalida cualquier instrucción previa de generación via CLI o browser manual. Actualizado al 23-Ene-2026.*
