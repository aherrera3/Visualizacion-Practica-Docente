# -*- coding: utf-8 -*-

# formula de rutherford:

import numpy as np
import matplotlib.pyplot as plt

Z=47                       # numero atomico plata
n=5.85e28                       # N atomos por unidad de vol en lamina target
k=8.9875e9                  # cte de coulomb 
e=1.602e-19
r=2e-2                  # distancia de la lamina (nucleo target) al detector.
E=9.60e-13          #energia cinetica de particulas alpha = 100MeV
c=3e8
I_0 = 3.12e9
A=5e-6                    # area del detector 
t=1e-6              # grosor de la lamina objetivo    

theta = np.linspace(10,120,100)*2*np.pi/360  # angulo de dispersion
print(theta*360/(2*np.pi))
#N = (Z*k/(2*r*c))**2 * (N_i*n*L)/E * (e/np.sin(theta/2))**4

#theta=150*2*np.pi/360

# numero particulas dispersadas
N = (I_0*A*n*t/r**2)* (k*Z*e**2/(2*E))**2 * 1/(np.sin(theta/2))**4

# parametro de impacto
#Q=          #carga del nucleo
#m
#v=(2*K/(m_e))**(1/2)          # velocidad de particula incidente
#b = k* e*Q * 1/(m*v**2) * np.cos(theta/2)/np.sin(theta/2)

plt.figure()
plt.plot(theta, N)

