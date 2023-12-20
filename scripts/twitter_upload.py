from tweepy import Client

# Tus claves y tokens de la aplicación de Twitter
bearer_token = 'your-bearer-token'
access_token = 'your-access-token'
access_token_secret = 'your-access-token-secret'

# Crear el cliente de la API
client = Client(bearer_token, access_token, access_token_secret)

def create_tweet(text, media=None):
    """
    Crea un tweet con texto y una imagen opcional
    """

    # Crear el cliente de la API
    client = Client(bearer_token, access_token, access_token_secret)
    if media == None:
        # Publicar un tweet
        client.create_tweet(text='Hello, Twitter!')
    else:
        # Publicar un tweet con imagen
        with open('path/to/image.png', 'rb') as image:
            client.create_tweet(text='Hello, Twitter!', media=image)
        
        # Publicar un tweet con video   
        with open('path/to/video.mp4', 'rb') as video:
            client.create_tweet(text='Hello, Twitter!', media=video, media_category='tweet_video')