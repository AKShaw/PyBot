import RPi.GPIO as gpio
from motor import Motor
from ussensor import UltraSonic
from algorithms import Straighten
from ioclass import InputOutput


gpio.setmode(gpio.BOARD)

motors = Motor((26, 24, 19, 21), "motor")
leftUS = UltraSonic((38, 40), "sensor")
rightUS = UltraSonic((37, 35), "sensor")

io = InputOutput(motors, leftUS, rightUS)

a = Straighten(io)
a.start()

"""while True:
    io.motors.moveForward(100, 2.5)
    a.straighten()"""

gpio.cleanup()
