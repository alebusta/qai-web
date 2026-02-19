# CHANGELOG - Bitácora de Decisiones Importantes

> Registro histórico de hitos, cambios de rumbo y decisiones estratégicas.

---

## 2026

### Febrero

#### [19-Feb-2026] - Búsqueda Híbrida & Saneamiento QaiLabs (Nzero)
**Tipo**: Arquitectura / Infraestructura / IA

**Decisión/Acción**:
- [ARQUITECTURA] **ADR-021 (Búsqueda Híbrida QMD)**: Integrado motor de búsqueda vectorial local para mejorar la memoria institucional. Nota: Sujeto a reversión si el performance no es óptimo.
- [ARQUITECTURA] **ADR-020 (Repositorio Híbrido)**: Finalizado saneamiento de `QaiLabs` en `origin`.
- [INFRA] **Saneamiento de .gitignore**: Configurado para ignorar sistemáticamente todo el contenido de `QaiLabs` exceptuando archivos `README.md` y el aviso de zona experimental.
- [REPOS] **Limpieza de Index**: Ejecutado `git rm --cached` para eliminar del seguimiento todos los archivos de prototipos (sii_connector, qai-web, etc.), manteniendo gitlinks para repositorios con vida propia.
- [SYNC] Sincronización completa con `origin/master`: el repositorio en la nube ahora es liviano, enfocado en el núcleo de la empresa y sirve como índice de experimentos.

**Impacto**: El HQ es más eficiente y seguro. Los agentes y humanos pueden ver la documentación de los experimentos en GitHub, pero el código fuente está correctamente segregado en sus respectivos silos.

#### [19-Feb-2026] - Hardening de Infraestructura & Primacía Corporativa (Nzero)
**Tipo**: Infraestructura / Protocolo / Arquitectura

**Contexto**: Se detectaron riesgos de duplicación de correos tras reinicios de sesión y desorden en la jerarquía de protocolos debido a la coexistencia de experimentos y normas corporativas.

**Decisión/Acción**:
- [ARQUITECTURA] **ADR-019 (Primacía Corporativa)**: Establecida la jerarquía de normas. Los archivos en `QaiCore` mandan sobre cualquier configuración encontrada en `QaiLabs`.
- [INFRA] **Gmail Idempotency**: Implementado sistema de registro de correos enviados (`sent_registry.json`) para evitar duplicidad de comunicaciones tras reinicios de sesión.
- [INFRA] **Experimental Zone Notice**: Desplegado `EXPERIMENTAL_ZONE_NOTICE.md` en áreas de prototipos para advertir a futuros agentes de no tomar scripts de prueba como normas corporativas.
- [PROCEDIMIENTO] **Cierre sesión: Tributario + procedimiento (Finn)**: Certificados F29 son tributarios (no legales). Dic ya estaba en Tributario/2025/12. Duplicado en Certificados enviado a papelera. Ene movido a Tributario/2026/01-enero y renombrado a 2026-01_F29_Declaracion_IVA.pdf. Procedimiento creado (nombre YYYY-MM_F29_Declaracion_IVA.pdf, ruta Tributario). DISENO y README tributario actualizados.

**Impacto**: Sistema blindado contra reinicios y mayor claridad para la colaboración entre agentes especializados.
