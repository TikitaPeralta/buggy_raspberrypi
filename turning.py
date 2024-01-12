import warnings # pip install pytest-warnings
from time import sleep
import RPi.GPIO as GPIO

warnings.simplefilter('ignore')
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

def forward_backward(sec, right_wheel, left_wheel):
    GPIO.output(right_wheel, True)
    GPIO.output(left_wheel, True)   
    #stop
    sleep(sec)
    GPIO.output(right_wheel, False)  
    GPIO.output(left_wheel, False)  

def turn(sec, wheel):
    GPIO.output(wheel, True)
    #stop
    sleep(sec)
    GPIO.output(wheel, False)  

def go():
    print("start")
    try:
        r, l = [25, 4], [27, 22]
        GPIO.setup(r[0], GPIO.OUT)
        GPIO.setup(r[1], GPIO.OUT)   # check color
        GPIO.setup(l[0], GPIO.OUT)  # 
        GPIO.setup(l[1], GPIO.OUT)  # 
        forward_backward(4, r[0], l[0])
        forward_backward(3, r[1], l[1])
        turn(5, l[0]) # right turning
        turn(2, r[0]) # left turning
    finally:
        GPIO.cleanup()
    

go()