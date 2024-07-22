from equipos import Equipo
class Nodo:
    __equipos:Equipo
    __siguiente:None
    def __init__(self,equi):
        self.__equipos=equi
        self.__siguiente=None
    
    def getEqui(self):
        return self.__equipos
    def getSigui(self):
        return self.__siguiente
    
    def setSigui(self,sigui):
        self.__siguiente=sigui
    def setEqui(self,equi):
        self.__equipos=equi