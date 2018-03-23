from random import random
from threading import Thread
import mraa
import time


class PHMeter:
    def __init__(self, pin):
        self.state = 7.0
        self.sensor = mraa.Aio(pin)
        print("PH level sensor was initialised!")
        return

    # Get the PH state
    def get_state(self):
        Thread(target=self.start_measurement(), args=()).start()
        return self.state

    # Method is not available for PH
    def set_state(self, state):
        return self.state

    def start_measurement(self):
        print("PH level measurement was started!")
        time.sleep(15)
        self.state = round(self.sensor.readFloat(), 2)
        # Debug:
        #self.state = round(self.state + random(), 1)
        print("PH level is: {}".format(self.state))
        return
