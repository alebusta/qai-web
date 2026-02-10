# ADR-006: Ubicación de Scripts de Setup en QaiCore

**Fecha**: 2025-12-27  
**Estado**: Aceptado  
**Contexto**: Después de implementar Google Drive API setup, scripts estaban en `/scripts/` (raíz corporativa)

---

## Problema

Los scripts de configuración inicial (`setup_gdrive.py`, `test_gdrive.py`) estaban ubicados en `/scripts/` en la raíz del repositorio corporativo, separados de la herramienta que configuran (`/QaiCore/tools/gdrive.py`).

**Problemas identificados**:
1. **Portabilidad**: Si alguien clona solo QaiCore, no puede hacer setup
2. **Migraciones**: Scripts separados de las herramientas que configuran
3. **Mantenimiento**: No está claro qué scripts son de QaiCore vs otros proyectos
4. **Replicación**: Dificulta onboarding de nuevos colaboradores

---

## Alternativas Consideradas

### Opción 1: Dejar en `/scripts/` (raíz)
**Pros**:
- Ya está ahí
- Visible inmediatamente

**Contras**:
- No viaja con QaiCore
- Mezcla scripts de diferentes proyectos
- No es autónomo

### Opción 2: Mover a `/QaiCore/scripts/`
**Pros**:
- Viaja con QaiCore
- Autónomo

**Contras**:
- Mezcla scripts de setup (one-time) con scripts de uso diario (potencialmente)

### Opción 3: Mover a `/QaiCore/scripts/setup/` ✅ **ELEGIDA**
**Pros**:
- Viaja con QaiCore ✅
- Autónomo ✅
- Separación clara entre "setup" (one-time) y "tools" (daily use) ✅
- Escalable (otros setups futuros: `setup/postgres_setup.py`, etc.) ✅

**Contras**:
- Cambia ubicación de scripts ya creados (una vez)

---

## Decisión

**Estructura elegida**:
```
/QaiCore/
  /tools/              ← Herramientas de uso diario
    gdrive.py
  /scripts/
    /setup/            ← Scripts de configuración inicial
      gdrive_initial_setup.py
      gdrive_test.py
      README.md
```

**Justificación**:
1. **Portabilidad**: Todo QaiCore puede clonarse independientemente
2. **Claridad**: Separación conceptual entre "tools" (runtime) y "setup" (bootstrap)
3. **Escalabilidad**: Cuando haya más integraciones (Postgres, Redis, etc.), habrá carpeta consistente
4. **Onboarding**: Nuevo colaborador sabe dónde buscar setup scripts

---

## Consecuencias

### Positivas
- ✅ QaiCore es un módulo autónomo
- ✅ Setup scripts documentados en un solo lugar
- ✅ Migraciones más fáciles (copiar `/QaiCore/` completo)
- ✅ Patrón replicable para futuras herramientas

### Negativas
- ⚠️ Cambio de ubicación (una vez) - documentado en walkthrough
- ⚠️ Paths en scripts deben ajustarse si usuario clona en ubicación diferente (ya manejado con paths absolutos en config)

### Neutras
- 📝 Walkthrough debe actualizarse con nueva ubicación
- 📝 Futuros scripts de setup seguirán este patrón

---

## Implementación

1. ✅ Crear `/QaiCore/scripts/setup/`
2. ✅ Mover `setup_gdrive.py` → `gdrive_initial_setup.py`
3. ✅ Mover `test_gdrive.py` → `gdrive_test.py`
4. ✅ Crear `README.md` en `/setup/` con instrucciones
5. ✅ Actualizar walkthrough con nueva ubicación
6. ✅ Crear este ADR

---

## Lecciones Aprendidas

1. **Pensar en portabilidad desde el día 1**: Scripts de setup deben vivir con las herramientas que configuran
2. **Separación conceptual**: Tools (runtime) vs Setup (bootstrap) vs Scripts (maintenance)
3. **README es crítico**: Scripts sin documentación son código muerto

---

**Revisiones**:
- 2025-12-27: Creado (Nzero + Alejandro)

**Referencias**:
- Walkthrough: Google Drive API Setup
- Código: `/QaiCore/tools/gdrive.py`
- Setup script: `/QaiCore/scripts/setup/gdrive_initial_setup.py`
