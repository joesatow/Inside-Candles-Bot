import base64
import requests

consumer_key = 'LmtI9RQNVHZ5Xfa3SPe4fZ8Ey'
consumer_secret = 'nIqzC9PJRgq1qw0C55iZgUr901y6YuCXLBe1UelhOYem28NGgT'

#Reformat the keys and encode them
key_secret = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')
#Transform from bytes to bytes that can be printed
b64_encoded_key = base64.b64encode(key_secret)
#Transform from bytes back into Unicode
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)
auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}
auth_data = {
    'grant_type': 'client_credentials'
}
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
print(auth_resp.status_code)
access_token = auth_resp.json()['access_token']

file = open('helper_funcs\AAPL_1664539952.png', 'rb')
data = file.read()
resource_url='https://upload.twitter.com/1.1/media/upload.json'
upload_image={
    'media':data,
    'media_category':'tweet_image'}
    
image_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
}

media_id=requests.post(resource_url,headers=image_headers,params=upload_image)
print(media_id.text)



def sendTweet(media):
    # print(type(media))
    # # media = base64.b64encode(media).decode('ascii')
    # # print(type(media))
    # url = f"https://upload.twitter.com/1.1/media/upload.json?media_data={media}"

    # payload={}
    # headers = {
    # 'Authorization': 'OAuth oauth_consumer_key="LmtI9RQNVHZ5Xfa3SPe4fZ8Ey",oauth_token="1575825559556616192-5lHCMRKipHzh9KgrLTxwMEJxAcKxuk",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1664560432",oauth_nonce="9w3bH1c3Vye",oauth_version="1.0",oauth_signature="Zl%2FybB1v2tfIxnMOtrY02058htY%3D"',
    # 'Cookie': 'guest_id=v1%3A166455939276297902; guest_id_ads=v1%3A166455939276297902; guest_id_marketing=v1%3A166455939276297902; personalization_id="v1_MWAsxbSTY1L28E/uXebIzg=="; lang=en'
    # }

    # response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)

    pass