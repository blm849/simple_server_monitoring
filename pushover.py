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
#		2017.05.21	Get the PushoverToken and UserID from an ini file
#
# Examples:
#
#       To call the program, enter: python pushover.py fileName sysName INIfile

#
#############################################################################

# Initialization of variables, etc.
import sys, subprocess, httplib, urllib
import ConfigParser
myMessage = ""
myPushoverToken = ""
myPushoverUserID = ""

# Get the parameters

if len(sys.argv) != 4:
	print 'To run this program, enter ' + str(sys.argv[0]) + ' filename sysName INIfile'
	print 'Argument List:', str(sys.argv)
	sys.exit(0)
else:
	inputFile = sys.argv[1]
	myTitle = sys.argv[2]
	myINIFile = sys.argv[3]
	
# Read the INI file
# The format of ini file is like this (minus the #). Note, no quote around the string
#[DEFAULT]
#myPushOverToken = your Pushover token string
#myPushoverUserID = your Pushover UserID string

config = ConfigParser.ConfigParser()
config.read(myINIFile)

try:
	myPushoverToken = config.get('DEFAULT', 'myPushoverToken')
	myPushoverUserID =  config.get('DEFAULT', 'myPushoverUserID')
except:
	print "An error occurred getting myPushoverToken or myPushoverUserID"
	
# If there is a problem with the token or userid, then exist
if (myPushoverToken == "") or (myPushoverUserID == ""):
	print 'Check your INI file: ' + myINIFile
	print 'Either myPushoverToken or myPushoverUserid is not properly assigned a value'
	sys.exit(0)
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