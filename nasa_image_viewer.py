import requests
from PIL import Image
from io import BytesIO

# Reemplaza con tu clave de API de NASA
API_KEY = 'zd22vaVpowWGsHFkZ3kOXeggdBapJI7NGh2Rl5fe'

def obtener_imagen_apod():
    # URL para obtener la imagen del día
    url = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'
    
    # Hacer la petición a la API
    response = requests.get(url)
    
    # Comprobar si la respuesta es correcta (código 200)
    if response.status_code == 200:
        # Convertir la respuesta a formato JSON
        data = response.json()
        
        # Obtener la URL de la imagen
        imagen_url = data['url']
        print(f"Imagen del día: {imagen_url}")
        
        # Si la imagen es de tipo JPG, la descargamos
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
