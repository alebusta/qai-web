# SII Connector - Backlog & Mejoras

## 🚀 Prioridad Alta
- [ ] **Reforzar Detección de Éxito:** Actualizar selectores en `sii_auth.py` para incluir "Folio Declaración" y "Certificado Declaración".
- [ ] **Captura de Respaldo Forzosa:** Implementar un guardado de screenshot al fallar el timeout en la pantalla de envío.
- [ ] **Validación de Folio:** Agregar lógica para extraer el folio mediante expresiones regulares (Regex).

## 🛠️ Funcionalidades Futuras
- [ ] **Descarga de PDF Original:** Automatizar el clic en el botón de impresión/descarga y mover el archivo del directorio de descargas a `output/recibos/`.
- [ ] **Notificación post-envío:** Integrar un sistema para enviar el folio por correo o Slack una vez confirmado.
- [ ] **Soporte para múltiples RUTs:** Permitir el cambio de contexto de empresa sin reiniciar el navegador.

## 🐞 Bugs/Ajustes
- [ ] **Estabilidad del SII:** Manejar mejor los pop-ups de encuestas que a veces bloquean el botón de "Aceptar".
