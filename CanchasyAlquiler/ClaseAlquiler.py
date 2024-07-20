class Alquiler:
    __nombre_persona=str
    __id=str
    __HoraMinutos=str
    __duracion=int
    
    def __init__(self,nombrePersona,id,HoraM,duracion):
        self.__nombre_persona= nombrePersona
        self.__id= id
        self.__HoraMinutos= HoraM
        self.__duracion= duracion

    def get_nombre(self):
        return self.__nombre_persona
    def get_id(self):
        return self.__id
    def get_HorasMinutos(self):
        return self.__HoraMinutos
    def get_duracion(self):
        return self.__duracion
    def __gt__(self,otro):
        return self.__HoraMinutos > otro.get_HorasMinutos()
    
    def __str__(self):
        return (f"Alquiler: {self.__nombre_persona},{self.__id},{self.__HoraMinutos},{self.__duracion}")
    