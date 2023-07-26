import RPi.GPIO as GPIO
#library to control GPIO
import time

#Set pinmode
GPIO.setmode(GPIO.BOARD) 

LED = 8

#set led initial value
GPIO.setup(LED,GPIO.OUT, initial=GPIO.LOW)

#try구문인데, while로만 무한루프
#0.5초 간격으로 high,low벙갈아 가며 바꾸기
try:
    while 1:
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(0.5)
        
        GPIO.output(LED,GPIO.LOW)
        time.sleep(0.5)

#다음과 같은 상황은  터미널에서 모형을 돌리는 중에 Ctrl+c 를 눌렀거나
#주피터 노트북에서 모형을 놀리고 있는중에 stop을 할 때, session에서 돌아가고 있는 모형이 날라가는 것을 방지해준다
except KeyboardInterrupt:
    pass
    
GPIO.cleanup()
