class Visualizaciones:
    __idM:int
    __idPeli:str
    __fecha:str
    __hora:str
    __minutos:int
    def __init__(self,idM,ideP,fecha,hora,minu):
        self.__idM=idM
        self.__idPeli=ideP
        self.__fecha=fecha
        self.__hora=hora
        self.__minutos=minu
        
    def getIdM(self):
        return self.__idM
    def getIP(self):
        return self.__idPeli
    def getFecha(self):
        return self.__fecha
    def getHora(self):
        return self.__hora
    def getMinut(self):
        return self.__minutos
    
    def __eq__(self,otro):
        return (self.__idM, self.__fecha, self.__hora) == (otro.getIdM(), otro.getFecha(), otro.getHora())
       
    def mostrarCadena(self):
           print((self.getIdM(),self.getFecha(),self.getHora()))
    
    