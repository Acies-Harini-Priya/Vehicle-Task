from Car import Car

class NonElectricCar(Car):
    def __init__(self, make, color, year, mileage, model, no_of_seats, engine_type,transmission_type):
        super().__init__(make, color, year, mileage, model, no_of_seats)
        self.engine_type = engine_type
        self.transmission_type = transmission_type
        self.airbags = True

    def display_info(self):
        car_info = super().display_info()
        car_info += f", Engine Type: {self.engine_type}, Transmission Type: {self.transmission_type}"
        return car_info

    def safetyCheck(self):
        if self.airbags:
            return "Airbags are installed in this car."
        else:
            return "No airbags installed in this car."















# from Vehicle import Vehicle
# class NonElectricCar(Vehicle):
#     def __init__(self, make, color, year, mileage,fuelType):
#         super().__init__(make, color, year, mileage)
#         self.fuelType= fuelType
#         self.airbags = True
#
#     def display_info(self):
#         info = super().display_info()
#         info += f", Fuel Type: {self.fuelType}"
#         return info
#
#     def safetyCheck(self):
#         if self.airbags:
#             return "Airbags are installed in this car."
#         else:
#             return "No airbags installed in this car."