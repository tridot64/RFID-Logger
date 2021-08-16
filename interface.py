#!/usr/bin/env python

#  This is the setup file for the python interface and to intialize
#  Activities for each rfid.

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

print("RFID Activity logger setup")

print("Activities can be generalized (example: Leisure, Innovationg, misc etc.)")

temp = 0
stringData = []
print("Hit enter if no more activities are left!")
while (temp != ""):
    stri = "Enter activity name: " 
    temp = input(stri)
    stringData.append(temp)

stringData.pop()
reader = SimpleMFRC522()

for i in stringData:
    text = i
    print("Place unwritten tag for ", text)
    reader.write(text)
    print("Written")
    time.sleep(3)

GPIO.cleanup()