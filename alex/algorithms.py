import time
from motor import Motor
from ussensor import UltraSonic
import math


class Straighten:
    def __init__(self):
        global leftUS, rightUS, motors
        leftUS = UltraSonic((38,40), "sensor")
        rightUS = UltraSonic((37,35), "sensor")
        motors = Motor((26,24,19,21), "motor")

    @property
    def motors(self):
        return motors

    def getTheta(self):
        """GETS THE ROBOTS ANGLE"""
        leftDist = leftUS.sensor_detect()
        print("LEFT US: " + str(leftDist))
        rightDist = rightUS.sensor_detect()
        print("RIGHT US: " + str(rightDist))
        #totalWidth (hypotenuse) = leftUS + rightUS + robotWidth
        totalWidth = leftDist + rightDist + 6
        try:
            print (math.acos(100/totalWidth))
            return math.acos(100/totalWidth)
        except ValueError:
            return 0

    def straighten(self):
        initTheta = self.getTheta()
        motors.moveForward(100, 1)
        newTheta = self.getTheta()
        #Checks if the robot is pointed even further of course or not, corrects for whichever
        if newTheta < initTheta:
            while self.getTheta() >= 0.122:   #Spins while the robot is pointed more than 0.122 rads from straight
                motors.pivot("left",20, 1) #spin left for 1 second
        elif newTheta > initTheta:
            while self.getTheta() >= 0.122:
                motors.pivot("right", 20, 1) #spin right for 1 second

    def start(self):
        """ANGLES THE ROBOT MORE OR LESS STRAIGHT"""
        initTheta = self.getTheta()
        motors.pivot("left", 20, 1) #spin left for 1 second
        newTheta = self.getTheta()
        #Checks if the robot is pointed even further of course or not, corrects for whichever
        if newTheta < initTheta:
            while self.getTheta() >=0.122:   #Spins while the robot is pointed more than 0.122 rads from straight
                motors.pivot("left",20, 1) #spin left for 1 second
        elif newTheta > initTheta:
            while self.getTheta() >= 0.122:
                motors.pivot("right", 20, 1) #spin right for 1 second


