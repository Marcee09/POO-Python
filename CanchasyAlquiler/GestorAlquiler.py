from ClaseAlquiler import Alquiler
import csv

class Gestor_Alquiler:
    def __init__(self):
        self.__listaA=[]

    def agrega_alquiler(self):
        archivo= open("Alquiler.csv")
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if (len(fila)>=4):
                A=Alquiler(fila[0],fila[1],fila[2],int (fila[3]))
                self.__listaA.append(A)


    def muestra_alquiler(self):
        for alquiler in self.__listaA:
            print (alquiler)

    
    def duracionA(self,alquiler):
        return  alquiler.get_duracion()/60
           
        
    
    def calcula_tot_recau(self,GC):
        tot=0
        for alquiler in self.__listaA:
            importe=GC.obtiene_imp(alquiler.get_id())
            tot+=(importe*self.duracionA(alquiler))
    
    def ImporteAlquiler(self,alquiler,GC):
        imp= GC.obtiene_imp(alquiler.get_id())
        return self.duracionA(alquiler)*imp 


    def listadoHyM(self, GC):
        self.__listaA.sort()
        print(f"{'Hora':<10} {'Id de la cancha':<20} {'Duracion':<15} {'Importe por hora':<20} {'Importe Alquiler':<20}")
        total_recau = 0
        for alquiler in self.__listaA:
            duracion = self.duracionA(alquiler)
            importe_hora = GC.obtiene_imp(alquiler.get_id())
            importe_alquiler = self.ImporteAlquiler(alquiler, GC)
            total_recau += importe_alquiler
            print(f"{alquiler.get_HorasMinutos():<10} {alquiler.get_id():<20} {duracion:<15.2f} {importe_hora:<20.2f} {importe_alquiler:<20.2f}")
        print(f"Total recaudado es: {total_recau:.2f}")
            

    def total_minutos(self,ID):
        i=0
        tot=0
        while i<len(self.__listaA):
            if (self.__listaA[i].get_id()==ID):
                tot+=self.__listaA[i].get_duracion()
            i+=1
        if tot==0:
                print(f"Cancha no encontrada")
        return tot
            