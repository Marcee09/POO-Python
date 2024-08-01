
class Pedido:
    __patMoto:str
    __idePedido:int
    __comidaPedida:str
    __tiempoEstiEntrega:int
    __tiempoRealEntrega:int
    __precioPedido:float
    def __init__(self,pat,ide,comida,tE,tR,precio):
        self.__patMoto=pat
        self.__idePedido=ide
        self.__comidaPedida=comida
        self.__tiempoEstiEntrega=tE
        self.__tiempoRealEntrega=tR
        self.__precioPedido=precio
    
    def getPatente(self):
        return self.__patMoto
    def getIdePedido(self):
        return self.__idePedido
    def getComida(self):
        return self.__comidaPedida
    def getTiempoEst(self):
        return self.__tiempoEstiEntrega
    def getTiempoReal(self):
        return self.__tiempoRealEntrega
    def getPrecio(self):
        return self.__precioPedido
    
    def setTiempoReal(self,treal):
        self.__tiempoRealEntrega=treal
    
    def __str__(self):
        return f'Pedidos: identificador {self.__idePedido} comida {self.__comidaPedida} patente de moto: {self.__patMoto} tiempo estimado:{self.__tiempoEstiEntrega} tiempo real de entrega:{self.__tiempoRealEntrega} precio:{self.__precioPedido}'
    
  