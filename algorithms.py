class check_sensors(object):
    def __init__(self, sensor_distance):
        self.sensor_distance = sensor_distance
        #sensor_distance[0] = right sensor distance
        #sensor_distance[1] = left sensor distance
        #sensor_distance[2] = center sensor distance

    u"""def check_start(self):
        if (self.sensor_distance[2] >= 0.15):
            if (self.sensor_distance[0,1] < 0.15) or (self.sensor_distance[0,1] > 0.45):        #trying to achieve checking both sensors for a case where they are outside of the ranges.
                                                                                                #dont know if this works or not though
                return "CALC"   #calcalate position method. using feedback from sensors
            elif (0.15 <= self.sensor_distance[0,1] <= 0.45):
                return "GOOD"   #nothing needs to change. start program
        elif (self.sensor_distance[2] < 0.15):
            if (self.sensor_distance[0,1] < 0.15) or (self.sensor_distance[0,1] > 0.45):
                return "REV_CALC"
            elif (0.15 <= self.sensor_distance[0,1] <= 0.45):
                return "REV"
    """

    @property
    def check_start(self):
        if self.sensor_distance[2] < 0.15:
            if (self.sensor_distance[0,1] < 0.15) or (self.sensor_distance[0,1] > 0.45):
                return u"REV_ONE" #rev_one being to only reverse on wheel, opposite one to the sensor.
            elif (0.15 <= self.sensor_distance[0,1] <= 0.45):
                return u"REV"
        else:
            if (self.sensor_distance[0,1] < 0.15) or (self.sensor_distance[0,1] > 0.45):        #trying to achieve checking both sensors for a case where they are outside of the ranges.
                                                                                                #dont know if this works or not though
                return u"CALC"   #calcalate position method. using feedback from sensors
            elif 0.15 <= self.sensor_distance[0, 1] <= 0.45:
                return u"GOOD"   #nothing needs to change. start program