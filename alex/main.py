import RPi.GPIO as gpio

from algorithms import Straighten


gpio.setmode(gpio.BOARD)

a = Straighten()
a.start()
a.straighten()

gpio.cleanup()
