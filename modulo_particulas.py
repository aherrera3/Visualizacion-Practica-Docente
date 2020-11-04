
from abc import ABC, abstractmethod
import vpython as vp

vp.scene.background = vp.color.black
vp.scene.width = 1000 
vp.scene.height = 600

class Particula(ABC):
    
    def __init__(self, posicion, velocidad, nombre):
        self.posicion=posicion
        self.nombre=nombre
        self.velocidad=velocidad
        self.etiqueta = vp.label(pos=posicion, text=nombre, color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0)
        
    #Metodos
    @abstractmethod
    def mover():
        pass
    
    #@abstractmethod
    def crear():
        pass
    
    #@abstractmethod
    def eliminar():
        pass
    
    #@abstractmethod   
    def evolucion_temporal(dt):
        pass    


class ParticulaFundamental(Particula,ABC):
    
    #Metodo contructor
    def __init__(self, posicion, velocidad, color, masa, radio, nombre):
        super().__init__(posicion, velocidad, nombre)
        self.color=color
        self.masa=masa
        self.radio=radio
        self.esfera= vp.sphere(pos=posicion,radius=radio,color=color, make_trail=True,shininess=0,masa=masa,velocidad=velocidad)
    
class ParticulaCompuesta(Particula,ABC):
    
    # Metodo constructor
    def __init__(self, posicion, velocidad, lado, nombre):
        super().__init__(posicion, velocidad, nombre)                   #hereda el atributo posicion y etiqueta de la superclase
        self.lado=lado
        self.apotema=(3)**0.5*lado/6
        
    def mover():
        pass
        
class Neutron(ParticulaCompuesta):    
    
    def mover(self):
        print("neutron: ", self.lado, self.posicion)


class Electron(ParticulaFundamental):
    
    def mover(self):
        print("electron: ", self.etiqueta)
        
    def evolucion_temporal(self, dt):
        self.posicion = vp.vector(self.posicion + self.velocidad*dt)      # actualiza la posicion
     
class AntineutrinoElectronico(ParticulaFundamental): 
    
    def mover():
        print("antineutrino")
    
    def evolucion_temporal(self, dt):
        self.posicion = vp.vector(self.posicion + self.velocidad*dt)
         
        