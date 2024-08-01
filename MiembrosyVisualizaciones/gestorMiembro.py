from miembro import Miembro
import csv
import numpy as np

class GestorMiembro:
    __miembro:np.ndarray
    __cantidad: int
    __dimension:int
    __incremento:int
    def __init__(self):
        self.__miembro=np.empty(0,dtype=Miembro)
        self.__cantidad=0
        self.__dimension=0
        self.__incremento=1
    
    def getMiembro(self):
        return self.__miembro
    
    def mostrarMiembros(self):
        for miembro in self.__miembro:
            print(miembro)
    
    def agregarMiembro(self,nuMiem):
        if self.__cantidad==self.__dimension:
             self.__dimension+=self.__incremento
             self.__miembro.resize(self.__dimension)
        self.__miembro[self.__cantidad]=nuMiem
        self.__cantidad+=1
    
    def cargarMiembro(self):
        archivo=open("miembros2.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=False
        for fila in reader:
            if bandera==False:
                bandera=True
            else:
                if len(fila)==3:
                    id=int(fila[0])
                    AyN=fila[1]
                    correo=fila[2]
                    miembroN=Miembro(id,AyN,correo)
                    self.agregarMiembro(miembroN)
        archivo.close()
    
    def obtenerId(self,correo):
        i=0
        
        while i< len(self.__miembro) and correo!=self.__miembro[i].getCorreo():
            i+=1
        if i< len(self.__miembro):
            return self.__miembro[i].getid()
        else:
            -1
            
    def mostrarIguales(self,id):
        i=0
        while i <len(self.getMiembro()) and id!= self.__miembro[i].getid():
            i+=1
        else:
            print(self.__miembro[i].getid(),self.__miembro[i].getAyN(),self.__miembro[i].getCorreo())
        
    
                    
                
        
        