## Archivo para crear los escenarios del programa

import vpython as vp
import modulo_particulas as mod


def Escenario1_creacion():
    # creacion de objetos:
    e1 = mod.Electron(vp.vector(-15,0,0), vp.vector(1,0,0), vp.vector(0.1,1,0.7), 0.0005, 1, "electron") 
    an1 = mod.AntineutrinoElectronico(vp.vector(5,0,0), vp.vector(1,0,0), vp.vector(0.8,0.5,0.3), 0.00001, 0.5, "antineutrino")  
    
    return e1, an1      
        
def Escenario1_avance(ejecutando,e1,an1,dt):
    if(ejecutando):
        # evolucion del sistema  
        e1.evolucion_temporal(dt)
        an1.evolucion_temporal(dt)  
        
                
