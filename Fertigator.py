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
        self.state = 0

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

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = int(state)
        # Load the last state
        if self.state:
            print("Loading machine state...")
            self.load_machine_state()
            print("Done! Launching automatic mode...")
            Thread(target=self.automatic_mode, args=()).start()
        else:
            print("Saving machine state...")
            self.save_machine_state()
            self.stop_pumps()
            print("Done! Good bye!")



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
        # First goes water:
        self.water_pump.set_state(1)
        for i in range(140):
            time.sleep(0.2)
            self.water_level.state = self.water_level.state + 1
        self.water_pump.set_state(0)
        print("Water added!")
        # The second is fertilizer:
        self.fertilizer_pump.set_state(1)
        for i in range(40):
            time.sleep(0.2)
            self.water_level.state = self.water_level.state + 1
        self.fertilizer_pump.set_state(0)
        print("Fertilizer added!")

        # Now we need to mix it.
        self.mixer.set_state(1)

        # Control PH while automatic mode is enabled.
        while self.state:
            # Let us check PH
            ph = self.ph.get_state()
            time.sleep(5)
            if ph >= self.plant.ph + self.plant.ph_variance:
                # Too high PH level, need to add the acid:
                self.acid_pump.set_state(1)
                time.sleep(5)
                self.acid_pump.set_state(0)
                self.ph.state -= 0.5
                continue
            # Too low PH level, need to add the alkali:
            if ph <= self.plant.ph - self.plant.ph_variance:
                self.alkali_pump.set_state(1)
                time.sleep(5)
                self.alkali_pump.set_state(0)
                self.ph.state += 0.5
                self.water_level.state = self.water_level.state + 1
                continue
            self.mixer.set_state(0)
            self.main_container_pump_in.set_state(1)
            self.main_container_pump_out.set_state(1)
            time.sleep(5)
            self.main_container_pump_in.set_state(0)
            self.main_container_pump_out.set_state(0)
        return

    def save_machine_state(self):
        return

    def load_machine_state(self):
        return

    def stop_pumps(self):
        self.main_container_pump_in.set_state(0)
        self.main_container_pump_out.set_state(0)
        self.water_pump.set_state(0)
        self.acid_pump.set_state(0)
        self.alkali_pump.set_state(0)
        self.fertilizer_pump.set_state(0)
