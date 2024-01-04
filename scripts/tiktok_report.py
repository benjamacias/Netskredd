import pdb
import requests
import json
from dotenv import load_dotenv
import os
from tiktok_validation import validar_tiktok
import time

load_dotenv()  # carga las variables de entorno desde el archivo .env
TIKTOK_HEADER = os.getenv('TIKTOK_HEADER')  # obtén el token de acceso

url = 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad.id'
response = validar_tiktok()

headers = {
    'authorization': 'Bearer ' + response
}

data = {
    "filters": {
        "ad_published_date_range": {
            "min": "20221001",
            "max": "20230510"           # rango de fechas de publicacion (añomesdia)
        },
        "country": "NO" # abreviatura paiz
    },
    "search_term": "dentist", # palabra clave
    "max_count": 20 # numero de resultados
}

max_retries = 0  # Define el número máximo de reintentos

while url:
    response_data = {"error": True}  # Initialize with an error to enter the loop
    while max_retries < 2:
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
            response_data = response.json()
            
            max_retries += 1

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying

    # check if there is a next page
    if 'next_page' in data:
        url = data['next_page']
    else:
        url = None

print(response_data)

"""
while url:
    response_data = {"error": True}  # Inicializamos con un error para entrar en el bucle
    while "error" in response_data:
        pdb.set_trace()
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_data = response.json()

        if "error" in response_data:
            print("Error en la solicitud: ", response_data["error"])
            # Aquí puedes agregar un tiempo de espera antes de reintentar, si lo deseas
            # import time

    # check if there is a next page
    if 'next_page' in data:
        url = data['next_page']
    else:
        url = None
"""