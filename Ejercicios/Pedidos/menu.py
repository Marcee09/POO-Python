from GestorMotos import gestorMoto
from GestorPedidos import gestorPedido

def menu():
    opcion=-1
    GestMoto=gestorMoto()
    GestPedido=gestorPedido()
    
    GestMoto.cargarMotos()
    GestPedido.cargarPedidos()
    
    while opcion!=0:
        print("Menu de opciones")
        print("""
                 1.Cargar nuevo pedido
                 2.Modificacion del tiempo real de un pedido
                 3.Mostrar datos del conductor y su tiempo promedio de entrega
                 4.Mostrar listado para pago de comisiones
                 0.Para salir del menu""")
        
        opcion=int(input("Ingrese una opcion: "))
        
        if opcion <0 or opcion>4:
            print("No es opcion valida,elige una opcion del menu")
        
        elif opcion ==1:
            idePedido=GestPedido.obtenerIde()
            comida=input("Ingrese la comida pedida: ")
            tiempoEst=int(input("Ingrese el tiempo estimado de entrega en minutos:"))
            tiempoReal=0
            precio=float(input("Ingrese el precio del pedido: "))
            
            patenteCorrecta = None
            while patenteCorrecta is None:
                patente = input("""Ingrese una patente de la lista para asignar el pedido a un conductor
                --- Patentes de motos de conductores de la empresa ---
                          [AAA111]
                          [ABB111]
                          [BBA222]
                          [BBB222]
                          [CCC333]
                          [DDD444] :""")
                
                patenteVerif = GestMoto.validarPatente(patente)
                if patenteVerif != -1:
                    patenteCorrecta = patenteVerif
                else:
                    print("Patente no válida. Por favor, intente de nuevo.")
            
            GestPedido.cargarNuevoPedido(idePedido, comida, tiempoEst, tiempoReal, patenteCorrecta,precio)
            print("Pedido cargado de manera exitosa")
            
        elif opcion==2:
            pate=input("Ingrese numero de patente: ")
            idePedi=int(input("Ingrese el identificador del pedido: "))
            tiempR=int(input("Ingrese el  tiempo real de entrega en minutos: "))
            GestPedido.modificarTiempoReal(pate,idePedi,tiempR)
        
        elif opcion==3:
            patenteMoto=input("Ingrese la patente de la moto del conductor: ") 
            GestMoto.mostrarDatosConductor(patenteMoto,GestPedido)   
        
        elif opcion==4:
            GestMoto.listadoConductores(GestPedido)
        
        elif opcion==0:
            print("Ha salido del menu")
            