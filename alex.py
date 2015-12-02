import RPi.GPIO as gpio
from motor import Motor
import threading
import time

gpio.setmode(gpio.BOARD)


def leftMotorMethod():
    leftMotor = Motor((21, 19), "motor")
    while True:
        leftMotor.moveForward(100)


def rightMotorMethod():
    rightMotor= Motor((21, 19), "motor")
    while True:
        rightMotor.moveForward(100)

lm = threading.Thread(target=leftMotorMethod())
#rm = threading.Thread(target=rightMotorMethod())

lm.start()
#rm.start()


