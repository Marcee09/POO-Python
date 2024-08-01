class Departamento:
    __id:int
    __nomYApePropietario:str
    __numPiso:int
    __numDepto:int
    __cantHabitaciones:int
    __cantBanios:int
    __superfCubierta:float
    def __init__(self,id,nya,numP,numD,cantH,cantB,sup):
        self.__id=id
        self.__nomYApePropietario=nya
        self.__numPiso=numP
        self.__numDepto=numD
        self.__cantHabitaciones=cantH
        self.__cantBanios=cantB
        self.__superfCubierta=sup
    
    def getIdDepto(self):
        return self.__id
    def getNomProp(self):
        return self.__nomYApePropietario
    def getNumPiso(self):
        return self.__numPiso
    def getNumDpto(self):
        return self.__numDepto
    def getCantHab(self):
        return self.__cantHabitaciones
    def getCantBanios(self):
        return self.__cantBanios
    def getSupCub(self):
        return self.__superfCubierta