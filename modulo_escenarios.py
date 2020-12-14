## Archivo para crear los escenarios del programa
# -*- coding: utf-8 -*-

import vpython as vp
import modulo_particulas as mod
import numpy as np

particulas=[]

s = "# particulas dispersadas vs angulo"
rutherford = vp.graph(title=s, xtitle='angle', ytitle='# particles', fast=False, width=600)

# Funcion que elimina los objetos del escenario
def limpiar_escenario():
    for obj in vp.scene.objects:
        obj.visible=False
        if obj.make_trail:
            obj.clear_trail()
        del obj
    global particulas, rutherford
    particulas.clear()
    rutherford.delete()
        
    
# Para escenario 2 y 3
datos = np.loadtxt("longitudes_de_onda.csv", dtype=int)    #datos de longitudes de ondas
conversion = {}
for i in datos:
    conversion[str(i[0])] = (i[1]/255, i[2]/255, i[3]/255)    
    
##############################################################################
# Escenario 1: Características de partículas
##############################################################################

# Funcion que crea las particulas del escenario 1
def escenario1_creacion():
    global particulas
    particulas.clear()
    # creacion de objetos y añadir objetos:
    titulo = vp.text(text='Modelo Estandar',pos=vp.vector(40,29,0), align='center', color=vp.color.green,height=5)
    titulo_leptones =vp.text(text='Leptones',pos=vp.vector(5,25,0), align='center', color=vp.color.green,height=3)
    titulo_quarks =vp.text(text='Quarks',pos=vp.vector(25,25,0), align='center', color=vp.color.purple,height=3)
    titulo_bosones =vp.text(text='Bosones',pos=vp.vector(65,25,0), align='center', color=vp.color.blue,height=3)

    particulas_fermionicas=[
        [],
        [],
        []
    ]
    for i in range(len(particulas_fermionicas)):
        for k in range(4):
            particulas_fermionicas[i].append(vp.sphere(pos=vp.vector(k*10,20-(i*10),0),radius=4-i,iden="fermiones:"+str(i)+","+str(k)))
    particulas_bosonicas= [
        [],
        [],
        []
    ]
    for i in range(len(particulas_bosonicas)):
        for k in range(2):
            if i==2 and k==1: break
            else:    particulas_bosonicas[i].append(vp.sphere(pos=vp.vector(60+k*10,20-(i*10),0),radius=2,color =vp.color.red,iden="bosones:"+str(i)+","+str(k)))

    zoom_label=vp.vector(0,0,0)
    boson_00_nombre=vp.label(pos=particulas_bosonicas[0][0].pos-zoom_label, text='Z', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    boson_01_nombre=vp.label(pos=particulas_bosonicas[0][1].pos-zoom_label, text='Bosones W', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    boson_10_nombre=vp.label(pos=particulas_bosonicas[1][0].pos-zoom_label, text='Fotón', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_bosonicas[1][0].color=vp.vector(255/273, 242/273, 0)
    particulas_bosonicas[1][0].emissive=True
    boson_11_nombre=vp.label(pos=particulas_bosonicas[1][1].pos-zoom_label, text='Gluón', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    boson_20_nombre=vp.label(pos=particulas_bosonicas[2][0].pos-zoom_label, text='Higgs', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 

    fermion_00_nombre=vp.label(pos=particulas_fermionicas[0][0].pos-zoom_label, text='Electrón', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_fermionicas[0][0].color=vp.vector(0, 74, 2)/273

    fermion_10_nombre=vp.label(pos=particulas_fermionicas[1][0].pos-zoom_label, text='Muón', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_fermionicas[1][0].color=vp.vector(0, 189, 9)/273    

    fermion_20_nombre=vp.label(pos=particulas_fermionicas[2][0].pos-zoom_label, text='Tau', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_fermionicas[2][0].color=vp.vector(0, 255, 12)/273    

    fermion_01_nombre=vp.label(pos=particulas_fermionicas[0][1].pos-zoom_label, text='Neutrino \nElectrónico', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_fermionicas[0][1].color=vp.vector(0, 74, 2)/273    

    fermion_11_nombre=vp.label(pos=particulas_fermionicas[1][1].pos-zoom_label, text='Neutrino \nMuónico', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_fermionicas[1][1].color=vp.vector(0, 189, 9)/273    

    fermion_21_nombre=vp.label(pos=particulas_fermionicas[2][1].pos-zoom_label, text='Neutrino \nTauónico', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_fermionicas[2][1].color=vp.vector(0, 255, 12)/273       

    fermion_02_nombre=vp.label(pos=particulas_fermionicas[0][2].pos-zoom_label, text='Down', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_fermionicas[0][2].color=vp.vector(52, 0, 92)/273

    fermion_12_nombre=vp.label(pos=particulas_fermionicas[1][2].pos-zoom_label, text='Strange', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_fermionicas[1][2].color=vp.vector(88, 0, 156)/273

    fermion_22_nombre=vp.label(pos=particulas_fermionicas[2][2].pos-zoom_label, text='Bottom', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_fermionicas[2][2].color=vp.vector(144, 0, 255)/273
    
    vp.label(pos=particulas_fermionicas[0][3].pos-zoom_label, text='Up', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_fermionicas[0][3].color=vp.vector(52, 0, 92)/273

    vp.label(pos=particulas_fermionicas[1][3].pos-zoom_label, text='Charm', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_fermionicas[1][3].color=vp.vector(88, 0, 156)/273

    vp.label(pos=particulas_fermionicas[2][3].pos-zoom_label, text='Top', color=vp.vector(0.1,1,0.7), opacity=0.7, height=15, box=0) 
    particulas_fermionicas[2][3].color=vp.vector(144, 0, 255)/273
    

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
        

def dar_mensaje_escenario1(identificador: str)->str:
    mensaje=""
    if identificador=="bosones:0,0":
        mensaje="              "+'<img src="imagenes/bosonZ.png" width=420 height=200>'+"            "+'<img src="imagenes/bosonesZyWDescubrimiento.png" width=400 height=250>'+"\n\n\n"+ "                                           "+" Mas información en: "+ '<a href="https://home.cern/science/physics/z-boson" target="_blank">The Z boson | CERN (home.cern)</a>'+"\n"
    elif identificador=="bosones:0,1":
        mensaje="              "+'<img src="imagenes/bosonesW.png" width=420 height=200>'+"            "+'<img src="imagenes/bosonesZyWDescubrimiento.png" width=400 height=250>'+"\n\n\n"+ "                                           "+" Mas información en: "+ '<a href="https://home.cern/science/physics/w-boson-sunshine-and-stardust" target="_blank">W boson: Sunshine and stardust | CERN (home.cern)</a>'+"\n"
    elif identificador=="bosones:1,0":
        mensaje="              "+'<img src="imagenes/bosonPhoton.png" width=420 height=200>'+"            "+'<img src="imagenes/bosonPhotonDescubrimiento.png" width=400 height=170>'+"\n\n\n"
    elif identificador=="bosones:1,1": 
        mensaje="              "+'<img src="imagenes/bosonGluon.png" width=420 height=250>'+"            "+'<img src="imagenes/bosonGluonDescubrimiento.png" width=400 height=250>'+"\n\n\n"
    elif identificador=="bosones:2,0":     
        mensaje="              "+'<img src="imagenes/bosonHiggs.png" width=420 height=250>'+"            "+'<img src="imagenes/bosonHiggsDescubrimiento.png" width=400 height=250>'+"\n\n\n"+ "                                           "+" Mas información en: "+ '<a href="https://www.youtube.com/watch?v=joTKd5j3mzk&ab_channel=TED-Ed" target="_blank">The Higgs Field, explained - Don Lincoln - YouTube</a>'+"\n"
    elif identificador=="fermiones:0,0":     
        mensaje="              "+'<img src="imagenes/electron.png" width=420 height=237>'+"            "+'<img src="imagenes/electron_descubrimiento.png" width=400 height=250>'+"\n\n\n"
    elif identificador=="fermiones:1,0":     
        mensaje="              "+'<img src="imagenes/muon.png" width=420 height=237>'+"            "+'<img src="imagenes/muon_descubrimiento.png" width=500 height=205>'+"\n\n\n"
    elif identificador=="fermiones:2,0":     
        mensaje="              "+'<img src="imagenes/tau.png" width=420 height=237>'+"            "+'<img src="imagenes/tau_descubrimiento.png" width=500 height=215>'+"\n\n\n"
    elif identificador=="fermiones:0,1":     
        mensaje="              "+'<img src="imagenes/neutrinoElectronico.png" width=420 height=237>'+"            "+'<img src="imagenes/neutrinoElectronico_descubrimiento.png" width=480 height=235>'+"\n\n\n"
    elif identificador=="fermiones:1,1":     
        mensaje="              "+'<img src="imagenes/neutrinoMuonico.png" width=420 height=237>'+"            "+'<img src="imagenes/neutrinoMuonico_descubrimiento.png" width=530 height=220>'+"\n\n\n"
    elif identificador=="fermiones:2,1":     
        mensaje="              "+'<img src="imagenes/neutrinoTauonico.png" width=420 height=237>'+"            "+'<img src="imagenes/neutrinoTauonico_descubrimiento.png" width=500 height=235>'+"\n\n\n"
    elif identificador=="fermiones:0,2":     
        mensaje="              "+'<img src="imagenes/down.png" width=420 height=220>'+"            "+'<img src="imagenes/quarkDown_descubrimiento.png" width=500 height=206>'+"\n\n\n"+ "                                           "+" Mas información en: "+ '<a href="https://www.youtube.com/watch?v=LraNu_78sCw&ab_channel=PhysicsGirl" target="_blank">Quarks Explained in Four Minutes - YouTube</a>'+"\n"
    elif identificador=="fermiones:1,2":     
        mensaje="              "+'<img src="imagenes/strange.png" width=420 height=237>'+"            "+'<img src="imagenes/strange_descubrimiento.png" width=500 height=209>'+"\n\n\n"
    elif identificador=="fermiones:2,2":     
        mensaje="              "+'<img src="imagenes/bottom.png" width=420 height=237>'+"            "+'<img src="imagenes/bottom_descubrimiento.png" width=500 height=215>'+"\n\n\n"
    elif identificador=="fermiones:0,3":     
        mensaje="              "+'<img src="imagenes/quarkUp.png" width=390 height=200>'+"            "+'<img src="imagenes/quarkUpDescubrimiento.png" width=400 height=230>'+"\n\n\n"
    elif identificador=="fermiones:1,3":     
        mensaje="              "+'<img src="imagenes/quarkCharm.png" width=420 height=215>'+"            "+'<img src="imagenes/quarkCharmDescubrimiento.png" width=400 height=230>'+"\n\n\n"
    elif identificador=="fermiones:2,3":     
        mensaje="              "+'<img src="imagenes/quarkTop.png" width=400 height=200>'+"            "+'<img src="imagenes/quarkTopDescubrimiento.png" width=400 height=230>'+"\n\n\n"+ "                                           "+" Mas información en: "+ '<a href="https://www.youtube.com/watch?v=lxWR16c9Kf0&ab_channel=Fermilab" target="_blank">Introducing the top quark – YouTube</a>'+"\n"
    return mensaje

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
    # se crea el nucleo en el centro
    vp.sphere(pos=vp.vector(0,0,0), radius=0.5, color=color, make_trail=True, shininess=0, masa=m_nucleo, velocidad=vp.vector(0,0,0)) 
    particulas.append([mod.Alpha(pos, vel, m_alfa, 0.5, "Alpha", conversion), True]) #booleano determina si la particula se mueve o no  

# Funcion que da avance al escenario 2   
def escenario2_avance(dt): 
    global particulas, t, n, theta
    for i in range(len(particulas)):
        # si las particulas se están moviendo
        if particulas[i][1]:
            particulas[i][0].evolucion_temporal1(dt)      
            # detiene el mov de la particula si pos en magnitud es > 10:
            if(vp.mag(particulas[i][0].posicion)>10 and particulas[i][1]):
                theta.append(vp.atan(particulas[i][0].posicion.y/particulas[i][0].posicion.x)*360/(2*np.pi))
                print("a ", theta)
                particulas[i][0].velocidad = vp.vector(0, 0, 0)
                particulas[i][1]=False
            # cambia de color cuando pase por el valor en x=0 
            if(round(particulas[i][0].posicion.x, 0) == 0):
                try: theta_r = 2/vp.atan(particulas[i][0].posicion.y/(k*e**2) * m_alfa*vp.mag(particulas[i][0].velocidad)**2) #usando parametro de impacto teorico para poner el color
                except:  
                    theta_r = 0
                    print("error por division entre cero")
                l_nueva=theta_a_wl(theta_r*360/(2*np.pi))
                particulas[i][0].cambiarColor(l_nueva)
                
        # crea y agrega nuevas particulas alpha al arreglo
        if(t>3):
            pos_y = np.random.random()-0.5     #parametro de impacto aleatorio
            pos = vp.vector(-8, pos_y, 0)
            vel = vp.vector(v,0,0)
            particulas.append([mod.Alpha(pos, vel, m_alfa, 0.5, "Alpha", conversion),True]) 
            t=0
            n+=1
    t+=dt


def discretizar_angulos(theta:list)->np.ndarray:
    secciones=np.zeros(100)    # arreglo con la cantidad de particulas por angulo (100 secciones que representan 180 grados)
    theta=np.abs(theta)
    delta = 180/100            #1.8 grado ahora es 1 grado
    
    for i in range(len(theta)):
        if(theta[i]<0): theta[i] = abs(theta[i])
        valor =  int(theta[i]//delta)   # entero
        secciones[valor] = secciones[valor]+1
     
    return secciones  
      
def grafica_rutherford(y:np.ndarray):
    ind = np.where(y>0)
    y=y[ind]
    #s = "# particulas dispersadas vs angulo"
    #rutherford = vp.graph(title=s, xtitle='angle', ytitle='# particles', fast=False, width=600)
    funct = vp.gdots(color=vp.color.red, size=6, label='dots')
    for angle in range(0,len(y)):
        vp.rate(100)
        funct.plot(angle, y[angle])


# Funcion que reinicia el escenario 2
def escenario2_reiniciar():
    limpiar_escenario()
    escenario2_creacion()
     
##############################################################################
# Escenario 3: Scattering de Compton
##############################################################################    

t = 0 #variables globales usadas en los metodos.
n = 0

def escenario3_creacion():
    #estado inicial
    global particulas, conversion,t,n
    particulas.clear()
    
    t=0
    n=0
    # Creacion de objetos:
    #Se asigna un booleano para saber si la particula se encuentra antes del choque (True) o despues del choque (False)
    particulas.append([ mod.Photon(vp.vector(8, 0, 0), vp.vector(0, 0, 0), 380, conversion), True ])

def theta_a_wl(theta:float)->float:
    return round(380+(199*(1-np.cos(theta))), 0)

def choque(foton: object)->list: #choque de un foton, cambia longitud de onda.
    v = vp.mag(foton.velocidad)
    theta = np.random.random()*np.pi*2
    phi = np.arccos(np.random.random()*2-1)
    vx = v*np.sin(theta)*np.cos(phi)
    vy = v*np.sin(theta)*np.sin(phi)
    vz = v*np.cos(theta)
    wave_lenghtf = theta_a_wl(theta)
    #retorna la direción de la velocidad nueva y la longitud de onda nueva
    return vp.vector(vx, vy, vz), wave_lenghtf 

def escenario3_avance(dt):
    global particulas, t, n, conversion
    for i in range(len(particulas)):
        # Verifica si la particula esta en el punto de choque
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