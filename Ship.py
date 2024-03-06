from NonElectric import NonElectric
from PassengerAndCrew import PassengerAndCrew
import json

class Ship(PassengerAndCrew,NonElectric):
    def __init__(self,make,model,color,year,engine="",transmission="",passenger_count=None,lifeboats=None):
        NonElectric.__init__(self,make,model,color,year,engine,transmission)

        self.passenger_count = passenger_count
        self.lifeboats = lifeboats
    def safetyCheck(self):
        if self.lifeboats >= (self.passenger_count/6):
            return "Yes enough lifeboats are available."
        else:
            return "No, Atleast {} lifeboats are required.".format(int(self.passenger_count/6))
    def displayInfo(self):

        output = {
                "Company": self.make,
                "Type": "Non Electrical",
                "Engine": {
                    "EngineType": self.engine,
                    "TransmissionType": f"{self.transmission}",
                },
                "Color": self.color,
                "Model": self.model
        }
        return json.dumps(output, indent=4)

    def setPassengerCount(self, count):
        self.passenger_count = count

    def getPassengerCount(self):
        return self.passenger_count