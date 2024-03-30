# Servidor Web de API ChatGPT y Lector de Logs

Este proyecto consiste en un servidor web de ChatGPT implementado en Python que guarda logs de conversaciones y un lector de esos logs.

## Descripción

El objetivo de este proyecto es proporcionar una interfaz web simple para interactuar con el modelo de lenguaje GPT (Generative Pre-trained Transformer) de OpenAI, comúnmente conocido como ChatGPT. Además, el servidor web guarda las conversaciones en un archivo de registro (log) con día, fecha y hora para su posterior lectura.

El lector de logs permite visualizar las conversaciones previamente almacenadas en los logs, con chats coloreados, facilitando el seguimiento de interacciones pasadas.

## Funcionalidades

- **Servidor web de ChatGPT**: Proporciona una interfaz web para interactuar con el modelo de lenguaje GPT.
- **Guardado de logs**: Almacena las conversaciones en un archivo de registro para su posterior revisión.
- **Lector de logs**: Permite visualizar las conversaciones previamente almacenadas en los logs.

## Requisitos

Python: Necesitarás tener Python instalado en tu sistema. Puedes descargar la última versión desde python.org/downloads.

Este proyecto utiliza las siguientes bibliotecas externas. Debes instalarlas utilizando pip:

- tkinter
- colorama
- inquirer
- configparser
- subprocess
- openai
- flask

Puedes instalar las bibliotecas externas necesarias utilizando pip. Abre una terminal y ejecuta los siguientes comandos uno por uno:

```
pip install tkinter
pip install colorama
pip install inquirer
pip install configparser
pip install openai
pip install flask
```

## Uso

Para utilizar el servidor web de ChatGPT y el lector de logs, sigue estos pasos:

1. Ejecuta el servidor web utilizando el archivo `pychatGPT.py`.
2. Accede al servidor web a través de tu navegador web por la ruta http://127.0.0.1:5000 y sigue las instrucciones para interactuar con ChatGPT.
3. Utiliza el lector de logs ejecutando `lectorlogs.py` para visualizar conversaciones pasadas almacenadas en los logs.
4. Los logs se almacenan automáticamente en la carpeta `logs`.

Dentro de la carpeta `templates`, encontrarás un archivo `index.html` que puedes modificar para implementar diferentes colores a `<code>`, ya que el servidor distingue entre texto corriente y código, coloreándolo con `highlight.min.js`.

El archivo `pychatGPT.py` tiene un menú que te permite configurar el API key, el motor y otros datos necesarios para la ejecución del servidor.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commits (`git commit -am 'Añade nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Crea un Pull Request.

## Licencia

Este proyecto está bajo la Licencia Creative Commons No Comercial Sin Derivados (CC BY-NC-ND), lo que significa que puedes leer, compartir y utilizar el código libremente para fines no comerciales, siempre y cuando incluyas el aviso de copyright y la licencia en todas las copias o partes sustanciales del software. No se permite la venta del software sin permiso previo del titular de los derechos de autor. Este software se proporciona "tal cual", sin garantía de ningún tipo. Consulta el archivo `LICENSE` para obtener más detalles.

Para obtener permiso para utilizar este software con fines comerciales o realizar modificaciones, contáctame para discutir la posibilidad de obtener una licencia adecuada.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto conmigo:

- Autor: **GatoHacker**
- E-Mail: gatohackeronline@gmail.com
