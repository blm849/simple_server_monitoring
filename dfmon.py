#############################################################################
#
# dfmon.py                                    
#
# Description:
#  
#	This python program runs a df command and determines disk usage and 
#   see if the usage went above a certain threshold
#	Note: when you see the word 'disk', think 'mount point'
#
# History:
#
#       2015.08.12	Initial implementation. (BLM)
# 	    2016.09.09	Allow the user to pass a parameter
#
# Examples:
#
#       To call the program, enter: python vmstatmon.py [diskThreshold]
# 		where diskThreshold = an optional parameter. If a disk is X% used,
#		and X > diskThreshold, then the user will be informed the disk has
#       passed the threshold. If no parameter is passed, the diskThreshold
#		value is 80 as see below
#
#############################################################################

# Initialization of variables, etc.
import sys, subprocess
diskThreshold = 80
diskAtRisk = ""

# Main body of the shell script.

# If a parameter is passed and it is between 0 and 100, then assign it to diskThreshold
if len(sys.argv) == 2:
	if (int(sys.argv[1]) in range(0, 100)): 
		diskThreshold = int(sys.argv[1])

# Run the vmstat command, and capture the last line.

Cmd = "df -h"
p = subprocess.Popen(Cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for line in p.stdout.readlines():
	if line.find("%") > 0:
		dfResults = line.split()
		n = dfResults.__len__()
		m = n - 1
		mminus1 = m - 1
		mminus2 = m - 2
		diskUse = dfResults[mminus1][:-1]
		diskAvailable = dfResults[mminus2]
		if diskUse.isdigit():
			idiskUse = int(diskUse)
			if idiskUse > diskThreshold:
				mountPoint = dfResults[m]
				diskAtRisk = diskAtRisk + mountPoint + " (" + diskUse + "% / disk left " + diskAvailable + ") "		

retval = p.wait()

# Finalization  of the script and and exit.  

if diskAtRisk != "":
	print  "The following exceed the threshold(" + str(diskThreshold) + "%): " + diskAtRisk
else:
	print  "No mount points exceed the threshold(" + str(diskThreshold) + "%)"
	


