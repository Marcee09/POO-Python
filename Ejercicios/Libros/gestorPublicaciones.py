from nodo import Nodo
from libroImpreso import LibroImpreso
from audioLibro import AudioLibro

import csv
class GestorPublicaciones:
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getServi()
            self.__actual=self.__actual.getSiguiente()
            return dato
            
    
    def agregarPublicacion(self,publi):
        nodo=Nodo(publi)
        
        if self.__comienzo is None:
            self.__comienzo=nodo
        else:
            actual=self.__comienzo
            while actual.getSiguiente() is not None:
                actual= actual.getSiguiente()
            actual.setSiguiente(nodo)
            
        self.__tope +=1
    
    def mostrarPublicaciones(self):
        print(f"{'Titulo':<30} {'Categoria':<30}")
        actual=self.__comienzo
        
        while actual is not None :
                publicacion=actual.getPublicacion()
                print(f"{publicacion.getTitulo():<30}{publicacion.getCategoria():<30}")
                actual = actual.getSiguiente()
                
            
    def cargarPublicaciones(self):
        try:
            archivo1=open("Libros/libros.csv")
            archivo2=open("Libros/cd.csv")
            if archivo1 or archivo2:
                reader1=csv.reader(archivo1,delimiter=";")
                reader2=csv.reader(archivo2,delimiter=";")
                bandera1=False
                bandera2=False
                for fila in reader1:
                    if bandera1==False:
                        bandera1=True
                    elif len(fila)==6:
                        tit=fila[0]
                        cat=fila[1]
                        precio=float(fila[2])
                        nomA=fila[3]
                        fecha=fila[4]
                        cantP=int(fila[5])
                        nuevoLibroImpreso=LibroImpreso(tit,cat,precio,nomA,fecha,cantP)
                        self.agregarPublicacion(nuevoLibroImpreso)
                
                for fila in reader2:
                    if bandera2==False:
                        bandera2=True
                    elif len(fila)==5:
                        tit=fila[0]
                        cat=fila[1]
                        precio=float(fila[2])
                        tiempoRepr=int(fila[3])
                        nomNarra=fila[4]
                        nuevoAudioLibro=AudioLibro(tit,cat,precio,tiempoRepr,nomNarra)
                        self.agregarPublicacion(nuevoAudioLibro)
                archivo1.close()
                archivo2.close()
            else:
                raise(FileNotFoundError)
            
        except FileNotFoundError:
            print("No se encontro el archivo")
    
    def agregarAudioLibro(self,titulo,categoria,precio,tiempo,nomNarra):
        actual=self.__actual
        while actual is not None:
            actual=actual.getSiguiente()
        if actual is None:
            publicacion=AudioLibro(titulo,categoria,precio,tiempo,nomNarra)
            self.agregarPublicacion(publicacion)
            print("El libro ha sido cargado")
    
    def agregarLibroImpreso(self,titulo,categoria,precio,nomAutor,fecha,cantPag):
        actual=self.__comienzo
        while actual is not None:
            actual=actual.getSiguiente()
        if actual is None:
            publicacion=LibroImpreso(titulo,categoria,precio,nomAutor,fecha,cantPag)
            self.agregarPublicacion(publicacion)
            print("El libro ha sido cargado")
        
    
    def mostrarTipoDePublicacion(self,posicion):
        try:
            if posicion < 0 or posicion >= self.__tope:
                raise IndexError("Posición fuera de rango")
                
            actual = self.__comienzo
            indice = 0
                    
            while actual is not None and indice < posicion:
                actual = actual.getSiguiente()
                indice += 1
                    
            if actual is not None:
                    publicacion = actual.getPublicacion()
                    if isinstance(publicacion, LibroImpreso):
                        print("La publicación en la posición", posicion, "es un Libro Impreso.")
                    elif isinstance(publicacion, AudioLibro):
                        print("La publicación en la posición", posicion, "es un Audio Libro.")
                    else:
                        print("La publicación en la posición", posicion, "es de un tipo desconocido.")
            else:
                print("No hay publicación en la posición", posicion)
                        
        except IndexError:
            print("Posicion fuera de rango")
    
    def mostrarCantidad(self):
        actual=self.__comienzo
        totalLibrosImpresos=0
        totalAudioLibros=0
        cantidadOtros=0
        
        while actual is not None:
            publicacion=actual.getPublicacion()
            if isinstance(publicacion,LibroImpreso):
                totalLibrosImpresos+=1
            elif isinstance(publicacion,AudioLibro):
                totalAudioLibros+=1
            else:
                cantidadOtros+=1
            actual=actual.getSiguiente()
        
        print("Cantidad de libros impresos: ",totalLibrosImpresos)
        print("Cantidad de audiolibros o cd: ",totalAudioLibros)
        print("Cantidad de libros con categoria no definida: ",cantidadOtros)
        
                
                    
            