from __future__ import absolute_import
import RPi.GPIO as gpio


class Pins(object):
    def __init__(self, IO_pins, type):
        self.IO_pins = IO_pins
        self.type = type
        if (type=="sensor"):
            gpio.setup(self.IO_pins[0], gpio.IN)    #io_pins[0] referring to the first value in the tuple (echo)
            gpio.setup(self.IO_pins[1], gpio.OUT)   #io_pins[1] reffering to the next value in the type (trig)
        elif (type=="motor"):
            gpio.setup(self.IO_pins[0], gpio.OUT)   #io_pins[0] will be motor forward
            gpio.setup(self.IO_pins[1], gpio.OUT)   #io_pins[1] will be motor backward

            print "pins set correctly"
        elif (type=="infrared"):
            gpio.setup(self.IO_pins[0], gpio.OUT)   #io_pins[0] is the only one required by infrared sensors.