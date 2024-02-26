from Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, make, color, year, mileage, model, no_of_seats):
        super().__init__(make, color, year, mileage)
        self.model = model
        self.no_of_seats = no_of_seats