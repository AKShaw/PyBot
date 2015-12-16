import math
import time
from motor import Motor
from ussensor import UltraSonic

class Straighten:
    def __init__(self):
        self.motors = Motor((26, 24, 19, 21), "motor")
        self.leftUS = UltraSonic((38, 40), "sensor")
        self.rightUS = UltraSonic((37, 35), "sensor")

    @property
    def motors(self):
        return self.motors

    def getTrackWidth(self):
        self.motors.pivot("left", 50, 5)
        width_list = []
        for i in range(0, 20):
            right_distance = self.rightUS.sensor_detect()
            left_distance = self.leftUS.sensor_detect()
            width_list.insert(i, right_distance+left_distance+6)
            time.sleep(0.25)
        return min(width_list)

    def getTheta(self, trackWidth):
        """GETS THE ROBOTS ANGLE"""
        leftDist = self.leftUS.sensor_detect()
        print("LEFT US: " + str(leftDist))
        rightDist = self.rightUS.sensor_detect()
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
        self.motors.pivot("left", 20, 0.5) #spin left for 1 second
        print("Moved")
        newTheta = self.getTheta(trackWidth)
        #Checks if the robot is pointed even further of course or not, corrects for whichever
        if newTheta < initTheta:
            while self.getTheta(trackWidth) >=0.122:   #Spins while the robot is pointed more than 0.122 rads from straight
                self.motors.pivot("left", 20, 1) #spin left for 0.25 second
        elif newTheta > initTheta:
            while self.getTheta(trackWidth) >= 0.122:
                self.motors.pivot("right", 20, 1) #spin right for 0.25 second

