import RPi.GPIO as GPIO
import time
import pygame.mixer
from sys import exit

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
pygame.mixer.init(44100, -16, 1, 1024)

soundA = pygame.mixer.Sound("/usr/share/sounds/alsa/quackyou.wav")


print "first quack"
GPIO.output(25, GPIO.LOW)
time.sleep(3)

print "Fan off"
GPIO.output(25, GPIO.HIGH)
time.sleep(1)
