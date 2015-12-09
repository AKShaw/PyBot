import RPi.GPIO as gpio
from motor import Motor
import threading
import time

gpio.setmode(gpio.BOARD)

motor = Motor((26,24,19,21), "motor")

motor.moveForward(100)
time.sleep(3)
motor.moveBackward(100)
time.sleep(3)
motor.spinForward(50, 100)
time.sleep(4)
motor.spinForward(100, 50)


