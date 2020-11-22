## Archivo para crear los escenarios del programa

import vpython as vp
import modulo_particulas as mod
import numpy as np

particulas=[]

# Funcion que retorna el arreglo con las particulas del escenario actual
def darParticulas():
    return particulas


##############################################################################
# Escenario 1
##############################################################################

# Funcion que crea las particulas del escenario 1
def Escenario1_creacion():
    global particulas
    particulas.clear()
    
    # creacion de objetos:
    e1 = mod.Electron(vp.vector(-15,0,0), vp.vector(1,0,0), vp.vector(0.1,1,0.7), 0.0005, 1, "electron") 
    an1 = mod.AntineutrinoElectronico(vp.vector(5,0,0), vp.vector(1,0,0), vp.vector(0.8,0.5,0.3), 0.00001, 0.5, "antineutrino")  
    
    particulas.append(e1)
    particulas.append(an1)
    
    print("escenario 1 creacion: ", particulas)
    
    return e1, an1      
   
# Funcion que da avance al escenario 1     
def Escenario1_avance(ejecutando,e1,an1,dt):    # funciona bien
    if(ejecutando):
        # evolucion del sistema  
        e1.evolucion_temporal(dt)
        an1.evolucion_temporal(dt)  
        
        
# Funcion que elimina el escenario 1    
def Escenario1_destruccion(e1, an1):        # no funciona bien
    global particulas
    particulas.clear()
    e1.self_destruction()    
    an1.self_destruction()
    #e1.eliminar()
    #an1.eliminar()
    
    

##############################################################################
# Escenario 2
##############################################################################    
# Funcion que crea las particulas del escenario 2
def Escenario2_creacion():
    global particulas
    particulas.clear()
    # creacion de objetos:
    alfa = mod.Alpha(vp.vector(-15,0,0), vp.vector(1,0,0), vp.vector(0.1,1,0.7), 6.64e-27, 2, "Particula \n alpha" )
    nucleo = mod.Nucleo(vp.vector(5,0,0), vp.vector(1,0,0), vp.vector(0.8,0.5,0.3), 0.001, 1, "Nucleo \n (target)")  
    
    particulas.append(alfa)
    particulas.append(nucleo)
    
    #print("escenario 2 creacion: ", particulas)
    
    return alfa, nucleo      
   
# Funcion que da avance al escenario 2     
def Escenario2_avance(ejecutando,alfa,nucleo,dt):  
    if(ejecutando):
        # evolucion del sistema  
        alfa.evolucion_temporal(dt)
        nucleo.evolucion_temporal(dt)  
        
        
# Funcion que elimina el escenario 2  
def Escenario2_destruccion(alfa, nucleo):  
    alfa.self_destruction()  
    nucleo.self_destruction()  
    #alfa.eliminar()
    #nucleo.eliminar()   
    
        
##############################################################################
# Escenario 3
##############################################################################    

def Escenario3_ejecutar():
    global particulas
    particulas.clear()
    
    datos = np.loadtxt("longitudes_de_onda.csv", dtype=int)
    conversion = {}
    
    for i in datos:
        conversion[str(i[0])] = (i[1]/255, i[2]/255, i[3]/255)

    def choque(foton: object):
        v = vp.mag(foton.velocidad)
        theta = np.random.random()*np.pi*2
        phi = np.arccos(np.random.random()*2-1)
        vx = v*np.sin(theta)*np.cos(phi)
        vy = v*np.sin(theta)*np.sin(phi)
        vz = v*np.cos(theta)
        wave_lenghtf = round(380+(199*(1-np.cos(theta))), 0)
        return vp.vector(vx, vy, vz), wave_lenghtf
    
  
    # Creacion de objetos:
    fotones = [[ mod.Photon(vp.vector(4, 0, 0), vp.vector(0, 0, 0), 380, conversion), True ]]
    
    # corre: 
    dt = 0.1
    t = 0
    n = 0
    while True:
        vp.rate(50)
    
        t += dt
    
        for i in range(len(fotones)):
            if round(fotones[i][0].posicion.x, 0) == 10 and fotones[i][1]: #and u:
                velocidad_nueva, l_nueva = choque(fotones[i][0])
                fotones[i][0].cambiar_velocidad(velocidad_nueva)
                fotones[i][0].cambiar_longitud_onda(l_nueva)
                fotones[i][0].evolucion_temporal(dt)
                fotones[i][1] = False
                n += 1
            else:
                fotones[i][0].evolucion_temporal(dt)
            if vp.mag(fotones[i][0].posicion - vp.vector(10,0,0)) >= 10.0:
                fotones[i][0].velocidad = vp.vector(0, 0, 0)
            if t >=2.5:
                fotones.append([ mod.Photon(vp.vector(4,0,0), vp.vector(0,0,0), 380, conversion), True])
                t=0
        if n >= 200:
            break



# Elimina el escenario anteior que se está ejecutando 
def eliminarAnterior(eventoAnterior: str):
    if(eventoAnterior=="Escenario1"): 
        Escenario1_destruccion(particulas[0], particulas[1])
    elif(eventoAnterior=="Escenario2"):
        Escenario2_destruccion(particulas[0], particulas[1])
    
    #...

   

                
