from clientes import Cliente
class Nodo:
    __cliente:Cliente
    __siguiente:None
    def __init__(self,cliente):
        self.__cliente=cliente
        self.__siguiente=None
    
    def getCliente(self):
        return self.__cliente
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,sigui):
        self.__siguiente=sigui