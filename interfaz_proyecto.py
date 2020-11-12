
import vpython as vp
import modulo_particulas as mod 
import modulo_escenarios as esc

vp.scene.title = "Proyecto Practica Docente\n\n"

vp.scene.background = vp.color.black
vp.scene.width = 1000 
vp.scene.height = 600

vp.scene.caption = "\nExperimentos"
vp.scene.append_to_caption("\n caption")

###########
# BOTONES
###########

running = False

def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"

beginButton = vp.button(text="Run", pos=vp.scene.title_anchor, bind=Run)    

def Reset(r):
    pass
    #estado_inicial()
    # para y reinicia la operacion anterior

resetButton = vp.button(text="Reset", pos=vp.scene.title_anchor, bind=Reset)    
    

##############


def Iniciar_aplicacion(m):
    evento = m.selected
    if(evento=="escenario_1"):
        
        # corre programa: 
        t = 0
        dt = 0.1
        
        e1,an1=esc.Escenario1_creacion()
        
        while t<10:
            vp.rate(20)
            ejecutando = running
            
            if(running):  
                esc.Escenario1_avance(ejecutando,e1,an1,dt)  
                t+=dt
                
    #elif(evento=="escenario_2"):
                 
                
                
    
    
vp.menu(choices=["Elige un experimento", "escenario_1", "escenario_2", "esc_3", "esc_4"], index=0, bind=Iniciar_aplicacion)

