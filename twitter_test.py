import urlparse
import oauth2 as oauth
import tweepy
import json
import config

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

"""
for tweet in public_tweets[:5]:
    print tweet.text.encode('utf-8')
    print tweet.favorite_count
    print tweet.retweeted
    print tweet.user.name.encode('utf-8')
"""


user_tweets = api.user_timeline('etemple10',count=200)

# list of 200 of my tweets
large_tweets = [tweet.text.encode('utf-8') for tweet in user_tweets]
print len(large_tweets)

for tweet in user_tweets[:5]:
    print tweet.text.encode('utf-8')
    print tweet.created_at
    print tweet.favorited
    print tweet.entities['hashtags']
    print tweet.retweet_count


my_favd = api.retweets_of_me()

# list of my favd tweets
favd_tweets = [tweet.text.encode('utf-8') for tweet in my_favd]
print len(favd_tweets)