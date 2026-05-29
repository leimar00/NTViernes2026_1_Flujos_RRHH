import requests


def consumir_tabla_entrevista():
    url = "https://localhost:8080/api/entrevista"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos
