from random import random
from threading import Thread
#import mraa
import time

class WaterLevel:
    def __init__(self):
        self.state = 0.0
        print("Water level sensor was initialised!")
        return

    # Get the PH state
    def get_state(self):
        print("Water level is: {}".format(self.state))
        Thread(target=self.start_measurement(), args=()).run()
        return self.state

    def start_measurement(self):
        print("Water level measurement was started!")
        time.sleep(5)
        self.state = random()
        print("Water level is: {}".format(self.state))
        return
