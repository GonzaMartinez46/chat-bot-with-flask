from flask import Flask, request, jsonify
from utils import *
app = Flask(__name__)


@app.route("/prompt",methods = ['POST'])
def hello_gonza():
    try:
        # Intentar obtener los datos JSON de la solicitud
        data = request.json

        # Verificar que los datos existan y que contengan la clave 'prompt'
        if not data or 'prompt' not in data:
            return jsonify({"error": "El campo 'prompt' es requerido."}), 400

        # Obtener el valor de 'prompt'
        prompt = data.get('prompt')
        response = request_chatBot(prompt)
        content = response.choices[0].message.content

        # Responder con el contenido formateado
        return f"<p>{content}</p>"
    
    except Exception as e:
        # Manejar cualquier otra excepción
        return jsonify({"error": "Ocurrió un error inesperado.", "message": str(e)}), 500

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"