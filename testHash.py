import secrets
import requests
import json
import time
import os
import urllib.parse
import hmac
import hashlib
import base64
from urllib.parse import urlencode, quote_plus
from helper_funcs.API_keys import getKey

url = "https://api.twitter.com/2/tweets"

consumer_key = getKey('api_key')
consumer_key_secret = getKey('consumer_key_secret')
access_token = getKey('access_token')
access_token_secret = getKey('access_token_secret')

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

nonce = secrets.token_urlsafe()
nonce = ''.join(filter(str.isalnum, nonce))
timestamp = int(time.time())

DST = "OAuth "
oauth_consumer_key = os.environ['api_key']
payload = {"oauth_consumer_key": oauth_consumer_key, "oauth_token":access_token, "oauth_signature_method":"HMAC-SHA1"}
#print(urlencode(payload, quote_via=quote_plus))

parameterString = urlencode(
    {
        "oauth_consumer_key": oauth_consumer_key,
        "oauth_nonce": nonce,
        "oauth_signature_method": 'HMAC-SHA1',
        "oauth_timestamp": timestamp,
        "oauth_token": access_token,
        "oauth_version": "1.0"
    },
    quote_via=quote_plus
)

percentEncodedURL = urllib.parse.quote("https://api.twitter.com/2/tweets", safe="")
percentEncodedParameterString = urllib.parse.quote(parameterString, safe="")
signatureBaseString = "POST&" + percentEncodedURL + "&" + percentEncodedParameterString
signingKey = urllib.parse.quote(consumer_key_secret, safe="") + '&' + urllib.parse.quote(access_token_secret, safe="")

signatureBaseString = b'POST&https%3A%2F%2Fapi.twitter.com%2F1.1%2Fstatuses%2Fupdate.json&include_entities%3Dtrue%26oauth_consumer_key%3Dxvz1evFS4wEEPTGEFPHBog%26oauth_nonce%3DkYjzVBB8Y0ZFabxSWbWovY3uYSQ2pTgmZeNu2VS4cg%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1318622958%26oauth_token%3D370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb%26oauth_version%3D1.0%26status%3DHello%2520Ladies%2520%252B%2520Gentlemen%252C%2520a%2520signed%2520OAuth%2520request%2521'
signingKey = b"kAcSOqF21Fu85e7zjz7ZN2U4ZRhfV3WpwPAoE3Z7kBw&LswwdoUaIvS8ltyTt5jkRh4J50vUPVVHtR2YPi5kE"

def get_signture(data, secret_key):
    signature = hmac.new(secret_key, data, hashlib.sha1).digest()
    signature = base64.b64encode(signature).decode('utf-8')
    return signature

get_signture(signatureBaseString, signingKey)