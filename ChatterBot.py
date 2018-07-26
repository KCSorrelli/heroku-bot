# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE
