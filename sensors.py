import RPi.GPIO as GPIO
from gpiozero import MotionSensor
import sys, time, logging, requests

ledGreen = 17
ledRed = 18
switch = 27
sensor = 4
openhab_host = "192.168.10.13"
openhab_port = "8080"

stateSensor = 0
stateSwitch = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)
motion = MotionSensor(sensor)

def post_command(item, command):
	# Post a command to OpenHAB
	url = 'http://%s:%s/rest/items/%s'%(openhab_host, openhab_port, item)
	req = requests.post(url, data=command)
	if req.status_code != requests.codes.ok:
		req.raise_for_status()

def main():
	global stateSensor
	global stateSwitch
	while True:
		if GPIO.input(switch):
			if (stateSwitch == 0):
				post_command("GPIO_SwitchDoor", "ON")
				GPIO.output(ledRed, GPIO.HIGH)
			stateSwitch = 1
		else:
			if (stateSwitch == 1):
				post_command("GPIO_SwitchDoor", "OFF")
				GPIO.output(ledRed, GPIO.LOW)
			stateSwitch = 0
		if motion.motion_detected:
			if (stateSensor == 0):
				post_command("GPIO_MotionSensor", "ON")
				GPIO.output(ledGreen, GPIO.HIGH)
			stateSensor = 1
		else:
			if (stateSensor == 1):
				post_command("GPIO_MotionSensor", "OFF")
				GPIO.output(ledGreen, GPIO.LOW)
			stateSensor = 0

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print "Bye"
	except:
		print "Error or exception occurred!"
	finally:
		GPIO.cleanup()
		sys.exit()
