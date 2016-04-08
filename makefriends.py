import sys
import os
import stat
import cgi

def readFile():
	print "Content-type:text/html\n\n"
	print "<html><head><title>Make Friends</title></head>"
	print "<body>"
	try:
		input = open("users.txt","r")
		read = input.readlines()
		inputTuple = []
		for line in read:
			singleLine = line.rstrip()
			print singleLine
			inputTuple.append(singleLine)
	except IOError, (errno, strerror):
		print "I/O error(%s): %s"%(errno, strerror)
	except:
		print "Unexpected error"
	input.close()
	print "</body>"
	print "</html>"
readFile()
