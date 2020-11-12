
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
# en carpeta ESCENARIOS
##############


##############


def Iniciar_aplicacion(m):
    evento = m.selected
    if(evento=="escenario_1"):
        
        # corre programa: 
        t = 0
        dt = 0.1

        e1 = mod.Electron(vp.vector(-15,0,0), vp.vector(1,0,0), vp.vector(0.1,1,0.7), 0.0005, 1, "electron") 

        # antineutrino
        an1 = mod.AntineutrinoElectronico(vp.vector(5,0,0), vp.vector(1,0,0), vp.vector(0.8,0.5,0.3), 0.00001, 0.5, "antineutrino")  
  
        while t<10:
            vp.rate(20)
            if(running):
                # evolucion del sistema  
                e1.evolucion_temporal(dt)
                an1.evolucion_temporal(dt)    
        #while t<10:
         #   vp.rate(20)
          #  ejecutando = running
           # esc.Escenario1(ejecutando, dt)
            #if(running):  
                #esc.Escenario1(dt)
                #e1.evolucion_temporal(dt)
                #an1.evolucion_temporal(dt)    
                t+=dt
    
    
vp.menu(choices=["Elige un experimento", "escenario_1", "esc_2", "esc_3", "esc_4"], index=0, bind=Iniciar_aplicacion)

