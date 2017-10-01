import RPi.GPIO as GPIO
import time
import atexit
import subprocess
def exit_handler():
	pwm.stop()
	GPIO.cleanup()
def FanOn(dutyCycle,fanTime,pwm,pwme):
	process = subprocess.Popen('/opt/vc/bin/vcgencmd measure_temp',stdout = subprocess.PIPE,shell=True)
	temp,err = process.communicate()
	temp = str(temp).replace("temp=","")
	temp = str(temp).replace("\'C\n","")
	temp = float(temp)
	start=exit = int(time.time())
	pwme.ChangeDutyCycle(dutyCycle)
	pwm.ChangeDutyCycle(dutyCycle)
	while(temp > 50):
		exit = int(time.time())
#		if (dutyCycle = 0):
#			time.sleep(300)
#		else:
		process = subprocess.Popen('/opt/vc/bin/vcgencmd measure_temp',stdout = subprocess.PIPE,shell=True)
		temp,err = process.communicate()
		temp = str(temp).replace("temp=","")
		temp = str(temp).replace("\'C\n","")
		temp = float(temp)
		if (int(exit - start) > 400):
			pwm.ChangeDutyCycle(100)
			pwme.ChangeDutyCycle(100)
		time.sleep(10)

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
pwme = GPIO.PWM(23,50)
pwm = GPIO.PWM(25,50)
pwme.start(100)
pwm.start(0)
atexit.register(exit_handler)
try:
	while 1:
		process = subprocess.Popen('/opt/vc/bin/vcgencmd measure_temp',stdout = subprocess.PIPE,shell=True)
		temp,err = process.communicate()
		temp = str(temp).replace("temp=","")
		temp = str(temp).replace("\'C\n","")
		temp = float(temp)
		if(temp<78):
			time.sleep(10)		
#	FanOn(0,10,pwm,pwme)
		else:
			FanOn(25,180,pwm,pwme)
		pwm.ChangeDutyCycle(0)
		pwme.ChangeDutyCycle(0)
finally:
	exit_handler()
