from publicacion import Publicacion

class LibroImpreso(Publicacion):
    __nombreAutor:str
    __fechaEdicion:str
    __cantPaginas:int
    def __init__(self,tit,cat,precio,nom,fecha,cantP):
        super().__init__(tit,cat,precio)
        self.__nombreAutor=nom
        self.__fechaEdicion=fecha
        self.__cantPaginas=cantP
    
    def getNomAutor(self):
        return self.__nombreAutor
    def getFechaEdicion(self):
        return self.__fechaEdicion
    def getCantPag(self):
        return self.__cantPaginas