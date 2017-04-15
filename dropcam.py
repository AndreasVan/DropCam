
#!/usr/bin/env python

from subprocess import call
import subprocess
import sys
import time
import picamera
import datetime
timestamp=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
camera = picamera.PiCamera()
while  True:
         camera.resolution=(1024,768)
         camera.rotation=0
         camera.start_preview()
         camera.capture(timestamp+".jpg")

         photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/usbdrv/"+timestamp+".jpg "+timestamp+".jpg "
         call([photofile], shell=True)
         print "wait 15 minutes"
         time.sleep(900)


