## Archivo para crear los escenarios del programa

import vpython as vp
import modulo_particulas as mod


def Escenario1(ejecutando, dt):
    # creacion de objetos:
    # electron:
    e1 = mod.Electron(vp.vector(-15,0,0), vp.vector(1,0,0), vp.vector(0.1,1,0.7), 0.0005, 1, "electron") 

    # antineutrino
    an1 = mod.AntineutrinoElectronico(vp.vector(5,0,0), vp.vector(1,0,0), vp.vector(0.8,0.5,0.3), 0.00001, 0.5, "antineutrino")  
  
    if(ejecutando):
        # evolucion del sistema  
        e1.evolucion_temporal(dt)
        an1.evolucion_temporal(dt)    
                
