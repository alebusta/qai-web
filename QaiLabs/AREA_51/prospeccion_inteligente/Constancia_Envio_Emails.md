# Constancia de Envío de Emails para CirclePack 2026

**Fecha:** 13 de febrero de 2026

## Objetivo
Enviar emails personalizados a contactos de expositores interesados en participar en CirclePack Chile 2026, promocionando los servicios de stands sustentables de LITE de LatinARQ.

## Proceso Realizado

### 1. Análisis y Preparación de Datos
- **Archivo de Datos:** `expositores_circlepack_V2_FINAL.xlsx`
- **Criterios de Filtrado:**
  - Activo = 'Sí'
  - Nombre no vacío
  - Correo != 'No encontrado'
  - Exclusión de contactos ya enviados previamente (7 contactos)
- **Procesamiento:** Capitalización de nombres (primera letra mayúscula)
- **Resultado:** 23 contactos filtrados para envío

### 2. Diseño del Template de Email
- **Asunto:** "¿Y si tu stand también fuera circular en Circlepack 2026?"
- **Contenido:** Basado en `Texto_mail.md`, con saludo personalizado "Hola {Nombre},"
- **Formato:** HTML con logo embebido (CID attachment)
- **Firma:** Iliana Alzurutt, Encargada de Desarrollo de Negocios - LITE de LatinARQ

### 3. Desarrollo del Script
- **Archivo:** `email_sender.py`
- **Librerías:** pandas, smtplib, email, imaplib, datetime
- **Funcionalidades:**
  - Lectura y filtrado de Excel
  - Envío vía SMTP (mail.latinarq.com, puerto 587, TLS)
  - Embebido de logo vía CID
  - Guardado de emails enviados en carpeta Sent vía IMAP
  - Actualización de Excel con columna 'Fecha_envio'
- **Archivos Adicionales:**
  - `README.md`: Instrucciones de uso
  - `requirements.txt`: Dependencias (pandas)

### 4. Pruebas
- Envío de emails de prueba a direcciones conocidas (iliana.alzurutt@latinarq.com, albus@hotmail.com, afbs77@gmail.com)
- Verificación de formato en Outlook y Gmail
- Ajustes: Corrección de tamaño de logo, embebido CID, eliminación de título del cuerpo

### 5. Envío Completo
- Comando Ejecutado: `python email_sender.py`
- Emails Enviados: 23
- Confirmación: Emails guardados en Sent folder, Excel actualizado con fecha de envío

## Resultados
- **Total Emails Enviados:** 23
- **Destinatarios:** Lista de nombres y correos en el script de ejecución
- **Estado:** Emails enviados exitosamente, guardados en Sent folder, y Excel actualizado
- **Archivos Modificados:** `expositores_circlepack_V2_FINAL.xlsx` (agregada columna 'Fecha_envio')

## Notas Técnicas
- Configuración SMTP: mail.latinarq.com:587 (TLS)
- IMAP para Sent folder: mail.latinarq.com:993 (SSL)
- Logo embebido para compatibilidad con Gmail y Outlook
- Manejo de errores en envío y guardado

## Responsable
Iliana Alzurutt - Encargada de Desarrollo de Negocios, LITE de LatinARQ

Esta constancia certifica la ejecución exitosa del proceso de envío de emails según los criterios establecidos.
