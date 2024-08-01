
class Publicacion:
    __titulo:str
    __categoria:str
    __precioBase:str
    def __init__(self,tit,cat,precio):
        self.__titulo=tit
        self.__categoria=cat
        self.__precioBase=precio
    
    def getTitulo(self):
        return self.__titulo
    def getCategoria(self):
        return self.__categoria
    def getPrecioBase(self):
        return self.__precioBase