#############################################################################
#
# pushover.py                                    
#
# Description:
#  
#	This program reads a file and sends it out via Pushover
#
# History:
#
#       2015.08.12	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python pushover.py fileName sysName

#
#############################################################################

# Initialization of variables, etc.
import sys, subprocess, httplib, urllib
myMessage = ""
myPushoverToken = "<your pushover token>"
myPushoverUserID = "<your pushover ID>"

# Get the parameters

if len(sys.argv) != 3:
	print 'To run this program, enter ' + str(sys.argv[0]) + ' filename sysName'
	print 'Argument List:', str(sys.argv)
	sys.exit(0)
else:
	inputFile = sys.argv[1]
	myTitle = sys.argv[2]
	
#print inputFile

# Main body of the shell script.

#Check to see if the pingTable exists and it is a text file.
try:
	f = open(inputFile)
	lines = f.readlines()
	for line in lines:
		myMessage = myMessage + line
	f.close()
			
except:
	myMessage = "Error reading " + inputFile

try:
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
		urllib.urlencode({
		"token": myPushoverToken,
		"user": myPushoverUserID,
		"title": myTitle,
		"message": myMessage,
	}), { "Content-type": "application/x-www-form-urlencoded" })
	conn.getresponse()
except:
	print "Errors trying to connect to the API for pushover"

sys.exit(0)