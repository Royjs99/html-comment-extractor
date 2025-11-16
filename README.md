# html-comment-extractor
Esta herramienta se encarga de realizar extracción de comentarios de archivos HTML. 
Es útil para la enumeración y reconocimiento de páginas web.

## Características
- Manejo de errores de conexión
- Manejo de diccionarios

## Requisitos
**requests**

## Instalación
pip3 install requests

## Uso de la herramienta
python3 html-extract-comments.py -u http://<IP> -d /usr/share/dict.txt

El parámetro -d hace referencia al diccionario de directorios de la página.
El parámetro -u hace referencia a la página.

## Ejemplo de uso
python3 html-extract-comments.py -u http://192.168.1.143 -d ./dict.txt

python3 html-extract-comments.py --url http://192.168.1.143 --dictionary ./dict.txt
