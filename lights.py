import RPi.GPIO as GPIO
from gpiozero import MotionSensor
import time
import sys

ledGreen = 17
ledRed = 18
switch = 27
sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)
motion = MotionSensor(sensor)

try:
	while True:
		if (GPIO.input(switch) or motion.motion_detected):
			GPIO.output(ledGreen, GPIO.HIGH)
			GPIO.output(ledRed, GPIO.LOW)
		else:
			GPIO.output(ledGreen, GPIO.LOW)
			GPIO.output(ledRed, GPIO.HIGH)
except KeyboardInterrupt:  
    print "Bye"

except:   
	print "Other error or exception occurred!"  
  
finally:  
	GPIO.cleanup() # this ensures a clean exit  
	sys.exit()
