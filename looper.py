#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from datetime import date, datetime

today = date.today()

reader = SimpleMFRC522()


d = today.strftime("%d%m%Y")
print(d)
filename = d+".txt"
file = open(filename,"w")
i = 0
GPIO.setup(10,GPIO.IN)
while True:
	if(GPIO.input(10)==GPIO.HIGH):
    	id, text = reader.read()
    	now = datetime.now()
    	stri = now.strftime("%H:%M:%S")
    	writ = stri + " " + text + "\n"
    	file.write(writ)
    	i = i +1
    else:
    	break

file.close()
GPIO.cleanup()

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)

gfile = drive.CreateFile({'parents': [{'id':'1Xp7xRkAywWTI6KmsT2l6_yeBMRtjUcrW'}]})

gfile.SetContentFile(filename)
gfile.Upload()
