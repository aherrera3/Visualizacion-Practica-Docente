## Archivo con la creacion de la interfaz y llamado de la creacion de escenarios
# -*- coding: utf-8 -*-

import vpython as vp
import modulo_escenarios as mod_esc

vp.scene.title = "                                                                     <b>Visualizacion proyecto Practica Docente</b>\n\n"
vp.scene.background = vp.color.black
vp.scene.width = 1000 
vp.scene.height = 600

# BOTONES
running = False

def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"

vp.button(text="Run", pos=vp.scene.title_anchor, bind=Run)    

t = 0
def Reset(r):
    global t
    t=0
    if menu.selected=="Informacion": mod_esc.escenario1_reiniciar()
    elif menu.selected=="Rutherford Scattering": mod_esc.escenario2_reiniciar()
    elif menu.selected=="Compton Scattering": mod_esc.escenario3_reiniciar()
    Ejecutar(menu)

vp.button(text="Reset", pos=vp.scene.title_anchor, bind=Reset)    

particula_enfocada=False
def mover_camara(posicion_nueva):
    global particula_enfocada
    pos_actual=vp.scene.camera.pos
    pos_original=vp.vector(30, 10, 17.3205)
    if particula_enfocada:
        distancia = pos_original - pos_actual
    else:
        distancia = posicion_nueva - pos_actual
    distancia_x = distancia.x
    distancia_y = distancia.y
    distancia_z = distancia.z
    pasos=50
    dx=distancia_x/pasos
    dy=distancia_y/pasos
    dz=distancia_z/pasos
    n=0
    while True:
        vp.rate(50)
        vp.scene.camera.pos=vp.scene.camera.pos + vp.vector(dx,dy,dz)
        n+=1
        if n==50:
            break
    if particula_enfocada:
        vp.scene.camera.pos=pos_original
    particula_enfocada= not particula_enfocada

def getevent():
    hit = vp.scene.mouse.pick #selecciona cualquier objeto
    #vp.scene.camera.pos=hit.pos
    #print(hit.pos)
    
    global particula_enfocada, identificador
    
    zoom=vp.vector(0,0,29)
    try:
        if particula_enfocada == False:
            identificador=hit.iden
            print("id",identificador)
        agregar_mensaje_escenario1(identificador)
        mover_camara(hit.pos-zoom)
        print(vp.scene.camera.pos)
    except:
        mover_camara(vp.vector(30, 10, 17.3205))
        vp.scene.camera.fov=60
        print(vp.scene.camera.pos)


mensaje_adicional_inicial = "\n                                             "+'<img src="imagenes/tablaParticulas.png" width=500 height=500>'
message = ["""\n                                                                  <b>Carateristicas de particulas fundamentales</b>\n """+mensaje_adicional_inicial,
           '''\n                                                                      <b>Scattering de Partículas alpha</b>\n''',
           '''\n                                                                      <b>Scattering de Compton</b>\n ''']
        
def agregar_mensaje_escenario1(identificador:str):
    global message
    if particula_enfocada==False:
            message[0]="""\n                                                                 <b>Carateristicas de particulas fundamentales</b>\n """
            mensaje = mod_esc.dar_mensaje_escenario1(identificador)
            message[0]+="\n"+mensaje+"\n"
    else:
        message[0]="""\n                                                                 <b>Carateristicas de particulas fundamentales</b> """+mensaje_adicional_inicial
    vp.scene.caption=message[0]   # se agrega el mensaje al escenario1    
    

def Ejecutar(m):
    global t, message
    vp.scene.userzoom = True 
    vp.scene.userspin = True 
    vp.scene.pan = True 
    vp.scene.autoscale=True

    vp.scene.unbind('mousedown', getevent)
    mod_esc.limpiar_escenario()
    
    # captura el evento   
    evento = m.selected    
    
    if(evento == "Informacion"):
        # corre programa: 
        vp.scene.bind("mousedown", getevent) #define lo que sucede si se hace clik
        t = 0
        dt = 0.001
        vp.scene.userzoom = False # no puede hacer zoom
        vp.scene.userspin = False # no puede girar la escena
        vp.scene.pan = False #no puede mover la escena 
        print(vp.scene.camera.pos)
        vp.scene.camera.pos=vp.vector(30, 10, 17.3205)

        mod_esc.escenario1_creacion()
        vp.scene.caption = message[0]

        #vp.scene.camera.pos=vp.vector(0,20,-10)
        print(vp.scene.camera.pos)

    elif(evento == "Rutherford Scattering"):
        dt = 0.01
        
        mod_esc.escenario2_creacion()
        vp.scene.caption = message[1]
        vp.scene.camera.pos=vp.vector(0, 0, 17.3205)
        while True:
            vp.rate(500)
            if running:
                mod_esc.escenario2_avance(dt)
            if mod_esc.n==50:  
                # se genera la grafica
                mod_esc.grafica_rutherford(mod_esc.discretizar_angulos(mod_esc.theta))
                message[1]+=" \n                            "+'<img src="imagenes/rutherfordGraph.png" width=700 height=300>\n\n'
                vp.scene.caption = message[1]
                break
            
    elif(evento == "Compton Scattering"):    
        dt = 0.01
        
        mod_esc.escenario3_creacion()
        vp.scene.caption = message[2]
        vp.scene.camera.pos=vp.vector(0, 0, 14)
        while True:
            vp.rate(500)
            try:
                if running:
                    mod_esc.escenario3_avance(dt)
                if mod_esc.n >50:
                    break
            except:
                break
            
    else: # el evento == "Elige un escenario"        
         vp.scene.caption =""
            

       
vp.wtext(pos=vp.scene.title_anchor, text="                                                                                                                                           ")

# Menu de eleccion de escenarios
#    Llama a la funcion Ejecutar(m) y ejecuta el escenario con el evento m correspondiente
menu=vp.menu(choices=["Elige un escenario", "Informacion", "Rutherford Scattering", "Compton Scattering"], index=0, pos=vp.scene.title_anchor, bind=Ejecutar)

        
#vp.scene.caption = '''\n Experimentos demostrativos ...
#otra linea ...
#Otralinea ...'''

vp.scene.append_to_caption('                     ')
vp.scene.append_to_caption('\n')

