from pins import Pins
from time import *
import RPi GPIO as GPIO

class UltraSonic(Pins):
	def __init__(self, trig, echo):
		super().__init__(trig, echo)
		self.__trig = trig
		self.__echo = echo

	@property
	def trig(self):
	    return self.__trig

    @trig.setter
    def trig(self, value):
    	self.__trig = value

    @property
    def echo(self):
        return self.__echo

    @echo.setter
    def echo(self, value):
    	self.__echo = value

	def US(self, trig, echo):
        GPIO.output(trig, True)
		time.sleep(0.00001)
		GPIO.output(trig, False)

		while GPIO.input(echo)==0:
		  pulse_start = time.time()

		while GPIO.input(echo)==1:
		  pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start

		distance = pulse_duration * 17150

		return round(distance, 2)