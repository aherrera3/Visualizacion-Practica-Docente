
import vpython as vp
import modulo_escenarios as mod_esc

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

algunoEjecutandose = False

def Ejecutar(m):
    # captura el evento   
    evento = m.selected
    global algunoEjecutandose
    
    # verifica que ningun esté ejecutandose:
    #        si False, entonces elimina el escenario actual en ejecuccion
    #if(algunoEjecutandose):
    #    esc.eliminarEjecutandose(evento)
    
    p1=None
    p2=None
    
    if(evento == "Escenario1"):
        algunoEjecutandose=True
        
        # corre programa: 
        t = 0
        dt = 0.1
        
        p1,p2=mod_esc.Escenario1_creacion()
       
        while t<10:
            vp.rate(20)
            ejecutando = running
            
            if(running):  
                mod_esc.Escenario1_avance(ejecutando,p1,p2,dt)  
                t+=dt
       
                
    elif(evento == "Escenario2"):
        algunoEjecutandose=True
        if(p1!=None and p2!=None):
            mod_esc.Escenario1_destruccion(p1,p2)
        
       
                 
       
# Menu de eleccion de escenarios
#    Llama a la funcion Ejecutar(m) y ejecuta el escenario con el evento m correspondiente
vp.menu(choices=["Elige un experimento", "Escenario1", "Escenario2", "Escenario3", "Escenario4"], index=0, bind=Ejecutar)

