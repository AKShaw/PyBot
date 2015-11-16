from pins import Pins

class UltraSonic(Pins):
	def __init__(self, trig, echo):
		super().__init__(pin1, pin2)
		self.__trig = trig
		self.__echo = echo

	@property
	def trig(self):
	    return self.__trig

    @trig.setter
    def trig(self):
    	self.__trig = value

    @property
    def echo(self):
        return self._echo

    @echo.setter
    def echo(self):
    	self.__echo = value

	def US(self, trig, echo):