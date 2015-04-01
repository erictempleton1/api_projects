import tweepy
import config

"""
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
"""


class TwitterConn(object):

    def __init__(self):
        auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
        auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    def my_tweets(self):
        self.user_tweets = self.api.user_timeline('etemple10',count=200)
        large_tweets = [tweet.text.encode('utf-8') for tweet in self.user_tweets]
        return len(large_tweets)
