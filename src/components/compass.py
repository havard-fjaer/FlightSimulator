"""
Encapsulates how to handle the transition between 359 and 0 degrees when rotating a compass.
"""
class Compass: 
    
    def __init__(self, degrees=0):
        self.degrees = degrees
    
    def reset(self):
        self.degrees = 0

    def inc(self, interval=1, currentDegrees=None):

        if interval <= 0:
            raise ValueError("Interval must be higher than 0.")

        if interval >=360:
            raise ValueError("Interval must be 359 or lower.")

        if currentDegrees != None:
            self.degrees = currentDegrees
        
        innerDegrees = self.degrees + interval
        if innerDegrees >= 360:
            self.degrees = innerDegrees - 360
        else:
            self.degrees = innerDegrees

    def dec(self, interval=1, currentDegrees=None):

        if interval <= 0:
            raise ValueError("Interval must be higher than 0.")

        if interval >=360:
            raise ValueError("Interval must be 359 or lower.")

        if currentDegrees != None:
            self.degrees = currentDegrees
        
        innerDegrees = self.degrees - interval
        if innerDegrees < 0:
            self.degrees = innerDegrees + 360
        else:
            self.degrees = innerDegrees


            
