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
def estado_inicial():
    t=0
    neutron = mod.proton(vector(-15,0,0), vector(1,0,0), 0.5)


t = 0
dt = 0.1
vel_neutron = 1
pos_desintegracion = -1
t_desintegracion = 10
desintegracion=False

neutron = mod.neutron(vector(-15,0,0), vector(1,0,0) , 5)

while  True:
    rate(20)
    if running:
        if desintegracion==False:
            if t <t_desintegracion:
                neutron.evolucion_temporal(dt)
            else:
                #inicio de la desintegracion
                desintegracion=True
                neutron.eliminar()
                proton=mod.proton(neutron.posicion,neutron.velocidad,5)
                particulas_generados=[mod.electron(neutron.posicion,vector(*np.random.rand(3)*2-1)),mod.antineutrino_electronico(neutron.posicion,vector(*np.random.rand(3)*2-1))]
        else:
            if t<20:
                proton.evolucion_temporal(dt)
                #evolucion temporal de la particulas generadas
                for part in particulas_generados:
                    part[0].pos+=part[0].velocidad*dt
                    part[1].pos+=part[0].velocidad*dt
        t+=dt
