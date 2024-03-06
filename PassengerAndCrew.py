from abc import ABC, abstractmethod
class PassengerAndCrew(ABC):
    @abstractmethod
    def setPassengerCount(self, count):
        pass

    @abstractmethod
    def getPassengerCount(self):
        pass
