
import vpython as vp
import modulo_escenarios as mod_esc

vp.scene.title = "                                                                                  <b>Proyecto Practica Docente</b>\n\n"
vp.scene.background = vp.color.black
vp.scene.width = 1000 
vp.scene.height = 600
vp.scene.caption = "\n ... "


# BOTONES

running = False
seOprimioReset = False
evento = ""

def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"

beginButton = vp.button(text="Run", pos=vp.scene.title_anchor, bind=Run)    

def Reset(r):
    #global running, evento
    pass
    #mod_esc.escenario1_reiniciar()
    #seOprimioReset = True
    #if(running):
    #    Ejecutar(evento)
    #estado_inicial()
    # para y reinicia la operacion anterior

resetButton = vp.button(text="Reset", pos=vp.scene.title_anchor, bind=Reset)    


##############
def Ejecutar(m):
    global seOprimioReset, evento
    
    if(seOprimioReset==False):
        mod_esc.limpiar_escenario()
        
        # captura el evento   
        evento = m.selected    
    
    if(evento == "Escenario1"):
        # corre programa: 
        t = 0
        dt = 0.001
        
        if(seOprimioReset==False):
            mod_esc.escenario1_creacion()
        
        while True:
            vp.rate(12000)
            ejecutando = running
            
            if(running):  
                mod_esc.escenario1_avance(ejecutando,dt)  
                t+=dt
            if t>10:
                break
            
        #if(seOprimioReset):
            #seOprimioReset = False
            #Ejecutar(m)
            
        
    elif(evento == "Escenario2"):
        # corre programa: 
        t = 0
        dt = 0.001
        
        mod_esc.escenario2_creacion()
        
        while True:
            vp.rate(12000)
            ejecutando = running
            
            if(running):  
                mod_esc.escenario2_avance(ejecutando,dt)  
                t+=dt
            if t>10:
                break
            
    elif(evento == "Escenario3"):    
        mod_esc.escenario3_creacion()
        dt = 0.001
        while True:
            vp.rate(12000)
            ejecutando = running
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
vp.menu(choices=["Elige un experimento", "Escenario1", "Escenario2", "Escenario3", "Escenario4"], index=0, pos=vp.scene.title_anchor, bind=Ejecutar)


vp.scene.append_to_caption('                     ')
vp.scene.append_to_caption('\n')
