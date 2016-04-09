#!/usr/bin/env python
import cgi

def writeBack(toWrite): #dictionary that needs to be copied to file
	output = open("friends.txt","w")
	for user in toWrite:
		output.write(user)
		for friend in toWrite[user]:
			output.write(" "+friend)
		output.write('\n')
	output.close()

def addFriends():
	currentUser = "Mark"
	changesMade = 0
	input = open("friends.txt","r")
        read = input.readlines()
        dict = {}#to store users and their friends
	print "Content-type:text/html\n\n"
        print "<html><body>"
        for line in read:
		line = line.replace("\n", "")
                parse = line.split(" ")
                user = parse[0]
                parse.remove(parse[0])
                dict[user] = parse
	input.close()
	form = cgi.FieldStorage() #put recieved data into dictionary
	friendsChosen = []#stores friends chosen in a list
	for tok in form:
		tok = tok.replace(" ","")
		friendsChosen.append(tok)
	#print "START",dict,"<br />"
	if currentUser in dict: #if user already has friends in database
		for friend in friendsChosen:
			if friend not in dict[currentUser]: #if friend is unique
				dict[currentUser].append(friend)
				#dict[friend].append(currentUser) #friendship goes both ways
				changesMade = 1
	else: #user does not have any friends yet
		dict[currentUser] = friendsChosen #add all chosen users to be friends
		#for friend in friendsChosen: #user is a friend to the ones he/she chose
			#dict[friend].append(currentUser)
		changesMade = 1
	#print "FINISH",dict
	if changesMade == 1: #to now waste rewriting the same thing
		writeBack(dict)#write to file updated friends
	print "Success! Changes(if any) have been made to your account!<br />"
	print "<form action=\"login.html\">"
	print "Go back to dashboard<input type=\"submit\" value=\"Dashboard\">"
	print "</form>"
	print "</body></html>"
addFriends()	
