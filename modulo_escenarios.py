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
    # creacion de objetos y añadir objetos:
    particulas.append(mod.Electron(vp.vector(-15,0,0), vp.vector(1,0,0), vp.vector(0.1,1,0.7), 0.0005, 1, "electron") )
    particulas.append(mod.AntineutrinoElectronico(vp.vector(5,0,0), vp.vector(1,0,0), vp.vector(0.8,0.5,0.3), 0.00001, 0.5, "antineutrino")  )
    
# Funcion que da avance al escenario 1     
def escenario1_avance(ejecutando:bool, dt):    # funciona bien
    global particulas
    if(ejecutando):
        # evolucion del sistema  
        particulas[0].evolucion_temporal(dt)
        particulas[1].evolucion_temporal(dt)  
        
# Funcion que reinicia el escenario 1
def escenario1_reiniciar():
    global particulas
    particulas[0].reiniciar(vp.vector(-15,0,0), vp.vector(1,0,0))
    particulas[1].reiniciar(vp.vector(5,0,0), vp.vector(1,0,0))       
        

##############################################################################
# Escenario 2: Scattering de partículas alfa
##############################################################################    

# alpha
m_alfa=6.64e-27
v = 5
pos,vel = vp.vector(-8,0.5,0),vp.vector(v,0,0)   #cte
# nucleo
m_nucleo, color = 6.6e-15, vp.vector(0.1,1,0.7)
# ctes
t,n=0,0
k,e=mod.k,mod.e
# arreglo con la cantidad de particulas por angulo
theta = []

# Funcion que crea las particulas del escenario 2
def escenario2_creacion():
    global particulas,t,n,theta
    particulas.clear()
    theta.clear()
    
    t=0
    n=0
    # se crea el nucleo
    vp.sphere(pos=vp.vector(0,0,0), radius=0.5, color=color, make_trail=True, shininess=0, masa=m_nucleo, velocidad=vp.vector(0,0,0)) 
    # arreglos para guardar las particulas alpha. Inicia con una particula
    particulas.append([mod.Alpha(pos, vel, vp.vector(0.5,1,0.7), m_alfa, 0.5, "Alpha"), True]) #booleano determina si la particula se mueve o no
    # se añade el primer angulo
    
    #theta.append( 2/ vp.atan( pos.y/(k*e**2) * m_alfa*vp.mag(vel)**2 ) )
    #print("theta0:", theta)

# Funcion que da avance al escenario 2   
def escenario2_avance(dt): 
    global particulas, t, n, theta
    #f1 = vp.gdots(color=vp.color.cyan) # a graphics curve
    for i in range(len(particulas)):
        
        if particulas[i][1]:
            particulas[i][0].evolucion_temporal1(dt)      
        # detiene el mov de la particula si pos en magnitud es > 10:
            if(vp.mag(particulas[i][0].posicion)>10 and particulas[i][1]):
                theta.append(vp.atan(particulas[i][0].posicion.y/particulas[i][0].posicion.x)*360/(2*np.pi))
                print("a ", theta)
                particulas[i][0].velocidad = vp.vector(0, 0, 0)
                particulas[i][1]=False

        # crea y agrega nuevas particulas alpha al arreglo
        if(t>3):
            #f1.plot(t,1)
            pos_y = np.random.random()-0.5     #parametro de impacto aleatorio
            pos = vp.vector(-8, pos_y, 0)
            vel = vp.vector(v,0,0)
            particulas.append([mod.Alpha(pos, vel, color, m_alfa, 0.5, "Alpha"),True])        
            #theta.append( 2/vp.atan( pos_y/(k*e**2) * m_alfa*vp.mag(vel)**2 ) )
            #print("angulos actuales: ", theta) 
            t=0
            n+=1
    t+=dt

"""
import numpy as np
theta = [1.5387551139222004, -1.6724617793552317, -8.836827674329644,
         60.03414324074519, 1.6409927223139116, -1.55856538913673, 
         2.945731636791351, -1.6089658339948623, -2.331830001086867,
         5.19311372811911, 1.5854349236843959, -2.289364383521525,
         -3.47566482972552, -1.574919600691814, 3.4597592440368223,
         1.6205752204885029, -1.5771257861450048, -2.0046151701832744,
         2.1644759283159276, 1.6534729826578518, 1.554628910813631, 
         -19.138090140942047, 1.5420664586270714, -1.6323007976718495,
         -4.9134141054439375, 1.562874229458306, 1.9084291563587101, 
         -1.8084729269947921, 1.5403175828939701, -1.5423236639497064,
         1.7276450756713093, 1.578523055686462]


secciones=np.zeros(100)
def discretizar_angulos(theta)->np.ndarray:
    theta=np.abs(theta)
    delta = 180/100           #1.8 grado ahora es 1 grado
    
    for i in range(len(theta)):
        if(theta[i]<0): theta[i] = abs(theta[i])
        
        valor =  int(theta[i]//delta)   # entero
        secciones[valor] = secciones[valor]+1
     
    return secciones    
y = discretizar_angulos(theta)
print("discretizar angulos: ", y)    
 

def grafica_rutherford(y):
    import matplotlib.pyplot as plt
    plt.figure()
    print("valores de y: ",y)
    ind = np.where(y>0)
    x = np.arange(100)
    print("valores de y[ind]:",y[ind])
    plt.scatter(x[ind],y[ind])
    
grafica_rutherford(y)    
"""

# Funcion que reinicia el escenario 2
def escenario2_reiniciar():
    limpiar_escenario()
    escenario2_creacion()
     
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
        
# Funcion que reinicia el escenario 3
def escenario3_reiniciar():
    limpiar_escenario()
    escenario3_creacion()