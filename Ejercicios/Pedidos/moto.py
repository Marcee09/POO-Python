class Moto:
    __Patente:str
    __Marca:str
    __nombreConductor:str
    __apellidoConductor:str
    __kilometraje:int
    def __init__(self,patente,marca,nomC,apeC,kilom):
        self.__Patente=patente
        self.__Marca=marca
        self.__nombreConductor=nomC
        self.__apellidoConductor=apeC
        self.__kilometraje=kilom
    
    def getPatente(self):
        return self.__Patente
    def getMarca(self):
        return self.__Marca
    def getNomCond(self):
        return self.__nombreConductor
    def getApeCond(self):
        return self.__apellidoConductor
    def getKilom(self):
        return self.__kilometraje
    
    def __str__(self):
        return f'Datos conductor: Apellido{self.__apellidoConductor} Nombre{self.__nombreConductor}'
    
    