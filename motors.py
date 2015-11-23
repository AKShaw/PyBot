from pins import Pins
import RPi.GPIO as gpio
#PIN1 = FORWARD
#PIN2 = BACKWARD

class Motors(Pins):
    def __init__(self, pins):
        super().__init__(pins, "motor")
        self.__speed = speed
        motorForwardsPWM = gpio.PWM(self.IO_pins[0], 100)
        motorBackwardsPWM = gpio.PWM(self.IO_pins[1], 100)
        motorForwardsPWM.start(0)
        motorBackwardsPWM.start(0)

    def moveForward(self, speed):
        motorForwardsPWM.ChangeDutyCycle(speed)
        motorBackwardsPWM.ChangeDutyCycle(0)


    def moveBackwards(self,speed):
        motorBackwardsPWM.ChangeDutyCycle(speed)
        motorForwardPWM.ChangeDutyCycle(0)



