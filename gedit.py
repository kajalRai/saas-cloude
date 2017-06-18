#!/usr/bin/python

import os,sys,commands ,socket,time
f=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
os.system('ssh root@192.168.1.117 -X gedit')
print "press YES for other services"
ch1=raw_input()
if ch1=="Yes" or ch1=="yes"  :
	execfile('saas.py')
else :
	exit()
