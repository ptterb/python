import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

print "Fan off"
GPIO.output(25, GPIO.HIGH)
