#!/usr/bin/env python

import cgi


def main():
	# Prints to stdout the browser-coded string to tell browser output text is HTML format
	
	print "Content-type: text/html\n\n"
	print "<html><head>"
	#print "<link rel=\"stylesheet\" href=\"dashboard.css\" type=\"text/css\">"
	print "<title>Profile</title>"
	print "<link rel='stylesheet' href='dashboard.css' type='text/css'></head><body>"
        # Receiving form arguments from seefriends.c
        # user = username currently logged in
        # friendName = username of friend whose profile is currently being viewed

        form = cgi.FieldStorage()
        user = form['user'].value.replace(" ","")
        friendName = form['friendName'].value.replace("\r","")
	friendName = friendName.replace("\n","");
	print "<div id='square'>"
        print "<center><h1>",friendName,"'s Profile</h1></center>"
        print "</div>"

        print "<fieldset>"

        print "<legend><b>Details:</b></legend>"

        i = 0

        profileLine = "N/A"
        with open("/home/2014/rfrati2/public_html/users.txt", "r") as searchFile:
		for line in searchFile:
	        # Searches users.txt for friend's profile info. Evaluates every 4 lines (i.e. only usernames)
			if i%4 == 0:
				profileLine = line.replace("\n","")
				# Loads friend's profile details into html template

				if friendName == profileLine:

        	                # Adds Username:
					print "<p><b>Username: </b>",friendName,"</p><br/>"
	
                	        # Skips Password line and adds next line as profile Name
					searchFile.next()
					profileLine = searchFile.next()
					print "<p><b>Name: </b>",profileLine,"</p><br/>"


	                      	  # Adds next line as Occupation
					profileLine = searchFile.next()
					print "<p><b>Occupation: </b>",profileLine,"</p><br/>"
        # Moves to next line
		i = i+1

	searchFile.close()
# Return button. Directs to See Friends page

        print "</fieldset><br/>"
        print "<form action='seefriends.cgi' method=\"post\">"
	print "<input type='hidden' name='user' value='",user,"'>"
        print "<input type='submit' value='Return to See Friends'>"
        print "</form>"


        print "</body></html>"
main()	
	
	
	
	
		
		
