import RPi.GPIO as GPIO
import time

#BCM모드로 핀 설정, 버튼 핀은 15번
BUTTON = 15;
GPIO.setmode(GPIO.BCM)

#GPIO입력으로 설정, PULLUP/PULLDOWN 설정
#이 코드는 풀다운 == BUTTON눌렀을 때(반응 있을 시에) 반응하도록 설정
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#BUTTON의 인풋이 HIGH(3.3V)일 때 반응
while 1:
	if GPIO.input(BUTTON)==GPIO.HIGH:
		print("Button pushed")
	time.sleep(1)
