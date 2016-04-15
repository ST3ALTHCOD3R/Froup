#!/usr/bin/env python

import cgi


def main():
	# Prints to stdout the browser-coded string to tell browser output text is HTML format
	
	print "Content-type: text/html\n\n"
	print "<html><head>"
	print "<title>Dashboard</title>"
	print "<link rel=\"stylesheet\" href=\"dashboard.css\" type=\"text/css\">"
	print "</head><body>"
	
	# Parse query from Robert's Welcome Landing CGI or login.c
	currentUser = "None"
	form = cgi.FieldStorage() 
	
	if form.has_key('currentUser') and form['currentUser'].value != "":
		currentUser = form['currentUser'].value.replace(" ","")
	else: 
		print "<h1>Error! please enter valid UserName!</h1>"
		print "</body></html>"

	print "<div id=\"square\">"
        print "<center><h1>", currentUser,"'s Dashboard</h1></center>"
	print "</div>"	
	
	# User Status Updates:

	print "<h2>Status Updates:</h2><br />"
	
	
	# Searches and displays user's most recent post in the status.txt history file.
	# If no post is found "N/A" is displayed
	
	lastStatus = "N/A"
	with open("status.txt", "r") as searchFile:
		for line in searchFile:
			name = line.split(" ")
			if currentUser in name[0]:
				lastStatus= name[1:-1]#line.split(None,1)[1]
				lastStatus.append(name[-1])
	lastStatus = ' '.join(lastStatus)
	print "<p>Your latest status: ",lastStatus,"</p>"	
	print "<br />"
	
	# Posting a new Status update:
	print "<form action=\"status.py\" method=\"post\">"
	
	print "Status Update: <input type=\"text\" name=\"newStatus\" maxLength=\"100\" > "
	print "<input type=\"hidden\" name=\"currentUser\" value=\"",currentUser,"\">"
	print "<input type=\"submit\" value=\"Post\">"
	print "</form>"
	
	# Menu - Contains Make Friends, See Friends, and Logout buttons
	
	print "<fieldset>"
	
	print "<legend><b>Menu</b></legend>"
	
	print "<form action=\"http://cs.mcgill.ca/~rfrati2/makefriends.py\" method=\"post\">"
	print "<input type=\"hidden\" name=\"currentUser\" value=\"",currentUser,"\"> <br />"
	print "<input type=\"submit\" value=\"Make Friends!\">"
	print "</form><br />"
	
	print "<form action=\"seefriends.cgi\" method=\"post\">"
	print "<input type=\"hidden\" name=\"user\" value=\"",currentUser,"\"> <br />"
	print "<input type=\"submit\" value=\"See Friends!\">"
	print "</form><br />"
	
	# Logout button
	print "<form action=\"http://cs.mcgill.ca/~rfrati2/index.html\">"
	print "<input type=\"submit\" value=\"Logout\">"
	print "</form>"
	
	print "</fieldset><br />"
	
	# Friends Recent Status Updates:
	
	# Parses friends.txt file for list of user's friends. If none exist, the message
	# "You have no friends yet" is displayed instead of friend status updates. 
	
	allFriends="None"
	friendList = []
	
	# Extracts existing friends list from friends.txt:
	
	with open("../../../2014/rfrati2/public_html/friends.txt", "r") as searchFile:
		for line in searchFile:
			name = line.split(" ")
			if currentUser == name[0]:
				allFriends = line #.split(None,1)[1]
				break
	if allFriends == "None":
		print "<h3>Your Froup: None #foreveralone. Try making some friends!</h3>"
	else:
		print "<h3>Your Froup:", allFriends, "</h3><br>"

	print "<form><fieldset>"
	print "<legend><b>Recent Statuses:</b></legend>"
		
	updates = []
	if allFriends !="None":

		#for # All lines of status.txt, if line contains any of usernames in friendList[]
		# or currentUser, print in fieldset. 
                with open("status.txt", "r") as searchFile:
                        for line in searchFile:
				name = line.split(" ")
                                if name[0] in allFriends:
					name[-1] = name[-1].rstrip()
                                	updates.append(name)		
	else: #only will see their own updates
		with open("status.txt", "r") as searchFile:
                        for line in searchFile:
                                name = line.split(" ")
                                if name[0] == currentUser:
                                        name[-1] = name[-1].rstrip()
                                        updates.append(name)
	for i in range(1,21):
		for word in updates[-i]:
			print word
		print "<br />"
	print "</fieldset></form>"	
	print "</body></html>"
	
main()	
	
	
	
	
		
		
