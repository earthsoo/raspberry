import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO,BCM)
GPIO.setwarnings(False)

#TRIGGER핀과 ECHO핀 설정
TRIG = 23
ECHO = 24
print("Distance meaasurement in progress")

#TRIG와 ECHO를 각각 출력, 입력핀으로 설정.
#TRIG가 초음파 뱉는 거, ECHO가 돌아오는 초음파 인식
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#초기에 trig 신호 0으로 출력
GPIO.output(TRIG,False)
print("Waiting for sensor to settle")
time.sleep(2)

try:
   while True:
       #펄스신호를 만들기 위해 trig핀에 1출력
       #펄스신호==1 이라는 것은 trig 출력이라는 것임
       GPIO.ouput(TRIG,True)
       time.sleep(0.00001)
       GPIO.output(TRIG,False)

       while GPIO.input(ECHO) ==0:
           start = time.time()
       while GPIO.input(ECHO) == 1:
           stop = time.time()

        #echo에서 펄스 신호 받은 거 시간 차 계산
       check_time = stop - start
       #초음파 거리 계산
       distance=check_time * 34300 / 2
       print("Distance : %.1f cm"% distance)
       #0.4초 간격으로 센서 측정
       time.sleep(0.4)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
       

