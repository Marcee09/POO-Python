from departamento import Departamento
from edificio import Edificio

import csv

class GestorEdificio:
    __listaEdificios:list
    def __init__(self):
        self.__listaEdificios=[]
    
    def getListaEdificios(self):
        return self.__listaEdificios
    
    def cargarEdificios(self):
        archivo=open("Edificio/edificioNorte.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if len(fila)==6:
                id=int(fila[0])
                nom=fila[1]
                dire=fila[2]
                nomEmpC=fila[3]
                cantP=int(fila[4])
                cantD=int(fila[5])
                nuevoEdificio=Edificio(id,nom,dire,nomEmpC,cantP,cantD)
                self.__listaEdificios.append(nuevoEdificio)
        
        # Volver al principio del archivo para leer los departamentos
        archivo.seek(0)
        
        for fila in reader:
            if len(fila)==8:
                idE=int(fila[0])
                idD=int(fila[1])
                nyaProp=fila[2]
                numPiso=int(fila[3])
                numDepto=int(fila[4])
                cantH=int(fila[5])
                cantB=int(fila[6])
                supC=float(fila[7])
                nuevoDepto=Departamento(idD,nyaProp,numPiso,numDepto,cantH,cantB,supC)
                for edificio in self.__listaEdificios:
                    if idE==edificio.getIdEdi():
                        edificio.agregarDepto(nuevoDepto)
        archivo.close()
        
    def mostrar_lista(self):
        for edificio in self.__listaEdificios:
            
            print(f"Edificio ID: {edificio.getIdEdi()} | Nombre: {edificio.getNomEdi()} | Dirección: {edificio.getDire()} | Empresa Constructora: {edificio.getNomEmpC()}")
            print("Departamentos:")
            print(f"{'ID':<5} {'Propietario':<25} {'Piso':<5} {'Depto':<5} {'Hab':<5} {'Baños':<6} {'Superficie':<10}")
            for depto in edificio.getDeparta():
                print(f"{depto.getIdDepto():<5} {depto.getNomProp():<25} {depto.getNumPiso():<5} {depto.getNumDpto():<5} {depto.getCantHab():<5} {depto.getCantBanios():<6} {depto.getSupCub():<10}")
            print("-" * 80)
                        
                
    
    def mostrarPropietario(self,nombreEdificio):
        i=0
        print("Propietarios del ",nombreEdificio)
        print(f"{'ID dpto':<10} {'Propietario':<25}")
        while i<len(self.__listaEdificios) and nombreEdificio!=self.__listaEdificios[i].getNomEdi():
            i+=1
        if i<len(self.__listaEdificios) and nombreEdificio==self.__listaEdificios[i].getNomEdi():
            listaDptos=self.__listaEdificios[i].getDeparta()
            for departamento in listaDptos:
                idDpto=departamento.getIdDepto()
                nomProp=departamento.getNomProp()
                print(f"{idDpto:<10}{nomProp:<10}")
        
        else:
            print("El edificio no se encuentra")
        
    def mostrarSuperfTotal(self,nomEdi):
        i=0
        supTotal=0
        while i<len(self.__listaEdificios)and nomEdi!=self.__listaEdificios[i].getNomEdi():
            i+=1
        if i<len(self.__listaEdificios)and nomEdi==self.__listaEdificios[i].getNomEdi():
            listaDeptos=self.__listaEdificios[i].getDeparta()
            for departamento in listaDeptos:
                supTotal+=departamento.getSupCub()
        print("Superficie total cubierta: ",supTotal)
    
    def mostrarSupdeProp(self, nomProp):
        for edificio in self.__listaEdificios:
            supTotalProp = 0
            supTotalEdi = 0
            for departamento in edificio.getDeparta():
                supTotalEdi += departamento.getSupCub()
                if nomProp == departamento.getNomProp():
                    supTotalProp += departamento.getSupCub()
            if supTotalEdi > 0:  # Para evitar división por cero
                porcentaje = (supTotalProp / supTotalEdi) * 100
                print(f"Edificio: {edificio.getNomEdi()}")
                print(f"Superficie total cubierta del propietario {nomProp}: {supTotalProp}")
                print(f"Porcentaje que representa respecto del total: {porcentaje:.2f}%")
            else:
                print(f"Edificio: {edificio.getNomEdi()}")
                print(f"Superficie total cubierta del propietario {nomProp}: {supTotalProp}")
                print("Porcentaje que representa respecto del total: 0.00%")
                
    def mostrarCantDptos(self,numPiso):
        for edificio in self.__listaEdificios:
            cant=0
            for departamento in edificio.getDeparta():
                if departamento.getNumPiso()==numPiso:
                    if departamento.getCantBanios() >1 and departamento.getCantHab()==3:
                        cant+=1
            print(f"Edificio: {edificio.getNomEdi()}")
            print(f"Cantidad de departamentos con 3 dormitorios y mas de un banio para el piso {numPiso} es:",cant)
                        
        