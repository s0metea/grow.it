from threading import Thread
import time
#import mraa

class Pump:
    def __init__(self, pump_name):
        self.state = 0
        self.pump_name = pump_name
        print("The pump {} was initialised.".format(pump_name))
        return

    # Turn the pump on
    def set_state(self, state):
        self.state = bool(state)
        if self.state:
            Thread(target=self.run, args=()).start()
        return

    # Get the pump state
    def get_state(self):
        print("The pump {} state is: {}.".format(self.pump_name, self.state))
        return self.state

    def run(self):
        while self.state:
            print("The pump {} state is running.".format(self.pump_name))
            time.sleep(100)
        return

    def get_pump_name(self):
        return self.pump_name
