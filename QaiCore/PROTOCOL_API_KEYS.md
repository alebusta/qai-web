# Protocolo: Uso de API Keys y Servicios Externos

## 🔐 Regla de Oro: Human-in-the-Loop

**CRÍTICO**: Cualquier uso de API keys o servicios externos que consuman créditos/dinero **DEBE** ser aprobado explícitamente por Alejandro, excepto para los casos pre-autorizados listados abajo.

---

## ✅ Usos Pre-Autorizados (No requieren aprobación)

### 1. Gemini API - Backoffice
**API Key**: `[REDACTED — almacenada en variable de entorno GEMINI_API_KEY]`  
**Nombre**: backoffice  
**Propósito**: Asuntos de gestión de QAI  

**Casos de uso autorizados**:
- ✅ OCR de documentos financieros (comprobantes, facturas)
- ✅ Extracción de texto de PDFs escaneados
- ✅ Procesamiento de documentos administrativos
- ✅ Fallback cuando Tesseract falla

**Restricciones**:
- Solo usar como **fallback** (después de Tesseract)
- No usar para generación de contenido creativo
- No usar para análisis que no sean documentos

---

## ❌ Usos que SIEMPRE Requieren Aprobación

### Servicios que consumen créditos/dinero:
- ❌ Gemini API para casos NO listados arriba
- ❌ OpenAI API
- ❌ Anthropic API
- ❌ Cualquier servicio de pago (Stripe, etc.)
- ❌ Servicios de email masivo
- ❌ Servicios de almacenamiento con costo

### Protocolo cuando se necesita usar:
1. **Preguntar al usuario**: "Necesito usar [servicio] para [propósito]. Esto consumirá créditos. ¿Apruebas?"
2. **Esperar confirmación explícita**: "OK", "Sí", "Aprobado"
3. **Documentar uso**: Registrar en `AGENT_ACTIVITY.md`

---

## 📊 Registro de Uso de API Keys

### Gemini API - Backoffice
**Configurada**: 07-Ene-2026  
**Ubicación**: Variable de entorno `GEMINI_API_KEY`  
**Proyecto**: QAI (Google AI Studio)  
**Crédito disponible**: $300 USD (expira ~29-Mar-2026)

**Uso histórico**:
- 07-Ene-2026: Configuración inicial como fallback OCR

---

## 🛡️ Seguridad

### Almacenamiento de API Keys:
- ✅ Variables de entorno (User-level)
- ❌ Nunca en código fuente
- ❌ Nunca en archivos de configuración versionados
- ❌ Nunca en logs

### Rotación:
- Revisar y rotar API keys cada 3 meses
- Revocar inmediatamente si se expone

---

## 📝 Para Agentes (Finn, Lex, etc.)

**Antes de usar cualquier API key**:
1. Verificar si el uso está en la lista pre-autorizada
2. Si NO está pre-autorizado → Preguntar a Alejandro
3. Si SÍ está pre-autorizado → Usar y documentar en `AGENT_ACTIVITY.md`

**Ejemplo de pregunta**:
```
⚠️ Necesito usar Gemini API para [propósito específico].
Esto consumirá créditos del proyecto QAI.
¿Apruebas el uso?
```

---

**Última actualización**: 07-Ene-2026  
**Responsable**: Nzero
