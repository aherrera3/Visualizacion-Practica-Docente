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


##############
def Ejecutar(m):
    global t
    
    mod_esc.limpiar_escenario()
    
    # captura el evento   
    evento = m.selected    
    
    if(evento == "Escenario1"):
        # corre programa: 
        t = 0
        dt = 0.001
        vp.scene.userzoom = False # no puede hacer zoom
        vp.scene.userspin = False # no puede girar la escena
        vp.scene.pan = False #no puede mover la escena 
        print(vp.scene.camera.pos)
        vp.scene.camera.pos=vp.vector(0, 0, 17.3205)

        mod_esc.escenario1_creacion()
        vp.scene.caption = message[0]

        #vp.scene.camera.pos=vp.vector(0,20,-10)
        print(vp.scene.camera.pos)
        """
        while True:
            vp.rate(12000)
            ejecutando = running
            
            if(running):  
                mod_esc.escenario1_avance(ejecutando,dt)  
                t+=dt
            if t>10:
                break
        """
    elif(evento == "Escenario2"):
        dt = 0.001
        
        mod_esc.escenario2_creacion()
        vp.scene.caption = message[1]
        
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
menu=vp.menu(choices=["Elige un experimento", "Escenario1", "Escenario2", "Escenario3", "Escenario4"], index=0, pos=vp.scene.title_anchor, bind=Ejecutar)


message = ['''\n Experimento demostrativo 1 ...
        Efecto Fotoeléctrico ...
        Otralinea ...''', '''\n Experimento demostrativo 2 ...
        Scattering de Partículas alpha...
        Otralinea ...''', '''\n Experimento demostrativo 3 ...
        Scattering de Compton ...
        Otralinea ...''', '''\n Experimento demostrativo 4 ...
        Decaimiento beta negativo ...
        Otralinea ...''']

#vp.scene.caption = '''\n Experimentos demostrativos ...
#otra linea ...
#Otralinea ...'''

vp.scene.append_to_caption('                     ')
vp.scene.append_to_caption('\n')

