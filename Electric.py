from Vehicle import Vehicle
class Electric(Vehicle):

    def __init__(self, make, model,color, year,battery="",capacity=None,charging=None):
        super().__init__(make,model,color,year)
        self.battery = battery
        self.capacity = capacity
        self.charging = charging



