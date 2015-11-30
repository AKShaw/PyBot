import RPi.GPIO as gpio
from ussensor import UltraSonic
from algorithms import *
from motor import Motor
import time

gpio.setmode(gpio.BOARD)


rightMotor = Motor((24,26), "motor")
print (rightMotor)
leftMotor = Motor((21,19), "motor")
print (leftMotor)

while True:
    rightMotor.moveForward(100)
    leftMotor.moveForward2(100)