from __future__ import absolute_import
import pi2go

#PIN1 = FORWARD
#PIN2 = BACKWARD


class Motor():
    def __init__(self):
        pi2go.init()

    def moveForward(self, speed):
        pi2go.forward(speed)

    def moveBackward(self, speed):
        pi2go.backward(speed)

    def spinForward(self, leftSpeed, rightSpeed):
        pi2go.turnForward(leftSpeed, rightSpeed)

