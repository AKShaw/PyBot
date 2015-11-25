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

leftMotor = Motor((26,24))
print (leftMotor)
rightMotor = Motor((19,21))
print (rightMotor)

while True:
    leftMotor.moveForward(100)
    rightMotor.moveForward(100)


# this is where we can repeat these and collect the statistics in an array or something
# have them interact with the algorithms class, finding out what we need to do for the motors.

gpio.cleanup()