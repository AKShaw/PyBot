import RPi.GPIO as gpio
from motor import Motor
import threading
import time

gpio.setmode(gpio.BOARD)


def leftMotor():
    leftMotor = Motor((21, 19), "motor")
    while True:
        leftMotor.moveForward(100)


def rightMotor():
    rightMotor= Motor((21, 19), "motor")
    while True:
        rightMotor.moveForward(100)

lm = threading.Thread(target=leftMotor())
rm = threading.Thread(target=rightMotor())

lm.start()
rm.start()


