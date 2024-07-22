from nodo import Nodo
import csv
from maquiPesada import MaquiPesada
from herraElectrica import HerraElectrica
class GestorEquipo:
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getEqui()
            self.__actual=self.__actual.getSigui()
            return dato
    
    def agregarEquipo(self, equi):
        nodo = Nodo(equi)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            actual = self.__comienzo
            while actual.getSigui() is not None:
                actual = actual.getSigui()
            actual.setSigui(nodo)
        self.__tope += 1
    
    def cargarDatos(self):
        archivo=open("equipos.csv")
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader :
            if bandera==True:
                bandera=False
            else:
                if len(fila)==11:
                    M1=fila[0]
                    M2=fila[1]
                    M3=fila[2]
                    M4=int(fila[3])
                    M5=fila[4]
                    M6=fila[5]
                    M7=int(fila[6])
                    M8=int(fila[7])
                    M9=int(fila[8])
                    M10=fila[9]
                    M11=int(fila[10])
                    maquinaPesada=MaquiPesada(M2,M3,M4,M5,M6,M7,M8,M9,M10,M11)
                    self.agregarEquipo(maquinaPesada)  
                if len(fila)==10:
                    E1=fila[0]
                    E2=fila[1]
                    E3=fila[2]
                    E4=int(fila[3])
                    E5=fila[4]
                    E6=fila[5]
                    E7=fila[6]
                    E8=int(fila[7])
                    E9=int(fila[8])
                    E10=fila[9]
                    herraElectr=HerraElectrica(E2,E3,E4,E5,E6,E7,E8,E9,E10)
                    self.agregarEquipo(herraElectr)
        archivo.close()
        
    
    def VerTipo(self, pos):
        aux = self.__comienzo
        i = 0
        try:
            while aux is not None:
                if i == pos:
                    if isinstance(aux.getEqui(), MaquiPesada):
                        print("Es de tipo Maquina pesada")
                    elif isinstance(aux.getEqui(), HerraElectrica):
                        print("Es de tipo herramienta electrica")
                    return  # Salimos de la función si encontramos el equipo en la posición
                aux = aux.getSigui()
                i += 1
            # Si llegamos aquí, significa que el índice estaba fuera de rango
            raise IndexError
        except IndexError:
            print("Índice fuera de rango")
               
                   
    def Cantidad(self,anio):
        actual=self.__comienzo
        cant=0
        while actual is not None:
            if(isinstance(actual.getEqui(),HerraElectrica)):
               if actual.getEqui().getAnioF()==anio:
                   cant+=1
            actual=actual.getSigui()
        print("La cantidad de herramientas electricas es: ",cant)
    
    def CantidadMaquinasPesadas(self,cap):
        actual=self.__comienzo
        cant=0
        while actual is not None:
            if(isinstance(actual.getEqui(),MaquiPesada)):
               if actual.getEqui().getCapCarga()<=cap:
                   cant+=1
            actual=actual.getSigui()
        print("La cantidad de maquinas pesadas menores o iguales a la capacidad ingresada es: ",cant)
    
    def mostrarTodo(self):
        actual=self.__comienzo
        print(f"{'Marca':<15} {'Modelo':<15} {'Anio Fabr.':<15} {'Tipo de comb':<15} {'Potencia':<15} {'Tarifa':<15}")
        while actual is not None:
            if (isinstance(actual.getEqui(),MaquiPesada)):
                tarifa1=actual.getEqui().tarifaAlquiler()
                print(f"{actual.getEqui().getMarca():<15} {actual.getEqui().getModelo():<15} {actual.getEqui().getAnioF():<15} {actual.getEqui().getTipoC():<15} {actual.getEqui().getCapCarga():<15} {tarifa1:<15}")
            elif (isinstance(actual.getEqui(),HerraElectrica)):
                tarifa2=actual.getEqui().tarifaAlquiler()
                print(f"{actual.getEqui().getMarca():<15} {actual.getEqui().getModelo():<15} {actual.getEqui().getAnioF():<15} {actual.getEqui().getTipoC():<15} {actual.getEqui().getCapCarga():<15} {tarifa2:<15}")
            actual=actual.getSigui()   

                   
                
            
