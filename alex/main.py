import RPi.GPIO as gpio
from motor import Motor
from algorithms import Straighten


gpio.setmode(gpio.BOARD)

a = Straighten()
a.start()

while True:
    a.motors.moveForward(100, 2.5)
    a.straighten()

gpio.cleanup()
