#!/usr/bin/env python
import cgi

def addFriends():
	currentUser = "Michael"
	form = cgi.FieldStorage() #put recieved data into dictionary
	print "Content-type:text/html\n\n"
	print "<html><body>"
	for key in form:
		print key,"<br />"
	input = open("friends.txt","r")
	read = input.readlines()
	dict = {}#to store users and their friends
	for line in read:
		parse = line.split(" ")
		user = parse[0]
		parse.remove(parse[0])
		dict[user] = parse
	print dict,"<br />"
	print "</body></html>"
addFriends()	
