#!/usr/bin/env python
import sys
import os
import stat
import cgi

def readFile():
	print "Content-Type: text/html\n\n"
	print "<html><head><title>Make Friends</title></head>"
	print "<body>"
	try:
		input = open("users.txt","r")
		read = input.readlines()
		inputTuple = []
		i=0
		for line in read:
			singleLine = line.rstrip()
			if(i%4 == 0):
				print "Username: ",singleLine,"<br />"
			if(i%4 == 2):
				print "Full Name: ",singleLine,"<br />"
			i+=1
			inputTuple.append(singleLine)
	except IOError, (errno, strerror):
		print "I/O error(%s): %s"%(errno, strerror)
	except:
		print "Unexpected error"
	input.close()
	print "</body>"
	print "</html>"
readFile()
