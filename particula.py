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


def up(posicion,velocidad):
	color=vector(0.5,0.1,1)
	masa=0.002
	radio=1
	nombre="Up"
	s=sphere(pos=posicion,radius=radio,color=color, make_trail=True,shininess=1,masa=masa)
	nombre=label(pos=posicion, text=nombre, color=vector(0.1,1,0.7), opacity=0.7, height=15, box=0)
	return s,nombre

def down(posicion,velocidad):
	color=vector(0.4,0.8,0)
	masa=0.005
	radio=1
	nombre="Down"
	s=sphere(pos=posicion,radius=radio,color=color, make_trail=True,shininess=1,masa=masa)
	nombre=label(pos=posicion, text=nombre, color=vector(0.1,1,0.7), opacity=0.7, height=15, box=0)
	return s,nombre
class neutron:
	"""docstring for ClassName"""
	def __init__(self, posicion,velocidad,lado):
		#atributos del neutron
		self.posicion=posicion
		self.lado=lado
		self.velocidad=velocidad
		self.apotema=(3)**0.5*lado/6

		#creacion de las particulas que comonen en neutron con sus respectivos nombres
		self.up1,self.name_up1=up(vector(posicion.x,posicion.y+(self.apotema**2+(lado/2)**2)**0.5,posicion.z),self.velocidad)
		self.up2,self.name2=up(vector(posicion.x,posicion.y-self.apotema,posicion.z+(lado/2)),self.velocidad)
		self.down1,self.name3=down(vector(posicion.x,posicion.y-self.apotema,posicion.z-(lado/2)),self.velocidad)
		#propiedades de los resortes
		radio_string=0.4
		color_string=color.white
		#creacion de los resortes
		self.resorte12=helix(pos=self.up1.pos, axis=vector(0,-(3)**0.5*self.lado/2,-0.5*lado), radius=radio_string,color=color_string)
		self.resorte13=helix(pos=self.up2.pos, axis=vector(0,(3)**0.5*self.lado/2,-self.lado/2), radius=radio_string,color=color_string)
		self.resorte23=helix(pos=self.down1.pos, axis=vector(0,0,self.lado), radius=radio_string,color=color_string)
	def evolucion_temporal(self,dt):
		#movimiento de las particulas
		self.up1.pos=vector(self.up1.pos.x+(self.velocidad.x*dt),self.up1.pos.y+(self.velocidad.y*dt),self.up1.pos.z+(self.velocidad.z*dt))
		self.up2.pos=vector(self.up2.pos.x+(self.velocidad.x*dt),self.up2.pos.y+(self.velocidad.y*dt),self.up2.pos.z+(self.velocidad.z*dt))
		self.down1.pos=vector(self.down1.pos.x+(self.velocidad.x*dt),self.down1.pos.y+(self.velocidad.y*dt),self.down1.pos.z+(self.velocidad.z*dt))
		#movimiento de los resortes
		self.resorte12.pos=vector(self.resorte12.pos.x+(self.velocidad.x*dt),self.resorte12.pos.y+(self.velocidad.y*dt),self.resorte12.pos.z+(self.velocidad.z*dt))
		self.resorte13.pos=vector(self.resorte13.pos.x+(self.velocidad.x*dt),self.resorte13.pos.y+(self.velocidad.y*dt),self.resorte13.pos.z+(self.velocidad.z*dt))
		self.resorte23.pos=vector(self.resorte23.pos.x+(self.velocidad.x*dt),self.resorte23.pos.y+(self.velocidad.y*dt),self.resorte23.pos.z+(self.velocidad.z*dt))
	def eliminar(self):
		self.up1.visible=False
		self.up2.visible=False
		self.down1.visible=False
		self.resorte12.visible=False
		self.resorte13.visible=False
		self.resorte23.visible=False