import RPi.GPIO as GPIO


class Pins:
    def __init__(self, leftMF, leftMB, rightMF, rightMB, leftUSTrig, leftUSEcho, rightUSTrig, rightUSEcho):
        self.__leftMF = leftMF
        self.__leftMB = leftMB
        self.__rightMF = rightMF
        self.__rightMB = rightMB
        self.__leftUSTrig = leftUSTrig
        self.__leftUSEcho = leftUSEcho
        self.__rightUSTrig = rightUSTrig
        self.__rightUSEcho = rightUSEcho

    @property
    def LeftMF(self):
        return self.__leftMF

    @property
    def LeftMB(self):
        return self.__leftMB

    @property
    def RightMF(self):
        return self.__rightMF

    @property
    def RightMB(self):
        return self.__rightMB

    @property
    def LeftUSTrig(self):
        return self.__leftUSTrig

    @property
    def LeftUSEcho(self):
        return self.__leftUSEcho

    @property
    def RightUSTrig(self):
        return self.__rightUSTrig

    @property
    def RightUSEcho(self):
        return self.__rightUSEcho

    def setup(self, LeftUSTrig, RightUSTrig, LeftUSEcho, RightUSEcho):
        # In: Trig
        # Out: Echo, motors
        inPins = [LeftUSTrig, RightUSTrig]
        print(inPins)
        outPins = [LeftUSEcho, RightUSEcho]
        print (outPins)
        GPIO.setmode(GPIO.BOARD)
        for i in inPins:
            GPIO.setup(i, GPIO.IN)
        for j in outPins:
            GPIO.setup(j, GPIO.OUT)
