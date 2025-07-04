import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

def buscar_imagenes_tk(planeta, cantidad=5):
    # Igual que la función anterior, pero devuelve las URLs
    url = f"https://images-api.nasa.gov/search?q={planeta}&media_type=image"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        items = data['collection']['items']
        urls = [item['links'][0]['href'] for item in items[:cantidad]]
        return urls
    else:
        return []

def mostrar_imagenes_tk(urls):
    for url in urls:
        img_response = requests.get(url)
        img_data = Image.open(BytesIO(img_response.content))
        img_data.show()

def on_seleccionar():
    planeta = var_planeta.get()
    urls = buscar_imagenes_tk(planeta)
    if not urls:
        messagebox.showerror("Error", f"No se encontraron imágenes de {planeta}")
        return
    mostrar_imagenes_tk(urls)

root = tk.Tk()
root.title("NASA Planet Viewer")

var_planeta = tk.StringVar(root)
planetas = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
var_planeta.set(planetas[0])

tk.Label(root, text="Selecciona un planeta").pack(pady=10)
dropdown = tk.OptionMenu(root, var_planeta, *planetas)
dropdown.pack(pady=10)

btn = tk.Button(root, text="Mostrar imágenes", command=on_seleccionar)
btn.pack(pady=10)

root.mainloop()
