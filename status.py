#!/usr/bin/env python

import cgi
print "Content-type: text/html\n\n"
print "<html><head>"
print "<title>New Status Update</title>"
print "</head><body>"

form = cgi.FieldStorage() 
currentUser = form['currentUser'].value.replace(" ","")	
	
if form.has_key('newStatus') and form['newStatus'].value != "":
		
	
	statusToSave = form['newStatus'].value
	
	print "<h1><New Status Update:", statusToSave, "</h1>"

	with open("status.txt", "a") as myFile:
		try:
			myFile.write(currentUser+" "+statusToSave+"\n")
		except EOFerror:
			print "<p>File could not be opened</p>"
		else:
			print "<p>Your status update has been logged.</p>"
	
else: 
	print "<h1>Error:</h1>"
	print "<p>Invalid message input. Try again</p>"
	


# Returns to updated Dashboard page.	
	
print "<form action=\"dashboard.py\" method=\"post\">"
print "<input type=\"hidden\" name=\"currentUser\" value=\"",currentUser,"\">"
print "<input type=\"submit\" value=\"Return\">"
print "</form>"

print "</body></html>"

	
