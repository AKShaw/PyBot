import RPi.GPIO as gpio
from ussensor import UltraSonic
from algorithms import *
from motor import Motor
import time

gpio.setmode(gpio.BOARD)


leftMotor = Motor((26, 24))
print(rightMotor)
rightMotor = Motor((19, 21))
print(leftMotor)

while True:
    rightMotor.moveForward(100)


gpio.cleanup()
