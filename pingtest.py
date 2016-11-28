#############################################################################
#
# pingtest.py                                    
#
# Description:
#  
#	This program reads a list of IP addresses to ping from a table and then
#	pings them and outputs the result.
#
#	Note: this will not run under Windows. The ping parameters are 
#	different than Linux (where this will run), and the output is different
#	as well, you can use the HEAD or TAIL commands.
#
# History:
#
#       2015.08.11	Initial implementation. (BLM)
#       2016.09.09	Allow the user to pass the pingtable.txt as a parmeter
#
# Examples:
#
#       To call the program, enter: python pingtest.py [pingTable]
# 		where pingTable = an optional parameter contain the full filename
#		of the pingTable containing a list of IP addresses to ping.
#
#
#############################################################################

# Initialization of variables, etc.
# from subprocess import Popen, PIPE
import sys, subprocess, getopt

pingParms=' -c 5'					# Ping the IP address 5 times
pingTable='pingtable.txt'			# a table of IP addresses and other info
ipAddressesToPing = []				# a list of IP addresses 
verboseFlag = False					# False is default. True for more info.
packetLoss = ""						# All IPs with packet loss go here

# Main body of the shell script.

# If a parameter is passed then assign it to pingTable
if len(sys.argv) == 2:
	pingTable = sys.argv[1]

#Check to see if the pingTable exists and it is a text file.
try:
	f = open(pingTable)
	lines = f.readlines()
	for line in lines:
		if line[0].isdigit():
			ipAddressesToPing = ipAddressesToPing + [line.split()[0]]
except:
	print "Error trying to read " + pingTable ,
	print "Exiting."
	
# Loop through the list of ip addresses to ping and ping them.	
# Note we only capture the last result of the ping command using a combination
# of piping the results to tail and head.

for ipAddress in ipAddressesToPing:	

	pingCmd = "ping " + ipAddress + pingParms + '| tail -2 | head -1'
	p = subprocess.Popen(pingCmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	for line in p.stdout.readlines():
		if verboseFlag:
			print "Ping results for " + ipAddress + ":",
			print line,
		else:	
			pingResults = line.split()
			# If the results don't equal zero, then packet loss occurred.
			if pingResults[5] != "0%":
				packetLoss = packetLoss + ipAddress + "(" + pingResults[5] + ") "
			
	retval = p.wait()

# Finalization  of the script and and exit.  

if verboseFlag is False:
	print "Ping test complete. Pinged " + str(ipAddressesToPing.__len__()) + " ip addresses. ",
	if packetLoss != "":
		print  "Packet loss occurred for " + packetLoss
	else:
		print "No packet loss occurred."


