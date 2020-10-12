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
"""
#dos partículas en el eje x

def estado_inicial():
    t=0
    electron, electron_nombre = mod.electron(vector(-15,0,0), vector(1,0,0))
    muon, muon_nombre = mod.muon(vector(15,0,0), vector(-1,0,0))

electron, electron_nombre = mod.electron(vector(-15,0,0), vector(1,0,0))
muon, muon_nombre = mod.muon(vector(15,0,0), vector(-1,0,0))

t = 0
dt = 0.1
vel_electron = 1
vel_muon = 1
pos_choque = -1 - electron.radius   # pos de choque como prueba

#antes del choque
colision = False
while (not colision):
    rate(20) #fps
    electron.pos.x += dt * vel_electron   # se modifica la posicion del electron
    electron_nombre.pos = vector(electron.pos.x, electron.pos.y, electron.pos.z)  # para que la etiqueta siga a donde se mueva el electron
    muon.pos.x -= dt * vel_muon
    muon_nombre.pos = vector(muon.pos.x, muon.pos.y, muon.pos.z)
    
    if electron.pos.x >= pos_choque: # chocan en pos_choque 
        electron.visible = False
        muon.visible = False
        colision = True

# choque aleatorio
nballs = np.random.randint(2,5) #numero de partículas resultantes del choque
colores = [color.white, color.yellow, color.blue, color.green, color.red] #coleccion de colores
balls = []

#crea y almacena las partículas con un rango de velocidades aleatorias
for i in range(nballs):
	balls.append(sphere(pos=vector(0,0,0), radius=1, color=np.random.choice(colores), make_trail=True, shininess=0, masa=10, velocidad=np.random.rand(3)*2-1))


#despues del choque
t = 0
t_vida = 10    # tiempo de vida
stop = False
while (not stop):
	rate(20)
	for b in balls:
		b.pos.x=b.pos.x + b.velocidad[0]*dt
		b.pos.y=b.pos.y + b.velocidad[1]*dt
		b.pos.z=b.pos.z + b.velocidad[2]*dt
        
	t += dt
	if t >= t_vida:
		stop = True
"""

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

#antes del choque
desintegracion = False
while (not desintegracion):
    rate(20) #fps
    neutron.evolucion_temporal(dt)
    
    t = t + dt 
    if t >= t_desintegracion: # cuando se desintegra
        neutron.eliminar()
        desintegracion = True

particulas_generados=[mod.electron(neutron.posicion,vector(np.random.random()*2-1,np.random.random()*2-1,np.random.random()*2-1)),mod.antineutrino_electronico(neutron.posicion,vector(np.random.random()*2-1,np.random.random()*2-1,np.random.random()*2-1))]



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
"""
# choque aleatorio
nballs = np.random.randint(2,5) #numero de partículas resultantes del choque
colores = [color.white, color.yellow, color.blue, color.green, color.red] #coleccion de colores
balls = []

#crea y almacena las partículas con un rango de velocidades aleatorias
for i in range(nballs):
	balls.append(sphere(pos=vector(0,0,0), radius=1, color=np.random.choice(colores), make_trail=True, shininess=0, masa=10, velocidad=np.random.rand(3)*2-1))


#despues del choque
t = 0
t_vida = 10    # tiempo de vida
stop = False
while (not stop):
	rate(20)
	for b in balls:
		b.pos.x=b.pos.x + b.velocidad[0]*dt
		b.pos.y=b.pos.y + b.velocidad[1]*dt
		b.pos.z=b.pos.z + b.velocidad[2]*dt
        
	t += dt
	if t >= t_vida:
		stop = True
"""