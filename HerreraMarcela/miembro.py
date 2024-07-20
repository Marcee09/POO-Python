class Miembro:
    __idMiembro:int
    __apeYNom:str
    __correo:str
    def __init__(self,id,apyn,correo):
        self.__idMiembro=id
        self.__apeYNom=apyn
        self.__correo=correo
    
    def getid(self):
        return self.__idMiembro
    def getAyN(self):
        return self.__apeYNom
    def getCorreo(self):
        return self.__correo
    