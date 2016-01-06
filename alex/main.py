import RPi.GPIO as gpio
from subprocess import call
from algorithms import Straighten


gpio.setmode(gpio.BOARD)

a = Straighten()
while True:
    try:
        a.start()
    except KeyboardInterrupt:
        exit()
#

"""while True:
    a.motors.moveForward(100, 2.5)
    a.straighten()"""

gpio.cleanup()
