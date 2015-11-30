import RPi.GPIO as gpio
from ussensor import UltraSonic
from algorithms import *
from motor import Motor
import time

gpio.setmode(gpio.BOARD)


rightMotor = Motor((26,24))
print (rightMotor)
leftMotor = Motor((19,21))
print (leftMotor)

rightMotor.moveForward(100)
leftMotor.moveForward(100)


gpio.cleanup()
