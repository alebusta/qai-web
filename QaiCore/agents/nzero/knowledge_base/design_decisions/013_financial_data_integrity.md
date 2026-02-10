# ADR-013: Financial Data Integrity Protocol ("Zero-Loss Finance")

## Status
Proposed (Confirmed by Alejandro 10-Jan-2026)

## Context
The company's financial records were fragmented across multiple Google Spreadsheet versions, leading to confusion and risk of data loss or accidental deletion. A blank version was sitting in the official folder while the active version was in the root of the Shared Drive.

## Decision
Establish a mandatory protocol for financial data management to ensure a single Source of Truth (SSOT) and automated safety backups.

### 1. Unified Source of Truth
- **Official Location**: `QAI Company - Administración y Finanzas / QAI_Finanzas_2026`
- **Spreadsheet ID**: `1O7hENHvyLKcAOM9ynfvhibTX3pMynP2kFPMmGPxKNLw`
- All other versions must be archived or trashed.

### 2. Mandatory Local Backups
- Any agent (Finn, Nzero, etc.) performing a write operation on the Master Spreadsheet MUST run the `QaiCore/tools/backup_finance.py` tool immediately before and after the operation.
- Backups are stored in `TheQaiCo/Empresa/03_ADMINISTRACION_FINANZAS/backups/`.
- This ensures that if the GSheet is accidentally corrupted or deleted, we can restore from the latest local CSV.

### 3. Change Management
- Row deletions require explicit human approval.
- Data structure changes (new columns/sheets) must be recorded in this ADR or a specific financial manual.

## Consequences
- Increased operational safety.
- Slight overhead in execution time (running backup scripts).
- Local repository now acts as a cold storage for sensitive financial data.
