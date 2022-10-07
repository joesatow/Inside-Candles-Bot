import requests
import json
from helper_funcs.twitterAuth import getAuthHeader

authorizationHeader = getAuthHeader
url = "https://api.twitter.com/2/tweets"
headers = {
  'Authorization': authorizationHeader,
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