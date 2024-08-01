from visualizaciones import Visualizaciones
import csv

class GestorVisualizaciones:
    __listaVisualizaciones:list
    def __init__(self):
        self.__listaVisualizaciones=[]
    
    def mostrarVisu(self):
        return self.__listaVisualizaciones
        
    def getListaVisu(self):
        return self.__listaVisualizaciones
    
    def cargaVisua(self):
        archivo=open("Visualizaciones.csv")
        reader=csv.reader(archivo,delimiter=';')
        bandera=False
        for fila in reader:
            if bandera==False:
                bandera=True
            else:
                if len(fila)==5:
                    id=int(fila[0])
                    idPel=fila[1]
                    fech=fila[2]
                    hor=fila[3]
                    minu=int(fila[4])
                    nuevaVisua=Visualizaciones(id,idPel,fech,hor,minu)
                    self.__listaVisualizaciones.append(nuevaVisua)
        archivo.close()
    
    def calcularTotalMinu(self,IdMiembro):
        total=0
        for visu in self.__listaVisualizaciones:
            if IdMiembro==visu.getIdM():
                total+= visu.getMinut()
        print("Total de minutos: ",total)
    
    
    def mostrarC(self):
        for visu in self.__listaVisualizaciones:
            cadena=visu.mostrarCadena()
            print(cadena)
            
    
    def mostrarI(self, gestM):
        listaV = self.getListaVisu()
        j=0
        visuSimultaneas=[]
        for visualizacion in listaV:
            i=0
            for otra_visualizacion in listaV:
                if visualizacion == otra_visualizacion and i!=j:
                    id=visualizacion.getIdM()
                    if id not in visuSimultaneas:
                        visuSimultaneas.append(id)
                        gestM.mostrarIguales(id)
                        
                i+=1
            j+=1
        
                    
        
    
   
            