import RPi.GPIO as gpio
from ussensor import UltraSonic
from algorithms import *
from motor import Motor
import time

gpio.setmode(gpio.BOARD)


leftMotor = Motor((26, 24))
rightMotor = Motor((19, 21))

while True:
    rightMotor.moveForward(100)


gpio.cleanup()
