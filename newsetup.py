import RPi.GPIO as gpio
import time

class Pins(object):
    def __init__(self, pin_in, pin_out):
        self.pin_in = pin_in
        self.pin_out = pin_out

    """def setup(self, LeftUSTrig, RightUSTrig, LeftUSEcho, RightUSEcho):
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
            GPIO.setup(j, GPIO.OUT)"""
    #the stuff ive commented out above wont work in a class. it might be useful to setup the whole
    #board in the main class when we want everything set up.
    #so we really only need this stuff below rn. maybe im wrong idfk lel

    def pin_setup(self, pin_in, pin_out):
        gpio.setmode(gpio.BOARD)
        gpio.setup(pin_in, gpio.IN)
        gpio.setup(pin_out, gpio.OUT)
        return

class UltraSonic(Pins):
    def __init__(self, offset, trig, echo):
        self.offset = offset
        super(UltraSonic, self).__init__(trig, echo)

    def sensor_detect(self):
        gpio.output(self.pin_in, True)
        time.sleep(0.00001)
        gpio.output(self.pin_in, False)

        while gpio.input(self.pin_out) == 0:
            pulse_start = time.time()

        while gpio.input(self.pin_out) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        return round(distance, 2)
