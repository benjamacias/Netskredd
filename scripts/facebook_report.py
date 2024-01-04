import requests
from dotenv import load_dotenv
import os

load_dotenv()  # carga las variables de entorno desde el archivo .env
access_token = os.getenv('FACEBOOK_TOKEN')  # obtén el token de acceso
access_user= os.getenv('FACEBOOK_USER')  # obtén el token de acceso

#obtenemos id de los hashtags de facebook
url = "https://graph.facebook.com/v18.0/ig_hashtag_search"
params = {
    "user_id": access_user,
    "q": "bluebottle", #nombre del hashtag
    "access_token": access_token  # reemplaza {access-token} con tu token de acceso real
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Lanza una excepción si la respuesta contiene un código de estado HTTP de error

    # Imprime el estado de la respuesta
    print(response.status_code)

    # Imprime el contenido de la respuesta
    print(response.json())

except Exception as err:
    if response["message"] == "Unsupported get request. Object with ID '17841405309211844' does not exist, cannot be loaded due to missing permissions, or does not support this operation. Please read the Graph API documentation at https://developers.facebook.com/docs/graph-api":
        print("El usuario no existe") 