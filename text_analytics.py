
from tweepy import OAuthHandler
from tweepy import Stream
import apiconfig as config
import sys
from listner import StdOutListener






access_token=config.access_token
access_token_secret=config.token_secret
consumer_key=config.api_key
consumer_secret=config.api_secret

if __name__== '__main__':
    args=sys.argv
    del args[0]
    l=StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth,l)


    stream.filter(track=args)
