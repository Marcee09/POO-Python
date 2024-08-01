
class Cliente:
    __nombre:str
    __apellido:str
    __email:str
    __contrasena:str
    __direccion:str
    __telefono:str
    def __init__(self,nom,ape,email,contrasena,dire,tel):
        self.__nombre=nom
        self.__apellido=ape
        self.__email=email
        self.__contrasena=contrasena
        self.__direccion=dire
        self.__telefono=tel
    
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getEmail(self):
        return self.__email
    def getContrasena(self):
        return self.__contrasena
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono