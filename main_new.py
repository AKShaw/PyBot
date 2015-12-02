import RPi.GPIO as gpio
from ussensor import UltraSonic
from algorithms import *
from motor_new import Motor
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

rightMotor = Motor((24,26), "motor")
leftMotor = Motor((21,19), "motor")


rightMotor.moveForward(100)
leftMotor.moveForward(100)#sdf
#end motor control stuff (working)

# this is where we can repeat these and collect the statistics in an array or something
# have them interact with the algorithms class, finding out what we need to do for the motors.

#code below obtains 10 pulses of distance from both
#ultrasonic sensors and stores the vals in an array (working)
"""right_list = []
left_list = []
for i in range(0, 9):
    right_distance = right_sensor.sensor_detect()
    left_distance = left_sensor.sensor_detect()
    right_list.insert(i, right_distance)
    left_list.insert(i, left_distance)

t = tuple(right_list)
t1 = tuple(left_list)
print(t)
print(t1)"""
#working

gpio.cleanup()