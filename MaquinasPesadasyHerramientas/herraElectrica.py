from equipos import Equipo

class HerraElectrica(Equipo):
    __bateOCable:str
    def __init__(self,marca,mod,anio,tipo,poten,capC,tarifa,cantD,boC):
        super().__init__(marca,mod,anio,tipo,poten,capC,tarifa,cantD)
        self.__bateOCable=boC
    
    def getBOC(self):
        return self.__bateOCable
    
    def tarifaAlquiler(self):
        if self.getBOC()=="bateria":
            tarifa= (self.getTarifa()*self.getCantD())+(self.getTarifa()*self.getCantD()*0.10)
        elif self.getBOC()=="cable":
            tarifa=(self.getTarifa()*self.getCantD())
        
        return tarifa
    
    def __str__(self):
        return (f""" Herramientas Electricas: 
                Marca: {self.getMarca()}
                Modelo: {self.getModelo()}
                Anio : {self.getAnioF()}
                Tipo de Combustible: {self.getTipoC()}
                Potencia : {self.getPoten()}
                Capacidad : {self.getCapCarga()}""")