import RPi.GPIO as GPIO
import time

#���ʿ��� warning ����
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)
#PWM �ν��Ͻ� p �����, 18�� ���� PWM������ ����, ���ļ� = 50
p = GPIO.PWM(18,50)

p.start(0)

try:
    while 1:
        #dc���� 0���� 100���� 5��ŭ ����
        for dc in range(0,101,5):
            #��Ƽ�� ����
            p.ChangeDytyCycle(dc)
            time.sleep(0.1)
        #dc�� 100���� 0���� 5��ŭ ����
        for dc in range(100,-1,-5):
            #��Ƽ�� ����
            p.ChaneDutyCycle(dc)
            time.sleep(0.1)

except KeyboardInterrupt: #Ctrl+c ���ܹ߻����� ���ܽ�Ű��
    pass

p.stop() #pwm����
GPIO.cleanup()
