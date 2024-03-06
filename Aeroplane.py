from NonElectric import NonElectric
from PassengerAndCrew import PassengerAndCrew
import json

class Aeroplane(PassengerAndCrew,NonElectric):
    def __init__(self,make,model,color,year,engine="",transmission="",passenger_count=None,lifejackets=None):
        NonElectric.__init__(self,make,model,color,year,engine,transmission)

        self.passenger_count = passenger_count
        self.lifejackets = lifejackets
    def safetyCheck(self):
        if self.lifejackets == self.passenger_count:
            return "Yes enough lifejackets are available."
        else:
            return "No, Atleast {} lifejackets are required.".format(self.passenger_count)
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