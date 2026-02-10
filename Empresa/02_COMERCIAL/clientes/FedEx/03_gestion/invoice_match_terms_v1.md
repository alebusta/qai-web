# Términos Técnicos: Piloto de Validación - Servicio Invoice-Match (QAI)

**Proveedor**: The QAI Company SpA  
**Servicio**: Piloto de Validación de Procesamiento Inteligente y Match de Facturas (SaaS)

## 1. Alcance del Piloto
- Extracción automatizada de datos desde facturas (PDF/Imágenes) vía motores de IA.
- Validación contra Órdenes de Compra (PO) corporativas.
- Dashboard de auditoría y exportación de datos transaccionales.
- **Iteraciones Técnicas**: Se incluyen hasta **3 ciclos de ajuste fino** (fine-tuning) sobre los extractores para mejorar la precisión según formatos específicos del cliente detectados durante el periodo.

## 2. Vigencia y Límites del Piloto
- **Periodo de Uso**: Válido desde la fecha de activación hasta el **31 de Marzo de 2026**.
- **Límite Transaccional**: Incluye hasta **500 intentos de procesamiento** totales durante el periodo.
- **Usuarios Autorizados**: Hasta **5 cuentas nominales** (1 Administrador + 4 Operadores).
- **Continuidad**: Al finalizar el periodo o la cuota, se evaluará la transición a un contrato de servicio recurrente según necesidades de volumen.

## 3. Seguridad e Infraestructura Empresarial
- **Arquitectura AWS**: El servicio se aloja sobre infraestructura de **Amazon Web Services (AWS)** en centros de datos de alta disponibilidad, garantizando redundancia y continuidad operativa del 99.9%.
- **Capas de Seguridad**:
    - **Cifrado Industrial**: Datos protegidos mediante cifrado de punto a extremo (TLS 1.3) y en reposo mediante AES-256.
    - **Cumplimiento**: La infraestructura subyacente cumple con estándares globales (ISO 27001, SOC 2 y cumplimiento GDPR).
- **Privacidad IA**: El motor de procesamiento utiliza una arquitectura de "paso efímero". Los datos extraídos se procesan únicamente para la validación del documento y no se utilizan para el entrenamiento de modelos de lenguaje externos, garantizando la propiedad intelectual de FedEx.
- **Auditoría**: Acceso controlado mediante autenticación de doble factor (opcional) y registro de logs de actividad corporativa.

## 4. Inversión Piloto (Única)
- **Monto de Validación**: $990.000 CLP + IVA.
- **Facturación**: Pago único al inicio tras Orden de Compra por servicios de puesta en marcha y licenciamiento de piloto.
