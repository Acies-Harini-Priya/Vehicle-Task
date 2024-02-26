from Ship import Ship

class PassengerShip(Ship):
    def __init__(self, make, color, year, mileage, passenger_capacity, accommodation):
        super().__init__(make, color, year, mileage)
        self.passenger_capacity = passenger_capacity
        self.accommodation = accommodation
        self.lifeboat=True

    def display_info(self):
        ship_info = super().display_info()
        ship_info += f", Passenger Capacity: {self.passenger_capacity}, Accommodation: {self.accommodation}"
        return ship_info

    def safetyCheck(self):
        if self.lifeboat:
            return "Lifeboats are available on this ship."
        else:
            return "No lifeboats available on this ship."