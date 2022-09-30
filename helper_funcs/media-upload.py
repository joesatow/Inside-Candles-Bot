import os
import sys
import time

import json
import requests
from requests_oauthlib import OAuth1


MEDIA_ENDPOINT_URL = 'https://upload.twitter.com/1.1/media/upload.json'
POST_TWEET_URL = 'https://api.twitter.com/1.1/statuses/update.json'

CONSUMER_KEY = 'LmtI9RQNVHZ5Xfa3SPe4fZ8Ey'
CONSUMER_SECRET = 'nIqzC9PJRgq1qw0C55iZgUr901y6YuCXLBe1UelhOYem28NGgT'
ACCESS_TOKEN = '1575825559556616192-5lHCMRKipHzh9KgrLTxwMEJxAcKxuk'
ACCESS_TOKEN_SECRET = 'iniPvugA0SjXXRR5vFTEbYABrJ53Z4Anh1Ld18EAh5AFV'

FILENAME = 'AAPL_1664539952.png'
MEDIA_CATEGORY = 'dm_image'


oauth = OAuth1(CONSUMER_KEY,
  client_secret=CONSUMER_SECRET,
  resource_owner_key=ACCESS_TOKEN,
  resource_owner_secret=ACCESS_TOKEN_SECRET)


class TwitterMedia(object):

  def __init__(self, file_name, media_category):
    '''
    Defines media properties
    '''
    self.video_filename = file_name
    self.total_bytes = os.path.getsize(self.video_filename)
    self.media_id = None
    self.processing_info = None
    self.media_category = media_category


  def upload_init(self):
    '''
    Initializes Upload
    '''
    print('INIT')

    request_data = {
      'command': 'INIT',
      'media_type': 'image/jpeg',
      'total_bytes': self.total_bytes,
      'media_category': self.media_category,
      'shared': True # for media reuse in DMs. See: https://dev.twitter.com/rest/direct-messages/attaching-media
    }

    req = requests.post(url=MEDIA_ENDPOINT_URL, data=request_data, auth=oauth)
    media_id = req.json()['media_id']

    self.media_id = media_id

    print('Media ID: %s' % str(media_id))


  def upload_append(self):
    '''
    Uploads media in chunks and appends to chunks uploaded
    '''
    segment_id = 0
    bytes_sent = 0
    file = open(self.video_filename, 'rb')

    while bytes_sent < self.total_bytes:
      chunk = file.read(4*1024*1024)
      
      print('APPEND')

      request_data = {
        'command': 'APPEND',
        'media_id': self.media_id,
        'segment_index': segment_id
      }

      files = {
        'media':chunk
      }

      req = requests.post(url=MEDIA_ENDPOINT_URL, data=request_data, files=files, auth=oauth)

      if req.status_code < 200 or req.status_code > 299:
        print(req.status_code)
        print(req.text)
        sys.exit(0)

      segment_id = segment_id + 1
      bytes_sent = file.tell()

      print('%s of %s bytes uploaded' % (str(bytes_sent), str(self.total_bytes)))

    print('Upload chunks complete')


  def upload_finalize(self):
    '''
    Finalizes uploads and starts video processing
    '''
    print('FINALIZE')

    request_data = {
      'command': 'FINALIZE',
      'media_id': self.media_id
    }

    req = requests.post(url=MEDIA_ENDPOINT_URL, data=request_data, auth=oauth)
    print(req.json())

    self.processing_info = req.json().get('processing_info', None)
    self.check_status()


  def check_status(self):
    '''
    Checks video processing status
    '''
    if self.processing_info is None:
      return

    state = self.processing_info['state']

    print('Media processing status is %s ' % state)

    if state == u'succeeded':
      return

    if state == u'failed':
      sys.exit(0)

    check_after_secs = self.processing_info['check_after_secs']
    
    print('Checking after %s seconds' % str(check_after_secs))
    time.sleep(check_after_secs)

    print('STATUS')

    request_params = {
      'command': 'STATUS',
      'media_id': self.media_id
    }

    req = requests.get(url=MEDIA_ENDPOINT_URL, params=request_params, auth=oauth)
    
    self.processing_info = req.json().get('processing_info', None)
    self.check_status()


if __name__ == '__main__':
  twitterMedia = TwitterMedia(FILENAME, MEDIA_CATEGORY)
  twitterMedia.upload_init()
  twitterMedia.upload_append()
  twitterMedia.upload_finalize()