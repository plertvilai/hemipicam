#!/usr/bin/env python

import subprocess
import argparse

#use this script to delete video record files from remote host

parser = argparse.ArgumentParser(description = "Hemipicam video deleter")
parser.add_argument("timestamp")
args = parser.parse_args()


camN = 18
for i in range(1,camN+1):
	print "Hemipicam%.2d" %i
	t = args.timestamp
	subprocess.call('ssh -o ConnectTimeout=5 pi@hemipicam%.2d "ls hemipicam%.2d_%s* -l"'%(i,i,t),shell=True)
	print 