from Vehicle import Vehicle
class Aeroplane(Vehicle):
    def __init__(self, make, color, year, mileage):
        super().__init__(make, color, year, mileage)
        self.parachutes = True

    def safetyCheck(self):
        if self.parachutes:
            return "Parachutes are available on this aeroplane."
        else:
            return "No parachutes available on this aeroplane."
