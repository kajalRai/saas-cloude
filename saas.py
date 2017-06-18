#!/usr/bin/python

import os,sys,commands ,socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#x store the manu options
x='''
press 1  for  firefox :
press 2  for  gedit :
press 3  for  VLC  :
press 4  for  ScreenShot:
press 5  for  Calculater:
press 6  for  Webcam :
press 7  for  ImageVeiwer :
'''
#ch take the input for manu
ch=raw_input(x)

if ch=='1':
	#call the file firefox.py
	execfile('firefox.py')
elif ch=='2' :
	execfile('gedit.py')
elif ch=='3' :
	execfile('vlc.py')
elif ch=='4' :
	execfile('screenshot.py')
elif ch=='5' :
	execfile('calculator.py')
elif ch=='6' :
	execfile('webcam.py')
elif ch=='7' :
	execfile('imageviewer.py')
else :
	print "you choose a wrong option:" 
	
