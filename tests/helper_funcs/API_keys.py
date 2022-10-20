import os

# Set these variables to your corresponding environmental variables.  This is the source location for API keys throughout the program.
consumer_key = os.environ['api_key']
consumer_key_secret = os.environ['api_key_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']
td_api_key = os.environ['td_api_key']
sc_cookie = os.environ['sc_cookie']

# Function to grab keys 
def getKey(key):
    if key == "consumer_key":
        return consumer_key
    if key == "consumer_key_secret":
        return consumer_key_secret
    if key == "access_token":
        return access_token
    if key == "access_token_secret":
        return access_token_secret
    if key == "td_api_key":
        return td_api_key
    if key == "sc_cookie":
        return sc_cookie