from threading import Thread
from Mixer import Mixer
from PHMeter import PHMeter
from Plant import Plant
from Pump import Pump
from Tank import Tank
from WaterLevel import WaterLevel
import time


class Fertigator:
    def __init__(self):
        self.state = 1

        # We have a plant:
        self.plant = Plant(strain="Tomato", ph=7)

        # Mixer to mix the components
        self.mixer = Mixer(step_pin=1, direction_pin=2, enable_pin=3)
        # PH measurements:
        self.ph = PHMeter()
        # The main tank pumps:
        self.main_container_pump_in = Pump("Main container pump (in)")
        self.main_container_pump_out = Pump("Main container pump (out)")
        self.water_level = WaterLevel()
        # The tanks with the components:
        self.main_tank = Tank(max_level=0.9,
                              water_level_sensor=self.water_level,
                              pump_in=self.main_container_pump_in,
                              pump_out=self.main_container_pump_out,
                              ph=self.ph,
                              mixer=self.mixer)

        # 4 Pumps for each of the containers:
        self.water_pump = Pump("Water pump")
        self.acid_pump = Pump("Acid pump")
        self.alkali_pump = Pump("Alkali pump")
        self.fertilizer_pump = Pump("Fertilizer pump")
        return

    # Getters for the sensors:
    def get_mixer(self):
        return self.mixer

    def get_water_level(self):
        return self.water_level

    def get_ph(self):
        return self.ph

    def get_main_tank(self):
        return self.main_tank

    def get_plant(self):
        return self.plant

    def get_state(self, state):
        return self.state

    def set_state(self, state):
        # Load the last state
        self.state = state
        if state:
            Thread(target=self.automatic_mode(), args=()).run()
        return

    def automatic_mode(self):
        water_amount = 0.35
        fertilize_amount = 0.35
        alkali_amount = 0.1
        acid_amount = 0.1
        if water_amount + fertilize_amount + alkali_amount + acid_amount > self.main_tank.max_level:
            print("Water: {} + Fertilize: {} + Alkali: {} + Acid: {} > Maximum tank level: {} ".format(water_amount,
                                                                                                       fertilize_amount,
                                                                                                       alkali_amount,
                                                                                                       acid_amount,
                                                                                                       self.main_tank.max_level))
            return
        while self.state:
            # First goes water:
            while self.water_level.get_state() < water_amount:
                self.water_pump.set_state(1)
            print("Water added!")
            time.sleep(5)

            sum = water_amount + fertilize_amount
            # The second is fertilizer:
            while self.water_level.get_state() < sum:
                self.fertilizer_pump.set_state(1)
            print("Fertilizer added!")

            # Now we need to mix it for 5 seconds!
            self.mixer.set_state(1)
            time.sleep(5)

            # Let us check PH:
            while self.ph.get_state() != self.plant.ph:
                if self.water_level.get_state() < sum:
                    # Too high PH level, need to add the acid:
                    self.acid_pump.set_state(1)
                else:
                    if self.water_level.get_state() < sum:
                        # Too low PH level, need to add the alkali:
                        self.alkali_pump.set_state(1)
            return
