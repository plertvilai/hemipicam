#!/usr/bin/env python

#transfer files from local host to all hemipicam

import argparse
from subprocess import call

parser = argparse.ArgumentParser(description = "Hemipicam file upload")
parser.add_argument("local_path")
parser.add_argument("remote_path")
args = parser.parse_args()

camN = 18 #number of camera

for i in range(1,camN+1):
	command = "scp %s pi@hemipicam%.2d:%s" %(args.local_path,i,args.remote_path)
	print "Execute:"+command
	call(command,shell=True)
	print "Done"