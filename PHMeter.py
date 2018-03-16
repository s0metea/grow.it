class PHMeter:
    def __init__(self):
        self.state = 6.0
        return

    # Get the pump state
    def get_state(self):
        return self.state

    def change(self, mode, step=0.1):
        # Decrease:
        if mode == 0:
            self.state -= step
        else:
            # Increase:
            if mode == 1:
                self.state += step
        if self.state < 1:
            self.state = 1
        if self.state > 12:
            self.state = 12
        self.state = round(self.state, 2)
        print("Ph was changed to " + str(self.state))
        return self.state
