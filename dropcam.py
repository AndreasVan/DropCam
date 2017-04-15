#!/usr/bin/env python

from subprocess import call
import subprocess
import sys
import time
import picamera
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setwarnings(False)
GPIO_RED_LIGHT = 22
GPIO.output(GPIO_RED_LIGHT, True)
time.sleep(1)
GPIO.output(GPIO_RED_LIGHT, False)
time.sleep(1)
GPIO.output(GPIO_RED_LIGHT, True)
time.sleep(1)
GPIO.output(GPIO_RED_LIGHT, False)

timestamp=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
camera = picamera.PiCamera()
while  True:
         camera.resolution=(1024,768)
         camera.rotation=0
         camera.start_preview()
         camera.capture("/home/pi/usbdrv/" + timestamp+".jpg")
         photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/usbdrv/"+timestamp+".jpg "+timestamp+".jpg "
         call([photofile], shell=True)
         print "wait 15 minutes"
         time.sleep(900)


