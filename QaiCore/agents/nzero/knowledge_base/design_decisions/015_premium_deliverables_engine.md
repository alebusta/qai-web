# ADR 015: Engine de Generación de Entregables Estratégicos Premium

## Status
Accepted

## Context
QAI delivers high-impact commercial proposals and executive decks. Previous attempts using standard browser printing or simple PDF tools resulted in:
1.  **Visual Degeneration**: White borders in 16:9 decks, loss of background colors.
2.  **Asset Loss**: Missing Material Icons or logos due to race conditions during rendering.
3.  **Continuity Failure**: Key rendering scripts and master templates were accidentally deleted during "clean-up" sessions.

## Decision
Implement a formalized "High Fidelity Rendering Engine" as part of the QaiCore infrastructure.

### 1. Technical Standards
- **Standard Tool**: `QaiCore/tools/generate_all_pdfs.py` using Playwright.
- **Rendering Trigger**: The script MUST wait for `document.fonts.ready` before issuing the PDF command.
- **Asset Serving**: Use an internal HTTP server (Port 8585) to serve absolute URLs, avoiding `file://` protocol limitations.
- **Strict Aspect Ratios**: 16:9 (1280x720px) for Decks and A4 (210x297mm) for Proposals.

### 2. Design Aesthetic: "QAI Executive Horizon"
- **Color Palette**: 
  - Deep Blue: `#0F172A` (Cover/Accents)
  - QAI Blue: `#0284C7` (Content Titles/Highlights)
  - Teal: `#14B8A6` (Accents)
- **Hierarchy**: Hybrid layout (Dark cinematic cover + Clean white content slides).

### 3. Protection Policies
- **Core Tools**: Tools in `QaiCore/tools` are considered "Infrastructure" and must not be deleted by agents during project cleanup.
- **Master Templates**: Final designs must be saved as `MASTER_DESIGN.html` in the project folder to signal "immutable state" to cleanup agents.

## Consequences
- **Positive**: Consistent, agency-grade deliverables. Repeatable process. Safe cleanup.
- **Negative**: Adds a dependency on Playwright and Python/Node environment. Requires a background server process during generation.
