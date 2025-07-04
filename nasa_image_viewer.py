import os
from dotenv import load_dotenv
import requests
from PIL import Image
from io import BytesIO

# Cargar variables de entorno desde el archivo .env
load_dotenv()

API_KEY = os.getenv('NASA_API_KEY')

def obtener_imagen_apod():
    url = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        imagen_url = data['url']
        print(f"Imagen del día: {imagen_url}")
        
        if imagen_url.endswith('.jpg'):
            img_response = requests.get(imagen_url)
            img = Image.open(BytesIO(img_response.content))
            img.show()
        else:
            print(f'No se pudo mostrar la imagen, tipo de archivo no soportado: {imagen_url}')
    else:
        print(f"Error al obtener la imagen: {response.status_code}")

if __name__ == "__main__":
    obtener_imagen_apod()
