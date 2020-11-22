
from abc import ABC, abstractmethod
import vpython as vp


##############################################################################
# Clase principal
##############################################################################
class Particula(ABC):
    
    def __init__(self, posicion, velocidad, nombre):
        self.posicion=posicion
        self.velocidad=velocidad
        self.etiqueta = vp.label(pos=posicion, text=nombre, color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0)
        
    #Metodos
    #@abstractmethod
    #def mover():
    #    pass
    
    #@abstractmethod
    def crear():
        pass
    
    #@abstractmethod
    def eliminar():
        pass
    
    #@abstractmethod   
    def evolucion_temporal(dt):
        pass    
    
    #@abstractmethod
    def reiniciar():
        pass
        #self.posicion=pos_ini
        #self.velocidad=vel_ini



##############################################################################
# Clase que representa un particula fundamental y hereda de Particula
##############################################################################
class ParticulaFundamental(Particula, ABC):
    
    #Metodo contructor
    def __init__(self, posicion, velocidad, color, masa, radio, nombre):
        super().__init__(posicion, velocidad, nombre)
        self.color=color
        self.masa=masa
        self.radio=radio
        self.esfera= vp.sphere(pos=posicion,radius=radio,color=color, make_trail=True, shininess=0,masa=masa,velocidad=velocidad)

    #def eliminar(self):   
    #    self.esfera.visible=False
    #    self.etiqueta.visible=False
    #    del self.esfera
    #    del self.etiqueta
        
        #if (self.esfera.make_trail):   # si tiene trayectoria
        #    self.esfera.clear_trail()
            
    def evolucion_temporal(self, dt):
        self.posicion = vp.vector(self.posicion + self.velocidad*dt)
        self.esfera.pos=self.posicion        
        
    def self_destruction(self):
        self.esfera.visible=False
        self.etiqueta.visible=False
        if (self.esfera.make_trail):   # si tiene trayectoria
           self.esfera.clear_trail()
        del self
    

# Clase que representa a un electrón y hereda de ParticulaFundamental
class Electron(ParticulaFundamental):
    pass
   
        
# Clase que representa a un antineutrino electronico y hereda de ParticulaFundamental        
class AntineutrinoElectronico(ParticulaFundamental): 
    pass

class Alpha(ParticulaFundamental):
    pass
    
class Nucleo(ParticulaFundamental):
    pass


class Photon(ParticulaFundamental):
    def __init__(self, velocidad, posicion, longitud_onda, conversion:dict):
        self.conversion = conversion
        self.esfera = vp.sphere(pos=posicion, color=vp.vector(*conversion[str(longitud_onda)]), opacity=(1), make_trail=True, velocidad=velocidad,radius=0.3, trail_radius=(0.05))
        self.velocidad = velocidad
        self.posicion = posicion
        self.longitud_onda = longitud_onda
        
    #def evolucion_temporal(self, dt):
    #    self.esfera.pos += self.velocidad*dt
    #    self.posicion = self.posicion+self.velocidad*dt

    def cambiar_velocidad(self, velocidad_nueva):
        self.velocidad = velocidad_nueva

    def cambiar_longitud_onda(self, l_nueva):
        color_nuevo = vp.vector(*self.conversion[str(int(l_nueva))])
        self.esfera.color = color_nuevo
        self.esfera.trail_color = color_nuevo



##############################################################################
# Clase que representa un particula compuesta y hereda de Particula    
##############################################################################
class ParticulaCompuesta(Particula,ABC):
    
    # Metodo constructor
    def __init__(self, posicion, velocidad, lado, nombre):
        super().__init__(posicion, velocidad, nombre)                   #hereda el atributo posicion y etiqueta de la superclase
        self.lado=lado
        self.apotema=(3)**0.5*lado/6
        
# Clase que hereda de ParticulaCompuesta    
class Neutron(ParticulaCompuesta):    
    pass

         
        