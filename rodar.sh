#!/bin/bash
cd "$(dirname "$0")"
echo "Instalando dependencias (se precisar)..."
python3 -m pip install pygame numpy -q
echo
echo "Iniciando Nexus Engine..."
python3 main.py
