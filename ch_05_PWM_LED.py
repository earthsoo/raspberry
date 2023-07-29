import RPi.GPIO as GPIO
import time

#불필요한 warning 제거
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)
#PWM 인스턴스 p 만들고, 18번 핀을 PWM핀으로 설정, 주파수 = 50
p = GPIO.PWM(18,50)

p.start(0)

try:
    while 1:
        #dc값을 0에서 100까지 5만큼 증가
        for dc in range(0,101,5):
            #듀티비 변경
            p.ChangeDytyCycle(dc)
            time.sleep(0.1)
        #dc값 100에서 0까지 5만큼 감소
        for dc in range(100,-1,-5):
            #듀티비 변경
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)

except KeyboardInterrupt: #Ctrl+c 예외발생으로 열외시키기
    pass

p.stop() #pwm종료
GPIO.cleanup()
