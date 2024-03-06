from Vehicle import Vehicle
class NonElectric(Vehicle):
    def __init__(self,make, model,color, year,engine="",transmission=""):
        super().__init__(make,model,color,year)
        self.engine = engine
        self.transmission = transmission