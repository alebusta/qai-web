# Protocolo de Organización de Carpetas de Clientes (QAI Standard)

Para asegurar la consistencia operativa y facilitar el trabajo de los agentes (Nzero, Finn, etc.), se establece el siguiente estándar para todas las carpetas dentro de `Empresa/02_COMERCIAL/clientes/`.

## 1. Estructura Híbrida (Local + Cloud)

Cada cliente debe existir simultáneamente en el repositorio local (`Empresa/02_COMERCIAL/clientes/`) y en Google Drive (`Clientes/`). Ambas estructuras deben ser espejos exactos.

## 2. Subdirectorios Obligatorios (Protocolo 01-02-03)

- `01_insumos/`: Material base, requerimientos, datos del cliente.
- `02_entregas/`: **SSOT de Productos**. Solo archivos finales enviados (PDFs certificados).
- `03_gestion/`: Bitácoras, costos, Hitos de Memoria, y coordinación.

## 3. Automatización y Mantenimiento

- **Creación de Clientes**: Se debe ejecutar `python QaiCore/scripts/standardize_clients.py` para crear la estructura automáticamente en Drive y asegurar el cumplimiento del protocolo.
- **Autenticación**: Las credenciales se gestionan centralmente via `python QaiCore/scripts/auth_unified.py`.
- **Mirroring**: Los agentes deben asegurar que cualquier archivo en `02_entregas` local sea subido inmediatamente a Drive para visibilidad del usuario.

## 4. Convención de Nombres

- Formato: `YYYY-MM-DD_TIPO_CLIENTE_vX.pdf` (ej: `2026-02-11_PROPUESTA_CIAL_v2.pdf`).


---
*Este protocolo es parte del ADN operativo de QAI y debe ser respetado por todos los agentes y colaboradores.*
