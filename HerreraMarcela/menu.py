from gestorMiembro import GestorMiembro
from gestorVisualizaciones import GestorVisualizaciones

def menuOpciones():
    opcion=str
    GestMiembro=GestorMiembro()
    gestVis=GestorVisualizaciones()
    
    GestMiembro.cargarMiembro()

    gestVis.cargaVisua()
    
    while opcion !='c':
        print("---Menu de opciones---")
        print("a.Cantidad total de minutos que un miembro ha visto peliculas.")
        print("b.Mostrar datos de miembros que han realizado visulizaciones simultaneas.")
        print("c.Salir del menu.")
        
        opcion=input("Ingrese una opcion: ")
        if opcion =='a':
            correo=input("Ingrese el correo de un miembro: ")
            obtengoIdMiembro= GestMiembro.obtenerId(correo)
            gestVis.calcularTotalMinu(obtengoIdMiembro)
        
        elif opcion =='b':
            gestVis.mostrarI(GestMiembro)
        
        elif opcion == 'c':
            print("Saliste del menu de opciones")