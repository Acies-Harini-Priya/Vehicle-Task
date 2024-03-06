
from Car import Car
from MotorBike import MotorBike
from Ship import Ship
from Aeroplane import Aeroplane

if __name__ == "__main__":
     #Electric Car
     car1=Car("BMW","x series","Black",2015,"Lithium ion",8,4,None,None,6)
     #NonElectric Car
     car2=Car("Audi","Q7","Red",2020,"",None,None,"Petrol","Manual",8)

     # print(car1.displayInfo())
     # print(car1.safetyCheck())
     # print(car2.displayInfo())

     ship1=Ship( "Ocean Voyager","AquaQuest 2000","Navy Blue",2023,"Electric","Direct Drive",600,8)
     # print(ship1.displayInfo())
     # print(ship1.safetyCheck())

     aeroplane1=Aeroplane("Boeing","737","White",2022,"Jet","Automatic",200,200)
     # print(aeroplane1.displayInfo())
     # print(aeroplane1.safetyCheck())

     motorbike1=MotorBike("Harley-Davidson","Street Glide","Red",2018,"Lithium ion",8,4,None,None,True)
     print(motorbike1.displayInfo())
     print(motorbike1.safetyCheck())