from Electric import Electric
from NonElectric import NonElectric
import json

class Car(Electric, NonElectric):
    def __init__(self,make,model,color,year,battery="",capacity=None,charging=None,engine="",transmission="",airbags=None):
        if battery !="":
            Electric.__init__(self,make,model,color,year,battery,capacity,charging)
        elif engine !="":
            NonElectric.__init__(self,make,model,color,year,engine,transmission)
        else:
            raise ValueError("Either battery_capacity or fuel_type must be provided for Car.")
        self.airbags = airbags

    def safetyCheck(self):
        if self.airbags >= 6:
            return "Yes enough airbags are available."
        else:
            return "No"

    def displayInfo(self):
        if hasattr(self, 'battery') and self.battery != "":
            output ={
                "Company": self.make,
                "Type": "Electrical",
                "Battery":{
                    "BatteryType":self.battery,
                    "BatteryCapacity":f"{self.capacity} kwh",
                    "BatteryChargingTime":f"{self.charging} hrs"
                },
                "Color": self.color,
                "Model": self.model
            }
            return json.dumps(output,indent=4)
        else:
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

