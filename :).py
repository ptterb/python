import RPi.GPIO as GPIO
import time
import pygame.mixer
from sys import exit


GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
pygame.mixer.init(44100, -16, 1, 1024)

soundA = pygame.mixer.Sound("/usr/share/sounds/alsa/quackyou.wav")

soundChannelA = pygame.mixer.Channel(1)
print "soundboard ready"

print "Fan on"
soundChannelA.play(soundA)
time.sleep(1)
