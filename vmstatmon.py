#############################################################################
#
# vmstatmon.py                                    
#
# Description:
#  
#	This python program runs a vmstat command and extracts key information.
# 	such as free memory, swap space use, and CPU busy
#
#
# History:
#
#       2015.08.12	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python vmstatmon.py

#
#############################################################################

# Initialization of variables, etc.
import subprocess

# Main body of the shell script.

# Run the vmstat command, and capture the last line.

Cmd = "vmstat 1 5 | tail -1"
p = subprocess.Popen(Cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for line in p.stdout.readlines():
	vmstatResults = line.split()
	runQueue = vmstatResults[0]
	freeMemory = vmstatResults[3]	# The 4th word in the string is free memory amt
	swapIn = vmstatResults[6]
	CPUavailable = vmstatResults[14]
	print "CPU idle is " + CPUavailable + "%" + ", free memory is " + freeMemory + ", run queue size is " + runQueue + ", swapping in is " + swapIn
retval = p.wait()

# Finalization  of the script and and exit.  


