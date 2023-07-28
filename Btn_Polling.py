import RPi.GPIO as GPIO
import time

BUTTON = 15;
GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while 1:
	if GPIO.input(BUTTON)==GPIO.HIGH:
		print("Button pushed")
	time.sleep(1)
