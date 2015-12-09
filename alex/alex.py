import RPi.GPIO as gpio
from motor import Motor
import threading
import time

gpio.setmode(gpio.BOARD)

motor = Motor((26,24,19,21), "motor")

motor.moveForward(100, 5)

motor.moveBackward(100, 5)

motor.spinForward(0, 100, 4)

motor.spinForward(100, 0, 4)



