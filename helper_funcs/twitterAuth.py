import secrets
import time
import urllib.parse
import hmac
import hashlib
import base64
from helper_funcs.API_keys import getKey

# Get API keys
consumer_key = getKey('consumer_key')
consumer_key_secret = getKey('consumer_key_secret')
access_token = getKey('access_token')
access_token_secret = getKey('access_token_secret')

# Base URL
baseURL = "https://api.twitter.com/2/tweets"

# OAuth nonce
nonce = secrets.token_urlsafe()
nonce = ''.join(filter(str.isalnum, nonce))

# Oauth timestamp
timestamp = str(int(time.time()))

# Function to percent encode any passed in string
def percentEncode(str):
    return urllib.parse.quote(str, safe="")

# Percent encode every key/value pair
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

# Build parameter string
parameterString = oauth_consumer_key_KEY + '=' + oauth_consumer_key_VALUE + '&'
parameterString += oauth_nonce_KEY + '=' + oauth_nonce_VALUE + '&'
parameterString += oauth_signature_method_KEY + '=' + oauth_signature_method_VALUE + '&'
parameterString += oauth_timestamp_KEY + '=' + oauth_timestamp_VALUE + '&'
parameterString += oauth_token_KEY + '=' + oauth_token_VALUE + '&'
parameterString += oauth_version_KEY + '=' + oauth_version_VALUE

# Build signature base string by combining percent encoded base URL and parameter string
percentEncodedURL = percentEncode(baseURL)
percentEncodedParameterString = percentEncode(parameterString)
signatureBaseString = "POST&" + percentEncodedURL + "&" + percentEncodedParameterString

# Build signing key by combining percent encoded consumer secret and token secret
signingKey = percentEncode(consumer_key_secret) + '&' + percentEncode(access_token_secret)

# Function to hash signature base string and signing key using HMAC-SHA1
def get_signature(data, secret_key):
    signature = hmac.new(secret_key.encode(), data.encode(), hashlib.sha1).digest()
    signature = base64.b64encode(signature).decode('utf-8')
    return signature

# Set OAuth signature
signature = get_signature(signatureBaseString, signingKey)

# Set final percent encoded key/value pairs needed to build auth header.
oauth_signature_KEY = percentEncode("oauth_signature")
oauth_signature_VALUE = percentEncode(signature)

# Helper function for building auth header
def keyValHeader(key,val):
    return key + "=" + '"' + val + '"'

# Build auth header
DST = "OAuth "
DST += keyValHeader(oauth_consumer_key_KEY, oauth_consumer_key_VALUE) +  ","
DST += keyValHeader(oauth_token_KEY, oauth_token_VALUE) + ","
DST += keyValHeader(oauth_signature_method_KEY, oauth_signature_method_VALUE) + ","
DST += keyValHeader(oauth_timestamp_KEY, oauth_timestamp_VALUE) + ","
DST += keyValHeader(oauth_nonce_KEY, oauth_nonce_VALUE) + ","
DST += keyValHeader(oauth_version_KEY, oauth_version_VALUE) + ","
DST += keyValHeader(oauth_signature_KEY, oauth_signature_VALUE)

# Getter method to return auth header
def getAuthHeader():
    return DST