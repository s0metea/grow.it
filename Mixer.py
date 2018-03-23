from threading import Thread
#import mraa
import time

class Mixer:
    def __init__(self, step_pin, direction_pin, enable_pin):
        # By default we don't mix the water
        self.state = False
        self.step_pin = step_pin
        self.direction_pin = direction_pin
        self.enable_pin = enable_pin
        self.delay_time = 10

        # self.step_gpio = mraa.Gpio(step_pin)
        # self.direction_gpio = mraa.Gpio(direction_pin)
        # self.enable_gpio = mraa.Gpio(enable_pin)
        #
        # self.step_gpio.dir(mraa.DIR_OUT)
        # self.direction_gpio.dir(mraa.DIR_OUT)
        # self.enable_gpio.dir(mraa.DIR_OUT)
        print("The mixer was initialised!")

    # Start or Stop the mixing of the water
    def set_state(self, state):
        int_state = int(state)
        if int_state == 1:
            self.state = True
        else:
            self.state = False
        print("The mixer state was changed to: {}".format(self.state))
        if self.state:
            Thread(target=self.mix, args=()).start()
        return

    # Get the mixer state
    def get_state(self):
        print("The mixer state is: {}".format(self.state))
        return self.state

    def mix(self):
        print("The mixer was started")
        # Set direction:
        # self.direction_gpio.write(1)
        # # Enable pin:
        # self.enable_gpio.write(1)
        while self.state:
            # To control stepper we should change step gpio like: 1->0->1->0...
            # self.step_gpio.write(1)
            # time.sleep(self.delay_time)
            # self.direction_gpio.write(0)
            # time.sleep(self.delay_time)
            print("The mixer did a step.")
        # Disable pins
        # self.direction_gpio.write(0)
        # self.enable_gpio.write(0)
        # self.step_gpio.write(0)
        print("The mixer was stopped.")

