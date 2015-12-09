from pins import Pins
import RPi.GPIO as gpio
#PIN1 = FORWARD
#PIN2 = BACKWARD


class Motor(Pins):
    def __init__(self, pins, pinType):
        super().__init__(pins, pinType)
        global L1, L2, R1, R2
        L1 = gpio.PWM(self.IO_pins[0], 100)
        L2 = gpio.PWM(self.IO_pins[1], 100)
        R1 = gpio.PWM(self.IO_pins[2], 100)
        R2 = gpio.PWM(self.IO_pins[3], 100)

        L1.start(0)
        L2.start(0)
        R1.start(0)
        R2.start(0)

    def moveForward(self, speed):
        L1.ChangeDutyCycle(speed)
        R1.ChangeDutyCycle(speed)
        L2.ChangeDutyCycle(0)
        R2.ChangeDutyCycle(0)

        L2.ChangeFrequency(speed+5)
        R2.ChangeFrequency(speed+5)

    def moveBackward(self,speed):
        L1.ChangeDutyCycle(0)
        R1.ChangeDutyCycle(0)
        L2.ChangeDutyCycle(speed)
        R2.ChangeDutyCycle(speed)

        L1.ChangeFrequency(speed+5)
        R1.ChangeFrequency(speed+5)

    def spinForward(self, leftSpeed, rightSpeed):
        L1.ChangeDutyCycle(leftSpeed)
        R1.ChangeDutyCycle(rightSpeed)
        L2.ChangeDutyCycle(0)
        R2.ChangeDutyCycle(0)

        L2.ChangeFrequency(leftSpeed+5)
        R2.ChangeFrequency(rightSpeed+5)

