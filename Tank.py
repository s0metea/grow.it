from threading import Thread
#import mraa
import time

class Tank:
    # Tank capacity = [0.0; 1.0]
    def __init__(self, max_level, water_level_sensor, pump_in, pump_out, ph, mixer):
        self.level = water_level_sensor.get_state()
        self.max_level = max_level
        self.water_level_sensor = water_level_sensor
        self.pump_in = pump_in
        self.pump_out = pump_out
        self.mixer = mixer
        self.ph = ph
        print("The main tank was completely configured!")
        return

    def get_level(self):
        return self.water_level_sensor.get_state()

    def get_max_level(self):
        return self.max_level

    # Methods to control the pumps:
    def pump_in(self, state):
        self.pump_in.set_state(state)
        return

    def pump_out(self, state):
        self.pump_out.set_state(state)
        return

    def mixer(self, state):
        self.mixer.set_state(state)
        return

    def ph(self):
        self.ph.get_state()
        return

