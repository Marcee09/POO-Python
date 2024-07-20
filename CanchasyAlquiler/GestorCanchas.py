from ClaseCancha import Cancha
import numpy as np
import csv

class Gestor_Canchas:
    __Canchas:np.ndarray
    __incremento:int
    __dimension:int
    __cantidad:int

    def agrega(self,cancha):
        if (self.__cantidad==self.__dimension):
            self.__dimension+=self.__incremento
            self.__Canchas.resize(self.__dimension)
        self.__Canchas[self.__cantidad]=cancha
        self.__cantidad+=1
    def __init__(self):
        self.__cantidad=0
        self.__dimension=0
        self.__incremento=1
        self.__Canchas=np.empty([0],dtype=Cancha)
    def agregar_cancha(self):
        archivo=open("Canchas.csv")
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            if (len(fila)>=3):
                C= Cancha(fila[0],fila[1],float(fila[2]))
                self.agrega(C)
        archivo.close()

    def muestra(self):
        for cancha in self.__Canchas:
            print (cancha)

    def obtiene_imp(self, id):
        i = 0
        importe = None  # Usar None para indicar que no se encontró la cancha

        while i < len(self.__Canchas):
            if self.__Canchas[i].get_id() == id:
                importe = self.__Canchas[i].get_importe()
            
            i += 1

        return importe
    
    def total_min(self,ID,GA):
        i=0
        tot_min=0
        while i<len(self.__Canchas):
            if (self.__Canchas[i].get_id()==ID):
                tot_min=GA.total_minutos(ID)
                print(f"La cancha {ID} estuvo alquilada :{tot_min} minutos")
                return tot_min
            i+=1
        print(f"No se econtro cancha con ID:{ID}")
        return None
