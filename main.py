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
    global running
    #running=False
    global desintegracion
    desintegracion=False
    global particulas_generados
    for i in particulas_generados:
        try:
            i[0].clear_trail()
            i[0].visible=False
            i[1].visible=False
        except:
            i.eliminar(True)
    particulas_generados.clear()
    particulas_generados.append(mod.neutron(vector(-15,0,0), vector(1,0,0) , 5))
    global resting
    resting=True

resting=False
t = 0
dt = 0.01
vel_neutron = 1
pos_desintegracion = -1
t_desintegracion = 10
desintegracion=False
particulas_generados=[mod.neutron(vector(-15,0,0), vector(1,0,0) , 5)]

while  True:
    rate(500)
    if running:
        if desintegracion==False:
            if resting:
                resting=False
                continue

            if t <t_desintegracion:
                particulas_generados[0].evolucion_temporal(dt)
            else:
                #inicio de la desintegracion
                
                desintegracion=True
                particulas_generados[0].eliminar()
                
                particulas_generados.append(mod.proton(particulas_generados[0].posicion,particulas_generados[0].velocidad,5))
                particulas_generados+=[mod.electron(particulas_generados[0].posicion,vector(*np.random.rand(3)*2-1)),mod.antineutrino_electronico(particulas_generados[0].posicion,vector(*np.random.rand(3)*2-1))]
        else:
            if  resting:
                resting=False
                continue
            if t<20:
                particulas_generados[1].evolucion_temporal(dt)
                #evolucion temporal de la particulas generadas
                for i in range(2,len(particulas_generados)):
                    particulas_generados[i][0].pos+=particulas_generados[i][0].velocidad*dt
                    particulas_generados[i][1].pos+=particulas_generados[i][0].velocidad*dt
        t+=dt
