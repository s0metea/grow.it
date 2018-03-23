class Plant:
    def __init__(self, strain, ph):
        self.strain = strain
        self.ph = ph
        self.ph_variance = 1
        return

    def get_ph(self):
        return self.ph

    def get_strain(self):
        return self.strain

    def set_ph(self, ph):
        if ph:
            self.ph += 0.1
        else:
            self.ph -= 0.1
        if self.ph < 0:
            self.ph = 0
        if self.ph > 12:
            self.ph = 12
        self.ph = round(self.ph, 2)
        print("Plant PH was set to {}".format(self.ph))
        return self.ph

    def set_strain(self, strain):
        self.strain = strain
        print("Plant strain was set to {}".format(self.strain))
        return
