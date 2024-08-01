from gestorPublicaciones import GestorPublicaciones

def menuOpciones():
    opcion=-1
    gestPublicaciones=GestorPublicaciones()
    gestPublicaciones.cargarPublicaciones()
    while opcion!=5:
        print("""
              ----Menu----
              [1] Agregar publicacion a la coleccion
              [2] Mostrar por pantalla el tipo de publicacion que se encuentra en determinada posicion.
              [3] Mostrar la cantidad de publicaciones de cada tipo
              [4] Mostrar todas las publicaciones
              [5] Salir del menu.""")
        
        opcion=int(input("Ingresa una opcion: "))
        
        if opcion==1:
            titulo=input("Ingrese el titulo del libro: ")
            categoria=input("Ingrese la categoria del libro: ")
            precio=float(input("Ingrese el precio del libro: "))
            tipo=input("Ingrese tipo de libro (audiolibro:A/libro impreso:I): ")
            if tipo=='A':
                tiempo=int(input("Ingrese el tiempo de reproduccion en minutos: "))
                nomNarra=input("Ingrese el nombre del narrador: ")
                gestPublicaciones.agregarAudioLibro(titulo,categoria,precio,tiempo,nomNarra)
            elif tipo=='I':
                nomAutor=input("Ingrese el nombre del autor: ")
                fecha=input("Ingrese la fecha con formato(aaaa/mm/dd): ")
                cantPag=int(input("Ingrese la cantidad de paginas: "))
                gestPublicaciones.agregarLibroImpreso(titulo,categoria,precio,nomAutor,fecha,cantPag)
            
        
        elif opcion==2:
            posicion=int(input("Ingrese una posicion: "))
            gestPublicaciones.mostrarTipoDePublicacion(posicion)
        
        elif opcion==3:
            gestPublicaciones.mostrarCantidad()
        
        elif opcion==4:
            gestPublicaciones.mostrarPublicaciones()
        
        elif opcion==5:
            print("Ha salido del menu")
        
    