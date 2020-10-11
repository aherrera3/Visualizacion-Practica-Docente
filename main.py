from vpython import*
import numpy as np
import particula as pt
#propiedades de la pantalla
scene.background = color.black
scene.width = 1000 
scene.height = 600
#scene.forward = vector(-.5,-.3,-1) #posicion inicial de la camara

#dos partículas en el eje x
electron,electron_nombre=pt.electron(vector(-15,0,0),vector(1,0,0))
muon,muon_nombre=pt.muon(vector(15,0,0),vector(-1,0,0))
t=0
dt=0.1

#antes del choque
while True:
	rate(20) #fps
	electron.pos.x+=dt
	electron_nombre.pos=vector(electron.pos.x,electron.pos.y,electron.pos.z)
	muon.pos.x-=dt
	muon_nombre.pos=vector(muon.pos.x,muon.pos.y,muon.pos.z)
	
	if electron.pos.x>=-1:
		electron.visible=False
		muon.visible=False
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
	rate(20)
	for b in balls:
		b.pos.x=b.pos.x + b.velocidad[0]*dt
		b.pos.y=b.pos.y + b.velocidad[1]*dt
		b.pos.z=b.pos.z + b.velocidad[2]*dt
	t+=dt
	if t>10:
		break