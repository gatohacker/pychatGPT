import openai
from flask import Flask, render_template, request
import re
import csv
import datetime
import os
import configparser

# Inicializa la aplicación Flask
app = Flask(__name__)

# Inicializa el estado de la conversación
conversacion_estado = {'mensajes': []}

# Ruta al directorio de logs
carpeta_logs = 'logs'

# Función para convertir comillas invertidas en etiquetas <code>
def convertir_code(mensaje):
    # Encuentra todos los bloques de código entre comillas invertidas
    bloques_code = re.findall(r'```(.*?)```', mensaje, re.DOTALL)
    for bloque in bloques_code:
        # Reemplaza las comillas invertidas con etiquetas <code>
        mensaje = mensaje.replace(f'```{bloque}```', f'<code>{bloque}</code>')
    return mensaje

# Función para escribir en el archivo CSV
def escribir_en_csv(mensaje, rol, nombre_archivo):
    with open(nombre_archivo, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rol, mensaje])

# Lee la configuración desde el archivo config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Configura tu API Key de OpenAI y el motor
openai.api_key = config.get('openai', 'api_key')
engine = config.get('openai', 'engine')

# Configuración adicional para la API de OpenAI desde config.ini:
configuracion_openai = {
    "max_tokens": config.getint('configuracion_openai', 'max_tokens'),
    "temperature": config.getfloat('configuracion_openai', 'temperature'),
    "frequency_penalty": config.getfloat('configuracion_openai', 'frequency_penalty'),
}

# Ruta para mostrar el formulario
@app.route('/')
def inicio():
    return render_template('index.html')

# Ruta para procesar la solicitud del formulario
@app.route('/chat', methods=['POST'])
def chat():
    global conversacion_estado

    # Obtiene la entrada del formulario
    entrada_usuario = request.form['entrada_usuario']

    # Si es el inicio de una nueva sesión, crear un nuevo archivo CSV
    if not conversacion_estado['mensajes']:
        nombre_archivo = os.path.join(carpeta_logs, f'conver_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv')
        conversacion_estado['nombre_archivo'] = nombre_archivo

    # Añade la pregunta del usuario al contexto de la conversación
    conversacion_estado['mensajes'].append({'role': 'user', 'content': entrada_usuario})

    # Realiza la solicitud a la API de ChatGPT
    respuesta = openai.ChatCompletion.create(
        model=engine, 
        messages=conversacion_estado['mensajes'], 
        **configuracion_openai  # Pasa todas las configuraciones adicionales aquí
    )

    # Obtiene la respuesta generada por ChatGPT
    respuesta_chat = respuesta['choices'][0]['message']['content'].strip()

    # Convierte comillas invertidas en etiquetas <code>
    respuesta_chat = convertir_code(respuesta_chat)

    # Escribir en el archivo CSV
    escribir_en_csv(entrada_usuario, 'Usuario', conversacion_estado['nombre_archivo'])
    escribir_en_csv(respuesta_chat, 'PyChatGPT', conversacion_estado['nombre_archivo'])

    # Divide el texto en líneas y agrega todas las líneas como un solo elemento al contexto de la conversación
    conversacion_estado['mensajes'].append({'role': 'assistant', 'content': respuesta_chat})

    # Renderiza el template HTML con la respuesta
    return render_template('index.html', conversacion=conversacion_estado['mensajes'])

if __name__ == '__main__':
    app.run(debug=True)
