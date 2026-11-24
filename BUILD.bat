@echo off
cd /d "%~dp0"
echo.
echo   NEXUS ENGINE BUILD
echo   Made in Nexus
echo.
python -m pip install pyinstaller pygame numpy -q
python build.py %*
echo.
pause
