@echo off
title Build Nexus Engine EXE
cd /d "%~dp0"

echo ============================================
echo  Nexus Engine — Windows EXE builder
echo ============================================
echo.

where python >nul 2>nul
if errorlevel 1 (
  echo [ERROR] Python not found. Install Python 3.9+ and check "Add to PATH".
  pause
  exit /b 1
)

echo [1/3] Installing PyInstaller + dependencies...
python -m pip install --upgrade pip
python -m pip install pyinstaller pygame numpy

echo.
echo [2/3] Building NexusEngine.exe ...
python -m PyInstaller --noconfirm --clean --windowed --onefile ^
  --name "NexusEngine" ^
  --collect-all pygame ^
  main.py

if errorlevel 1 (
  echo [ERROR] Build failed.
  pause
  exit /b 1
)

echo.
echo [3/3] Done.
echo EXE: %cd%\dist\NexusEngine.exe
echo SmartScreen may warn until the EXE is code-signed.
pause
