# -*- coding: utf-8 -*-

import vpython as vp
#import csv
import numpy as np

vp.scene.title = "                                                                                  <b>Pruebas</b>\n\n"
vp.scene.background = vp.color.black
vp.scene.width = 1000 
vp.scene.height = 600
    
# c.i
pos = vp.vector(-8,0.5,0)
#print(vp.mag(pos))

E=9.60e-13
m_alfa = 6.64e-27

#v=(2*E/m_alfa)**(1/2)
#print(v)
v=10
vel = vp.vector(v,0,0)   #cte

radio = 0.5
color = vp.vector(0.1,1,0.7)
m_Nucleo = 1
e=1.602e-19
k=8.987e9

# se crea el nucleo
nucleo = vp.sphere(pos=vp.vector(0,0,0), radius=0.5, color=color, make_trail=True, shininess=0, masa=m_Nucleo, velocidad=vp.vector(0,0,0))

# arreglos para guardar las particulas alpha. Inicia con una particula
particulas = [vp.sphere(pos=pos, radius=radio, color=color, make_trail=True, shininess=0, masa=m_alfa, vel=vel)]


######### prueba
# graficas

f1 = vp.gdots(color=vp.color.cyan) # a graphics curve
#for x in vp.arange(0, 8.05, 0.1): # x goes from 0 to 8
#    f1.plot( x,5*vp.cos(2*x)*vp.exp(-0.2*x) )

#Eg = vp.graph(title="energy (eV), K(blue)+U(green)=magenta, vs. time", height=200 )
#Kg = vp.gcurve(graph=Eg, color=vp.vector(0,0,0.8))

#########


dt = 0.001
t=0
n=0
while True:
    vp.rate(5000)
    for i in range(len(particulas)):
                
        # actualizacion (por diferencias finitas)
        pos_antigua_x, pos_antigua_y = particulas[i].pos.x, particulas[i].pos.y
            
        # avance de posicion 
        particulas[i].pos.x += particulas[i].vel.x*dt
        particulas[i].pos.y += particulas[i].vel.y*dt
        
        particulas[i].pos = vp.vector(particulas[i].pos.x, particulas[i].pos.y, 0)
        
        # avance de velocidades
        particulas[i].vel.x += e**2 *k *dt *pos_antigua_x /(m_alfa*(pos_antigua_x**2+pos_antigua_y**2)**(3/2)) 
        particulas[i].vel.y += e**2 *k *dt *pos_antigua_y /(m_alfa*(pos_antigua_x**2+pos_antigua_y**2)**(3/2)) 
        
        # detiene el mov de la particula si pos en magnitud es > 10:
        if(vp.mag(particulas[i].pos)>10):
            particulas[i].vel = vp.vector(0, 0, 0)
        #print(i)
        # crea y agrega nuevas particulas alpha al arreglo
        if(t>3):
            print("pos y: ", i )#,particulas[i].pos.y)
            n+=1
            f1.plot(t,n)
            
            pos_y = np.random.random()-0.5     #parametro de impacto aleatorio
            pos = vp.vector(-8, pos_y, 0)
            vel = vp.vector(v,0,0)
            particulas.append(vp.sphere(pos=pos, radius=radio, color=color, make_trail=True, shininess=0, masa=m_alfa, vel=vel))
            t=0
    t+=dt
    
    if(len(particulas)>30):
        break








"""
def avance():
    # parametros de la hiperbola
    a,b=2,1
    
    #datos= open("datos.csv", "a")   # "a" : append mode
    #writer=csv.writer(datos)
    
    # avance
    t=0
    dt=0.01
    while(t<20):
        vp.rate(50)
        pos_inicial.x += vel_inicial.x*dt       # en x
        #pos_inicial.y += b/a * (pos_inicial.x**2 - a**2 )**(1/2)
        pos_inicial.y=(b/a*(pos_inicial.x**2 -a**2) )**(1/2)
        
        # escribe en el archivo
        #writer.writerow((pos_inicial.x, pos_inicial.y))
        
        alpha.pos = vp.vector(pos_inicial.x,pos_inicial.y,0)
        print(alpha.pos)
        
        t = t+dt
        
    #datos.close()
    
avance()

# grafica
import matplotlib.pyplot as plt

datos= open("datos.csv")
lineaMala = datos.readline().split(";")
lineaMala.pop(0)
lineaMala.pop(0)

ejes = []
for i in range(4000):
    linea = datos.readline().split(",")
    if(len(linea)==2):    
        ejes.append(linea)

datos.close()

print(ejes, len(ejes))

listax = []
listay = []
for listaInterna in ejes:
    listax.append(float(listaInterna[0]))
    listay.append(float(listaInterna[1]))
   

plt.figure()
plt.plot(listax, listay)
"""

