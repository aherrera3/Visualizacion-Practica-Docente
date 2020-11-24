## Archivo para crear los escenarios del programa

import vpython as vp
import modulo_particulas as mod
import numpy as np

particulas=[]

#datos de longitudes de ondas
datos = np.loadtxt("longitudes_de_onda.csv", dtype=int)
conversion = {}
for i in datos:
    conversion[str(i[0])] = (i[1]/255, i[2]/255, i[3]/255)

def limpiar_escenario():
    
    for obj in vp.scene.objects:
        obj.visible=False
        if obj.make_trail:
            obj.clear_trail()
        del obj
    global particulas
    particulas.clear()

##############################################################################
# Escenario 1
##############################################################################

# Funcion que crea las particulas del escenario 1
def Escenario1_creacion():
    global particulas
    particulas.clear()
    limpiar_escenario()
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

    
    

##############################################################################
# Escenario 2
##############################################################################    
# Funcion que crea las particulas del escenario 2
def Escenario2_creacion():
    global particulas
    particulas.clear()
    limpiar_escenario()
    # creacion de objetos:
    alfa = mod.Alpha(vp.vector(-15,0,0), vp.vector(1,0,0), vp.vector(0.1,1,0.7), 6.64e-27, 2, "Particula \n alpha" )
    nucleo = mod.Nucleo(vp.vector(5,0,0), vp.vector(1,0,0), vp.vector(0.8,0.5,0.3), 0.001, 1, "Nucleo \n (target)")  
    
    particulas.append(alfa)
    particulas.append(nucleo)

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
t = 0 #variables globales usadas en los metodos.
n = 0
def Escenario3_creacion():
    #estado inicial
    global particulas, conversion,t,n
    particulas.clear()
    limpiar_escenario()
    t=0
    n=0
    # Creacion de objetos:
    #Se asigna un booleano para saber si la particula se encuentra antes del choque (True)
    #o despues del choque (False)
    particulas.append([ mod.Photon(vp.vector(4, 0, 0), vp.vector(0, 0, 0), 380, conversion), True ])

def choque(foton: object): #choque de un foton, cambia longitud de onda.
    v = vp.mag(foton.velocidad)
    theta = np.random.random()*np.pi*2
    phi = np.arccos(np.random.random()*2-1)
    vx = v*np.sin(theta)*np.cos(phi)
    vy = v*np.sin(theta)*np.sin(phi)
    vz = v*np.cos(theta)
    wave_lenghtf = round(380+(199*(1-np.cos(theta))), 0)
    #retorna la direción de la velocidad nueva y la longitud de onda nueva
    return vp.vector(vx, vy, vz), wave_lenghtf 

def escenario3_avance(dt):
    global particulas, t, n, conversion
    for i in range(len(particulas)):
        #verifica si la particula esta en el punto de choque
        if round(particulas[i][0].posicion.x, 0) == 10 and particulas[i][1]: 
            #genera el choque
            velocidad_nueva, l_nueva = choque(particulas[i][0])
            #actualiza las propiedades
            particulas[i][0].cambiar_velocidad(velocidad_nueva)
            particulas[i][0].cambiar_longitud_onda(l_nueva)
            #evolucion temporal
            particulas[i][0].evolucion_temporal(dt)
            #la particula choco 
            particulas[i][1] = False
            n += 1
        else:
            particulas[i][0].evolucion_temporal(dt)

        #detiende la particula si se ha alejado mas de 10
        if vp.mag(particulas[i][0].posicion - vp.vector(10,0,0)) >= 10.0:
            particulas[i][0].velocidad = vp.vector(0, 0, 0)
        #genera particulas nuevas cada cierto tiempo
        if t >=2.5:
            particulas.append([ mod.Photon(vp.vector(4,0,0), vp.vector(0,0,0), 380, conversion), True])
            t=0
    t+=dt
        

# Elimina el escenario anteior que se está ejecutando 
def eliminarAnterior(eventoAnterior: str):
    if(eventoAnterior=="Escenario1"): 
        Escenario1_destruccion(particulas[0], particulas[1])
    elif(eventoAnterior=="Escenario2"):
        Escenario2_destruccion(particulas[0], particulas[1])
    
    #...

   

                
