class Tank:
    # Tank capacity = [0.0; 1.0]
    def __init__(self):
        self.level = 0.0
        return

    # Fill the tank
    def fill(self):
        self.level = 1.0
        return

    # Pour out the tank
    def pour_out(self):
        self.level = 0.0
        return

    def get_level(self):
        return self.level

