import RPi.GPIO as GPIO
import time

BUTTON = 15
LED= 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED,GPIO.OUT)

light_on = False
def button_callback(channel):
	global light_on
	if light_on == False:
		GPIO.output(LED,1)
		print("LED ON!")
		
	else:
		GPIO.output(LED,0)
		print("LED OFF!")
	light_on = not light_on
	
GPIO.add_event_detect(BUTTON,GPIO.RISING,callback=button_callback, bouncetime=300)

while 1:
	time.sleep(0.1)
