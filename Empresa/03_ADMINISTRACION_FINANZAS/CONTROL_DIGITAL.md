# Control Digital Financiero: The QAI Company

> **Visión Nzero**: Este documento centraliza los accesos, IDs y estructuras lógicas del "Cerebro Financiero" de QAI en la nube.

---

## 1. Google Sheets: El Sistema Operativo
**Spreadsheet Principal (2026)**: `1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw`  
**URL**: [QAI_Finanzas_2026](https://docs.google.com/spreadsheets/d/1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw/edit)

### Pestañas y Funciones
- `Registro_Diario`: Log central de ingresos/gastos.
- `Runway`: Proyección de flujo de caja.
- `PyL`: Estado de resultados.
- `Prestamos_Socio`: Tracking de capital inyectado por Alejandro.
- `Control_Facturacion`: Seguimiento de OCs y facturas emitidas.

---

## 2. Google Drive: El Archivo Central
La documentación financiera se organiza por **Dominio y Tiempo** en la carpeta corporativa.

### Carpeta Madre: `03_ADMINISTRACION_FINANZAS`
- `contabilidad/`: Facturas, Boletas, Cartolas bancarias.
- `tributario/`: Declaraciones F29 (mensual) y F22 (anual).
- `legal/`: Escrituras, RUT, Contratos de servicios (Docs Legales).
- `reportes/`: Informes de gestión mensuales.

---

## 3. Cuentas y Credenciales
*Nota: Solo se listan datos de identificación. Las claves nunca deben estar en texto plano.*

- **Banco Chile (Empresa)**: Cuenta Vista `00-001-24253-56`.
- **SII**: Acceso con Certificado Digital a nombre de Alejandro Bustamante.
- **Supabase**: Proyectos `Invoice-Match` y `Gestion-Zen`.
- **Google Cloud Console**: Tracking de APIs Gemini/Groq.

---

## 4. Mantenimiento y Backup
- **Backup Mensual**: El primer día de cada mes, Finn descarga una copia del Sheet en formato CSV/Excel a la carpeta `contabilidad/backups/`.
- **Reconciliación**: Mensualmente se cruza la cartola del Banco Chile contra el `Registro_Diario`.

---
*Para normativa y procedimientos, ver [MANUAL_TRIBUTARIO_Y_OPERATIVO.md](file:///c:/Users/abustamante/TheQaiCo/Empresa/03_ADMINISTRACION_FINANZAS/MANUAL_TRIBUTARIO_Y_OPERATIVO.md)*
