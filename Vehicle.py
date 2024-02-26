from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, make, color, year, mileage):
        self.make = make
        self.color = color
        self.year = year
        self.mileage = mileage

    def display_info(self):
        return f"Make: {self.make}, Color: {self.color}, Year: {self.year}, Mileage: {self.mileage}"

    @abstractmethod
    def safetyCheck(self):
        # return "No specific safety features implemented for this vehicle."
        pass



