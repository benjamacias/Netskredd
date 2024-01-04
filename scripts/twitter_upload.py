# -*- coding: utf-8 -*-
import requests
import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import os
import json
import base64
import hashlib
import urllib
import re
import twitter
from requests_oauthlib import OAuth1  # Agrega esta línea


# Define tus claves de API de Twitter
client_key = 'Jxgd7i1SPAAfrj1yp8HSzPvJ9'
client_secret = 'VeU0Bh1NTQ4ASHQC9ZCEyleu1bDzK18VusaBS3NjkzJSDaB0v5'

resource_owner_key = '1737461353424515072-MyzhHvurwBpayOmt8b8tTTEi3i6YMY'
resource_owner_secret = 'ZpHVl1A1eXn30UFlbp66oYUZPjRshTE5LbZga7IAvNohO  '

# Crea una sesión OAuth1
auth = OAuth1(client_key, client_secret, resource_owner_key, resource_owner_secret)

# Define la URL de la API de Twitter para publicar un tweet
url = 'https://api.twitter.com/1.1/statuses/update.json'

# Define el texto del tweet
payload = {'status': 'Hello, world!'}

# Realiza la solicitud POST a la API de Twitter
response = requests.post(url, auth=auth, data=payload)

# Imprime la respuesta
print(response.json())

'AAAAAAAAAAAAAAAAAAAAAIFArgEAAAAA8QeAxXpksvB0XzD%2FIh5Ny5tPRdE%3DrYRcbAoQAQgekjFLjgp7C6v126XhoWYHLCEabJyubYbT11HU5x'
'1737461353424515072-UXLOZnaaVS68Y72P3ATM2X3sssFxlr'
"Oauth 2.0"
'SU5Ydkx2Z2ZaRENBQ1dPU2ZGcm46MTpjaQ',
'OyBUST5y03v9_36q0lvfuqdPZTDyUCRYjgYWhw1SZu9_pMXREJ'
"""
api = twitter.Api(consumer_key='Jxgd7i1SPAAfrj1yp8HSzPvJ9',
                  consumer_secret='VeU0Bh1NTQ4ASHQC9ZCEyleu1bDzK18VusaBS3NjkzJSDaB0v5',
                  access_token_key='AAAAAAAAAAAAAAAAAAAAAIFArgEAAAAA8QeAxXpksvB0XzD%2FIh5Ny5tPRdE%3DrYRcbAoQAQgekjFLjgp7C6v126XhoWYHLCEabJyubYbT11HU5x',
                  access_token_secret='OyBUST5y03v9_36q0lvfuqdPZTDyUCRYjgYWhw1SZu9_pMXREJ')"""