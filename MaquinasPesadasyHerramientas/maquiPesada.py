from equipos import Equipo

class MaquiPesada(Equipo):
    __tipo: str
    __peso: int
    def __init__(self,marca,mod,anio,tipo,poten,capC,tarifa,cantD,tip,peso):
        super().__init__(marca,mod,anio,tipo,poten,capC,tarifa,cantD)
        self.__tipo=tip
        self.__peso=peso
    
    def getTipo(self):
        return self.__tipo
    def getPeso(self):
        return self.__peso
    
    def tarifaAlquiler(self):
        if self.getPeso()<=10:
            tarifa=self.getTarifa()*self.getCantD()
        elif self.getPeso()>10:
            tarifa=(self.getTarifa()*self.getCantD())+ (self.getTarifa()*self.getCantD()*0.20)
        return tarifa

    def __str__(self):
        return (f""" Herramientas Electricas: 
                Marca: {self.getMarca()}
                Modelo: {self.getModelo()}
                Anio : {self.getAnioF()}
                Tipo de Combustible: {self.getTipoC()}
                Potencia : {self.getPoten()}
                Capacidad : {self.getCapCarga()}""")