from random import random
from threading import Thread
import mraa
import time

class WaterLevel:
    def __init__(self, pin):
        # The sensor length in mm. By default we use 200mm sensor
        # 1 mm
        self.length = 200
        self.low = 0
        self.high = self.length
        self.step = 0.1
        self.sensor = mraa.Aio(pin)
        self.state = self.sensor.readFloat(),
        print("Water level sensor was initialised!")
        return

    # Get the water level:
    def get_state(self):
        print("Water level is: {}".format(self.state))
        Thread(target=self.start_measurement, args=()).start()
        return self.state

    # Method is not available for Water level sensor
    def set_state(self, state):
        return self.state

    def start_measurement(self):
        print("Water level measurement was started!")
        self.state = round(self.sensor.readFloat(), 2)
        print("Water level is: {}".format(self.state))
        return
