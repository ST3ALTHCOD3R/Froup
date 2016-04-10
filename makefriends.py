#!/usr/bin/env python
import cgi

def readFile():
	form = cgi.FieldStorage()
	currentUser = "NONE"
	if form.has_key('currentUser'):
		currentUser = form["currentUser"].value.replace(" ","")
	print "Content-Type: text/html\n\n"
	print "<html><head><title>Make Friends</title></head>"
	print "<body>"
	try:
		input = open("users.txt","r")
		read = input.readlines()
		i=0
		skip = 0
		print "<form action=\"newfriends.py\" method=\"get\">"
		print "USERNAME | FULL NAME<br />"
		for line in read:
			singleLine = line.rstrip()
			if(i%4 == 0):
				user = singleLine
				if user == currentUser: #they cannot be friends with themselves
					skip = 1
				else:
					print user
					skip = 0
			if(i%4 == 2):
				if skip == 0:
					print " | ",singleLine,"<input type=\"checkbox\" name=\"",user,"\">","<br />"
			i+=1
		print "<input type=\"hidden\" name=\"currentUser\" value=\"",currentUser,"\">"
		print "<input type=\"submit\" value=\"Submit\">"
                print "</form>"
	except IOError, (errno, strerror):
		print "I/O error(%s): %s"%(errno, strerror)
	except:
		print "Unexpected error"
	input.close()
	print "Or go back to the dashboard<br />"
	print "<form action=\"dashboard.py\" method=\"post\">"
	print "<input type=\"hidden\" name=\"currentUser\" value=\"",currentUser,"\">"
	print "<input type=\"submit\" value=\"Dashboard\">"
	print "</form>"
	print "</body>"
	print "</html>"
readFile()
