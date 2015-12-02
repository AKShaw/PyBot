from pins import Pins
import RPi.GPIO as gpio
#PIN1 = FORWARD
#PIN2 = BACKWARD

class Motor(Pins):
    def __init__(self, pins, type, motorForwardsPWM, motorBackwardsPWM):
        super().__init__(pins, type, motorForwardsPWM, motorBackwardsPWM)
        self.motorForwardsPWM = motorForwardsPWM
        self.motorBackwardsPWM = motorBackwardsPWM
        gpio.setup(self.IO_pins[0], gpio.OUT)
        gpio.setup(self.IO_pins[1], gpio.OUT)

        motorForwardsPWM = gpio.PWM(self.IO_pins[0], 100)
        motorBackwardsPWM = gpio.PWM(self.IO_pins[1], 100)
        motorForwardsPWM.start(0)
        motorBackwardsPWM.start(0)

    def moveForward(self, speed):
        self.motorBackwardsPWM.ChangeDutyCycle(0)
        self.motorForwardsPWM.ChangeDutyCycle(speed)

    def moveBackwards(self,speed):
        print ("Moving backwards")
        self.motorForwardsPWM.ChangeDutyCycle(0)
        self.motorBackwardsPWM.ChangeDutyCycle(speed)

"""class Motor(Pins):
    def __init__(self, motorForwardsPWM, motorBackwardsPWM, pins, type):
        super().__init__(pins, type)
        self.motorForwardsPWM = motorForwardsPWM
        self.motorBackwardsPWM = motorBackwardsPWM

    def moveForward(self, speed):
        motorForwardsPWM = gpio.PWM(self.IO_pins[0], 100)
        motorBackwardsPWM = gpio.PWM(self.IO_pins[1], 100)
        motorForwardsPWM.start(0)
        motorBackwardsPWM.start(0)
        print ("Moving forwards")
        print("DEBUG: pf = "+str(self.IO_pins[0])+" pb= "+str(self.IO_pins[1]))
        motorBackwardsPWM.ChangeDutyCycle(0)
        motorForwardsPWM.ChangeDutyCycle(speed)

    def moveBackwards(self,speed):
        print ("Moving backwards")
        motorForwardsPWM.ChangeDutyCycle(0)
        motorBackwardsPWM.ChangeDutyCycle(speed)"""