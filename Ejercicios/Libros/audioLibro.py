from publicacion import Publicacion

class AudioLibro(Publicacion):
    __tiempoRepro:int
    __nomNarrador:str
    def __init__(self,tit,cat,precio,tiempo,nomN):
        super().__init__(tit,cat,precio)
        self.__tiempoRepro=tiempo
        self.__nomNarrador=nomN
    
    def getTiempo(self):
        return self.__tiempoRepro
    def getNomNarrador(self):
        return self.__nomNarrador   