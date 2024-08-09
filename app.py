# app.py

from flask import Flask, request, jsonify
from core import recuperar_documentos, consultar_llm

app = Flask(__name__)

@app.route('/recuperar_documentos', methods=['POST'])
def recuperar_docs():
    """
    Recibe una pregunta y devuelve documentos relevantes
    """
    data = request.get_json()
    question = data.get('question')
    
    if not question:
        return jsonify({'error': 'No se proporcionó una pregunta'}), 400

    try:
        # Recupera del repositorio los documentos relevantes para responder la consulta
        documentos = recuperar_documentos(question)
        result= (str(documentos),200)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 

@app.route('/consultar', methods=['POST'])
def consultar():
    """
    Recibe una pregunta y devuelve documentos relevantes
    """
    data = request.get_json()
    question = data.get('question')
    
    if not question:
        return jsonify({'error': 'No se proporcionó una pregunta'}), 400

    try:
        # Recupera del repositorio los documentos relevantes para responder la consulta para armar el contexto:
        contexto= recuperar_documentos(question)
        respuesta = consultar_llm(contexto,question)
        result= (respuesta,200)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 
