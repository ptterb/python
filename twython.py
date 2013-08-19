import sys
from twython import Twython
#Using oauth_1 to access personal account.
#Using oauth_2 to access an application

APP_KEY = 'zNKX8aerJVc1SkYLINQHg'
APP_SECRET='aywSxm4Un1okiDtZLg2ZjSz0WYt09azXz6i9xoXA'
OAUTH_TOKEN= '1648701380-OpdNZv2hTQEmO1zgSa5tltnabU2waoDrCNAFlb0'
OAUTH_TOEKN_SECRET='gr3iuLIVRbVIb0JBpIA2tuezfnN1oRiTLtn5pdNipg'

photo= open('/home/pi/ThankYouDuck/camera/image.jpg')
photo1= open('/home/pi/ThankYouDuck/camera/image1.jpg')

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN,OAUTH_TOEKN_SECRET)
twitter.verify_credentials()

who_mention = open('/home/pi/ThankYouDuck/who.txt')

user_data = who_mention.readline().split(" ")
username = user_data[0]

twitter.update_status_with_media(media=photo,
                                 status='Thank You '+'@'+ username +' '+ 'You are awesome! Here $








