import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO,BCM)
GPIO.setwarnings(False)

#TRIGGER�ɰ� ECHO�� ����
TRIG = 23
ECHO = 24
print("Distance meaasurement in progress")

#TRIG�� ECHO�� ���� ���, �Է������� ����.
#TRIG�� ������ ��� ��, ECHO�� ���ƿ��� ������ �ν�
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#�ʱ⿡ trig ��ȣ 0���� ���
GPIO.output(TRIG,False)
print("Waiting for sensor to settle")
time.sleep(2)

try:
   while True:
       #�޽���ȣ�� ����� ���� trig�ɿ� 1���
       #�޽���ȣ==1 �̶�� ���� trig ����̶�� ����
       GPIO.ouput(TRIG,True)
       time.sleep(0.00001)
       GPIO.output(TRIG,False)

       while GPIO.input(ECHO) ==0:
           start = time.time()
       while GPIO.input(ECHO) == 1:
           stop = time.time()

        #echo���� �޽� ��ȣ ���� �� �ð� �� ���
       check_time = stop - start
       #������ �Ÿ� ���
       distance=check_time * 34300 / 2
       print("Distance : %.1f cm"% distance)
       #0.4�� �������� ���� ����
       time.sleep(0.4)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
       

