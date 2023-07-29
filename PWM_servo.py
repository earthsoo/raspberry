import RPi.GPIO as GPIO
import time

#�� ����
SERVO_PIN = 18
#���޼��� �� �߰� �ϱ�
GPIO.setwarning(False)
#BCM���� ��� ����
GPIO.setmode(GPIO.BCM)
#��������� ����
GPIO.setup(SERVO_PIN,GPIO.OUT)
#���ļ� 50�� PWM���� �������� �� ������
servo=GPIO.PWM(SERVO_PIN,50)
#��Ƽ�� 0���� PWM����
servo.start(0)

try:
    #��Ƽ�� �����ؼ� �������� ȸ����Ű��
    while True:
        servo.ChangeDutyCycle(7.5) #90��
        time.sleep(1)
        servo.ChangeDutyCycle(12.5) #180��
        time.sleep(1)
        servo.ChangeDutyCycle(2.5) #0��
        time.sleep(1)

#ctrl c ������ ���߱�
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()