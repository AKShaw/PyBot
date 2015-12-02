from pins import Pins
import RPi.GPIO as gpio
#PIN1 = FORWARD
#PIN2 = BACKWARD

class Motor(Pins):
    def __init__(self, pins, pin_type):
        super().__init__(pins, pin_type)
        global motorForwardsPWM
        motorForwardsPWM = gpio.PWM(self.IO_pins[0], 100)
        print("set")
        global motorBackwardsPWM
        motorBackwardsPWM = gpio.PWM(self.IO_pins[1], 100)
        print("set")
        motorForwardsPWM.start(0)
        motorBackwardsPWM.start(0)

    def moveForward(self, speed):
        print("start motor fowards")
        motorBackwardsPWM.ChangeDutyCycle(0)
        motorForwardsPWM.ChangeDutyCycle(speed)
        print("should have started")

    def moveBackwards(self, speed):
        print ("Moving backwards")
        motorForwardsPWM.ChangeDutyCycle(0)
        motorBackwardsPWM.ChangeDutyCycle(speed) #ijii

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