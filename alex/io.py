from motor import Motor
from ussensor import UltraSonic
import time
import math


class InputOutput:
    def __init__(self):
        self.motors = Motor((26, 24, 19, 21), "motor")
        self.leftUS = UltraSonic((38, 40), "sensor")
        self.rightUS = UltraSonic((37, 35), "sensor")

    @property
    def motors(self):
        return self.motors

    @property
    def leftUS(self):
        return self.leftUS

    @property
    def rightUS(self):
        return self.rightUS
