from ElectricCar import ElectricCar
from NonElectricCar import NonElectricCar
from CargoShip import CargoShip
from PassengerShip import PassengerShip
from Aeroplane import Aeroplane
from PerformSafetyCheck import PerformSafetyCheck


if __name__ == "__main__":
    car1 = ElectricCar("Tesla","Red",2023,10000,"Model S",5,"Lithium ion",100,4)
    safety_checker = PerformSafetyCheck()
    safety_checker.performSafetyCheck(car1)



    car2 = NonElectricCar("Toyota","Blue",2022,8000,"Camry",5,"Gasoline","Automatic")
    safety_checker.performSafetyCheck(car2)



    ship1 = CargoShip("Titanic", "White", 1912, 0,3000,"cranes")
    safety_checker.performSafetyCheck(ship1)

    ship2=PassengerShip("Maersk Line", "Blue", 2015, 0,20000,"cranes")
    safety_checker.performSafetyCheck(ship2)




    aeroplane = Aeroplane("Boeing", "747", 2020, 10000)
    safety_checker.performSafetyCheck(aeroplane)

    # make = input("Enter the make of the car: ")
    # color = input("Enter the color of the car: ")
    # year = int(input("Enter the year of the car: "))
    # mileage = int(input("Enter the mileage of the car: "))
    # model = input("Enter the model of the car: ")
    # no_of_seats = int(input("Enter the number of seats in the car: "))
    # engine_type = input("Enter the engine type of the car: ")
    # transmission_type = input("Enter the transmission type of the car (Automatic/Manual): ")
    #
    # non_electric_car = NonElectricCar(
    #     make=make,
    #     color=color,
    #     year=year,
    #     mileage=mileage,
    #     model=model,
    #     no_of_seats=no_of_seats,
    #     engine_type=engine_type,
    #     transmission_type=transmission_type
    # )
    # safety_checker.performSafetyCheck(non_electric_car)







# electricCar1=ElectricVehicle("Tesla Model S","Grey",2023,480,98)
# print(electricCar1.display_info())
# print(electricCar1.display_batteryCapacity())
# print(electricCar1.safetyCheck())

# nonElectricCar1=NonElectricVehicle("Ford Mustang","Black",1995, 450,"Petrol")
# print(nonElectricCar1.display_info())
# print(nonElectricCar1.display_fuelType())

#Car
# car1=Car("Audi","Grey",2023,480)
# print(car1.display_info())
# print(car1.safetyCheck())

# Ship
# ship1=Ship("Cruise","Green",2023,23000 )
# print(ship1.display_info())
# print(ship1.safetyCheck())

#Aeroplane
# aeroplane1=Aeroplane("Jet","White",2000,25000)
# print(aeroplane1.display_info())
# print(aeroplane1.safetyCheck())