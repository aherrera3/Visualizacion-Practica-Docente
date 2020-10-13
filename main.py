# -*- coding: utf-8 -*-

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


# PARTE LOGICA
# desintegracion

def estado_inicial():
    t=0
    neutron = mod.proton(vector(-15,0,0), vector(1,0,0), 0.5)

neutron = mod.neutron(vector(-15,0,0), vector(1,0,0), 5)

t = 0
dt = 0.1
vel_neutron = 1
pos_desintegracion = -1
t_desintegracion = 10

#antes de la desintegracion
desintegracion = False
while (not desintegracion):
    rate(20) #fps
    neutron.evolucion_temporal(dt)
    
    t = t + dt 
    if t >= t_desintegracion: # cuando se desintegra
        neutron.eliminar()
        desintegracion = True

#creacion de partículas producto de la desintegracion
particulas_generados=[mod.electron(neutron.posicion,vector(*np.random.rand(3)*2-1)),mod.antineutrino_electronico(neutron.posicion,vector(*np.random.rand(3)*2-1))]

#luego de la desintegracion
proton=mod.proton(neutron.posicion,neutron.velocidad,5)
while  True:
    rate(20)
    proton.evolucion_temporal(dt)
    for part in particulas_generados:
        part[0].pos+=part[0].velocidad*dt
        part[1].pos+=part[0].velocidad*dt
    t+=dt
    if t>=20:
        break