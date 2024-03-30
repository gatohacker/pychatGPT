import configparser
import os
import inquirer
import subprocess

def ejecutar_server():
    if not os.path.exists('config.ini'):
        print("Debes configurar la aplicación antes de ejecutar el servidor.")
        return

    subprocess.run(["python", "serverpychatGPT.py"])

def configurar_server():
    config = configparser.ConfigParser()

    api_key = input("Ingresa tu API key: ").strip()
    while not api_key:
        print("La API key no puede dejarse en blanco.")
        api_key = input("Ingresa tu API key: ").strip()

    engine_choices = [
        "gpt-4-turbo-preview",
        "gpt-4",
        "gpt-3.5-turbo-16k",
        "gpt-3.5-turbo-0125",
        "gpt-3.5-turbo"
    ]
    engine = inquirer.prompt([
        inquirer.List('engine',
                      message="Selecciona el motor (engine):",
                      choices=engine_choices,
                      ),
    ])['engine']

    max_tokens = input("Ingresa el valor de max tokens (deja vacío para usar el valor por defecto de 256): ").strip() or "256"
    temperature = input("Ingresa el valor de temperature (deja vacío para usar el valor por defecto de 0.7): ").strip() or "0.7"
    frequency_penalty = input("Ingresa el valor de frequency penalty (deja vacío para usar el valor por defecto de 0.2): ").strip() or "0.2"

    config['openai'] = {
        'api_key': api_key,
        'engine': engine,
    }
    config['configuracion_openai'] = {
        'max_tokens': max_tokens,
        'temperature': temperature,
        'frequency_penalty': frequency_penalty
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def menu():
    while True:
        questions = [
            inquirer.List('action',
                          message="Selecciona una opción:",
                          choices=['Ejecutar serverpychatGPT', 'Configurar serverpychatGPT', 'Salir']
                          ),
        ]
        answer = inquirer.prompt(questions)['action']
        
        if answer == 'Ejecutar serverpychatGPT':
            ejecutar_server()
        elif answer == 'Configurar serverpychatGPT':
            configurar_server()
        elif answer == 'Salir':
            break

if __name__ == "__main__":
    menu()
