import RPi.GPIO as gpio

class Pins(object):
    def __init__(self, IO_pins, type):
        self.IO_pins = IO_pins
        if (type=="sensor"):
            gpio.setup(self.IO_pins[0], gpio.IN)  # io_pins[0] referring to the first value of the tuple e.g. pin 21 (trig)
            gpio.setup(self.IO_pins[1], gpio.OUT)  # io_pins[1] reffering to the next value we entered e.g. pin 22 (echo)
        elif (type=="motor"):
            gpio.setup(self.IO_pins[0], gpio.OUT)
            gpio.setup(self.IO_pins[1], gpio.OUT)
