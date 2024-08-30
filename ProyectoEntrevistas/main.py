from flask import Flask, jsonify,request, render_template
import google.generativeai as genai

app= Flask(__name__)



GOOGLE_API_KEY=''
genai.configure(api_key = GOOGLE_API_KEY )
model = genai.GenerativeModel('gemini-pro')




@app.route('/')
def home():
    return render_template('index.html')


@app.route("/chat")
def enviarChat():
    # Obtener la pregunta completa enviada desde el front-end
    pregunta = request.args.get('pregunta', '')  
    
    if not pregunta:
        return jsonify({'respuesta': 'No se recibió ninguna pregunta.'}), 400

    # Generar contenido utilizando el modelo de IA con la pregunta proporcionada
    response = model.generate_content(pregunta)
    respuesta_ia = response.text if response.text else "Hubo un error en la generación de la respuesta."

    return jsonify({'respuesta': respuesta_ia})

if __name__ == '__main__':
    app.run()