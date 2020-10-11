from vpython import*

#make_trail hace que la partícula tenga una trayectoria visible


def electron(posicion,velocidad):
	color=vector(0.1,1,0.7)
	masa=0.0005
	radio=1
	nombre="electron"
	s=sphere(pos=posicion,radius=radio,color=color, make_trail=True,shininess=0,masa=masa)
	nombre=label(pos=posicion, text=nombre, color=vector(0.1,1,0.7), opacity=0.7, height=15, box=0)
	return s,nombre

def muon(posicion,velocidad):
	color=vector(0.9,0,1)
	masa=0.106
	radio=2
	nombre="Muon"
	s=sphere(pos=posicion,radius=radio,color=color, make_trail=True,shininess=0,masa=masa)
	nombre=label(pos=posicion, text=nombre, color=vector(0.1,1,0.7), opacity=0.7, height=15, box=0)
	return s,nombre