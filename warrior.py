from jugador import Jugador
# 6 puntos de daño si el oponente no 
# es vulnerable 
# 10 puntos de daño si el 
# oponente es vulnerable 

class Warrior(Jugador):

    def __init__(self):
        self.__posicion = None
        self.__nombre = "guerrero"
        self.__vulnerable = False
        self.__health = 30
        self.__danio = None
    
    def toString(self):
        return self.__nombre

    @property
    def isVulnerable(self):
        return self.__vulnerable

    @property
    def damagePoints(self):
        return self.__danio 

    @damagePoints.setter     
    def damagePoints(self, vulnerable):

        if vulnerable == 1:
            self.__danio = 10
        elif vulnerable == 0:
            self.__danio = 6
        else:
            print("dato no corresponde")

    @property
    def saludactual(self):
        return self.__health

    @saludactual.setter
    def saludactual(self, danio):
        self.__health = self.__health - danio
    