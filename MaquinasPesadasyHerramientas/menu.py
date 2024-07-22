from equipos import Equipo
from gestorEquipo import GestorEquipo
def menuOpciones():
    opcion=int
    gestE=GestorEquipo()
    gestE.cargarDatos()
    while (opcion!=5):
        print ("[1]Ver que tipo de maquina se escuentra en una posicion ")
        print ("[2]Cantidad de herramientas electricas en un anio dado ")
        print ("[3]Cantidad de equipos de maquinas pesada cuyo peso es menor al ingresado")
        print ("[4]Mostrar informacion de todos los equipos ")
        print ("[5]Salir del programa. ")
        opcion=int (input ("Ingrese opcion: "))

        if (opcion==1):
            pos=int(input("Ingrese una posicion: "))
            gestE.VerTipo(pos)
            
        elif opcion ==2:
            anio=int(input("Ingrese algun anio: "))
            gestE.Cantidad(anio)
            
        elif opcion ==3:
            cap=int(input("Ingrese una capacidad de carga: "))
            gestE.CantidadMaquinasPesadas(cap)
        
        elif opcion ==4:
            gestE.mostrarTodo()
            
        elif opcion==5:
            print("Salio del menu")
