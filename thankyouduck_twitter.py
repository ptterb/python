import subprocess
from os.path import exists
import pygame.mixer
from time import sleep
from sys import exit


#initialize pygame mixer and loading sound file
pygame.mixer.init(48000, -16, 1, 1024)
soundA = pygame.mixer.Sound("/home/pi/ThankYouDuck/soundfile/lala.wav")
soundChannelA = pygame.mixer.Channel(1)
print "Soundboard Ready."


#command = "twitter replies"  # the shell command
command = "python twitter_stream.py"
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#Launch the shell command:
output = process.communicate()
#each_mentions = output[0].split("\n")
#first_mention = each_mentions[0]
first_mention = output[0]


#Create a last mention file when this code first run
if not exists('last_mention.txt'):
    create_last_mention = open('last_mention.txt','w')
    create_last_mention.write('This is last mention.txt')
    create_last_mention.close()

#open the last mention for comparison
last_mention = open('last_mention.txt')
last = last_mention.readline()

#Read the most recent mention file and save in current.txt file
current_mention = open('current.txt','w')
current_mention.write(first_mention)
current_mention.close()

current_mention = open('current.txt')
current = current_mention.readline()

#save username who mention thankyouduck
#who_mention = current.split(' ')
#username = open('who.txt','w')
#username.truncate()
#username.write(who_mention[0])
#username.close()

print "\n"
print "Start compare current and last mention"
#print "\n"
#print "Read last mention :" + last
#print "Read current mention:" + current
if current == last:
    print "Hmm...it seems like nobody mentions you at this time."

elif not current == last:
    print "Somebody mentioned you!! Let's inflate the ducky!"
    if ":)" in current or ":-)" in current or "thank" in current:

        #To get username from mention, using 'twitter replies" command here
        command2 = "twitter replies"
        process2 = subprocess.Popen(command2, stdout=subprocess.PIPE, stderr=None, shell=True)
        output2 = process2.communicate()
        username = output2[0].split(' ')
        username_txt = open ('who.txt','w')
        username_txt.write(username[0])
        username_txt.close()

        #Activate camera
        print "Taking a picture"
        subprocess.call(["fswebcam","-r","960x720","-d","/dev/video0",
                         "/home/pi/ThankYouDuck/camera/image.jpg"])
        soundChannelA.play(soundA)
        subprocess.call(["python","on.py"])
        sleep(1)

 subprocess.call(["fswebcam","-r","960x720","-d","/dev/video0",
                         "/home/pi/ThankYouDuck/camera/image1.jpg"])
        print "Tweet back to user"
        subprocess.call(["python","/home/pi/ThankYouDuck/twython-3.0.0/twython.py"])
        exit()
    elif ":(" in current:
        print "I am sad now :("
    else:
        print " No command found"

#store current to mention to last mention
current_to_last = open('last_mention.txt','w')
current_to_last.truncate()
current_to_last.write(current)
