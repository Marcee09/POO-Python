from gestorEdificio import GestorEdificio

def menuDeOpciones():
    opcion=-1
    gestEdificio=GestorEdificio()
    
    gestEdificio.cargarEdificios()
    gestEdificio.mostrar_lista()
    
    while opcion!=0:
        print("""
                                    ---MENU---
              [1] Mostrar nombre y apellido de los propietarios de cada departamento de un edificio.
              [2] Mostrar la superficie total cubierta de un edificio.
              [3] Mostrar superficie total cubierta de un departmento y el porcentaje que representa del total.
              [4] Contar y mostrar la cantidad de departamentos que tienen 3 dormitorios y mas de un banio.
              [5] Salir del menu.""")
    
        opcion=int(input("Ingrese una opcion del menu: "))
        
        if opcion ==1:
            nombreEdificio=input("Ingrese el nombre del edificio: ")
            gestEdificio.mostrarPropietario(nombreEdificio)
        
        elif opcion==2:
            nomEdifi=input("Ingrese el nombre de un edificio: ")
            gestEdificio.mostrarSuperfTotal(nomEdifi)
        
        elif opcion==3:
            nomProp=input("Igrese apellido y nombre del propietario: ")
            gestEdificio.mostrarSupdeProp(nomProp)
        
        elif opcion==4:
            numPiso=int(input("Ingrese numero de piso: "))
            gestEdificio.mostrarCantDptos(numPiso)
        
        elif opcion==5:
            print("Ha salido del menu")