import requests
import json
from dotenv import load_dotenv
import os

def validar_tiktok():
    url = 'https://open.tiktokapis.com/v2/oauth/token/'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control': 'no-cache',
    }

    data = {
        'client_key': 'awqb5rg5pax0ug02',
        'client_secret': '8vUzxwnuArm0C8NqjUPO8wu3559sBTsp',        
        'grant_type': 'client_credentials'
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()['access_token']
# Imprime la respuesta

'''
url = 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad.id'

response = validar_tiktok()
headers = {
    'authorization': 'Bearer ' + response
}
data = {
    "filters": {
        "ad_published_date_range": {
            "min": "20230101",
            "max": "20230102"           # rango de fechas de publicacion (añomesdia)
        },
        "country": "NO" # abreviatura paiz
    },
    "search_term": "coffee", # palabra clave
    "max_count": 20 # numero de resultados
}


while url:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())

    # check if there is a next page
    if 'next_page' in data:
        url = data['next_page']
    else:
        url = None
'''