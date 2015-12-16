import time
import math


class InputOutput:
    def __init__(self, motors, leftUS, rightUS):
        self.motors = motors
        self.leftUS = leftUS
        self.rightUS = rightUS


    @property
    def motors(self):
        return self.motors

    @property
    def leftUS(self):
        return self.leftUS

    @property
    def rightUS(self):
        return self.rightUS
