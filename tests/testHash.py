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

consumer_key = getKey('consumer_key')
consumer_key_secret = getKey('consumer_key_secret')
access_token = getKey('access_token')
access_token_secret = getKey('access_token_secret')
baseURL = "https://api.twitter.com/2/tweets"
nonce = secrets.token_urlsafe()
nonce = ''.join(filter(str.isalnum, nonce))
#nonce = '2e1acZT4H5d'
timestamp = str(int(time.time()))
#timestamp = '1665161180'

def percentEncode(str):
    return urllib.parse.quote(str, safe="")

# consumer_key = 'xvz1evFS4wEEPTGEFPHBog'
# consumer_key_secret = 'kAcSOqF21Fu85e7zjz7ZN2U4ZRhfV3WpwPAoE3Z7kBw'
# nonce = "kYjzVBB8Y0ZFabxSWbWovY3uYSQ2pTgmZeNu2VS4cg"
# timestamp = "1318622958"
# access_token = "370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb"
# access_token_secret = "LswwdoUaIvS8ltyTt5jkRh4J50vUPVVHtR2YPi5kE"
# baseURL = "https://api.twitter.com/1.1/statuses/update.json"

oauth_consumer_key_KEY = percentEncode("oauth_consumer_key")
oauth_consumer_key_VALUE = percentEncode(consumer_key)

oauth_nonce_KEY = percentEncode("oauth_nonce")
oauth_nonce_VALUE = percentEncode(nonce)

oauth_signature_method_KEY = percentEncode("oauth_signature_method")
oauth_signature_method_VALUE = percentEncode("HMAC-SHA1")

oauth_timestamp_KEY = percentEncode("oauth_timestamp")
oauth_timestamp_VALUE = percentEncode(timestamp)

oauth_token_KEY = percentEncode("oauth_token")
oauth_token_VALUE = percentEncode(access_token)

oauth_version_KEY = percentEncode("oauth_version")
oauth_version_VALUE = percentEncode("1.0")

include_entities_KEY = percentEncode("include_entities")
include_entities_VALUE = percentEncode("true")

status_KEY = percentEncode("status")
status_VALUE = percentEncode("Hello Ladies + Gentlemen, a signed OAuth request!")

#parameterString = include_entities_KEY + '=' + include_entities_VALUE + "&"
parameterString = oauth_consumer_key_KEY + '=' + oauth_consumer_key_VALUE + '&'
parameterString += oauth_nonce_KEY + '=' + oauth_nonce_VALUE + '&'
parameterString += oauth_signature_method_KEY + '=' + oauth_signature_method_VALUE + '&'
parameterString += oauth_timestamp_KEY + '=' + oauth_timestamp_VALUE + '&'
parameterString += oauth_token_KEY + '=' + oauth_token_VALUE + '&'
parameterString += oauth_version_KEY + '=' + oauth_version_VALUE
#parameterString += status_KEY + '=' + status_VALUE

# parameterString = include_entities_KEY + '=' + include_entities_VALUE + "&"
# parameterString += oauth_consumer_key_KEY + '=' + oauth_consumer_key_VALUE + '&'
# parameterString += oauth_nonce_KEY + '=' + oauth_nonce_VALUE + '&'
# parameterString += oauth_signature_method_KEY + '=' + oauth_signature_method_VALUE + '&'
# parameterString += oauth_timestamp_KEY + '=' + oauth_timestamp_VALUE + '&'
# parameterString += oauth_token_KEY + '=' + oauth_token_VALUE + '&'
# parameterString += oauth_version_KEY + '=' + oauth_version_VALUE + '&'
# parameterString += status_KEY + '=' + status_VALUE


# parameterString = urlencode(
#     {
#         "include_entities": "true",
#         "oauth_consumer_key": consumer_key,
#         "oauth_nonce": nonce,
#         "oauth_signature_method": 'HMAC-SHA1',
#         "oauth_timestamp": timestamp,
#         "oauth_token": access_token,
#         "oauth_version": "1.0",
#         "status": percentEncode(b"Hello Ladies + Gentlemen, a signed OAuth request!")
#     },
#     quote_via=quote_plus
# )
#print(parameterString)


percentEncodedURL = percentEncode(baseURL)
percentEncodedParameterString = percentEncode(parameterString)
signatureBaseString = "POST&" + percentEncodedURL + "&" + percentEncodedParameterString
#print(signatureBaseString)
signingKey = percentEncode(consumer_key_secret) + '&' + percentEncode(access_token_secret)
#print(signingKey)

def get_signture(data, secret_key):
    signature = hmac.new(secret_key.encode(), data.encode(), hashlib.sha1).digest()
    signature = base64.b64encode(signature).decode('utf-8')
    print(signature)
    return signature

signature = get_signture(signatureBaseString, signingKey)

oauth_signature_KEY = percentEncode("oauth_signature")
oauth_signature_VALUE = percentEncode(signature)

def keyValHeader(key,val):
    return key + "=" + '"' + val + '"'

DST = "OAuth "
DST += keyValHeader(oauth_consumer_key_KEY, oauth_consumer_key_VALUE) +  ","
DST += keyValHeader(oauth_token_KEY, oauth_token_VALUE) + ","
DST += keyValHeader(oauth_signature_method_KEY, oauth_signature_method_VALUE) + ","
DST += keyValHeader(oauth_timestamp_KEY, oauth_timestamp_VALUE) + ","
DST += keyValHeader(oauth_nonce_KEY, oauth_nonce_VALUE) + ","
DST += keyValHeader(oauth_version_KEY, oauth_version_VALUE) + ","
DST += keyValHeader(oauth_signature_KEY, oauth_signature_VALUE)

url = "https://api.twitter.com/2/tweets"

consumer_key = getKey('api_key')
access_token = getKey('access_token')
headers = {
  'Authorization': DST,
  'Content-Type': 'application/json',
  'Cookie': 'guest_id=v1%3A164748160617485457; guest_id_ads=v1%3A164748160617485457; guest_id_marketing=v1%3A164748160617485457; personalization_id="v1_PFHqkQhmwp141oUu4hPm9w=="'
}

def sendTweet(tweetText):
    payload = json.dumps({
        "text": tweetText
    })

    print(requests.request("POST", url, headers=headers, data=payload).json())

sendTweet("test all params")
