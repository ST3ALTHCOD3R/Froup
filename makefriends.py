#!/usr/bin/env python
import cgi

def readFile():
	print "Content-Type: text/html\n\n"
	print "<html><head><title>Make Friends</title></head>"
	print "<body>"
	try:
		input = open("users.txt","r")
		read = input.readlines()
		i=0
		print "<form action=\"newfriends.py\" method=\"get\">"
		print "USERNAME | FULL NAME<br />"
		for line in read:
			singleLine = line.rstrip()
			if(i%4 == 0):
				user = singleLine
				print user
			if(i%4 == 2):
				print " | ",singleLine,"<input type=\"checkbox\" name=\"",user,"\">","<br />"
			i+=1
		print "<input type=\"submit\" value=\"Submit\">"
                print "</form>"
	except IOError, (errno, strerror):
		print "I/O error(%s): %s"%(errno, strerror)
	except:
		print "Unexpected error"
	input.close()
	print "</body>"
	print "</html>"
readFile()
