import urlparse
import oauth2 as oauth
import tweepy
import json
import config

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets[:5]:
    print tweet.text.encode('utf-8')
    print tweet.favorite_count
    print tweet.retweeted
    print tweet.user.name.encode('utf-8')
