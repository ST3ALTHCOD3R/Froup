#!/usr/bin/env python
import cgi

def addFriends():
	currentUser = "imalonelysoul12"
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

	form = cgi.FieldStorage() #put recieved data into dictionary
	friendsChosen = []#stores friends chosen in a list
	for tok in form:
		tok = tok.replace(" ","")
		friendsChosen.append(tok)
	print "START",dict,"<br />"
	if currentUser in dict: #if user already has friends in database
		for user in friendsChosen:
			if user not in dict[currentUser]: #if friend is unique
				dict[currentUser].append(user)
				dict[user].append(currentUser) #friendship goes both ways
	else: #user does not have any friends yet
		dict[currentUser] = friendsChosen #add all chosen users to be friends
		for friend in friendsChosen: #user is a friend to the ones he/she chose
			dict[friend].append(currentUser)
	print "FINISH",dict
	print "</body></html>"
addFriends()	
