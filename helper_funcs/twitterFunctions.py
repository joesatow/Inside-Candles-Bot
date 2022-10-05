import requests
import json
import os

url = "https://api.twitter.com/2/tweets"

consumer_key = os.environ['api_key']
access_token = os.environ['access_token']
headers = {
  'Authorization': f'OAuth oauth_consumer_key={consumer_key},oauth_token={access_token},oauth_signature_method="HMAC-SHA1",oauth_timestamp="1664974150",oauth_nonce="6mq1ZoUDcul",oauth_version="1.0",oauth_signature="QOHNnh9t0P4lka%2FiI6CVnkaU9ls%3D"',
  'Content-Type': 'application/json',
  'Cookie': 'guest_id=v1%3A166497415009100398; guest_id_ads=v1%3A166497415009100398; guest_id_marketing=v1%3A166497415009100398; personalization_id="v1_XekPHh1IsmmpHayLaY20zw=="'
}

def sendTweet(tweetText, mediaID):
    payload = json.dumps({
        "text": tweetText, 
        "media": {
            "media_ids": [mediaID]
        }
    })

    requests.request("POST", url, headers=headers, data=payload)
