import requests
import json

access_token = 'your-access-token'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
    'X-Restli-Protocol-Version': '2.0.0'
}
def subir_linkedin(text=None, media=None, type=None):
    data = {
        "author": "urn:li:person:your-person-id",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    response = requests.post('https://api.linkedin.com/v2/ugcPosts', headers=headers, data=json.dumps(data))

    print(response.json())