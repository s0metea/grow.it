class Pump:
    def __init__(self):
        self.state = 0
        return

    # Turn the pump on
    def on(self):
        self.state = 1
        return

    # Turn the pump off
    def off(self):
        self.state = 0
        return

    # Get the pump state
    def get_state(self):
        return self.state
