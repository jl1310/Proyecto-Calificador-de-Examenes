@echo off
title Servidor Frontend UMG
echo Iniciando servidor web local...

REM Cambia la ruta a tu carpeta frontend
cd /d "C:\Users\yorch\OneDrive\Documentos\UMG\INTELIGENCIA ARTIFICIAL\Proyecto Final\frontend"

REM Cambia el puerto si deseas (8001 por defecto)
start "" http://localhost:8001/index.html

REM Iniciar servidor HTTP de Python
python -m http.server 8001

pause
