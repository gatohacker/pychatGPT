import csv
import os
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore, Style
import inquirer

# Inicializa colorama para soportar colores en la consola
init(autoreset=True)

# Diccionario para mapear nombres de color a objetos Colorama
colores = {
    'Negro': Fore.BLACK,
    'Rojo': Fore.RED,
    'Verde': Fore.GREEN,
    'Amarillo': Fore.YELLOW,
    'Azul': Fore.BLUE,
    'Magenta': Fore.MAGENTA,
    'Cian': Fore.CYAN,
    'Blanco': Fore.WHITE
}

# Colores preseleccionados para Usuario y PyChatGPT
color_usuario = Fore.CYAN
color_pychatgpt = Fore.MAGENTA

# Función para mostrar las conversaciones del archivo CSV seleccionado
def mostrar_conversaciones(archivo_csv):
    with open(archivo_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            fecha, rol, mensaje = row
            if rol == 'Usuario':
                print(color_usuario + f"{fecha} [{rol}]: {mensaje}")
            elif rol == 'PyChatGPT':
                print(color_pychatgpt + f"{fecha} [{rol}]: {mensaje}")

# Función para seleccionar un archivo CSV de la carpeta 'logs'
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter

    # Abre un diálogo para seleccionar un archivo CSV de la carpeta 'logs'
    archivo_csv = filedialog.askopenfilename(initialdir='logs', title='Seleccionar archivo CSV', filetypes=[('Archivos CSV', '*.csv')])

    # Muestra las conversaciones del archivo seleccionado
    if archivo_csv:
        print(f"\nMostrando conversaciones del archivo: {archivo_csv}")
        mostrar_conversaciones(archivo_csv)
        return True  # Indica que se ha seleccionado un archivo
    else:
        return False  # Indica que no se ha seleccionado ningún archivo

# Función principal
def main():
    global color_usuario
    global color_pychatgpt
    
    continuar = True
    while continuar:
        questions = [
            inquirer.List('opciones',
                message="¿Qué deseas hacer?",
                choices=[
                    ('Leer una conversación', 'leer'),
                    ('Cambiar colores', 'colores'),
                    ('Salir de LectorLogs', 'salir')
                ],
            ),
        ]
        respuesta = inquirer.prompt(questions)
        if respuesta['opciones'] == 'leer':
            continuar = seleccionar_archivo()
        elif respuesta['opciones'] == 'colores':
            # Preguntar por los nuevos colores
            new_colors = inquirer.prompt([
                inquirer.List('color_usuario', message="Nuevo color para Usuario: ", choices=list(colores.keys()), default='Cian'),
                inquirer.List('color_pychatgpt', message="Nuevo color para PyChatGPT: ", choices=list(colores.keys()), default='Magenta'),
            ])
            # Actualizar los colores
            color_usuario = colores[new_colors['color_usuario']]
            color_pychatgpt = colores[new_colors['color_pychatgpt']]
            print("Colores actualizados.")
        else:
            continuar = False

if __name__ == "__main__":
    main()
