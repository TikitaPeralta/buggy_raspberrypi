'''
reading inputs:
1: GPIO.HIGH | True | 3.3V
0: GPIO.FALSE | False | 0V
'''

import warnings # pip install pytest-warnings
from time import sleep
import RPI.GPIO as GPIO

warnings.simplefilter('ignore')
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

print("r")

GPIO.setup(25, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)   # check color
GPIO.setup(27, GPIO.OUT)  # 
GPIO.setup(22, GPIO.OUT)  # 

print("1")

GPIO.output(29, True)
time.sleep(3)
GPIO.output(29, False)

print("2")

time.sleep(3)

GPIO.output(31, True)
time.sleep(3)
GPIO.output(31, False)

print("3")

time.sleep(3)

GPIO.output(32, True)
time.sleep(3)
GPIO.output(32, False)

print("4")

time.sleep(3)

GPIO.output(33, True)
time.sleep(3)
GPIO.output(33, False)

print("5")

time.sleep(3)

exit()
print("6")
