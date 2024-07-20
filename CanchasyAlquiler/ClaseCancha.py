class Cancha:
    __id=str
    __tipo=str
    __importe=float

    def __init__(self,id,tipo,importe):
        self.__id= id
        self.__tipo= tipo
        self.__importe= importe

    def get_id(self):
        return self.__id
    def get_tipo(self):
        return self.__tipo
    def get_importe(self):
        return self.__importe
    def __str__(self):
        return (f"Cancha: {self.__id},{self.__tipo} ,{self.__importe}")