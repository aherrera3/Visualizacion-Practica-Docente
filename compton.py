
from vpython import*
import numpy as np
import particula as mod


# PARTE GRAFICA
#propiedades de la pantalla
scene.background = color.black
scene.width = 1000 
scene.height = 600
#scene.forward = vector(-.5,-.3,-1) #posicion inicial de la camara

# botones
running = False

def Run(b):  
    global running
    running = not running
    if running: 
        b.text = "Pause"
        # llamar a estado_inicial 
        # llama a iniciar aplicacion
    else: 
        b.text = "Run"
        # detener todo
    
bButton = button(text="Run", pos=scene.title_anchor, bind=Run)    
def Reset(r):
    estado_inicial()
    # para y reinicia la operacion anterior

rButton = button(text="Reset", pos=scene.title_anchor, bind=Reset)    
def estado_inicial():
    t=0
    global running
    #running=False



def longitud_de_onda(l):
    r=0.0 
    g=0.0
    b=0.0

    if ((l>=400.0) and (l<410.0)):
        t=(l-400.0)/(410.0-400.0)
        r+=(0.33*t)-(0.20*t*t)
    elif ((l>=410.0) and (l<475.0)):
        t=(l-410.0)/(475.0-410.0)
        r=0.14-(0.13*t*t)
    elif ((l>=545.0) and (l<595.0)):
        t=(l-545.0)/(595.0-545.0)
        r=(1.98*t)-(t*t)
    elif ((l>=595.0) and (l<650.0)):
        t=(l-595.0)/(650.0-595.0) 
        r=0.98+(0.06*t)-(0.40*t*t)
    elif ((l>=650.0) and (l<700.0)):
        t=(l-650.0)/(700.0-650.0)
        r=0.65-(0.84*t)+(0.20*t*t)
    if ((l>=415.0) and (l<475.0)):
        t=(l-415.0)/(475.0-415.0) 
        g=(0.80*t*t)
    elif ((l>=475.0) and (l<590.0)):
        t=(l-475.0)/(590.0-475.0)
        g=0.8 +(0.76*t)-(0.80*t*t)
    elif ((l>=585.0) and (l<639.0)): 
        t=(l-585.0)/(639.0-585.0)
        g=0.84-(0.84*t)
    if ((l>=400.0) and (l<475.0)):
        t=(l-400.0)/(475.0-400.0)
        b=(2.20*t)-(1.50*t*t)
    elif ((l>=475.0) and(l<560.0)) :
        t=(l-475.0)/(560.0-475.0)
        b=0.7-t+(0.30*t*t)
    return r,g,b
foton=helix(pos=vector(0,0,0), axis=vector(5,0,0), radius=0.5,color=vector(0,0,0))

elipse=ellipsoid(pos=vector(2.5,0,0),axis=vector(5,0,0), length=6, height=2, width=2,color=vector(250,0,0),opacity=(0.5))

"""
while  True:
    rate(500)
    if running:
        
"""