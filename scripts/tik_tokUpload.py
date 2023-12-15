import requests
import json
from dotenv import load_dotenv
import os
from tiktok_validation import validar_tiktok


def tiktok_upload(source_video, video_url):
    tiktokresponse = validar_tiktok()
    # Imprime la respuesta
    
    url = 'https://open.tiktokapis.com/v2/post/publish/inbox/video/init/'

    headers = {
        'Authorization': 'Bearer ' + tiktokresponse,
        'Cache-Control': 'no-cache',
    }

    video_size = os.path.getsize(video_url)

    data = {
        "source_info": 
        { 
            "source": video_url,
            "video_size": str(video_size),
            "chunk_size" : str(video_size),
            "total_chunk_count": 5
        }
        }

    # Se envia la request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Imprime la respuesta
    print(response.json())

def replace_slashes(path):
    return path.replace('/', '\\')

# Uso de la función
tiktok_upload("videoprueba", replace_slashes("C:/Users/irma/Downloads/pexels_videos_4636 (1080p).mp4"))