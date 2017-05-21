#############################################################################
#
# testpushover.py                                    
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
#       To call the program, enter: python testpushover.py fileName sysName
#
#############################################################################

# Initialization of variables, etc.
import sys, subprocess, httplib, urllib

myTitle = "test"
myMessage = "Hello World!"
myPushoverToken = "<your pushover token>"
myPushoverUserID = "<your pushover ID>"
	

conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": myPushoverToken,
    "user": myPushoverUserID,
	"title": myTitle,
    "message": myMessage,
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()

sys.exit(0)
