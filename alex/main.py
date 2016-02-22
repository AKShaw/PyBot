import RPi.GPIO as gpio
from algorithms import Straighten
import time
import atexit

gpio.setmode(gpio.BOARD)

a = Straighten()
a.start()

"""while True:
    a.straightenMove()"""

def exitHandler():
    print("Exiting")
    gpio.cleanup()

atexit.register(exitHandler)

gpio.cleanup()
