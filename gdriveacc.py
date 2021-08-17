#!/usr/bin/env python

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

upload_file_list = ['hello.txt']

for upload_file in upload_file_list:
    gfile = drive.CreateFile({'parents': [{'id':'1Xp7xRkAywWTI6KmsT2l6_yeBMRtjUcrW'}]})

    gfile.SetContentFile(upload_file)
    gfile.Upload()

