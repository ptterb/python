import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setup(25, GPIO.OUT)

while True:
	GPIO.output(25, GPIO.HIGH) 
	time.sleep(1) # I want to turn the pin off after "20sec"
	              # How to use the time function in python?
	GPIO.output(25, GPIO.LOW) 
	time.sleep(1)