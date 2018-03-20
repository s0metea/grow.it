from threading import Thread
import time


class Sensor:

    def __init__(self, name):
        self.state = 0
        self.name = name
        print("The sensor \"{}\" was initialised.".format(name))
        return

    # Turn the sensor on
    def set_state(self, state):
        self.state = bool(state)
        if self.state:
            Thread(target=self.start, args=()).start()
        return

    # Get the pump state
    def get_state(self):
        print("The sensor \"{}\" state is: {}.".format(self.name, self.state))
        return self.state

    def start(self):
        while self.state:
            print("The sensor \"{}\" is busy.".format(self.name))
            time.sleep(100)
        return

    def get_sensor_name(self):
        return self.name
