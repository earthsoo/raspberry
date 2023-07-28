import RPi.GPIO as GPIO
import time

BUTTON = 15
LED= 4

#BCM모드로 GPIO설정, BUTTON을 INPUT(PULL DOWN), LED를 OUTPUT으로
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED,GPIO.OUT)

#light의 초깃값 false
light_on = False

#callback함수, 계속 누르고 있을 때 output을 계속 출력하는 것 방지, 1번만 출력되도록
def button_callback(channel):
	global light_on #근데 갑자기 전역변수? 왜지
	
	#꺼진 상태에서만 켜고, 켜진 상태에서는 끔
	if light_on == False:  
		GPIO.output(LED,1)
		print("LED ON!")
	else:
		GPIO.output(LED,0)
		print("LED OFF!")

	#on off 상태 전환
	light_on = not light_on

#버튼의 rising감지 시 callback함수 호출, 바운스타임 설정해서 실수 방지
#바운스 타임== 아두이노의 디바운싱
GPIO.add_event_detect(BUTTON,GPIO.RISING,callback=button_callback, bouncetime=300)

while 1:
	time.sleep(0.1)
