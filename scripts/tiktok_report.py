import requests
import json
from dotenv import load_dotenv
import os
from tiktok_validation import validar_tiktok

load_dotenv()  # carga las variables de entorno desde el archivo .env
TIKTOK_HEADER = os.getenv('TIKTOK_HEADER')  # obtén el token de acceso

url = 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad,ad_group'
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
        "country": "IT" # abreviatura paiz
    },
    "search_term": "coffee", # palabra clave
    "max_count": 20 # numero de resultados
}


while url:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    data = response.json()

    # check if there is a next page
    if 'next_page' in data:
        url = data['next_page']
    else:
        url = None