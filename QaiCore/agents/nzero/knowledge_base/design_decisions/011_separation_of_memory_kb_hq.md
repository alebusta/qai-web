# ADR-011: Separación de Memoria (KB vs HQ)

## Contexto
Se detectó una proliferación de documentación en el directorio corporativo (`/Empresa/`) generada por agentes (específicamente Finn), donde se mezclaban investigaciones teóricas, notas de procesamiento y activos estratégicos finales. Esto genera ruido cognitivo para el humano y desorden estructural.

## Decisión
Establecer una frontera rígida entre el "Cerebro del Agente" y los "Activos de la Compañía".

### 1. El Knowledge Base (KB)
**Ubicación**: `/QaiCore/agents/[agente]/knowledge_base/`
**Propósito**: Memoria interna del agente.
**Contenido**: 
- Investigaciones teóricas ("¿Qué es el IVA?").
- Borradores de procesamiento.
- Bitácoras de errores y aprendizajes técnicos.
- Notas que el humano NO tiene por qué leer para operar el negocio.

### 2. El HQ / Empresa
**Ubicación**: `/Empresa/`, `/TorreDeControl/`
**Propósito**: Activos operativos y estratégicos de Alejandro.
**Contenido**:
- Informes Ejecutivos Consolidados.
- Datos Operativos Reales.
- Documentación Legal y Tributaria Oficial.
- Estrategia que Alejandro consulta para tomar decisiones.

## Consecuencias
- **HQ Limpio**: Solo información de alto valor para el humano.
- **Agentes Inteligentes**: Poseen conocimiento profundo sin saturar el sistema.
- **Sincronización**: Al terminar una tarea, el agente debe preguntarse: "¿Esto es una nota para mí (KB) o un entregable para Alejandro (HQ)?".
