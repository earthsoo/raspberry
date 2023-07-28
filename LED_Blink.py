#-*- coding:utf-8-*-

#GPIO라이브러리 불러오기
import RPi.GPIO as GPIO
import time

#4번핀으로 LED설정
led_pin = 4

#GPIO 핀을 사용할 때, 때로는 하드웨어에 대한 문제가 발생하거나 잘못된 동작이 발생할 수 있는데 이러한 상황에서 발생하 경고 메시지를 비활성화 해줌
GPIO.setwarnings(False)

#GPIO 핀번호 설정, LED핀을 출력핀으로 지정
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

#ON OFF 10회 반복
for i in range(10):
	GPIO.output(led_pin,1)
	time.sleep(1)
	GPIO.output(led_pin, 0)
	time.sleep(1)

#GPIO 모드 세팅 초기화 -->하드웨어적인 문제방지
GPIO.cleanup()
