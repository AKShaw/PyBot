import RPi.GPIO as gpio
from ussensor import UltraSonic
from algorithms import *
from motor import Motor
import time

gpio.setmode(gpio.BOARD)


rightMotor = Motor((24,26))
print (rightMotor)
leftMotor = Motor((19,21))
print (leftMotor)

while True:
    leftMotor.moveForward(100)
    rightMotor.moveForward(100)
