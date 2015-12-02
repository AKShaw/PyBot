from __future__ import absolute_import
from alex_pins import Pins
import RPi.gpio as gpio
from Adafruit_PWM_Servo_Driver import PWM
from sgh_PCF8591P import sgh_PCF8591P
#PIN1 = FORWARD
#PIN2 = BACKWARD


class Motor(Pins):
    def __init__(self, pins):
        super(Motor, self).__init__(pins, "motor")
        global mf, mb, pwm, pcfADC
        # Initialise the PCA9685 PWM device using the default address
        pwm = PWM(0x40, debug = False)
        pwm.setPWMFreq(60)  # Set frequency to 60 Hz

        # Initalise the ADC
        pcfADC = sgh_PCF8591P(1) #i2c, 0x48)

        #use pwm on inputs so motors don't go too fast
        gpio.setup(self.IO_pins[0], gpio.OUT)
        mf = gpio.PWM(self.IO_pins[0], 100)
        mf.start(0)

        gpio.setup(self.IO_pins[1], gpio.OUT)
        mb = gpio.PWM(self.IO_pins[1], 100)
        mb.start(0)

    def moveForward(self, speed):
        mf.ChangeDutyCycle(speed)
        mb.ChangeDutyCycle(0)

    def moveBackward(self, speed):
        mb.ChangeDutyCycle(speed)
        mf.ChangeDutyCycle(0)

