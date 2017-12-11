import RPi.GPIO as GPIO
from gpiozero import MotionSensor

ledGreen = 17
ledRed = 18
sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledRed, GPIO.OUT)
motion = MotionSensor(sensor)

while True:
	if motion.motion_detected:
		GPIO.output(ledGreen, GPIO.HIGH)
		GPIO.output(ledRed, GPIO.LOW)
	else:
		GPIO.output(ledGreen, GPIO.LOW)
		GPIO.output(ledRed, GPIO.HIGH)
