import RPi.GPIO as gpio
from ussensor import UltraSonic
from algorithms import *
from motor import Motor
import time

gpio.setmode(gpio.BOARD)


rightMotor = Motor((24,26))
print (rightMotor)
leftMotor = Motor((21,19))
print (leftMotor)

while True:
    rightMotor.moveForward(100)
    leftMotor.moveForward(100)