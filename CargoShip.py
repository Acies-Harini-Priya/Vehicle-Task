from Ship import Ship

class CargoShip(Ship):
    def __init__(self, make, color, year, mileage, cargo_capacity, cargo_handling_equipment):
        super().__init__(make, color, year, mileage)
        self.cargo_capacity = cargo_capacity
        self.cargo_handling_equipment = cargo_handling_equipment
        self.lifeboat=False

    def display_info(self):
        ship_info = super().display_info()
        ship_info += f", Cargo Capacity: {self.cargo_capacity}, Cargo Handling Equipment: {self.cargo_handling_equipment}"
        return ship_info

    def safetyCheck(self):
        if self.lifeboat:
            return "Lifeboats are available on this ship."
        else:
            return "No lifeboats available on this ship."



