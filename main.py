from vpython import*
import numpy as np
#propiedades de la pantalla
scene.background = color.black
scene.width = 1000 
scene.height = 600
#scene.forward = vector(-.5,-.3,-1) #posicion inicial de la camara

#dos partículas en el eje x
#make_trail hace que la partícula tenga una trayectoria visible
boson=sphere(pos=vector(-15,0,0),radius=2,color=color.red, make_trail=True,shininess=0,masa=10)
#nombre de la particula que sigue su trayectoria
boson_name=label(pos=vector(boson.pos.x,boson.pos.y+boson.radius,boson.pos.z), text="Boson 1", color=color.white, opacity=0.7, height=15, box=0)

boson2=sphere(pos=vector(15,0,0),radius=2,color=color.blue, make_trail=True,shininess=0,masa=10)
boson2_name=label(pos=vector(boson2.pos.x,boson2.pos.y+boson2.radius,boson2.pos.z), text="Boson 2", color=color.white, opacity=0.7, height=15, box=0)
t=0
dt=0.1

#antes del choque
while True:
	rate(50) #fps
	boson.pos.x+=dt
	boson_name.pos=vector(boson.pos.x,boson.pos.y+boson.radius,boson.pos.z)
	boson2.pos.x-=dt
	boson2_name.pos=vector(boson2.pos.x,boson2.pos.y+boson2.radius,boson2.pos.z)
	
	if boson.pos.x>=-1:
		boson.visible=False
		boson2.visible=False
		break

nballs=np.random.randint(2,5) #numero de partículas resultantes del choque
colores=[color.white,color.yellow,color.blue,color.green,color.red] #coleccion de colores
balls=[]

#crea y almacena las partículas con un rango de velocidades aleatorias
for i in range(nballs):
	balls.append(sphere(pos=vector(0,0,0),radius=1,color=np.random.choice(colores), make_trail=True,shininess=0,masa=10,velocidad=np.random.rand(3)*2-1))

t=0
#despues del choque
while True:
	rate(50)
	for b in balls:
		b.pos.x=b.pos.x + b.velocidad[0]*dt
		b.pos.y=b.pos.y + b.velocidad[1]*dt
		b.pos.z=b.pos.z + b.velocidad[2]*dt
	t+=dt
	if t>10:
		break