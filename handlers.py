import urllib
import webapp2
from html_templates import KOSMOPOLIS
import logging
import tweepy

class MainPage (webapp2.RequestHandler):

    def get(self):
        self.response.write(KOSMOPOLIS)

class Search(webapp2.RequestHandler):

    def get(self):
        #owner_username    = os.environ.get('TW_OWNER_USERNAME')
        #username          = os.environ.get('TW_USERNAME')
        consumer_key      = 'your consumerkey'
        consumer_secret   = 'your consumer_secret'
        access_key        = 'your access_key'
        access_secret     = 'your access_secret'
        searchquery = self.request.get('search')
        auth = tweepy.OAuthHandler(consumer_key=consumer_key,
            consumer_secret=consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth_handler=auth)#, secure=True, retry_count=3)
        self.response.write(api.search(searchquery))


