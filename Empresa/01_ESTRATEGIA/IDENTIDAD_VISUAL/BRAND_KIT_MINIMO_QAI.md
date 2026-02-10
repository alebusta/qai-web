# Brand Kit mínimo — The QAI Company (QAI)

> Objetivo: una **fuente única de verdad** para propuestas, emails y material comercial.
> Este kit es “mínimo viable”: suficiente para consistencia, sin bloquear avances.

## 1) Logo
- Archivo oficial (fondo blanco): [Empresa/01_ESTRATEGIA/IDENTIDAD_VISUAL/logoQAI.png](Empresa/01_ESTRATEGIA/IDENTIDAD_VISUAL/logoQAI.png)
- Archivo recomendado (fondo transparente): [Empresa/01_ESTRATEGIA/IDENTIDAD_VISUAL/logoQAI_transparent.png](Empresa/01_ESTRATEGIA/IDENTIDAD_VISUAL/logoQAI_transparent.png)
- Uso:
  - Fondo preferido: blanco.
  - Si el logo va sobre un fondo no blanco/gradiente: usar la versión transparente.
  - Tamaño recomendado en email: 140–160px ancho.
  - Tamaño recomendado en PDF: 28–36px alto.
  - Mantener aire alrededor del logo (mín. 12px).

## 2) Tipografía (MVP)
Como no tenemos aún tipografías corporativas embebidas/licenciadas, el estándar MVP es **system font stack**:
- `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`

Reglas:
- Evitar tipografías decorativas.
- Jerarquía por tamaño/peso, no por “ruido visual”.

## 3) Paleta (MVP)
Colores pensados para sobriedad + acento moderno (alineado al logo):
- `--qai-ink`: `#111827` (texto principal)
- `--qai-muted`: `#6B7280` (texto secundario)
- `--qai-line`: `#E5E7EB` (líneas y bordes)
- `--qai-bg`: `#F3F4F6` (fondo suave)
- `--qai-primary`: `#1976D2` (azul QAI)
- `--qai-accent`: `#14B8A6` (acento turquesa)

Extensión mínima (operación / dashboards / semáforos):
- `--qai-success`: `#16A34A`
- `--qai-warning`: `#F59E0B`
- `--qai-danger`: `#DC2626`
- `--qai-info`: `#2563EB`
- `--qai-highlight`: `#EEF2FF` (fondo suave para callouts)

Paleta de gráficos (categorías, sobria y legible en blanco):
- `--qai-chart-1`: `#1976D2` (azul)
- `--qai-chart-2`: `#14B8A6` (turquesa)
- `--qai-chart-3`: `#7C3AED` (violeta)
- `--qai-chart-4`: `#F59E0B` (ámbar)
- `--qai-chart-5`: `#0EA5E9` (celeste)
- `--qai-chart-6`: `#111827` (ink)

Reglas:
- Usar `--qai-primary` para títulos/secciones y CTAs.
- Usar `--qai-accent` como detalle (gradientes, highlights), no como color dominante.

### Tokens CSS (nombres canónicos)
Para HTML/CSS (propuestas y futuros decks HTML), usar esta convención:
- Base: `--qai-ink`, `--qai-muted`, `--qai-line`, `--qai-bg`, `--qai-primary`, `--qai-accent`
- Estados: `--qai-success`, `--qai-warning`, `--qai-danger`, `--qai-info`
- Charts: `--qai-chart-1..6`

## 4) Layout (A4, propuestas)
- Márgenes: 18mm (top/right/bottom/left).
- Ancho de texto cómodo: 60–85 caracteres por línea.
- Espaciado: 8 / 12 / 16 / 24 px (múltiplos de 4).
- Radio (cards): 12–14px.
- Bordes: 1px `--qai-line`.

Escala recomendada (múltiplos de 4):
- `--space-1`: 4px
- `--space-2`: 8px
- `--space-3`: 12px
- `--space-4`: 16px
- `--space-5`: 24px
- `--space-6`: 32px

