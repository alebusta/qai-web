# SOP: Generación de Propuestas de Inteligencia Estratégica

Este workflow describe el proceso para generar propuestas comerciales de "clase mundial" en The QAI Company, enfocadas en servicios de Vigilancia Tecnológica, Análisis de Datos o Consultoría de IA.

## 1. Fase de Ingesta (Inputs)
Para iniciar una propuesta, el agente necesita:
- **Brief del Cliente**: Nombre, industria, marcas, desafíos actuales.
- **Insumos de Investigación**: Tendencias detectadas, notas de reuniones, documentos técnicos.
- **Referencia del Competidor**: Si existe, su propuesta para identificar puntos de ataque.
- **Identidad Visual**: Acceso al `BRAND_KIT_MINIMO_QAI.md`.

## 2. Fase de Análisis (Processing)
- **Crítica Ácida**: Comparar el modelo tradicional (Competidor/Statics) vs. el modelo QAI (Radar Vivo/Dynamics).
- **Identificación de "Ganchos" WAO**: Seleccionar 2-3 problemas específicos del cliente (ej. Ley REP en CIAL) y proponer una solución automatizada/inteligente.
- **Definición de Módulos**: Determinar qué nivel de servicio requiere el cliente (Essential, Growth, Strategic).

## 3. Fase de Generación (Outputs)

### A. Propuesta Digital (HTML Premium)
- **Template**: `Empresa/02_COMERCIAL/templates/proposal/proposal_base.html`
- **Contenido**: 
    - Resumen ejecutivo (30 seg).
    - El "Por qué ahora" (Riesgo de inacción).
    - Metodología HITL (Human-in-the-loop).
    - Inversión clara (MVP + Fee Mensual).

### B. Prototipo Visual (Mockup)
- Generar un archivo `dashboard_mockup.html` que permita al cliente visualizar el servicio. No debe ser funcional al 100%, pero sí "sentirse" real.

### C. Deck de Presentación (16:9)
- **Formato**: Markdown para previsualización o HTML con grilla de 12 columnas.
- **Estética**: Minimalista (Apple/McKinsey), 1 idea por slide, máximo 10 slides.

### D. Estética y Pulido Final
- **Slogan Institucional**: Incluir siempre el slogan de QAI bajo el logo para reforzar la identidad (ej: "Soluciones de impacto...").
- **Iconografía**: Utilizar iconos oficiales de **Material Design** para asegurar un look limpio y tecnológico.
- **Micro-animaciones**: En mockups, incluir efectos de hover y transiciones suaves para el "efecto WAO".

## 4. Fase de Exportación y Entrega
- **HTML Interactivo**: Link principal para revisión en vivo.
- **PDF Formal**: Generar mediante "Imprimir a PDF" desde el navegador (Chrome/Edge), asegurando que los estilos `@media print` estén optimizados (sin saltos de página huérfanos).

## 5. Fase de Organización (Memoria)
- Crear carpeta en `Empresa/02_COMERCIAL/clientes/[NOMBRE_CLIENTE]/propuesta_vt_[ID]`.
- Almacenar todos los borradores, insumos y versiones finales.
- Registrar el aprendizaje en la bitácora de QAI.

---
*Este SOP es un documento vivo y debe ser actualizado tras cada proceso de venta.*
