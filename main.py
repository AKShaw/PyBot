import RPi.GPIO as gpio
from ussensor import UltraSonic
from algorithms import *
from motor import Motor
import time

gpio.setmode(gpio.BOARD)

right_sensor = UltraSonic((37, 35), "sensor")     #37 is echo (in), 35 is trig (out)
left_sensor = UltraSonic((38, 40), "sensor")      #38 is echo (in), 40 trig (out)
center_sensor = UltraSonic((8,8), "sensor")       #8 is echo (in) and trig (out)    #untested

#get start distances before any operation.
begin_right_distance = right_sensor.sensor_detect()
begin_left_distance = left_sensor.sensor_detect()
begin_center_distance = center_sensor.sensor_detect()

output_distances = check_sensors((begin_right_distance, begin_left_distance, begin_center_distance))
state = output_distances.check_start
#the return from this method will determine the first move of the robot.
#the state will be checked in this package. The method of movement is done in algorithms


#if distance on one of the sensors is greater than a value e.g. 75cm. call a function to rotate the robot at a specific degree
    #inside this, check whether there is anything close to the front ussensor.

#need a constant monitor on the sensors to detect the most minimal difference between values on the sensors. (this is where the array comes in useful)
#if we didnt use it, we may not be able to estimate an approximate position of the robot. If we just took a reading from one and tried to keep the robot
#to this value, it could end up having not enough room to rotate for instance.

# loop x amount
"""while True:
    print("Left:" + str(left_sensor.sensor_detect()))
    print("Right: " + str(right_sensor.sensor_detect()))  # this would give me the distance for right sensor
    time.sleep(1)# this would give me the distance for left sensor"""

#begin motor control stuff (working)
"""rightMotor = Motor((24,26))
print (rightMotor)
leftMotor = Motor((21,19))
print (leftMotor)

while True:
    rightMotor.moveForward(100)
    leftMotor.moveForward(100)"""
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