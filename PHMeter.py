from random import random
from threading import Thread
#import mraa
import time


class PHMeter:
    def __init__(self):
        self.state = 7.0
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
        time.sleep(5)
        self.state = random()
        print("PH level is: {}".format(self.state))
        return
