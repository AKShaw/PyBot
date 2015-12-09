import RPi.GPIO as gpio
from motor import Motor
import threading
import time

gpio.setmode(gpio.BOARD)

motor = Motor((26,24,19,21), "motor")

motor.moveForward(50)
time.sleep(3)
motor.moveBackward(50)
time.sleep(3)
motor.spinForward(30, 60)
time.sleep(4)
motor.spinForward(60, 30)


