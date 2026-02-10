@echo off
set "VENV_PYTHON=%~dp0.venv\Scripts\python.exe"

REM Ensure QaiCore modules are importable from any CWD (e.g. repo root)
set "PYTHONPATH=%~dp0;%PYTHONPATH%"

if not exist "%VENV_PYTHON%" (
    echo [ERROR] No se encuentra el entorno virtual en: %VENV_PYTHON%
    echo Asegurate de haber ejecutado la instalacion de QaiCore.
    exit /b 1
)

"%VENV_PYTHON%" %*
