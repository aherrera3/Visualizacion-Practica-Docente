
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

foton=helix(pos=vector(0,0,0), axis=vector(5,0,0), radius=0.5,color=vector(250,250,0))

elipse=ellipsoid(pos=vector(2.5,0,0), axis=vector(5,0,0), length=5, height=1, width=1,color=vector(250,250,0))

"""
while  True:
    rate(500)
    if running:
        
"""