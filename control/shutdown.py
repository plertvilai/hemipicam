from subprocess import call

camN = 18

for i in range(camN):
	command = 'ssh -o ConnectTimeout=5 pi@hemipicam%.2d "sudo shutdown -h now"' %(i+1)
	call(command,shell=True)