import warnings # pip install pytest-warnings
from time import sleep
import RPI.GPIO as GPIO

warnings.simplefilter('ignore')
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

print("start")

def wheel_direction(right, left):
    rf= right[0]
    rb = right[1]

    lf = left[0]
    lb = left[1]
    return rf, rb, lf, lb

def forward(sec, rwheel_f, lwheel_f):
    GPIO.output(rwheel_f, True)
    GPIO.output(lwheel_f, True)   
    #stop
    time.sleep(sec)
    GPIO.output(rwheel_f, False)  
    GPIO.output(lwheel_f, False)  

def backward(sec, rwheel_b, lwheel_b):
    GPIO.output(rwheel_b, True)
    GPIO.output(lwheel_b, True)   
    #stop
    time.sleep(sec)
    GPIO.output(rwheel_b, False)  
    GPIO.output(lwheel_b, False)  

def right_turn(sec, lwheel_f):
    GPIO.output(lwheel_f, True)
    #stop
    time.sleep(sec)
    GPIO.output(lwheel_f, False)  

def left_turn(sec, rwheel_f):
    GPIO.output(rwheel_f, True)
    #stop
    time.sleep(sec)
    GPIO.output(rwheel_f, False)  

def go():
    r_f, r_b, l_f, l_b = wheel_direction([25,4], [27,22])
    GPIO.setup(r_f, GPIO.OUT)
    GPIO.setup(r_b, GPIO.OUT)   # check color
    GPIO.setup(l_f, GPIO.OUT)  # 
    GPIO.setup(l_b, GPIO.OUT)  # 
    forward(4, r_f, l_f)
    backward(3, r_b, l_b)
    right_turn(5, l_f)
    left_turn(2, r_f)
    exit()

go()