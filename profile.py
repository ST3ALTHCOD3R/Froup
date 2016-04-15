#!/user/bin/env python

import cgi


	
# Receiving form arguments from seefriends.c 
# user = username currently logged in
# friendName = username of friend whose profile is currently being viewed 
	
form = cgi.FieldStorage() 
user = form['user'].value.replace(" ","")
friendName = form['friendName'].value.replace(" ", "")
	
	
# Generates html webpage
		
print "Content-Type:text/html\n\n"
print "<html><head>"
print "<title>Profile</title></head><body>"

	

print "<div id='square'>"
print "<center><h1>",currentUser,"'s Profile:</h1></center>"
print "</div>"	
	
print "<fieldset>"
	
print "<legend><b>Details:</b></legend>"
	
i = 0
	
profileLine = "N/A"
	
searchFile = open("home/2014/rfrati2/public_html/users.txt", "r")
for line in searchFile:
		
		
	# Searches users.txt for friend's profile info. Evaluates every 4 lines (i.e. only usernames)
			
	if i%4 == 0:
			
		profileLine = line
			
			
	# Loads friend's profile details into html template

		if friendName == profileLine:
					
			# Adds Username:
			print "<p><b>Username: </b> ',profileLine,'</p><br/>"
					
			# Skips Password line and adds next line as profile Name
					
			profileLine = searchFile.readline()
			profileLine = searchFile.readline()					
			print "<p><b>Name: </b>',profileLine,'</p><br/>"
					
			
			# Adds next line as Occupation
			profileLine = searchFile.readline()
			print "<p><b>Occupation: </b>',profileLine,'</p><br/>"

				
	# Moves to next line	
	i = i+1

searchFile.close()




# Return button. Directs to See Friends page			
				
print "</fieldset><br/>"
print "<form action='seefriends.cgi'>"
print "<input type='submit' value='Return to Froup'>"
print "</form>"

	
print "</body></html>"
	
