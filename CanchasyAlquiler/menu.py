from GestorAlquiler import Gestor_Alquiler
from GestorCanchas import Gestor_Canchas

def test():
    GA=Gestor_Alquiler()
    GA.agrega_alquiler()
    # GA.muestra_alquiler()
    GC=Gestor_Canchas()
    GC.agregar_cancha()
    # GC.muestra()
    opcion=0

    while(opcion!=3):
        print ("--MENU DE OPCIONES--")
        print("[1] Listado ordenado por horas y minutos de los alquileres registrados")
        print("[2] Cantidad total de minutos de una cancha alquilada")
        print("[3] Salir ")
        
        opcion=int(input("Ingrese opcion para iniciar ejecucion: "))

        if (opcion==1):
            GA.listadoHyM(GC)
        elif(opcion==2):
            ID= input("Ingrese ID de la cancha para mostrar total de minutos que estuvo alquilada: ")
            GC.total_min(ID,GA)
        elif(opcion==3):
            print("Adios...")


if __name__=='__main__':
    test()