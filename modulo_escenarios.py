## Archivo para crear los escenarios del programa

import vpython as vp
import modulo_particulas as mod
import numpy as np

particulas=[]

# Funcion que elimina los objetos del escenario
def limpiar_escenario():
    for obj in vp.scene.objects:
        obj.visible=False
        if obj.make_trail:
            obj.clear_trail()
        del obj
    global particulas
    particulas.clear()
        
##############################################################################
# Escenario 1: Efecto fotoelectrico
##############################################################################

# Funcion que crea las particulas del escenario 1
def escenario1_creacion():
    global particulas
    particulas.clear()
    # creacion de objetos:
    e1 = mod.Electron(vp.vector(-15,0,0), vp.vector(1,0,0), vp.vector(0.1,1,0.7), 0.0005, 1, "electron") 
    an1 = mod.AntineutrinoElectronico(vp.vector(5,0,0), vp.vector(1,0,0), vp.vector(0.8,0.5,0.3), 0.00001, 0.5, "antineutrino")  
    
    particulas.append(e1)
    particulas.append(an1)
    
# Funcion que da avance al escenario 1     
def escenario1_avance(ejecutando:bool, dt):    # funciona bien
    global particulas
    if(ejecutando):
        # evolucion del sistema  
        particulas[0].evolucion_temporal(dt)
        particulas[1].evolucion_temporal(dt)  
        
# Funcion que reinicia el escenario
def escenario1_reiniciar():
    global particulas
    particulas[0].reiniciar(vp.vector(-15,0,0), vp.vector(1,0,0))
    particulas[1].reiniciar(vp.vector(5,0,0), vp.vector(1,0,0))       
        

##############################################################################
# Escenario 2: Scattering de partículas alfa
##############################################################################    

# alpha
m_alfa=6.64e-27
pos = vp.vector(-8,0.5,0)
v = 5
vel = vp.vector(v,0,0)   #cte

# nucleo
m_nucleo, color = 6.6e-15, vp.vector(0.1,1,0.7)

t=0
n=0

# Funcion que crea las particulas del escenario 2
def escenario2_creacion():
    global particulas,t,n#, posiciones_iniales, velocidades_iniciales
    particulas.clear()
    t=0
    n=0
    # se crea el nucleo
    vp.sphere(pos=vp.vector(0,0,0), radius=0.5, color=color, make_trail=True, shininess=0, masa=m_nucleo, velocidad=vp.vector(0,0,0))
       
    # arreglos para guardar las particulas alpha. Inicia con una particula
    particulas.append(mod.Alpha(pos, vel, vp.vector(0.5,1,0.7), m_alfa, 0.5, "Alpha"))

# Funcion que da avance al escenario 2     
def escenario2_avance(dt): 
    global particulas, t, n
    for i in range(len(particulas)):
        
        particulas[i].evolucion_temporal1(dt)
        
        # detiene el mov de la particula si pos en magnitud es > 10:
        if(vp.mag(particulas[i].posicion)>10):
            particulas[i].velocidad = vp.vector(0, 0, 0)
            
        # crea y agrega nuevas particulas alpha al arreglo
        if(t>3):
            pos_y = np.random.random()-0.5     #parametro de impacto aleatorio
            pos = vp.vector(-8, pos_y, 0)
            vel = vp.vector(v,0,0)
            particulas.append(mod.Alpha(pos, vel, color, m_alfa, 0.5, "Alpha"))
            t=0
            n+=1
    t+=dt
 

     
##############################################################################
# Escenario 3
##############################################################################    

datos = np.loadtxt("longitudes_de_onda.csv", dtype=int)    #datos de longitudes de ondas
conversion = {}
for i in datos:
    conversion[str(i[0])] = (i[1]/255, i[2]/255, i[3]/255)

t = 0 #variables globales usadas en los metodos.
n = 0

def escenario3_creacion():
    #estado inicial
    global particulas, conversion,t,n
    particulas.clear()
    
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
        
