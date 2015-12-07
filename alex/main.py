from __future__ import absolute_import
import RPi.GPIO as gpio
from motor import Motor
import time

gpio.setmode(gpio.BOARD)

motors = Motor()

motors.moveForward(100)
time.sleep(5)
motors.moveBackward(100)
time.sleep(5)
motors.spinForward(80,100)
time.sleep(2.5)
motors.spinForward(100,80)
time.sleep(2.5)

gpio.cleanup()

