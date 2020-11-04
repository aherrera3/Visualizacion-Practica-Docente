
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


datos=np.loadtxt("longitudes_de_onda.csv",dtype=int)

conversion={}

for i in datos:
    conversion[str(i[0])] = (i[1],i[2],i[3])


def choque(foton):
    v=mag(foton.velocidad)
    theta=np.random.random()*np.pi
    phi=np.random.random()*np.pi*2
    vx=v*np.sin(theta)*np.cos(phi)
    vy=v*np.sin(theta)*np.sin(theta)
    vz=v*np.cos(theta)
    wave_lenghtf=round(380+(200*(1-np.cos(theta))),0)
    return vector(vx,xy,vz), wave_lenghtf

print(conversion['450'])
#foton=helix(pos=vector(0,0,0), axis=vector(5,0,0), radius=0.5,color=vector(0,0,0))

#elipse=ellipsoid(pos=vector(2.5,0,0),axis=vector(5,0,0), length=6, height=2, width=2,color=vector(*conversion["700"]),opacity=(0.5),velocidad=vector(3,0,0))
#print(conversion['380'])
#print(mag(elipse.velocidad))

dt=0.1



class photon:

    def __init__ (self, velocidad, posicion,longitud_onda):
        self.elipse=ellipsoid(pos=posicion,axis=velocidad, length=6, height=2, width=2,color=vector(*conversion[str(longitud_onda)]),opacity=(0.5),velocidad=velocidad)
        self.velocidad=velocidad
        self.posicion_resorte=self.elipse.pos - (2.5*self.velocidad/(mag(self.velocidad)))
        self.axis_resorte=(5*self.velocidad/mag(self.velocidad))
        self.resorte=helix(pos=self.posicion_resorte, axis=self.axis_resorte, radius=0.5,color=vector(0,0,0))
    def evolucion_temporal(self,dt):
        self.elipse.pos=self.elipse.pos+ self.velocidad*dt
        self.resorte.pos = self.resorte.pos + self.velocidad*dt

prueba=photon(vector(2,0,0), vector(0,0,0), 700)
prueba2=photon(vector(0,2,0), vector(0,0,0), 400)
prueba3=photon(vector(0,0,2), vector(0,0,0), 500)
t=0

while  True:
    rate(30)
    prueba.evolucion_temporal(dt)
    prueba2.evolucion_temporal(dt)
    prueba3.evolucion_temporal(dt)
    t+=dt
    if t >10:
        break
        
