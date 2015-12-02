from pins import Pins
import RPi.GPIO as gpio
from Adafruit_PWM_Servo_Driver import PWM
from sgh_PCF8591P import sgh_PCF8591P
#PIN1 = FORWARD
#PIN2 = BACKWARD


class Motor(Pins):
    def __init__(self, pins, pinType):
        super().__init__(pins, pinType)
        global pwm, pcfADC
        # Initialise the PCA9685 PWM device using the default address
        pwm = PWM(0x40, debug = False)
        pwm.setPWMFreq(60)  # Set frequency to 60 Hz
        pcfADC = sgh_PCF8591P(1) #i2c, 0x48)

        global motorForwardsPWM
        motorForwardsPWM = gpio.PWM(self.IO_pins[0], 100)
        global motorBackwardsPWM
        motorBackwardsPWM = gpio.PWM(self.IO_pins[1], 100)
        motorForwardsPWM.start(0)
        motorBackwardsPWM.start(0)

    def moveForward(self, speed):
        print ("Moving forwards")
        motorBackwardsPWM.ChangeDutyCycle(0)
        motorForwardsPWM.ChangeDutyCycle(speed)

    def moveBackwards(self,speed):
        print ("Moving backwards")
        motorForwardsPWM.ChangeDutyCycle(0)
        motorBackwardsPWM.ChangeDutyCycle(speed)

