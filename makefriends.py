#!/usr/bin/env python
import cgi

def readFile():
	form = cgi.FieldStorage()
	currentUser = "NONE"
	if form.has_key('currentUser'):#get the user from form
		currentUser = form["currentUser"].value.replace(" ","")
	print "Content-Type: text/html\n\n"
	print "<html><head><title>Make Friends</title>"
	print "<link rel=\"stylesheet\" href=\"dashboard.css\" type=\"text/css\"></head>"
	print "<body>"
	print "<div id='square'>"
	print " <h1><center>Make Friends</center></h1>"
	print "</div>"
	print "<fieldset><legend><b>Grow your Froup</b></legend>"
	print "<form action=\"newfriends.py\" method=\"get\">"
	print "<table style='width:50%' align='center'>"
	print "<tr><th>USERNAME</th><th>FULL NAME</th></tr>"
	try:
		input = open("users.txt","r")
		read = input.readlines()
		i=0
		skip = 0
		for line in read:
			singleLine = line.rstrip()#remove white spaces from end
			if(i%4 == 0):#only check lines that need to be checked. for usernames
				user = singleLine
				if user == currentUser: #they cannot be friends with themselves
					skip = 1
				else:
					print "<tr><td>",user,"</td>"
					skip = 0
			if(i%4 == 2):# for checking the full names
				if skip == 0:
					print "<td>",singleLine,"<input type=\"checkbox\" name=\"",user,"\">","</td></tr><br />"
			i+=1 #move onto another line
		print "</table><br />"
		print "<input type=\"hidden\" name=\"currentUser\" value=\"",currentUser,"\">"
		print "<input type=\"submit\" value=\"Submit\">"
                print "</form>"
	except IOError, (errno, strerror):
		print "I/O error(%s): %s"%(errno, strerror)
	except:
		print "Unexpected error"
	input.close()
	print "</fieldset>"
	print "<br />"
	print "<form action=\"http://cs.mcgill.ca/~mlabra2/dashboard.py\" method=\"post\">"#goes to dashboard
	print "<input type=\"hidden\" name=\"currentUser\" value=\"",currentUser,"\">"
	print "<input type=\"submit\" value=\"Back to Dashboard!\">"
	print "</form>"
	print "</body>"
	print "</html>"
readFile()
