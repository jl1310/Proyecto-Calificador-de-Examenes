# 📚 Sistema de Calificación Autónoma de Exámenes

Este proyecto implementa un sistema inteligente capaz de:

- 🖼️ Extraer texto desde imágenes escaneadas de exámenes
- 🧠 Evaluar respuestas con un modelo LLM local (`deepseek-r1` en Ollama)
- 📄 Generar informes personalizados en formato Word (`.docx`)
- 🌐 Presentar una interfaz web simple para docentes o alumnos

---

## 🎓 Proyecto Final – Inteligencia Artificial  
**Universidad Mariano Gálvez de Guatemala**  
Autor: [Tu Nombre]  
Carrera: Ingeniería en Sistemas

---

## ⚙️ Tecnologías utilizadas

- **Python 3.11+**
- **FastAPI** – Backend REST
- **Ollama** – Motor de LLM local con `deepseek-r1`
- **pytesseract** + **OpenCV** – OCR para leer imágenes
- **python-docx** – Generación de reportes `.docx`
- **HTML + CSS + JS** – Interfaz web simple
- **VS Code** – Editor de desarrollo
- **Git + GitHub** – Control de versiones

---

## 📁 Estructura del proyecto

proyecto-calificador/
├── main.py # Servidor FastAPI
├── iniciar_frontend.bat # Script para levantar frontend
├── .gitignore
├── README.md
├── models/ # OCR + análisis con LLM
│ ├── ocr_icr.py
│ └── llm_analysis.py
├── utils/ # Generador de reportes
│ └── report_generator.py
├── frontend/ # Interfaz web
│ ├── index.html
│ ├── styles.css
│ ├── script.js
│ └── LogoUMG1.png
├── assets/ # Recursos adicionales
│ └── LogoUMG1.png
