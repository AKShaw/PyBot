from __future__ import absolute_import
import RPi.GPIO as gpio
from motor import Motor
import time

gpio.setmode(gpio.BOARD)

motors = Motor()

motors.moveForward(20)
time.sleep(5)
motors.moveBackward(20)
time.sleep(5)
motors.spinForward(10,20)
time.sleep(2.5)
motors.spinForward(20,10)
time.sleep(2.5)

gpio.cleanup()

