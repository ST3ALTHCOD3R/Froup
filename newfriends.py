#!/usr/bin/env python
import cgi

def addFriends():
	form = cgi.FieldStorage() #put recieved data into dictionary
	print "Content-type:text/html\n\n"
	print "<html><body>"
	for key in form:
		print key,"<br />"
	print "</body></html>"
addFriends()	
