## Archivo para crear los escenarios del programa

import vpython as vp
import modulo_particulas as mod

particulas=[]

# Funcion que retorna el arreglo con las particulas del escenario actual
def darParticulas():
    return particulas


##############################################################################
# Escenario 1
##############################################################################

# Funcion que crea las particulas del escenario 1
def Escenario1_creacion():
    global particulas
    particulas.clear()
    
    # creacion de objetos:
    e1 = mod.Electron(vp.vector(-15,0,0), vp.vector(1,0,0), vp.vector(0.1,1,0.7), 0.0005, 1, "electron") 
    an1 = mod.AntineutrinoElectronico(vp.vector(5,0,0), vp.vector(1,0,0), vp.vector(0.8,0.5,0.3), 0.00001, 0.5, "antineutrino")  
    
    particulas.append(e1)
    particulas.append(an1)
    
    print("escenario 1 creacion: ", particulas)
    
    return e1, an1      
   
# Funcion que da avance al escenario 1     
def Escenario1_avance(ejecutando,e1,an1,dt):    # funciona bien
    if(ejecutando):
        # evolucion del sistema  
        e1.evolucion_temporal(dt)
        an1.evolucion_temporal(dt)  
        
        
# Funcion que elimina el escenario 1    
def Escenario1_destruccion(e1, an1):        # no funciona bien
    e1.eliminar()
    an1.eliminar()
    
    

##############################################################################
# Escenario 2
##############################################################################    
# Funcion que crea las particulas del escenario 2
def Escenario2_creacion():
    global particulas
    particulas.clear()
    print("lista vacia? :", particulas)
    # creacion de objetos:
    alfa = mod.Alpha(vp.vector(-15,0,0), vp.vector(1,0,0), vp.vector(0.1,1,0.7), 6.64e-27, 2, "Particula \n alpha" )
    nucleo = mod.Nucleo(vp.vector(5,0,0), vp.vector(1,0,0), vp.vector(0.8,0.5,0.3), 0.001, 1, "Nucleo \n (target)")  
    
    particulas.append(alfa)
    particulas.append(nucleo)
    print("lista con alfa y nucleo : ", particulas)
    
    #print("escenario 2 creacion: ", particulas)
    
    return alfa, nucleo      
   
# Funcion que da avance al escenario 2     
def Escenario2_avance(ejecutando,alfa,nucleo,dt):    # funciona bien
    if(ejecutando):
        # evolucion del sistema  
        alfa.evolucion_temporal(dt)
        nucleo.evolucion_temporal(dt)  
        
        
# Funcion que elimina el escenario 2  
def Escenario2_destruccion(alfa, nucleo):        # no funciona bien
    alfa.eliminar()
    nucleo.eliminar()   
    
        



# Elimina el escenario anteior que se está ejecutando 
def eliminarAnterior(eventoAnterior: str):
    if(eventoAnterior=="Escenario1"): 
        Escenario1_destruccion(particulas[0], particulas[1])
    elif(eventoAnterior=="Escenario2"):
        Escenario2_destruccion(particulas[0], particulas[1])
    
    #...

   

                
