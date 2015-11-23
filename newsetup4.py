import RPi.GPIO as gpio
import time

class Pins(object):
    def __init__(self, IO_pins):
        self.IO_pins = IO_pins
        gpio.setup(self.IO_pins[0], gpio.IN)  # io_pins[0] referring to the first value of the tuple e.g. pin 21 (trig)
        gpio.setup(self.IO_pins[1], gpio.OUT)  # io_pins[1] reffering to the next value we entered e.g. pin 22 (echo)

class UltraSonic(Pins):
    def __init__(self, pins):
        super().__init__(pins)

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

right_sensor = UltraSonic((21, 20))
left_sensor = UltraSonic((38, 40))

# loop x amount
print(right_sensor.sensor_detect())  # this would give me the distance for right sensor.
print(left_sensor.sensor_detect())  # this would give me the distance for left sensor

# this is where we can repeat these and collect the statistics in an array or something
# have them interact with the algorithms class, finding out what we need to do for the motors.