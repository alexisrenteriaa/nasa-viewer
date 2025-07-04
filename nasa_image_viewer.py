import requests
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

def buscar_imagenes(planeta):
    url = f"https://images-api.nasa.gov/search?q={planeta}&media_type=image"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        items = data['collection']['items']
        if items:
            # Obtener la primera imagen válida
            img_url = items[0]['links'][0]['href']
            print(f"Imagen encontrada: {img_url}")
            img_response = requests.get(img_url)
            img = Image.open(BytesIO(img_response.content))
            img.show()
        else:
            print(f"No se encontraron imágenes de {planeta}.")
    else:
        print(f"Error al buscar imágenes: {response.status_code}")

def menu():
    planetas = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    print("Selecciona un planeta:")
    for i, planeta in enumerate(planetas, 1):
        print(f"{i}. {planeta}")
    
    opcion = input("Opción: ")
    if opcion.isdigit() and 1 <= int(opcion) <= len(planetas):
        buscar_imagenes(planetas[int(opcion) - 1])
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    menu()
