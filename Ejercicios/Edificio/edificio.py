from departamento import Departamento
class Edificio:
    __id:int
    __nombre:str
    __direccion:str
    __nomEmpConstructora:str
    __cantPisos:int
    __cantDepto:int
    __departamento:Departamento
    def __init__(self,id,nom,dire,nomE,cantP,cantD):
        self.__id=id
        self.__nombre=nom
        self.__direccion=dire
        self.__nomEmpConstructora=nomE
        self.__cantPisos=cantP
        self.__cantDepto=cantD
        self.__departamento=[]
    
    def getIdEdi(self):
        return self.__id
    def getNomEdi(self):
        return self.__nombre
    def getDire(self):
        return self.__direccion
    def getNomEmpC(self):
        return self.__nomEmpConstructora
    def getCantPisos(self):
        return self.__cantPisos
    def getCantDepto(self):
        return self.__cantDepto
    def getDeparta(self):
        return self.__departamento
    
    def agregarDepto(self,nuevoDepto):
        
        if isinstance(nuevoDepto, Departamento):
            self.__departamento.append(nuevoDepto)
        else:
            raise TypeError("Debe ser una instancia de la clase Departamento")
        