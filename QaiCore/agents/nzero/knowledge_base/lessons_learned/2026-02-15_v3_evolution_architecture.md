# Lecciones Aprendidas: Evolución Arquitectural Web V3

**Fecha**: 15 de Febrero, 2026  
**Proyecto**: Web Corporativa V3  
**Agente**: Nzero (Arquitecto)

## 1. Contexto
Durante el desarrollo de la tercera iteración de la web de The QAI Company, se buscó romper con el diseño "genérico" de las versiones anteriores para adoptar una postura de **honestidad técnica radical** y el concepto de **"La Bisagra"**.

## 2. Aprendizajes Clave

### A. Modularización de la Fricción (Modales vs. Listas)
En la V1 y V2, los casos de uso intentaban mostrar toda la información en la tarjeta. Esto generaba ruido visual.
- **Lección**: Las tarjetas deben ser una "promesa de valor" (Título + Subtítulo). El detalle técnico (Fricción, Solución, Resultado) debe vivir en un espacio dedicado (Modal). 
- **Resultado**: Mejora la "escaneabilidad" de la página y permite que el usuario profundice solo en lo que le interesa.

### B. El Poder de los Símbolos Binarios (✓ vs ✗)
En el Manifiesto, el texto plano era difícil de digerir. Al usar una lista de "Lo que Sí hacemos" vs "Lo que No hacemos" con simbología clara:
- **Lección**: La claridad visual refuerza la honestidad. Ver un símbolo de rechazo (`✗`) junto a términos de "hype" (`Revolucionar`, `Sola`, `Disrupción`) genera confianza inmediata en un público técnico o ejecutivo cansado de promesas vacías.

### C. La Identidad de "La Bisagra"
Se identificó que QAI no es una consultora ni una startup funcional. 
- **Lección**: El valor real es la capacidad de conectar el **Dominio Experto** (quien conoce el dolor) con la **Tecnología Apropiada**. Esta identidad debe ser el eje central de toda la narrativa web.

### D. Cierre vs. Invasión (Footers Estratégicos)
Un CTA gigante puede sentirse como un anuncio.
- **Lección**: Un cierre sutil, con tipografía refinada y una invitación honesta a "evaluar el ROI", es más efectivo para convertir clientes corporativos que un botón de "Contrata ya" brillante.

## 3. Próximos Pasos Arquitecturales
- Mantener la línea monocromática para conservar el aire de "Laboratorio".
- Asegurar que cualquier nueva sección siga el protocolo de "Zero Verborrea".

---
**Nzero** | *Architect of Record*
