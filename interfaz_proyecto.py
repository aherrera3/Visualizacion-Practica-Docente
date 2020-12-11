## Archivo con la creacion de la interfaz y llamado de la creacion de escenarios

import vpython as vp
import modulo_escenarios as mod_esc

vp.scene.title = "                                                                                  <b>Proyecto Practica Docente</b>\n\n"
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
    if menu.selected=="Escenario1": mod_esc.escenario1_reiniciar()
    elif menu.selected=="Escenario2": mod_esc.escenario2_reiniciar()
    elif menu.selected=="Escenario3": mod_esc.escenario3_reiniciar()
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
    particula_enfocada= ~particula_enfocada

def getevent():
    hit = vp.scene.mouse.pick #selecciona cualquie objeto
    #vp.scene.camera.pos=hit.pos
    #print(hit.pos)
    
    global particula_enfocada
    
    zoom=vp.vector(0,0,29)
    try:
        if particula_enfocada == False:
            identificador=hit.iden
            print(identificador)
        mover_camara(hit.pos-zoom)
        
    except:
        mover_camara(vp.vector(30, 10, 17.3205))

def Ejecutar(m):
    global t
    vp.scene.userzoom = True 
    vp.scene.userspin = True 
    vp.scene.pan = True 
    vp.scene.autoscale=True

    vp.scene.unbind('mousedown', getevent)
    mod_esc.limpiar_escenario()
    
    # captura el evento   
    evento = m.selected    
    
    if(evento == "Escenario1"):
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
        #vp.scene.caption = message[0]
        vp.scene.caption=mensaje()

        #vp.scene.camera.pos=vp.vector(0,20,-10)
        print(vp.scene.camera.pos)

    elif(evento == "Escenario2"):
        dt = 0.001
        
        mod_esc.escenario2_creacion()
        vp.scene.caption = message[1]
        vp.scene.camera.pos=vp.vector(0, 0, 17.3205)
        while True:
            vp.rate(5000)
            
            if(running):
                mod_esc.escenario2_avance(dt)
            if(mod_esc.n>30):
                print(mod_esc.n)    
                break
            
    elif(evento == "Escenario3"):    
        dt = 0.0001
        
        mod_esc.escenario3_creacion()
        vp.scene.caption = message[2]
        vp.scene.camera.pos=vp.vector(0, 0, 14)
        while True:
            vp.rate(30000)
            try:
                if (running):
                    mod_esc.escenario3_avance(dt)
                if mod_esc.n >100:
                    break
            except:
                break

       
vp.wtext(pos=vp.scene.title_anchor, text="                                                                                                                                               ")

# Menu de eleccion de escenarios
#    Llama a la funcion Ejecutar(m) y ejecuta el escenario con el evento m correspondiente
menu=vp.menu(choices=["Elige un escenario", "Escenario1", "Escenario2", "Escenario3"], index=0, pos=vp.scene.title_anchor, bind=Ejecutar)


message = ['''\n Caraterísticas de partículas fundamentales
           ''', '''\n Scattering de Partículas alpha...
        Otralinea ...''', '''\n Scattering de Compton ...
        Otralinea ...''']
        
def mensaje():
    global message, particula_enfocada
    if(particula_enfocada):
        message[0].append("img bosonZ = 'bosonZ.png'")
        
        

#vp.scene.caption = '''\n Experimentos demostrativos ...
#otra linea ...
#Otralinea ...'''

vp.scene.append_to_caption('                     ')
vp.scene.append_to_caption('\n')

