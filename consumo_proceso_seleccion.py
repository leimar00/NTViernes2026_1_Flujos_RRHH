import requests

def consumir_tabla_seleccion():
    url = "http://localhost:8080/api/seleccion"
    respuesta = requests.get(url)
    respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
    datos = respuesta.json()  # Devolver la respuesta en formato JSON
    return datos