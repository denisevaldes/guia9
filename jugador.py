from abc import abstractmethod
from abc import ABCMeta

class Jugador(metaclass = ABCMeta):
    
    @abstractmethod
    def toString():
        pass 

    @abstractmethod
    def isVulnerable(self):
        pass

    @abstractmethod
    def damagePoints(self):
        pass

    @abstractmethod
    def saludactual(self):
        pass