#!/bin/bash

# Manual start script for starting the hemipicam system via ssh.  Do not use if 
# the init service is enabled.

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
if [ ! -f /var/lock/hemipicam ]; then
	nohup /home/pi/recordData.py $1 $2 $3 $4 > /home/pi/error.log 2>&1 &
	echo $! > /var/run/hemipicam.pid
	echo "Service started!"
	touch /var/lock/hemipicam
fi
exit