from clientes import Cliente
class ClienteNacional(Cliente):
    __provincia:str
    __localidad:str
    __codigoPostal:int
    def __init__(self,nom,ape,email,contrasena,dire,tel,prov,loc,codP):
        super().__init__(nom,ape,email,contrasena,dire,tel)
        self.__provincia=prov
        self.__localidad=loc
        self.__codigoPostal=codP
    
    def getProvincia(self):
        return self.__provincia
    def getLocalidad(self):
        return self.__localidad
    def getCodigoPostal(self):
        return self.__codigoPostal
    