# ADR-017: Persistence Guardrails and Amnesia Prevention

## Context
On February 12th, 2026, a critical synchronization failure occurred with the Lex agent. The agent reported multiple documentation updates (STATUS.md, INBOX.md, AGENT_ACTIVITY.md) as "completed" and "succeeded," but the changes were not actually persisted to the filesystem. This caused "Amnesia" in subsequent session segments, as new agents/models inherited an outdated state, leading to duplicate work and loss of trust in the "Institutional Memory."

## Decision
All QAI agents (Lex, Finn, Nzero) must adhere to the following **Persistence Guardrails**:

1.  **Read-After-Write (RAW) Verification**:
    -   After using a tool to edit a file (e.g., `replace_file_content`, `multi_replace_file_content`, `write_to_file`), the agent **MUST** perform a verification check using `view_file` or `grep_search` to ensure the content is physically present on disk.
    -   Confirming task completion to the user without this verification is considered a **Class A Failure**.

2.  **Explicit Atomic Commit**:
    -   Documentation updates must be performed and verified *before* reporting the primary task as completed.
    -   The "Closing Protocol" (STATUS, INBOX, ACTIVITY) must be treated as an atomic operation. Failure in one step requires re-verifying the whole set.

3.  **Landing Zone (temp_files) Protection**:
    -   No file in `/TorreDeControl/temp_files/` may be deleted without:
        -   A) Explicit user confirmation.
        -   B) Verification that the file is a redundant copy of a document already confirmed to be in its permanent location (Drive or Git).
    -   Agents must query the user if they encounter "Unknown" files in the landing zone before cleaning.

4.  **Buffer Awareness**:
    -   Agents must be aware that IDE buffers (Windsurf, Cursor) might show unsaved changes. Agents must force a "Save to Disk" or wait for file I/O completion signals before proceeding.

## Status
**Proposed & Implemented** - Feb 12th, 2026.

## Consequences
- **Positive**: Drastic reduction in "Agent Amnesia" and documentation drift. Increased reliability of the Torre de Control as a Single Source of Truth.
- **Negative**: Slight increase in tool-call overhead (extra `view_file` calls), but it's a necessary trade-off for data integrity.
