import warnings # pip install pytest-warnings
from time import sleep
import RPI.GPIO as GPIO

warnings.simplefilter('ignore')

GPIO.setmode(GPIO.BOARD)

GPIO.setup(25, GPIO.IN)

'''
reading inputs:
1: GPIO.HIGH | True | 3.3V
0: GPIO.FALSE | False | 0V
'''