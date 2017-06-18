#!/usr/bin/python

import os,sys,commands,time,socket,getpass

s_ip="192.168.122.1"
s_port=1234
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#telnet server username
s_usernm=raw_input("ENTER USER NAME:")
s_passwd=getpass.getpass("ENTER PASSWAORD:")

#send the username and passwd to server for login
c.sendto(s_usernm,(s_ip,s_port))
c.sendto(s_passwd,(s_ip,s_port))


data=c.recvfrom(100)
if data[0]=="connect successfully !!"  :
	print data	
	print "wait for services:"
else :  
	print data[0]
	exit()


