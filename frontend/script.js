document.getElementById("difficulty").addEventListener("input", function () {
  document.getElementById("difficultyLabel").innerText = this.value;
});

document.getElementById("examForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const imageFile = document.getElementById("examImage").files[0];
  const difficulty = document.getElementById("difficulty").value;
  const output = document.getElementById("output");

  if (!imageFile) {
    alert("Debe subir una imagen de examen.");
    return;
  }

  const formData = new FormData();
  formData.append("file", imageFile);
  formData.append("nivel", difficulty);

  output.innerText = "Procesando examen...";

  try {
    const response = await fetch("http://localhost:8000/calificar/", {
      method: "POST",
      body: formData
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Error ${response.status}: ${errorText}`);
    }

    const data = await response.json();

    if (data.error) {
      output.innerText = "❌ Error del servidor: " + data.error;
    } else {
      output.innerText =
        "📝 Texto extraído:\n" +
        (data.informe?.preguntas?.map(p => `Pregunta ${p.numero}: ${p.respuesta}`).join("\n") || "") +
        "\n\n🤖 Evaluación:\n" +
        "Puntaje Total: " + data.informe.puntaje_total +
        "\nConclusión: " + data.informe.conclusion?.fortalezas;
    }
  } catch (err) {
    output.innerText = "❌ Error al procesar: " + err.message;
    console.error(err);
  }
});