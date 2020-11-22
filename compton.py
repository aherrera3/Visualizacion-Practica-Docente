
from vpython import*
import numpy as np
import particula as mod


# PARTE GRAFICA
# propiedades de la pantalla
scene.background = color.black
scene.width = 1000
scene.height = 600
# scene.forward = vector(-.5,-.3,-1) #posicion inicial de la camara

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
    t = 0
    global running
    # running=False


datos = np.loadtxt("longitudes_de_onda.csv", dtype=int)

conversion = {}

for i in datos:
    conversion[str(i[0])] = (i[1], i[2], i[3])


def choque(foton):
    v = mag(foton.velocidad)
    theta = np.random.random()*np.pi
    phi = np.random.random()*np.pi*2
    vx = v*np.sin(theta)*np.cos(phi)
    vy = v*np.sin(theta)*np.sin(phi)
    vz = v*np.cos(theta)
    wave_lenghtf = round(380+(199*(1-np.cos(theta))), 0)
    return vector(vx, vy, vz), wave_lenghtf


print(conversion['450'])
#foton=helix(pos=vector(0,0,0), axis=vector(5,0,0), radius=0.5,color=vector(0,0,0))

#elipse=ellipsoid(pos=vector(2.5,0,0),axis=vector(5,0,0), length=6, height=2, width=2,color=vector(*conversion["700"]),opacity=(0.5),velocidad=vector(3,0,0))
# print(conversion['380'])
# print(mag(elipse.velocidad))

dt = 0.1


class photon:

    def __init__(self, velocidad, posicion, longitud_onda):
        
        self.esfera = sphere(pos=posicion, color=vector(*conversion[str(longitud_onda)]), opacity=(1), make_trail=True, velocidad=velocidad,radius=0.3,trail_radius=(0.05))
        self.velocidad = velocidad
        self.posicion = posicion
        self.longitud_onda = longitud_onda
        
    def evolucion_temporal(self, dt):
        self.esfera.pos += self.velocidad*dt
        self.posicion = self.posicion+self.velocidad*dt

    def cambiar_velocidad(self, velocidad_nueva):
        self.velocidad = velocidad_nueva

    def cambiar_longitud_onda(self, l_nueva):
        color_nuevo = vector(*conversion[str(int(l_nueva))])
        self.esfera.color = color_nuevo
        self.esfera.trail_color = color_nuevo


t = 0

fotones = [[photon(vector(4, 0, 0), vector(0, 0, 0), 380),True]]
n = 0
u = True
while True:
    rate(50)

    t += dt

    for i in range(len(fotones)):
        if round(fotones[i][0].posicion.x, 0) == 10 and fotones[i][1]: #and u:
            velocidad_nueva, l_nueva = choque(fotones[i][0])
            fotones[i][0].cambiar_velocidad(velocidad_nueva)
            fotones[i][0].cambiar_longitud_onda(l_nueva)
            fotones[i][0].evolucion_temporal(dt)
            fotones[i][1] = False
            n += 1
        else:
            fotones[i][0].evolucion_temporal(dt)
        if mag(fotones[i][0].posicion - vector(10,0,0)) >= 10.0:
            fotones[i][0].velocidad = vector(0, 0, 0)
        if t >=2.5:
            fotones.append([photon(vector(4,0,0), vector(0,0,0), 380),True])
            t=0
    if n >= 100:
        break

