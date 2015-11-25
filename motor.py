from pins import Pins
import RPi.GPIO as gpio
#PIN1 = FORWARD
#PIN2 = BACKWARD

class Motor(Pins):
    def __init__(self, pins):
        super().__init__(pins, "motor")
        global motorForwardsPWM
        motorForwardsPWM = gpio.PWM(self.IO_pins[0], 100)
        global motorBackwardsPWM
        motorBackwardsPWM = gpio.PWM(self.IO_pins[1], 100)
        motorForwardsPWM.start(0)
        motorBackwardsPWM.start(0)

    def moveForward(self, speed):
        print ("Moving forwards")
        motorForwardsPWM.ChangeDutyCycle(speed)
        motorBackwardsPWM.ChangeDutyCycle(0)


    def moveBackwards(self,speed):
        print ("Moving backwards")
        motorBackwardsPWM.ChangeDutyCycle(speed)
        motorForwardsPWM.ChangeDutyCycle(0)



