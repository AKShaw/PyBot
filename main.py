import RPi.GPIO as GPIO
from pins import Pins
import time


p = Pins(0, 0, 0, 0, 21, 20, 38, 40)
p.setup(p.LeftUSTrig, p.RightUSTrig, p.LeftUSEcho, p.RightUSEcho)

def US(Trig, Echo):
    GPIO.output(Trig, False)
    #print "Waiting For Sensor To Settle"
    time.sleep(0.5)

    GPIO.output(Trig, True)
    time.sleep(0.00001)
    GPIO.output(Trig, False)

    while GPIO.input(Echo)==0:
      pulse_start = time.time()

    while GPIO.input(Echo)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    return round(distance, 2)


while True:
    print ("Left: " + str(US(p.LeftUSTrig, p.LeftUSEcho)))
    print ("Right: " + str(US(p.RightUSTrig, p.RightUSEcho)))
