import abc
from abc import ABC
class Equipo(ABC):
    __marca: str
    __modelo: str
    __anioFab: int
    __tipoComb: str
    __potencia: str
    __capCarga: int
    __tarifaAlqu: int
    __cantDias: int
    def __init__(self,marca,mod,anio,tipo,poten,capC,tarifa,cantD):
        self.__marca=marca
        self.__modelo=mod
        self.__anioFab=anio
        self.__tipoComb=tipo
        self.__potencia=poten
        self.__capCarga=capC
        self.__tarifaAlqu=tarifa
        self.__cantDias=cantD
    
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getAnioF(self):
        return self.__anioFab
    def getTipoC(self):
        return self.__tipoComb
    def getPoten(self):
        return self.__potencia
    def getCapCarga(self):
        return self.__capCarga
    def getTarifa(self):
        return self.__tarifaAlqu
    def getCantD(self):
        return self.__cantDias
    
    @abc.abstractmethod
    def tarifaAlquiler(self):
        pass