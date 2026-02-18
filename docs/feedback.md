# Directiva de Diseño: Refactorización "QAI" (V2.0)

**Objetivo:** Elevar la percepción de marca de "SaaS estándar" a "Autoridad Intelectual & Consultoría Premium".

**Filosofía Visual:** Convergencia de Medium (Editorial), Apple (Estructura/Calma) y Jony Ive (Esencialismo).

---

## 1. Sistema de Diseño Global (Global Styles)

### A. Tipografía (Jerarquía Editorial)

- **Instrucción:** Implementar un sistema de pares tipográficos estricto.
    - **Titulares (H1, H2, H3):** Cambiar TODAS las instancias a una fuente **Serif Editorial** de alta calidad (Ej: *Tiempos Headline*, *Charter*, *Editorial New* o *Source Serif 4*).
    - **Cuerpo / UI / Etiquetas:** Mantener Sans-Serif geométrica/limpia (Ej: *Inter*, *Geist* o *Satoshi*).
    - **Dato Técnico (Opcional):** Usar Monoespaciada (*JetBrains Mono*) solo para números de datos o etiquetas pequeñas.

### B. Color y Logotipo (Esencialismo)

- **Logotipo:** Eliminar el gradiente púrpura/cian actual.
    - **Acción:** Convertir el logo a **Monocromo (Negro `#1C1C1E` o Gris Carbón)**. Si se requiere color, reducir la saturación al 20% para que sea casi imperceptible. La marca debe sentirse segura, no "gritar" atención.
- **Paleta de Colores:**
    - **Fondos Claros:** Eliminar el blanco puro (`#FFFFFF`). Usar **Blanco Hueso/Crema** (`#FAFAF9` o `#FDFDFD`) para reducir la fatiga visual.
    - **Fondos Oscuros:** Usar **Negro Suave** (`#050505` o `#121212`), nunca negro absoluto `#000000`.

### C. Textura y Atmósfera (Profundidad)

- **Instrucción:** El fondo blanco plano se siente "incompleto".
    - **Acción:** Añadir una capa de ruido (noise) granulado al 2-3% de opacidad sobre los fondos claros para simular papel de alta calidad.
    - **Alternativa:** Añadir líneas de cuadrícula o topografía de datos muy sutiles (opacity: 0.05) en el fondo.

---

## 2. Instrucciones por Sección (Paso a Paso)

### Sección 1: "Nuestro Motor" (Tarjetas de Servicios)

- **Iconografía (Crítico):**
    - **Eliminar:** Los iconos de línea actuales (cerebro, matraz, cohete). Son genéricos y bajan el valor percibido.
    - **Implementar:** Sustituir por **Formas Geométricas Abstractas 3D** (monocromáticas, textura mate/vidrio) O utilizar **Numeración Tipográfica Grande** (01, 02, 03) en fuente Monoespaciada.
- **Contenedores (Tarjetas):**
    - **Acción:** Las tarjetas actuales flotan sin definición.
    - **Opción A (Apple):** Añadir un fondo gris muy tenue (`#F5F5F7`) a cada tarjeta + `border-radius: 24px`.
    - **Opción B (Editorial):** Eliminar el borde de la tarjeta y usar líneas verticales divisoras de 1px (`#E5E5E5`) entre las columnas.
- **Títulos de Tarjeta:**
    - Cambiar "TheQai", "QaiLabs", "QaiProd" a la tipografía **Serif**. Tratarlos como nombres propios de sub-marcas.

### Sección 2: Manifiesto (Fondo Oscuro)

- **Titular Principal:**
    - Cambiar a **Serif**.
    - **Palabra Clave:** La palabra **"bisagra"** debe ir en **Cursiva (Italic)** dentro de la fuente Serif. Esto le da voz y énfasis narrativo.
- **Cuerpo de Texto:**
    - **Alineación:** Dejar de centrar el párrafo explicativo ("Vemos una desconexión..."). **Alinear a la izquierda**.
    - **Ancho:** Restringir el ancho del contenedor de texto a `60ch` (aprox 600px) para lectura óptima.
- **Estructura Visual:**
    - Insertar una **línea horizontal (hairline)** de 1px (color gris oscuro al 20% opacidad) separando el texto del manifiesto de las 3 columnas inferiores (Bootstrapped, AI-First, Democratización). Esto ancla visualmente el contenido.

### Sección 3: Soluciones (Grid Final)

- **Etiquetas de Estado:**
    - **Eliminar:** El texto gris plano "Próximamente".
    - **Implementar:** Componente tipo **"Pill" (Pastilla)**.
        - Estilo: Borde 1px sólido, texto en mayúsculas pequeñas (uppercase), fuente Monoespaciada o Sans-Serif pequeña (10-11px). Borde completamente redondeado.
        - *Referencia:* Estilo de "System Status" o "Loading".

### Footer (Pie de Página)

- **Alineación:**
    - Alinear ópticamente el logotipo del footer con el margen izquierdo del contenedor de contenido superior ("Grid de Soluciones"). No dejarlo flotando en un margen diferente.
- **Interacción:**
    - Añadir estados `hover` claros a los enlaces (LinkedIn, GitHub, Contact). Subrayado fino o cambio de opacidad al pasar el mouse.

---

## 3. Checklist de Calidad Final (QA Visual)

1. ¿El sitio respira? (Los márgenes laterales deben ser generosos, mantén el "aire").
2. ¿Hay contraste intelectual? (¿Se nota la diferencia entre la voz "humana/serif" y la voz "técnica/sans"?).
3. ¿Se siente táctil? (¿El fondo tiene esa textura sutil o sigue pareciendo una pantalla por defecto?).
4. ¿Los botones son píldoras perfectas? (Border-radius completo, no esquinas semi-redondeadas).