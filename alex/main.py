import RPi.GPIO as gpio
from motor import Motor
from ussensor import UltraSonic
import math
from  algorithms import *


def setup():
    """SETS UP BOARD, SENSORS AND MOTORS"""
    gpio.setmode(gpio.BOARD)
    global leftUS, rightUS, motors
    leftUS = UltraSonic((38,40), "sensor")
    rightUS = UltraSonic((37,45), "sensor")
    motors = Motor((26,24,19,21), "motor")

def start():
    """ANGLES THE ROBOT MORE OR LESS STRAIGHT"""
    initTheta = getTheta()
    motors.pivot("left", 20, 1) #spin left for 1 second
    newTheta = getTheta()
    #Checks if the robot is pointed even further of course or not, corrects for whichever
    if newTheta < initTheta:
        while getTheta() >=0.122:   #Spins while the robot is pointed more than 0.122 rads from straight
            motors.pivot("left",20, 1) #spin left for 1 second
    elif newTheta > initTheta:
        while getTheta() >= 0.122:
            motors.pivot("right", 20, 1) #spin right for 1 second

def getTheta():
    """GETS THE ROBOTS ANGLE"""
    leftDist = leftUS.sensor_detect()
    rightDist = rightUS.sensor_detect()
    #totalWidth (hypotenuse) = leftUS + rightUS + robotWidth
    totalWidth = leftDist + rightDist + 10
    return math.acos(100/totalWidth)


setup()
start()
gpio.cleanup()
