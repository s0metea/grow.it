from random import random
from threading import Thread
#import mraa
import time

class WaterLevel:
    def __init__(self, pin):
        # The sensor length in mm. By default we use 200mm sensor
        # 1 mm
        self.length = 200
        self.low = 0
        self.high = self.length
        self.step = 1
        # self.sensor = mraa.Aio(0)
        self.state = 0
        #self.state = self.sensor.readFloat()
        print("Water level sensor was initialised!")
        return

    # Get the PH state
    def get_state(self):
        print("Water level is: {}".format(self.state))
        Thread(target=self.start_measurement, args=()).start()
        return self.state

    # Method is not available for Water level sensor
    def set_state(self, state):
        return self.state

    def start_measurement(self):
        print("Water level measurement was started!")
        # self.state = self.sensor.readFloat()
        print("Water level is: {}".format(self.state))
        return
