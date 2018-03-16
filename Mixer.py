class Mixer:
    def __init__(self):
        # By default we don't mix the water
        self.state = 0

    # Start or Stop the mixing of the water
    def set_state(self, state):
        print (state)
        self.state = state
        return

    # Get the mixer state
    def get_state(self):
        return self.state
