import RPi.GPIO as GPIO
import time

#핀 설정
SERVO_PIN = 18
#경고메세지 안 뜨게 하기
GPIO.setwarning(False)
#BCM으로 모드 설정
GPIO.setmode(GPIO.BCM)
#출력핀으로 설정
GPIO.setup(SERVO_PIN,GPIO.OUT)
#주파수 50의 PWM으로 서보모터 핀 설정함
servo=GPIO.PWM(SERVO_PIN,50)
#듀티비 0으로 PWM시작
servo.start(0)

try:
    #듀티비 변경해서 서보모터 회전시키기
    while True:
        servo.ChangeDutyCycle(7.5) #90도
        time.sleep(1)
        servo.ChangeDutyCycle(12.5) #180도
        time.sleep(1)
        servo.ChangeDutyCycle(2.5) #0도
        time.sleep(1)

#ctrl c 누르면 멈추기
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()