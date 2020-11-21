## Archivo para crear los escenarios del programa

import vpython as vp
import modulo_particulas as mod

# Funcion que crea las particulas del escenario 1
def Escenario1_creacion():
    # creacion de objetos:
    e1 = mod.Electron(vp.vector(-15,0,0), vp.vector(1,0,0), vp.vector(0.1,1,0.7), 0.0005, 1, "electron") 
    an1 = mod.AntineutrinoElectronico(vp.vector(5,0,0), vp.vector(1,0,0), vp.vector(0.8,0.5,0.3), 0.00001, 0.5, "antineutrino")  
    
    return e1, an1      
   
# Funcion que da avance al escenario 1     
def Escenario1_avance(ejecutando,e1,an1,dt):    # funciona bien
    if(ejecutando):
        # evolucion del sistema  
        e1.evolucion_temporal(dt)
        an1.evolucion_temporal(dt)  
        
        
# Funcion que elimina el escenario 1    
def Escenario1_destruccion(e1, an1):        # no funciona bien
    e1.eliminar()
    an1.eliminar()
        
"""
# Elimina el escenario que está ejecutandose actualmente
def eliminarEjecutandose(evento:str):
    if(evento=="Escenario1"): 
        particula1, particula2 = Escenario1_creacion()
        Escenario1_destruccion(particula1, particula2)
    ##elif()
    
    #...
"""
   

                
