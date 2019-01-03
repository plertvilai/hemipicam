#!/usr/bin/env python

import subprocess
import argparse
import glob

#use this script to delete video record files from remote host

parser = argparse.ArgumentParser(description = "Hemipicam video deleter")
parser.add_argument("timestamp")
args = parser.parse_args()

def getFileList(n,t):
	l = subprocess.check_output('ssh pi@hemipicam%.2d "ls hemipicam%.2d_%s*"'%(n,n,t),shell=True)
	return l.split('\n')[0:-1] #last element is a blank, so need to delete from the list

camN = 18
for i in range(1,camN+1):
	#fileList = glob.glob('/home/pi/hemipicam%.2d_%s*'%(i,args.timestamp)) #get all filenames
	fileList = getFileList(i,args.timestamp)
	print 'Found %d files on hemipicam%.2d' %(len(fileList),i)
	print 'Deleting...'
	for file in fileList:
		command = 'ssh pi@hemipicam%.2d "rm %s"' %(i,file)
		subprocess.call(command,shell=True)
	print 'Done'
	print 