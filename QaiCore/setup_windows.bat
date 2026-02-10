@echo off
setlocal

echo [QAI] Setup Windows - QaiCore
cd /d "%~dp0"

REM 1) Crear venv si no existe
if not exist ".venv\Scripts\python.exe" (
  echo [QAI] Creando entorno virtual en .venv ...
  python -m venv .venv
)

REM 2) Instalar dependencias
echo [QAI] Instalando dependencias (requirements.txt) ...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt

REM 3) Instalar Chromium para Playwright (PDFs de alta calidad)
echo [QAI] Instalando Chromium (Playwright) ...
".venv\Scripts\python.exe" -m playwright install chromium

echo.
echo [QAI] Setup completado.
echo - Para ejecutar extraccion:    .\qrun.bat .\tools\document_processor.py "ruta"
echo - Para PDF propuestas:        .\qrun.bat -m tools.proposal_pdf --help
echo.
endlocal
