import RPi.GPIO as gpio

from algorithms import Straighten


gpio.setmode(gpio.BOARD)

a = Straighten()
a.start()

while True:
    a.straighten()

gpio.cleanup()
