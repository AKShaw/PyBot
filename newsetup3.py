import RPi.GPIO as gpio
import time

class Pins(object):
    def __init__(self, IO_pins, type):
        self.IO_pins = IO_pins
        if (type=="sensor"):
            gpio.setup(self.IO_pins[1], gpio.IN)  # io_pins[0] referring to the first value of the tuple e.g. pin 21 (trig)
            gpio.setup(self.IO_pins[0], gpio.OUT)  # io_pins[1] reffering to the next value we entered e.g. pin 22 (echo)
        elif (type=="motor"):
            gpio.setup(self.IO_pins[0], gpio.OUT)
            gpio.setup(self.IO_pins[1], gpio.OUT)


class UltraSonic(Pins):
    def __init__(self, pins, type):
        super().__init__(pins, type)

    def sensor_detect(self):
        gpio.output(self.IO_pins[0], True)
        time.sleep(0.00001)
        gpio.output(self.IO_pins[0], False)

        while gpio.input(self.IO_pins[1]) == 0:
            pulse_start = time.time()

        while gpio.input(self.IO_pins[1]) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        return round(distance, 2)

"""this example below is what it would appear like in a main class being called etc.
remember that we can create as many instances of the classes as we fuckin like so we dont need
to make shitty variables for each pin kek"""

gpio.setmode(gpio.BOARD)

right_sensor = UltraSonic((37, 35), "sensor")     #37 is echo (in), 35 is trig (out)
left_sensor = UltraSonic((38, 40), "sensor")      #38 is echo (in), 40 trig (out)

# loop x amount
while True:
    print(left_sensor.sensor_detect())
    print(right_sensor.sensor_detect())  # this would give me the distance for right sensor
    time.sleep(1)# this would give me the distance for left sensor

# this is where we can repeat these and collect the statistics in an array or something
# have them interact with the algorithms class, finding out what we need to do for the motors.

gpio.cleanup()