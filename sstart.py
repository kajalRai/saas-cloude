#!/usr/bin/python

import os,sys,commands,time,socket,getpass


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("192.168.10.147",1234))
#receive usrename and passwd
data=s.recvfrom(100)

data1=s.recvfrom(100)

if data[0]=="root" and data1[0]=="redhat" :
	s.sendto("connect successfully !!",data[1])

else   :
	s.sendto("athuntication problem!! wrong usrename or password",data[1])
	exit()
