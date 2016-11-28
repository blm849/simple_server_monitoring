#############################################################################
#
# processmon.py                                    
#
# Description:
#  
#	This python program runs a command to determine how many processes
#   are running.
#
# History:
#
#       2015.08.12	Initial implementation. (BLM)
#		2016.09.09	Allow the user to pass a parameter
#
# Examples:
#
#       To call the program, enter: python processmon.py processName
# 		where process = the name of the process you want to monitor 
#		(e.g. apache)
#
#############################################################################

# Initialization of variables, etc.
import sys, subprocess

# Get the parameter passed

if len(sys.argv) != 2:
	print 'To run this program, enter ' + str(sys.argv[0]) + ' processName'
	print 'Argument List:', str(sys.argv)
	sys.exit(0)
else:
	processName = sys.argv[1]

# Main body of the shell script.

# Check to see how many of the processes we are monitoring are running and tell the 
# user

Cmd = 'ps -ef | grep -v grep | grep -v processmon | grep ' + processName + ' | wc -l '
p = subprocess.Popen(Cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for line in p.stdout.readlines():
        cmdResults = line.split()[0]
	print 'Number of ' + processName + ' processes running is ' + cmdResults
retval = p.wait()

# Finalization  of the script and and exit.  


