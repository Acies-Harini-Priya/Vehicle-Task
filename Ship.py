from Vehicle import Vehicle
class Ship(Vehicle):
    def __init__(self, make, color, year, mileage):
        super().__init__(make, color, year, mileage)
        self.lifeboat = False


