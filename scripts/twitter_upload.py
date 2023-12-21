# -*- coding: utf-8 -*-
from twarc import Twarc2
import tweepy
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

load_dotenv("archivo.env")
# Tus claves y tokens de la aplicación de Twitter
bearer_token =  os.getenv("BEARER_KEY_TW")
#access_token = os.getenv("CONSUMER_KEY_TW") 
#access_token_secret =os.getenv("CONSUMER_SECRET_TW")

access_token = '1737461353424515072-XvFvIAl0IJ9iIfYi3YkaIbtFoUetIH'
access_token_secret = 'GN0Qd4cBGkDWaPgSM5E3YjX6ciIyEu7hzR5JcJVao7Hd6'
redirect_uri = "http://localhost:8000/callback"

url = 'https://api.twitter.com/oauth/access_token'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {
    'code': '1737461353424515072-6FfKshEJ8y9J6q8tY8jns0MAGk5Gq9',
    'grant_type': 'authorization_code',
    'client_id': 'SU5Ydkx2Z2ZaRENBQ1dPU2ZGcm46MTpjaQ',
    'redirect_uri': redirect_uri,
    'code_verifier': 'challenge'
}

response = requests.post(url, headers=headers, data=data)

# Imprime la respuesta
print(response.json())