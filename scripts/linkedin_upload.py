import re
import requests
import json
import os
import pdb
"""
class LinkedinAutomate:
    def __init__(self, access_token, yt_url, title, description):
        self.access_token = access_token
        self.yt_url = yt_url
        self.title = title
        self.description = description
        self.python_group_list = [9247360]
        self.headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

    def common_api_call_part(self, feed_type = "feed", group_id = None):
        payload_dict = {
            "author": f"urn:li:person:{self.user_id}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": self.description
                },
                "shareMediaCategory": "ARTICLE",
                "media": [
                        {
                        "status": "READY",
                        "description": {
                            "text": self.description
                        },
                        "originalUrl": self.yt_url,
                        "title": {
                            "text": self.title
                        },
                        "thumbnails": [
                                {
                                "url": self.extract_thumbnail_url_from_YT_video_url()
                                }
                            ]
                        }
                    ]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC" if feed_type == "feed" else "CONTAINER"
            }
        }
        if feed_type == "group":
            payload_dict["containerEntity"] = f"urn:li:group:{group_id}"

        return json.dumps(payload_dict)

    def extract_thumbnail_url_from_YT_video_url(self):
        exp = "^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*"
        s = re.findall(exp,self.yt_url)[0][-1]
        return  f"https://i.ytimg.com/vi/{s}/maxresdefault.jpg"

    def get_user_id(self):
        url = "https://api.linkedin.com/v2/me"
        response = requests.request("GET", url, headers=self.headers)
        jsonData = json.loads(response.text)
        return jsonData["id"]
    
    def feed_post(self):
        url = "https://api.linkedin.com/v2/ugcPosts"
        payload = self.common_api_call_part()

        return requests.request("POST", url, headers=self.headers, data=payload)
    
    def group_post(self, group_id):
        url = "https://api.linkedin.com/v2/ugcPosts"
        payload = self.common_api_call_part(feed_type = "group", group_id=group_id)
        
        return requests.request("POST", url, headers=self.headers, data=payload)


    def main_func(self):
        self.user_id = self.get_user_id()
        print(self.user_id)

        feed_post = self.feed_post()
        print(feed_post)
        for group_id in self.python_group_list:
            print(group_id)
            group_post = self.group_post(group_id)
            print(group_post)

access_token = "AQWJ1g0txwBsT778WA7VCYs8gKcodRn8Ujc9iG2xQCGIbieOLR7KM1upa-V0LOFb0Agy_hZ0PgXqpLP_DcEgVfkZ0dGEIpcHyV6VYagaKLiChH8JIcuV11tgOivkODsy1_qUPhVHxpMEbhVtGtr6sA9cyCbws0Shin3VwmwSggxr6uKR6JPBc9DOdPnXXlFqhQe3iG_d_UIHKdWAumwLnIiDBtAL5Mw4opVtGKWtfHETTP5z5fRzJH7rL4nIjGnraqIB-ywJr4jDWDJEbgSGZmAMRL_TFKMsUFkxL9bRP7p2-rLh20DamNXdefWzwd1qate4Fpcu-3oNQz2vyjLAH1lvMxlkRw"
yt_url = "https://www.youtube.com/watch?v=Mn6gIEM33uU"
title = "Prueba 1"
description = "Esta es solo una prueba de publicacion en linkedin desde python"

LinkedinAutomate(access_token, yt_url, title, description).main_func()
"""

class LinkedInPoster:

    def create_post(access_token,author, text):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        }

        body = {
            "author": f"urn:li:person:{author}",
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

        response = requests.post(
            "https://api.linkedin.com/v2/ugcPosts",
            headers=headers,
            data=json.dumps(body)
        )

        if response.status_code != 201:
            raise Exception(f"Request failed: {response.content}")
        
        return response.json()
 
    access_token = "AQWJ1g0txwBsT778WA7VCYs8gKcodRn8Ujc9iG2xQCGIbieOLR7KM1upa-V0LOFb0Agy_hZ0PgXqpLP_DcEgVfkZ0dGEIpcHyV6VYagaKLiChH8JIcuV11tgOivkODsy1_qUPhVHxpMEbhVtGtr6sA9cyCbws0Shin3VwmwSggxr6uKR6JPBc9DOdPnXXlFqhQe3iG_d_UIHKdWAumwLnIiDBtAL5Mw4opVtGKWtfHETTP5z5fRzJH7rL4nIjGnraqIB-ywJr4jDWDJEbgSGZmAMRL_TFKMsUFkxL9bRP7p2-rLh20DamNXdefWzwd1qate4Fpcu-3oNQz2vyjLAH1lvMxlkRw"
    create_post(access_token, "benja", "prueba de publicacion")
    
