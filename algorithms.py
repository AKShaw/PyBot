class check_sensors():
    def __init__(self, sensor_distance):
        self.sensor_distance = sensor_distance
        #sensor_distance[0] = right sensor distance
        #sensor_distance[1] = left sensor distance
        #sensor_distance[2] = center sensor distance


    """def check_front(self):
        if (self.sensor_distance[0] or self.sensor_distance[1]) < 0.15:
            return "BAD"     #not sure of BAD45, as i may implement it to do the calibration for all instances of 'BAD'
            #return "BAD45"  #BAD45 will indicate it needs a 45 degree rotation in the opposite direction based which sensor the reading came from
        else:
            return "GOOD"   #this will refer back to the main and indicate that no change in position needs to be made just yet"""

    """def check_front(self):
        if self.sensor_distance[2] < 0.15:
            #is the front sensor below 15cm?
            return "BAD_REV"
        else:
            return "GOOD"

    def check_start(self):
        if 0.15 < (self.sensor_distance[0] or self.sensor_distance[1]) < 0.45:
            self.check_front()
        else:
            self.check_front"""

    def check_start(self):
        if (self.sensor_distance[2] >= 0.15) and ((self.sensor_distance[0] or self.sensor_distance[1]) < 0.15):
            return "CALC"    #calcalate position method. using feedback from sensors
        elif (self.sensor_distance[2] < 0.15) and ((self.sensor_distance[0] or self.sensor_distance[1]) < 0.15):
            return "REV_CALC"    #reverse method, following calculate position method
        elif (self.sensor_distance[2] < 0.15) and (0.15 < (self.sensor_distance[0] or self.sensor_distance[1]) < 0.45):
            return "REV_CALC"    #reverse method only
        elif (self.sensor_distance[2] >= 0.15) and (0.15 < (self.sensor_distance[0] or self.sensor_distance[1]) < 0.45):
            return "GOOD"   #nothing needs to change, start program.
        else:
            return "CALC"   #calculate position method to get back on track
