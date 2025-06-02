import subprocess
import json
import re

def analyze_response(respuesta_estudiante, dificultad=5):
    model = "deepseek-r1"

    prompt = f"""
Actúa como un profesor experto en calificación de exámenes.

Tu tarea es calificar las respuestas del estudiante y devolver **solamente un objeto JSON** con la siguiente estructura (sin explicaciones ni texto adicional fuera del JSON):

{{
  "examen_id": "Examen_automático",
  "puntaje_total": 20,
  "preguntas": [
    {{
      "numero": 1,
      "respuesta": "Texto de la respuesta",
      "puntaje": 2,
      "justificacion": "Explicación clara de si está correcta o incorrecta"
    }}
  ],
  "conclusion": {{
    "fortalezas": "Texto",
    "debilidades": "Texto",
    "sugerencias": "Texto"
  }}
}}

Nivel de exigencia: {dificultad}/10

Respuestas del estudiante:
\"\"\"
{respuesta_estudiante}
\"\"\"

Tu respuesta debe contener **solo el JSON**.
"""

    try:
        result = subprocess.run(
            ['ollama', 'run', model, prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8'
        )

        print(" Salida del modelo LLM:")
        print("===")
        print(result.stdout)
        print("===")

        # Intentar extraer el primer bloque JSON de la respuesta
        matches = re.findall(r'\{[\s\S]*\}', result.stdout)

        if not matches:
            return {"error": "No se encontró ningún bloque JSON en la salida del modelo.", "respuesta_llm": result.stdout}

        return json.loads(matches[0])

    except Exception as e:
        return {
            "error": f"Error al parsear JSON: {str(e)}",
            "respuesta_llm": result.stdout if result else '---'
        }