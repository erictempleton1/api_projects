import urlparse
import oauth2 as oauth
import tweepy
import json
import config

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets[:5]:
    print tweet.text.encode('utf-8')
    print tweet.favorite_count
    print tweet.retweeted
    print tweet.user.name.encode('utf-8')

user_info = api.user_timeline('etemple10')

