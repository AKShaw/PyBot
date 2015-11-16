class Pins:
    def __init__(self, pin1, pin2):
        self.__pin1 = pin1
        self.__pin2 = pin2

    @property
    def Pin1(self):
        return self.__pin1

    @Pin1.setter
    def Pin1(self, value):
        self.__pin1 = value

    @property
    def Pin2(self):
        return self.__pin2

    @Pin2.setter
    def Pin2(self, value):
        self.__pin2 = value




