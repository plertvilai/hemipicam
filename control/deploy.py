#!/usr/bin/env python

from subprocess import call
from datetime import datetime
import argparse
import time

camN = 18

#get timestamp
t = datetime.now()
timestamp = '%.4d%.2d%.2d_%.2d%.2d' %(t.year,t.month,t.day,t.hour,t.minute)

parser = argparse.ArgumentParser(description = "Hemipicam start recording")
parser.add_argument("recT") #recT = record interval in seconds
parser.add_argument("waitT") #waitT = wait time between record interval in seconds
parser.add_argument("maxN") #maxN = maximum recording interval
args = parser.parse_args()

for i in range(1,camN+1):
	command = 'ssh pi@hemipicam%.2d "sudo ./hemipicam_stop.sh "' %i
	print "Execute: "+command
	call(command,shell=True)
	print "Done"

print "-------------------------------"
print 

st = time.time()
for i in range(1,camN+1):
	command = 'ssh pi@hemipicam%.2d "sudo ./hemipicam_start.sh %s %s %s %s"' %(i,args.recT,args.waitT,args.maxN,timestamp)
	print "Execute: "+command
	call(command,shell=True)
	print "Done"
	print time.time()-st