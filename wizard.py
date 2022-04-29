#no se aplica sobrecarga ya que no se tienen dos 
#metodos llamados igual, que requieran diferentes tipos de variables
from jugador import Jugador

class Wizard(Jugador):
    
    def __init__(self):
        self.__posicion = None
        self.__nombre = None 
        self.__vulnerable = 0
        self.__puntos = 30
        self.__spell = 0
        self.__danio = 0
    
    def toString(self):
        pass 
    
    @property
    def isVulnerable(self):

        if self.__spell == 1:
            self.__vulnerable = 1
        else:
            self.__vulnerable = 0

        return self.__vulnerable

    @property
    def damagePoints(self):
        return self.__danio
 
    def damagePoints(self):

         if self.__spell == 1:
            self.__danio = 12
         else:
            self.__danio = 3

         return self.__danio
    
    @property
    def saludactual(self):
        return self.__puntos

    @saludactual.setter
    def saludactual(self, danio):
        if isinstance(danio, int):
            self.__puntos = self.__puntos - danio
            return self.__puntos
        else:
            return print("dato ingresado no corresponde")

    
    @property
    def preparespell(self):
        return self.__spell 

    @preparespell.setter
    def preparespell(self,hechizo):

        if hechizo == 0:
            self.__spell = 1
        else:
            self.__spell = 0
    