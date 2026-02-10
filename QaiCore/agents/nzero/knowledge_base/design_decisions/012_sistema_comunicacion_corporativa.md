# ADR-012: Sistema de Comunicación Corporativa y Coordinación de Agentes

**Estado**: Aceptado  
**Fecha**: 02 de Enero de 2026  
**Contexto**: QAI Company requiere un sistema estandarizado para enviar comunicaciones externas (emails) que mantenga la identidad visual y permita la autonomía de los agentes (Finn, Lex) bajo la supervisión de Nzero.

## Decisiones

### 1. Centralización de Identidad Visual
El logo oficial y las firmas se almacenan en `/Empresa/01_ESTRATEGIA/IDENTIDAD_VISUAL/`. Cualquier template de email debe referenciar estos recursos.

### 2. Roles y Facultades
- **Nzero**: Controlador de tráfico (Triage) y guardián de la memoria. Procesa la `landing zone`.
- **Finn**: Ejecutor de comunicaciones financieras y cobranza.
- **Lex**: Ejecutor de comunicaciones legales.

### 3. Protocolo de Envío ("Human-in-the-loop")
Todo email generado por un agente debe pasar por un proceso de **PREVIEW** antes de ser enviado. El agente debe generar un archivo `temp_files/email_preview.html` y solicitar aprobación al usuario.

### 4. Infraestructura Gmail API
Se utiliza la API de Gmail integrada con las credenciales de Google Workspace de la empresa, evitando dependencias de SMTP externas y aprovechando la seguridad de OAuth2.

## Consecuencias
- **Positivas**: Identidad de marca consistente, mayor autonomía de agentes, reducción de errores de envío mediante previsualización.
- **Negativas**: Requiere un paso manual de aprobación (deseado en esta etapa).
