import math
import time
from motor import Motor
from ussensor import UltraSonic

class Straighten:
    def __init__(self):
        global motors, leftUS, rightUS
        motors = Motor((26, 24, 19, 21), "motor")
        leftUS = UltraSonic((38, 40), "sensor")
        rightUS = UltraSonic((37, 35), "sensor")

    @property
    def motors(self):
        return motors

    def getTrackWidth(self):
        motors.pivot("left", 50, 5)
        width_list = []
        for i in range(0, 20):
            right_distance = rightUS.sensor_detect()
            left_distance = leftUS.sensor_detect()
            width_list.insert(i, right_distance+left_distance+6)
            time.sleep(0.25)
        return min(width_list)

    def getTheta(self, trackWidth):
        """GETS THE ROBOTS ANGLE"""
        leftDist = leftUS.sensor_detect()
        print("LEFT US: " + str(leftDist))
        rightDist = rightUS.sensor_detect()
        print("RIGHT US: " + str(rightDist))
        #totalWidth (hypotenuse) = leftUS + rightUS + robotWidth
        totalWidth = leftDist + rightDist + 6
        try:
            print (math.acos(trackWidth/totalWidth))
            return math.acos(trackWidth/totalWidth)
        except ValueError:
            return 0

    """def straighten(self):
        """

    def start(self):
        """ANGLES THE ROBOT MORE OR LESS STRAIGHT"""
        trackWidth = self.getTrackWidth()
        print(str(trackWidth))
        initTheta = self.getTheta(trackWidth)
        motors.pivot("left", 20, 0.5) #spin left for 1 second
        print("Moved")
        newTheta = self.getTheta(trackWidth)
        #Checks if the robot is pointed even further of course or not, corrects for whichever
        if newTheta < initTheta:
            while self.getTheta(trackWidth) >=0.122:   #Spins while the robot is pointed more than 0.122 rads from straight
                motors.pivot("left", 20, 1) #spin left for 0.25 second
        elif newTheta > initTheta:
            while self.getTheta(trackWidth) >= 0.122:
                motors.pivot("right", 20, 1) #spin right for 0.25 second

