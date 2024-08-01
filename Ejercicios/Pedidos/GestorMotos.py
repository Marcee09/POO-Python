from moto import Moto

import csv
class gestorMoto:
    __listaMotos:list
    def __init__(self):
        self.__listaMotos=[]
    
    def getListaMotos(self):
        return self.__listaMotos
    
    def __str__(self):
        
        headers = ["Apellido", "Nombre",]
        
        header_str = f"{headers[0]:<15} {headers[1]:<15}"
        
        conductores_str = [
            f"{moto.getApeCond()}{moto.getNomCond()}"
            for moto in self.__listaMotos
        ]
        
        return header_str + "\n" + "\n".join(conductores_str)
    
    def cargarMotos(self):
        archivo=open("Pedidos/datosMotos.csv")
        reader=csv.reader(archivo,delimiter=';')
        bandera=False
        for fila in reader:
            if bandera==False:
                bandera=True
            elif len(fila)==5:
                patente=fila[0]
                marca=fila[1]
                nombre=fila[2]
                apellido=fila[3]
                kilometraje=fila[4]
                nuevaMoto=Moto(patente,marca,nombre,apellido,kilometraje)
                self.__listaMotos.append(nuevaMoto)
        archivo.close()
    
    def validarPatente(self, patente):
        i = 0
        while i < len(self.__listaMotos) and self.__listaMotos[i].getPatente() != patente:
            i += 1
        if i < len(self.__listaMotos) and self.__listaMotos[i].getPatente() == patente:
            return patente
        else:
            return -1
    
    def mostrarDatosConductor(self,patenteMoto,gestorPedido):
        i=0
        
        while i<len(self.__listaMotos) and patenteMoto!=self.__listaMotos[i].getPatente():
            i+=1
        if i<len(self.__listaMotos)and patenteMoto==self.__listaMotos[i].getPatente():
            datosConductor = f"{self.__listaMotos[i].getApeCond()}, {self.__listaMotos[i].getNomCond()}"
            promedioEntrega= gestorPedido.PromedioEntrega(patenteMoto)
            promedioEntero=int(promedioEntrega)
            print(f"Conductor: {datosConductor}")
            print("Promedio real en minutos de entregas que hizo:",promedioEntero)
            
        else:
            print("No se encuentra la moto con la patente proporcionada")
    
    def listadoConductores(self,gestorP):
        listaPedidos=gestorP.getLista()
        
        for conductor in self.getListaMotos():
            
            precioTotal=0
            patente=conductor.getPatente()
            conductor=conductor.getApeCond()+' '+conductor.getNomCond()
            print("Patente de moto: ",patente)
            print("Conductor: ",conductor)
            print(f"{'id pedido':<10} {'Tiempo est':<15}{'Tiempo real':<15} {'Precio':<15}")
            for pedido in listaPedidos:
               
                if patente==pedido.getPatente():
                    print(f"{pedido.getIdePedido():<10} {pedido.getTiempoEst():<15}{pedido.getTiempoReal():<15}{pedido.getPrecio():<15}")
                    precioTotal+=pedido.getPrecio()
            comision=precioTotal*0.20
            print("Total: ",precioTotal)
            print("Comisiones: ",comision)
            print("----------------------------------------------------------------------")
            
            