from publicacion import Publicacion
class Nodo:
    __publicacion: Publicacion
    __siguiente:None
    def __init__(self,publi):
        self.__publicacion=publi
        self.__siguiente=None
    
    def getPublicacion(self):
        return self.__publicacion
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,sigui):
        self.__siguiente=sigui
        