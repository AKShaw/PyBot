from __future__ import absolute_import
from pins import Pins
from time import *
import RPi.GPIO as gpio

class Infrared(Pins):
    def __init__(self, pins):
        super(Infrared, self).__init__(pins)

