import RPi.GPIO as gpio
from algorithms import Straighten
import time

gpio.setmode(gpio.BOARD)

a = Straighten()
a.start()

while True:
    a.straighten()
    time.sleep(2)

gpio.cleanup()
