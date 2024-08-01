from coleccion import Coleccion


def test():
    coleccion=Coleccion()
    
    nom="Florencia"
    Ape="Torres"
    Correo="FlorTorres@gmail.com"
    Contra="1234"
    Dire="Mendoza 123(s)"
    Tel="264555"
    Prov="San Juan"
    Loc="Rawson"
    codP=5425
    
    coleccion.agregarNuevoClienteNacional(nom,Ape,Correo,Contra,Dire,Tel,Prov,Loc,codP)
    
    nom="Facundo"
    Ape="Fores"
    Correo="Facu@gmail.com"
    Contra="2345"
    Dire="Libertador 234(s)"
    Tel="2645666"
    
    
    coleccion.agregarNuevoClienteLocal(nom,Ape,Correo,Contra,Dire,Tel)
    
    nom="Clemente"
    Ape="Castro"
    Correo="Clemente@gmail.com"
    Contra="6666"
    Dire="Av Rioja 555(s)"
    Tel="2645656"
    Prov="Mendoza"
    Loc="Capital"
    codP=5300
    
    coleccion.agregarNuevoClienteNacional(nom,Ape,Correo,Contra,Dire,Tel,Prov,Loc,codP)
    
    coleccion.mostrarClientes()
    
    posicion=int(input("Ingrese una posicion de la lista: "))
    
    coleccion.mostrarTipoDeCliente(posicion)
    
    
    