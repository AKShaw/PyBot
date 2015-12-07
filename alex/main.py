from __future__ import absolute_import
import RPi.GPIO as gpio
from motor import Motor
import time

gpio.setmode(gpio.BOARD)

#rightMotor = Motor((24,26))
leftMotor = Motor((21, 19))

while True:
    #rightMotor.moveForward(100)
    leftMotor.moveForward(100)