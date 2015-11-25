import RPi.GPIO as gpio
from ussensor import UltraSonic
from motor import Motor
import time

gpio.setmode(gpio.BOARD)

#right_sensor = UltraSonic((37, 35), "sensor")     #37 is echo (in), 35 is trig (out)
#left_sensor = UltraSonic((38, 40), "sensor")      #38 is echo (in), 40 trig (out)

# loop x amount
"""while True:
    print("Left:" + str(left_sensor.sensor_detect()))
    print("Right: " + str(right_sensor.sensor_detect()))  # this would give me the distance for right sensor
    time.sleep(1)# this would give me the distance for left sensor"""

rightMotor = Motor((24,26))
print (rightMotor)
leftMotor = Motor((21,19))
print (leftMotor)

while True:
    rightMotor.moveForward(100)
    #leftMotor.moveForward(100)

# this is where we can repeat these and collect the statistics in an array or something
# have them interact with the algorithms class, finding out what we need to do for the motors.
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
gpio.cleanup()