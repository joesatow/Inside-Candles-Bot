from webbrowser import get
import requests
import json
import os
from helper_funcs.API_keys import getKey

url = "https://api.twitter.com/2/tweets"

consumer_key = getKey('api_key')
access_token = getKey('access_token')
headers = {
  'Authorization': f'OAuth oauth_consumer_key={consumer_key},oauth_token={access_token},oauth_signature_method="HMAC-SHA1",oauth_timestamp="1665092513",oauth_nonce="J8MbG3bAETl",oauth_version="1.0",oauth_signature="%2FsHPxD6fG69c1ITrIrRAfjkgnK0%3D"',
  'Content-Type': 'application/json',
  'Cookie': 'guest_id=v1%3A164748160617485457; guest_id_ads=v1%3A164748160617485457; guest_id_marketing=v1%3A164748160617485457; personalization_id="v1_PFHqkQhmwp141oUu4hPm9w=="'
}

def sendTweet(tweetText, mediaID):
    payload = json.dumps({
        "text": tweetText, 
        "media": {
            "media_ids": [mediaID]
        }
    })

    requests.request("POST", url, headers=headers, data=payload)
