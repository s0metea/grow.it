class Plant:
    def __init__(self, strain, ph):
        self.strain = strain
        self.ph = ph
        return

    # Get the pump state
    def get_ph(self):
        return self.ph

    def get_strain(self):
        return self.strain

    # Get the pump state
    def set_ph(self, ph):
        self.ph = ph
        return self.ph

    def set_strain(self, strain):
        self.strain = strain
        return
