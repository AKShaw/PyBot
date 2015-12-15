import RPi.GPIO as gpio
from algorithms import Straighten
from io import InputOutput


gpio.setmode(gpio.BOARD)
io = InputOutput()

a = Straighten(io)
a.start()

"""while True:
    io.motors.moveForward(100, 2.5)
    a.straighten()"""

gpio.cleanup()
