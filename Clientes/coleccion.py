
from clientesNacionales import ClienteNacional
from clientes import Cliente

from nodo import Nodo
class Coleccion:
    __comienzo:Nodo
    def __init__(self):
        self.__comienzo=None
    
    def agregarCliente(self,cliente):
        nodo=Nodo(cliente)
        
        if self.__comienzo is None:
            self.__comienzo=nodo
        else:
            actual=self.__comienzo
            while actual.getSiguiente() is not None:
                actual= actual.getSiguiente()
            actual.setSiguiente(nodo)
            
    
    def agregarNuevoClienteNacional(self,nom,Ape,Correo,Contra,Dire,Tel,Prov,Loc,codP):
            clienteN=ClienteNacional(nom,Ape,Correo,Contra,Dire,Tel,Prov,Loc,codP)
            self.agregarCliente(clienteN)
    
    def agregarNuevoClienteLocal(self,nom,Ape,Correo,Contra,Dire,Tel):
            clienteL=Cliente(nom,Ape,Correo,Contra,Dire,Tel)
            self.agregarCliente(clienteL)
    
    def mostrarClientes(self):
        print("---Clientes Nacionales---")
        print(f"{'Nombre':<30} {'Provincia':<30}")
        actual=self.__comienzo
        
        while actual is not None :
            cliente=actual.getCliente()
            if isinstance(cliente, ClienteNacional):
                print(f"{cliente.getNombre():<30}{cliente.getProvincia():<30}")
                actual = actual.getSiguiente()
            else:
                actual=actual.getSiguiente()
    
    def mostrarTipoDeCliente(self,posicion):
                
            actual = self.__comienzo
            indice = 0
                    
            while actual is not None and indice < posicion:
                actual = actual.getSiguiente()
                indice += 1
                    
            if actual is not None:
                    cliente = actual.getCliente()
                    if isinstance(cliente, ClienteNacional):
                        print("El cliente en la posición", posicion, "es un cliente nacional.")
                    else:
                        print("El cliente en la posición", posicion, "es un cliente local.")
            else:
                print("No hay clientes en la posición", posicion)
        
        