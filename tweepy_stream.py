# Using Tweepy to search for string "Thankyouduck" in twitter stream

import sys
import tweepy
import twitter

consumer_key="zNKX8aerJVc1SkYLINQHg"
consumer_secret="aywSxm4Un1okiDtZLg2ZjSz0WYt09azXz6i9xoXA"
access_key = "1648701380-OpdNZv2hTQEmO1zgSa5tltnabU2waoDrCNAFlb0"
access_secret = "gr3iuLIVRbVIb0JBpIA2tuezfnN1oRiTLtn5pdNipg"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        #import pdb; pdb.set_trace()
        print status.text # str(status.id)
        #Getting tweet_id from twitter_stream to reply
        tweet_id = open('tweet_id.txt','w')
        tweet_id.write(str(status.id))
        tweet_id.close()

        return False

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

twitter_stream = tweepy.streaming.Stream(auth, CustomStreamListener())

#Searching for the string
iterator = twitter_stream.filter(track=['thankyouduck'])
