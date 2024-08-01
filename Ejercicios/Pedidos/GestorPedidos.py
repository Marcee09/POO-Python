from pedido import Pedido

import csv

import numpy as np

class gestorPedido:
    __listaPedidos:np.ndarray
    __cantidad:int
    __dimension:int
    __incremento:int
    def __init__(self):
        self.__listaPedidos=np.empty(0,dtype=Pedido)
        self.__cantidad=0
        self.__dimension=0
        self.__incremento=1
    
    def getLista(self):
        return self.__listaPedidos
    
    def __str__(self):
        # Encabezados
        headers = ["Identificador", "Comida", "Patente de Moto", "Tiempo Estimado", "Tiempo Real", "Precio"]
        
        # Crear una fila de encabezado con formato
        header_str = f"{headers[0]:<15} {headers[1]:<15} {headers[2]:<15} {headers[3]:<20} {headers[4]:<20} {headers[5]:<10}"
        
        # Crear las filas de los pedidos con formato
        pedidos_str = [
            f"{pedido.getIdePedido():<15} {pedido.getComida():<15} {pedido.getPatente():<15} {pedido.getTiempoEst():<20} {pedido.getTiempoReal():<20} {pedido.getPrecio():<10}"
            for pedido in self.__listaPedidos
        ]
        
        # Unir encabezado y filas de pedidos
        return header_str + "\n" + "\n".join(pedidos_str)
        
    
    def agregarPedido(self,pedido):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaPedidos.resize(self.__dimension)
        self.__listaPedidos[self.__cantidad]= pedido
        self.__cantidad+=1
    
    def cargarPedidos(self):
        archivo=open("Pedidos/datosPedidos.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=False
        for fila in reader:
            if bandera==False:
                bandera=True
            elif len(fila)==6:
                patMoto=fila[0]
                ide=int(fila[1])
                comida=fila[2]
                tiempoEst=int(fila[3])
                tiempoReal=int(fila[4])
                precio=float(fila[5])
                nuevoPedido=Pedido(patMoto,ide,comida,tiempoEst,tiempoReal,precio)
                self.agregarPedido(nuevoPedido)
        archivo.close()
    
    def obtenerIde(self):
        if self.__cantidad == 0:
            return 1  # Si la lista está vacía, empezamos con el ID 1
        else:
            ultimoPedido = self.__listaPedidos[self.__cantidad - 1]
            ultimoIde = ultimoPedido.getIdePedido()  
            return ultimoIde + 1
        
    def cargarNuevoPedido(self,idePedido, comida, tiempoEst, tiempoReal, patenteCorrecta,precio):
        nuevoPedido=Pedido(patenteCorrecta,idePedido,comida,tiempoEst,tiempoReal,precio)
        self.agregarPedido(nuevoPedido)
        print(self)
        return
    
    def modificarTiempoReal(self,paten,idePedi,tiempR):
        i=0
        
        while i< len(self.__listaPedidos) and paten!=self.__listaPedidos[i].getPatente() or self.__listaPedidos[i].getIdePedido()!=idePedi:
            i+=1
        if i<len(self.__listaPedidos)and paten==self.__listaPedidos[i].getPatente()and self.__listaPedidos[i].getIdePedido()==idePedi:
            self.__listaPedidos[i].setTiempoReal(tiempR)
            print("El tiempo real del pedido ha sido modificado")
            print(self)
        else:
            print("No se encuentra el pedido")
            
    def PromedioEntrega(self,patente):
        sumaMinutos=0
        cantidadPedidos=0
        for pedido in self.__listaPedidos:
            if patente==pedido.getPatente():
                sumaMinutos+=pedido.getTiempoReal()
                cantidadPedidos+=1
        if cantidadPedidos == 0:
            print("Este conductor no realizo ninguna entrega de pedido")
        return sumaMinutos/cantidadPedidos

  