@echo off
cd /d "%~dp0"
echo Instalando dependencias (se precisar)...
python -m pip install pygame numpy -q
echo.
echo Iniciando Nexus Engine...
python main.py
if errorlevel 1 pause
