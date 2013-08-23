
import sys
from twython import Twython
#Using oauth_1 to access personal account.
#Using oauth_2 to access an application

APP_KEY = 'zNKX8aerJVc1SkYLINQHg'
APP_SECRET='aywSxm4Un1okiDtZLg2ZjSz0WYt09azXz6i9xoXA'
OAUTH_TOKEN= '1648701380-OpdNZv2hTQEmO1zgSa5tltnabU2waoDrCNAFlb0'
OAUTH_TOKEN_SECRET='gr3iuLIVRbVIb0JBpIA2tuezfnN1oRiTLtn5pdNipg'

#photo= open('/home/pi/ThankYouDuck/camera/my_gif.GIF')
photo= open('/home/pi/thankyouduck/camera/ducky.jpg')


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
twitter.verify_credentials()

who_mention = open('/home/pi/thankyouduck/who.txt')

user_data = who_mention.readline().split(" ")
username = user_data[0]
#tweet_id = user_data[len(user_data)-1]
#status='@'+ username +'I am inflated :) '+ ''
status= 'Quack '+ '@'+ username+' '
tweet_id =open('/home/pi/thankyouduck/tweet_id.txt').readline()

twitter.update_status_with_media(media=photo,
                                 status=status,
                                 in_reply_to_status_id=tweet_id)
print "Tweet back to the user"

