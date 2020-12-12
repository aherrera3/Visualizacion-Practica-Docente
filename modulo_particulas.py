## Archivo con las clases que representan a cada partícula.

from abc import ABC
import vpython as vp
#import numpy as np

# constantes globales
e=1.602e-19
k=8.987e9*10

##############################################################################
# Clase principal: representa un particula fundamental.
##############################################################################
class ParticulaFundamental(ABC):
    #Metodo contructor
    def __init__(self, posicion, velocidad, masa, radio, nombre, conversion:dict):
        self.posicion=posicion
        self.velocidad=velocidad
        self.etiqueta=vp.label(pos=posicion, text=nombre, color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
        #self.color=color
        self.masa=masa
        self.radio=radio
        self.conversion=conversion
        #Se crea a esfera en VPython que representa a la particula
        self.esfera=vp.sphere(pos=posicion,radius=radio,color=vp.vector(*conversion[str(380)]), make_trail=True, shininess=0,masa=masa,velocidad=velocidad)
 
    def reiniciar(self, pos_ini, vel_ini):
        self.posicion=pos_ini
        self.esfera.pos=self.posicion
        self.velocidad=vel_ini    
        self.esfera.vel=self.velocidad
        if self.esfera.make_trail:
            self.esfera.clear_trail()
            
    def cambiarColor(self, l_nueva):
        color_nuevo = vp.vector(*self.conversion[str(int(l_nueva))])
        self.esfera.color = color_nuevo
        self.esfera.trail_color = color_nuevo        


# Clase que representa a una particula alpha y hereda de ParticulaFundamental       
class Alpha(ParticulaFundamental): 
    def evolucion_temporal1(self, dt):
        # actualizacion (por diferencias finitas)
        pos_antigua_x, pos_antigua_y = self.posicion.x, self.posicion.y
        # avance de posicion 
        self.posicion.x += self.velocidad.x*dt
        self.posicion.y += self.velocidad.y*dt
        self.posicion = vp.vector(self.posicion.x, self.posicion.y, 0)
        self.esfera.pos=self.posicion
         # avance de velocidades
        self.velocidad.x += e**2 *k *dt *pos_antigua_x /(self.masa*(pos_antigua_x**2+pos_antigua_y**2)**(3/2)) 
        self.velocidad.y += e**2 *k *dt *pos_antigua_y /(self.masa*(pos_antigua_x**2+pos_antigua_y**2)**(3/2)) 
        self.velocidad = vp.vector(self.velocidad.x, self.velocidad.y, 0)
        self.esfera.velocidad=self.velocidad      
        

class Photon(ParticulaFundamental):
    def __init__(self, velocidad, posicion, longitud_onda, conversion:dict):
        self.conversion = conversion
        self.velocidad = velocidad
        self.posicion = posicion
        self.longitud_onda = longitud_onda
        #Se crea a esfera en VPython que representa a la particula
        self.esfera = vp.sphere(pos=posicion, color=vp.vector(*conversion[str(longitud_onda)]), opacity=(1), make_trail=True, velocidad=velocidad,radius=0.3, trail_radius=(0.05))
        
    def evolucion_temporal(self, dt):
        self.posicion=vp.vector(self.posicion + self.velocidad*dt)
        self.esfera.pos=self.posicion        

    def cambiar_velocidad(self, velocidad_nueva):
        self.velocidad = velocidad_nueva

    def cambiar_longitud_onda(self, l_nueva):
        color_nuevo = vp.vector(*self.conversion[str(int(l_nueva))])
        self.esfera.color = color_nuevo
        self.esfera.trail_color = color_nuevo

