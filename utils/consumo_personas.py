import requests


def consumir_tabla_personas():
    url = "https://localhost:8080/api/personas"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos