#Run a crontab at 8 am to fully inflate the ducky.

import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
#subprocess.call(["fswebcam", "-r","960x720","-d","/dev/video0","/home/pi/thankyouduck/camera/ducky.jpg"])
GPIO.setup(25, GPIO.OUT)

#Morning inflation
GPIO.output(25, GPIO.HIGH)
time.sleep(60)
GPIO.output(25, GPIO.LOW)
time.sleep(10)
GPIO.output(25, GPIO.HIGH)
time.sleep(60)
GPIO.output(25, GPIO.LOW)
time.sleep(10)
GPIO.output(25, GPIO.HIGH)
time.sleep(60)
GPIO.output(25, GPIO.LOW)
time.sleep(10)

