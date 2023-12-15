from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import os

load_dotenv()  # carga las variables de entorno desde el archivo .env
ACCESS_KEY = os.getenv('YT_KEY')  # obtén el token de acceso

DEVELOPER_KEY = "AIzaSyDrpuv0rioK7r99oSHo-7wK5DA_ZSFKaFg"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_most_popular_videos(region_code):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Call the videos.list method to retrieve the most popular videos.
    response = youtube.videos().list(
        part='snippet,contentDetails,statistics',
        chart='mostPopular',
        regionCode=region_code,
        maxResults=50
    ).execute()

    for video in response['items']:
        print(video['snippet']['title'])

try:
    get_most_popular_videos('NO')  # Replace 'US' with your region code
except HttpError as e:
    print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))