
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
#particulas = []
eventoAnterior = "" # lista con el evento anterior

p1=None
p2=None

def Ejecutar(m):
    global algunoEjecutandose, p1, p2, eventoAnterior
    
    # verifica que ningun escenario esté ejecutandose: si True, entonces elimina el escenario en ejecuccion
    if(algunoEjecutandose):
        mod_esc.eliminarAnterior(eventoAnterior)
        
    
    # captura el evento   
    evento = m.selected
    
    
    if(evento == "Escenario1"):
        #for obj in vp.scene.objects:
        #    obj.visible=False
        #    del obj
            
        eventoAnterior = evento
        algunoEjecutandose=True
        
        # corre programa: 
        t = 0
        dt = 0.1
        
        p1,p2=mod_esc.Escenario1_creacion()
        #particulas.append(p1)
        #particulas.append(p2)
       
        while t<10:
            vp.rate(20)
            ejecutando = running
            
            if(running):  
                mod_esc.Escenario1_avance(ejecutando,p1,p2,dt)  
                t+=dt
       
        
    elif(evento == "Escenario2"):
        #del p1
        #del p2
        print(p1,p2)
        #for obj in vp.scene.objects:
        #    obj.visible=False
        #    del obj
        #print("p1 exite? : ", p1)
        #p1.visible=False
        #del p1
        #p2.visible=False
        #del p2
            
        #print("posicion de:" ,p1.posicion)    
        
        #print("p1 exite despues? : ", p1)
        #print(" particulas sí existe: ", particulas)    
            
        eventoAnterior = evento
        algunoEjecutandose=True
        
        # corre programa: 
        t = 0
        dt = 0.1
        
        p1,p2=mod_esc.Escenario2_creacion()
        #particulas.append(p1)
        #particulas.append(p2)
       
        while t<10:
            vp.rate(20)
            ejecutando = running
            
            if(running):  
                mod_esc.Escenario2_avance(ejecutando,p1,p2,dt)  
                t+=dt
                
    elif(evento == "Escenario3"):
        #for obj in vp.scene.objects:
        #    obj.visible=False
        #    del obj
            
        eventoAnterior = evento
        algunoEjecutandose=True          
         
        mod_esc.Escenario3_ejecutar()
                 
       
# Menu de eleccion de escenarios
#    Llama a la funcion Ejecutar(m) y ejecuta el escenario con el evento m correspondiente
vp.menu(choices=["Elige un experimento", "Escenario1", "Escenario2", "Escenario3", "Escenario4"], index=0, bind=Ejecutar)

