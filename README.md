# simple_server_monitoring
Really simple server monitoring software for Linux systems

## How it works
I have found that I usually need to monitor the same things on servers. 
Specifically, I need to keep track of 
1. Disk usage
2. System performance
3. Network connectivity
4. Specific processes

Of course there are lots of things that could be monitored, but I find these four are a 
minimum for ensuring my Linux servers stay up and running.

## The Python Scripts

To perform those 4 monitoring tasks, I wrote these 4 simple python scripts: 

1. dfmon.py: Checks on disk usage
2. vmstatmon.py: Monitors system performance
3. pingtest.py: Check on the availability of IP addresses. Needs the pingtable.txt to run
4. processmon.py: Monitors specific processes

The python scripts are straightforward. They run a command, process the
results, and send the results to standard out (STDOUT). Each script has a more detailed
description of how they work in a comment at the beginning of the code.

## The Shell Scripts

Combined with the python scripts are some very simple shell scripts. For this repo, I have
included two of these shell scripts: prod1.sh and prod1a.sh. 

1.	prod1.sh: this script runs all four python scripts and sends the output to an output 
file. You can see an example of such a file here (prod1mon.txt).
2.	prod1a.sh: this script takes the output of prod1.sh and calls a python script called
pushover.py.

## The reporting scripts
In addition to the 4 python scripts below, there are some additional scripts.
1.	pushover.py: this script works with the Pushover service to send the output from prod1.sh
to users of the Pushover app. You can find out more about Pushover here: https://pushover.net/
Essentially I use the Pushover API to send the monitoring results from the Linux system
to my mobile device that is running the Pushover app. 
2.	testpushover.py: this script is a way of testing that you have connectivity from the 
Linux system to the Pushover service.

To call these scripts, enter: python pushover.py or python testpushover.py

## Some design notes
One of the advantages to this approach is that I can have different scripts for 
different systems. For example, I could have 2 servers: PROD1 and PROD2. On PROD1, I could
have a prod1.sh script that calls the 4 python monitoring scripts with one set of 
parameters, while on PROD2 I could have a prod2.sh script that calls the 4 python monitoring
scripts with different parameters. 
Likewise, on PROD1.sh, I could have a script just for one group that just monitors 
their processes and tells them if it is up or down. 
It's easy to combine the scripts in different ways to get the monitoring you want.
In addition, because the scripts are simple, it is easy to create different versions of 
them to monitor in different ways.

## The crontab entry
To automate the reporting, you want to set up a cron table entry, like this

00 9-21 * * * /home/bernie/prod1.sh /home/bernie && /home/bernie/prod1a.sh

Every hour between 9 a.m. and 9 p.m. the prod1.sh script is run with one parameter, /home/bernie
Then prod1a.sh is called right after it. 

P.S. prod1a.sh could be improved: I leave this as an exercise for the reader. :)
