import requests
import json

url = "https://api.twitter.com/2/tweets"

headers = {
  'Authorization': 'OAuth oauth_consumer_key="LmtI9RQNVHZ5Xfa3SPe4fZ8Ey",oauth_token="1575825559556616192-5lHCMRKipHzh9KgrLTxwMEJxAcKxuk",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1664722905",oauth_nonce="pls6CnNDIvr",oauth_version="1.0",oauth_signature="QAPeTPhfT5mE1yu2bZ6Gh%2BzTDIQ%3D"',
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

    response = requests.request("POST", url, headers=headers, data=payload)
