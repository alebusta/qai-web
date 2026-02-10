# ADR-008: Zona de Aterrizaje para Archivos Operativos (temp_files)

**Fecha**: 2025-12-28  
**Estado**: Aceptado  
**Contexto**: El Founder necesitaba un lugar centralizado para entregar archivos a los agentes sin ensuciar la raíz del proyecto ni las carpetas estratégicas.

---

## Problema

Anteriormente, los archivos para procesar (transcripciones, borradores, documentos temporales) se subían al root o se buscaban en carpetas arbitrarias, lo que generaba:
1.  **Desorden**: Acumulación de archivos temporales en el workspace.
2.  **Fricción**: Los agentes no sabían dónde buscar el "trabajo nuevo".
3.  **Riesgo**: Archivos sensibles podían quedar olvidados en carpetas de código.

---

## Decisión

Implementar la carpeta `/TorreDeControl/temp_files/` como la **Landing Zone** (Zona de Aterrizaje) oficial.

### Reglas Operativas:
1.  **InBox de Archivos**: El Founder deposita archivos aquí para que el agente los procese.
2.  **Zero InBox (Obligatorio)**: Un agente solo puede considerar una tarea "completada" si ha procesado los archivos de `temp_files` y los ha movido a su destino final o eliminado.
3.  **Ubicación**: Se sitúa en la Torre de Control por ser el centro de operaciones diarias, separándola de los activos estratégicos (`/Empresa/`) y del código (`/QaiLabs/`).

---

## Consecuencias

### Positivas
- ✅ **Orden**: Workspace limpio de archivos temporales.
- ✅ **Eficiencia**: Los agentes revisan sistemáticamente esta carpeta al iniciar sesión.
- ✅ **Trazabilidad**: Es claro qué está pendiente de procesar.

### Trade-offs
- ⚠️ Requiere disciplina del agente para limpiar la carpeta tras el procesamiento.

---

**Autor**: Nzero  
**Aprobado por**: Alejandro (Founder)  
**Relacionado con**: ADR-001 (Torre de Control)
