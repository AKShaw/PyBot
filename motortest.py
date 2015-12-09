import RPi.GPIO as gpio
from motor import Motor
import threading
import time

gpio.setmode(gpio.BOARD)

motors = Motor((26,24,19,21), "motor")

motors.moveForward(100, 3)
motors.moveBackward(100, 3)
motors.spinForward(0, 100, 3)
motors.spinForward(100, 0, 3)


gpio.cleanup()



