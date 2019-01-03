#!/usr/bin/env python

import subprocess

#use this script to ping each pi camera during deployment

camN = 18
for i in range(1,camN+1):
	print 'Hemipicam%.2d' %i
	subprocess.call('ssh -o ConnectTimeout=5 pi@hemipicam%.2d "ls"' %i, shell=True) 