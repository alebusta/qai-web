# ADR-020: Estrategia de Repositorio Híbrido (README-only) para QaiLabs

**Fecha**: 2026-02-19  
**Estado**: Aceptado  
**Contexto**: The QAI Company gestiona múltiples proyectos simultáneamente. Algunos proyectos en `QaiLabs` escalan hasta tener sus propios repositorios independientes (ej: `invoiceMatch`, `qai-web`). Mantener el código fuente de estos proyectos dentro del repositorio principal (`TheQaiCo`) genera ruido, conflictos de dependencias y dificulta la colaboración externa.

## Problema
El repositorio principal se estaba volviendo pesado y desordenado al incluir código fuente de prototipos que ya tienen su propia vida en repositorios independientes bajo las cuentas de `alebusta` o `qai-labs`.

## Decisión: Repositorio "Shell" con Documentación
Se decide transformar la carpeta `QaiLabs` en un índice documental en lugar de un contenedor de código:

1.  **Exclusión de Código**: Se excluye todo el código fuente, binarios y artefactos de construcción de proyectos en `QaiLabs` de la subida al repositorio `origin` (GitHub).
2.  **README Persistence**: Se permite explícitamente la presencia de archivos `README.md` de todos los niveles en `QaiLabs`. Esto permite que el repositorio principal funcione como un catálogo o índice de todos los experimentos.
3.  **Gitlinks / Submódulos**: Para proyectos críticos, se utilizarán punteros de Git (gitlinks) si es necesario, pero la norma general es ignorar el contenido via `.gitignore`.
4.  **Configuración de `.gitignore`**:
    ```gitignore
    QaiLabs/**/*
    !QaiLabs/**/
    !QaiLabs/**/README.md
    !QaiLabs/EXPERIMENTAL_ZONE_NOTICE.md
    !QaiLabs/README.md
    ```

## Consecuencias
- **Positivas**: 
    - Repositorio principal liviano y enfocado en la "Torre de Control".
    - Estructura clara de catálogo: en GitHub se ve qué proyectos existen y sus manuales, pero el código vive donde pertenece.
    - Evita fugas accidentales de código experimental hacia el repo corporativo.
- **Negativas**: 
    - Requiere un paso adicional (`git add --force`) si un agente desea subir un archivo específico que no sea un README a un experimento (aunque esto debe evitarse).
    - Los desarrolladores deben clonar repositorios adicionales para trabajar en el código fuente de los prototipos.

---
**Autor**: Nzero  
**Aprobado por**: Alejandro (Founder)  
**Relacionado con**: ADR-019 (Primacía Corporativa Labs)
