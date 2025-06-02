from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from models.ocr_icr import extract_text_from_image
from models.llm_analysis import analyze_response
from utils.report_generator import create_report

import datetime
import os
import re

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"mensaje": "Servidor corriendo correctamente"}


#  Función para detectar el nombre del estudiante desde el texto OCR
def detectar_nombre(texto):
    patrones = [
        r"(?i)nombre\s*:\s*(.+)",
        r"(?i)estudiante\s*:\s*(.+)",
    ]
    for patron in patrones:
        match = re.search(patron, texto)
        if match:
            return match.group(1).strip()
    return None


@app.post("/calificar/")
async def calificar(file: UploadFile, nivel: int = Form(...)):
    print(f"📥 Recibido archivo con nivel {nivel}")

    contents = await file.read()
    with open("temp.jpg", "wb") as f:
        f.write(contents)

    print(" Imagen guardada como temp.jpg")

    texto = extract_text_from_image("temp.jpg")
    print(" Texto extraído:", texto[:100] if texto else "Vacío")

    if not texto.strip():
        return {"error": "No se pudo extraer texto de la imagen. Verifica la calidad."}

    resultado_llm = analyze_response(texto, nivel)

    if "error" in resultado_llm:
        return {"error": resultado_llm["error"]}

    # 🔍 Buscar nombre del estudiante en el texto extraído
    nombre = detectar_nombre(texto)
    id_generado = "Examen_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    if nombre:
        resultado_llm["examen_id"] = f"{nombre.replace(' ', '_')}_{id_generado}"
        resultado_llm["nombre_estudiante"] = nombre
    else:
        resultado_llm["examen_id"] = id_generado
        resultado_llm["nombre_estudiante"] = "No identificado"

    #  Crear el reporte
    nombre_archivo = f"{resultado_llm['examen_id']}.docx"
    archivo_path = create_report(resultado_llm, output_path=nombre_archivo)

    return {
        "informe": resultado_llm,
        "archivo": archivo_path
    }