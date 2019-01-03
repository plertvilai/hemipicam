#!/usr/bin/env python

import socket
import time
import picamera
import signal
import threading
import os
import pwd
import grp
import argparse

# This script runs on the Pi to record video.


parser = argparse.ArgumentParser(description = 'HemiPiCam Record Script')
parser.add_argument("recT",type=int) #recT = record interval in seconds
parser.add_argument("waitT",type=int) #waitT = wait time between record interval in seconds
parser.add_argument("maxN",type=int) #maxN = maximum recording interval
parser.add_argument("timestamp") #timestamp from local host; format yyyymmdd_hhmm
args = parser.parse_args()


record_cv = threading.Condition()

run = True
hostname = socket.gethostname()
if hostname == 'hemipicam01':
	from gpiozero import LED


output_file = "/home/pi/%s_%s_" % (hostname, args.timestamp)


#add delay to account for deploy delay
nn = int(hostname[9:11]) #get host number
dT = (18-nn)*0.65 #0.65 is the delay time between camera execution
time.sleep(dT)




def handler(signum, frame):
	global record_cv
	global run
	global camera
	print("Got signal!")
	camera.stop_recording()
	run = False
	uid = pwd.getpwnam("pi").pw_uid
	gid = grp.getgrnam("pi").gr_gid
	os.chown(output_file, uid, gid)
signal.signal(signal.SIGINT, handler)



def recording(rt,n,filename,host):
	'''Main recording function. wt= wait time between records in seconds.
	rt = record time in seconds.
	n = file number
	filename = initialized file name for this deployment
	host = pi name''' 
	t = time.time() #get record timestamp
	name = filename + str(n) + '.h264' #filename with n iterator 

	camera = picamera.PiCamera()
	camera.resolution = (1640, 1232)
	camera.framerate = 15
	camera.awb_mode = 'sunlight'
	# camera.awb_gains = (0, 0)
	# camera.brightness = 50
	# camera.contrast = 0
	# camera.exposure_mode = 'off'

	if host == 'hemipicam01':

		led = LED(24)
		led.on()

	print("Recording")

	camera.start_recording(name, format='h264')
	camera.wait_recording(1)
	if host == 'hemipicam01':
		led.off()
	camera.wait_recording(rt)
	camera.stop_recording()
	camera.close()
	return t

#------------Main Iteration-------------------#
for n in range(args.maxN):
	t = recording(args.recT,n,output_file,hostname)
	time.sleep(args.waitT)