#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


from datetime import date, datetime

today = date.today()

reader = SimpleMFRC522()


d = today.strftime("%d%m%Y")
print(d)
filename = d+".txt"
file = open(filename,"w")
i = 0
while i < 4:
    id, text = reader.read()
    now = datetime.now()
    stri = now.strftime("%H:%M:%S")
    writ = stri + " " + text + "\n"
    file.write(writ)
    i = i +1

file.close()
GPIO.cleanup()