Jerarquía tipográfica mínima (PDF/HTML):
- H1 (portada): 40–56px, weight 700
- H2 (secciones): 20–24px, weight 650–700
- H3 (subsecciones): 14–16px, weight 650
- Body: 11–12.5pt, weight 400
- Small: 9–10pt, color `--qai-muted`

## 5) Deck 16:9 (MVP)
Objetivo: un deck de 10–12 slides, con grilla consistente y 1 mensaje por slide.

### Tamaño y safe area
- Canvas: **1920×1080** (16:9)
- Safe margins (recomendado): **96px** (izq/der) y **80px** (arriba/abajo)

### Grilla (12 columnas)
- Columnas: 12
- Gutter: 32px
- Baseline spacing: múltiplos de 8px

### Tipografía (deck)
- Título (H1): 56–72px, weight 700, tracking -0.02em
- Subtítulo (H2): 32–40px, weight 650
- Body: 24–28px, weight 400
- Caption/footnote: 16–18px, color `--qai-muted`

### Componentes (mínimos)
- **Cover**: título + subtítulo + cliente + fecha (sin ruido)
- **Section divider**: 1 frase + 1 insight clave
- **2-column**: izquierda (idea), derecha (bullets/tabla)
- **KPI cards (3-up)**: 3 tarjetas con label + valor + micro-explicación
- **Timeline**: tabla 2–4 filas (Fase / Resultado / Semana)
- **Inversión**: tabla (MVP / mensual) + supuestos
- **Architecture (alto nivel)**: 4–6 cajas, flechas mínimas

Reglas:
- No más de 6 bullets por slide.
- Preferir tablas y diagramas simples sobre texto largo.
- Un CTA único en el cierre.

## 6) Voz y tono (QAI)
Basado en manifiesto/overview:
- **Sin humo**: concreto, verificable, accionable.
- **Minimalismo radical**: densidad alta, estructura escaneable.
- **Humano al centro**: IA como palanca, HITL como control.
- **Cero burocracia**: cada sección debe ayudar a decidir.

Checklist rápido:
- ¿Se entiende el “qué” en 10 segundos?
- ¿Se entiende el “por qué ahora” en 20 segundos?
- ¿Hay un CTA único?

## 7) Email corporativo (SSOT)
- Template base oficial: [Empresa/03_ADMINISTRACION_FINANZAS/templates/BASE_EMAIL_CORPORATIVO.md](Empresa/03_ADMINISTRACION_FINANZAS/templates/BASE_EMAIL_CORPORATIVO.md)
- Preview HITL: `TorreDeControl/temp_files/email_preview.html`

## 8) Propuestas (SSOT)
- Template HTML: [Empresa/02_COMERCIAL/templates/proposal/proposal_base.html](Empresa/02_COMERCIAL/templates/proposal/proposal_base.html)
- CSS: [Empresa/02_COMERCIAL/templates/proposal/proposal_style.css](Empresa/02_COMERCIAL/templates/proposal/proposal_style.css)
- Preview HTML: `TorreDeControl/temp_files/proposal_preview.html`

Componentes (mínimos) a estandarizar:
- Portada “frame blanco” (premium, 1 idea)
- Header/footers discretos
- Cards (callout) para “Resumen ejecutivo”
- Tablas (timeline / inversión) con zebra suave + bordes finos
- Badges de estado (success/warning/danger)

## Pendiente (Brand Kit completo)
- Tipografía corporativa (archivo + licencia + embedding)
- Variante logo (SVG, monocromo, negativo)
- Paleta extendida (alertas, semáforos, gráficos) + guía de uso
- Grilla deck 16:9 y componentes (cards, tablas, diagramas)
- Plantilla deck (SSOT) + componentes reutilizables
- Librería de gráficos (colores + estilos de ejes/labels)
