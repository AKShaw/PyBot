from pins import Pins
from time import *
import RPi.GPIO as GPIO

class UltraSonic(Pins):
    def __init__(self, pins, type):
        super().__init__(pins, type)

    def sensor_detect(self):
        gpio.output(self.IO_pins[1], True)
        time.sleep(0.00001)
        gpio.output(self.IO_pins[1], False)

        while gpio.input(self.IO_pins[0]) == 0:
            pulse_start = time.time()

        while gpio.input(self.IO_pins[0]) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        return round(distance, 2)