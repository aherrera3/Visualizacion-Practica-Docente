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
boson2=sphere(pos=vector(15,0,0),radius=2,color=color.blue, make_trail=True,shininess=0,masa=10)

t=0
dt=0.1
while True:
	rate(50)
	boson.pos.x+=dt
	boson2.pos.x-=dt
	
	if boson.pos.x>=-1:
		boson.visible=False
		boson2.visible=False
		break

nballs=np.random.randint(2,5)
colores=[color.white,color.yellow,color.blue,color.green,color.red]
balls=[]
for i in range(nballs):
	balls.append(sphere(pos=vector(0,0,0),radius=1,color=np.random.choice(colores), make_trail=True,shininess=0,masa=10,velocidad=np.random.rand(3)*2-1))

t=0
while True:
	rate(50)
	for b in balls:
		b.pos.x=b.pos.x + b.velocidad[0]*dt
		b.pos.y=b.pos.y + b.velocidad[1]*dt
		b.pos.z=b.pos.z + b.velocidad[2]*dt
	t+=dt
	if t>10:
		break