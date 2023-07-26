import RPi.GPIO as GPIO
#library to control GPIO
import time

#Set pinmode
GPIO.setmode(GPIO.BOARD) 

LED = 8

#set led initial value
GPIO.setup(LED,GPIO.OUT, initial=GPIO.LOW)

#try
try:
    while 1:
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(0.5)
        
        GPIO.output(LED,GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass
    
GPIO.cleanup()
