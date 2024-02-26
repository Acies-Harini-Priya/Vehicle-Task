from Car import Car

class ElectricCar(Car):
    def __init__(self, make, color, year, mileage, model, no_of_seats, battery_type, battery_capacity, charging_time):
        super().__init__(make, color, year, mileage, model, no_of_seats)
        self.battery_type = battery_type
        self.battery_capacity = battery_capacity
        self.charging_time = charging_time
        self.airbags = True

    def display_info(self):
        car_info = super().display_info()
        car_info += f", Battery Type: {self.battery_type}, Battery Capacity: {self.battery_capacity} Kwh, Charging Time: {self.charging_time} hrs"
        return car_info

    def safetyCheck(self):
        if self.airbags:
            return "Airbags are installed in this car."
        else:
            return "No airbags installed in this car."












# from Vehicle import Vehicle
# class ElectricCar(Vehicle):
#     def __init__(self, make, color, year, mileage,batteryType):
#         super().__init__(make, color, year, mileage)
#         self.batteryType = batteryType
#         self.airbags = True
#
#     def display_info(self):
#         info = super().display_info()
#         info += f", Battery Type: {self.batteryType}"
#         return info
#
#     def safetyCheck(self):
#         if self.airbags:
#             return "Airbags are installed in this car."
#         else:
#             return "No airbags installed in this car."







# class ElectricCar(Vehicle):
#     def __init__(self, make, color, year, mileage):
#         super().__init__(make, color, year, mileage)
#         self.airbags = True
#
#     def safetyCheck(self):
#         if self.airbags:
#             return "Airbags are installed in this car."
#         else:
#             return "No airbags installed in this car."