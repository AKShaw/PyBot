from pins import Pins
#PIN1 = FORWARD
#PIN2 = BACKWARD

class Motors(Pins):
    def __init__(self, speed, pin1, pin2):
        super().__init__(pin1, pin2)
        self.__speed = speed

    @property
    def Speed(self):
        return self.__speed

    @Speed.setter
    def Speed(self, value):
        self.__speed = value

    def moveForward(self, pin1, speed):
        gpio.setup(pin1, gpio.OUT)
        gpio.PWM(pin1, speed)

    def moveBackwards(self, pin2, speed):
        #Move motor backwards


