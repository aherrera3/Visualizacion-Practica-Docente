from vpython import*

#make_trail hace que la partícula tenga una trayectoria visiblea

def electron(posicion,velocidad):
	color=vector(0.1,1,0.7)
	masa=0.0005
	radio=1
	nombre="Electrón"
	s=sphere(pos=posicion,radius=radio,color=color, make_trail=True,shininess=0,masa=masa,velocidad=velocidad)
	nombre=label(pos=posicion, text=nombre, color=vector(0.1,1,0.7), opacity=0.7, height=15, box=0)
	return s,nombre
def antineutrino_electronico(posicion,velocidad):
	color=vector(0.9,0,0)
	masa=0.0005/10000
	radio=0.5
	nombre="Antineutrino electronico"
	s=sphere(pos=posicion,radius=radio,color=color, make_trail=True,shininess=0,masa=masa,velocidad=velocidad)
	nombre=label(pos=posicion, text=nombre, color=vector(1,1,1), opacity=0.4, height=15, box=0)
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
class proton:
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
		self.up1.pos=vector(self.up1.pos + self.velocidad*dt)
		self.up2.pos=vector(self.up2.pos + self.velocidad*dt)
		self.down1.pos=vector(self.down1.pos+self.velocidad*dt)
		#movimiento de los resortes
		self.resorte12.pos=vector(self.resorte12.pos +self.velocidad*dt)
		self.resorte13.pos=vector(self.resorte13.pos +self.velocidad*dt)
		self.resorte23.pos=vector(self.resorte23.pos + self.velocidad*dt)
		#movimiento de la particula en general
		self.posicion=vector(self.posicion+self.velocidad*dt)
	def eliminar(self):
		self.up1.visible=False
		self.up2.visible=False
		self.down1.visible=False
		self.resorte12.visible=False
		self.resorte13.visible=False
		self.resorte23.visible=False
	def crear(self):
		self.up1.visible=True
		self.up2.visible=True
		self.down1.visible=True
		self.resorte12.visible=True
		self.resorte13.visible=True
		self.resorte23.visible=True
	def mover(self, posicion):
		self.posicion=posicion
		self.up1.pos=vector(posicion.x,posicion.y+(self.apotema**2+(self.lado/2)**2)**0.5,posicion.z)
		self.up1.clear_trail()
		self.up2.pos=vector(posicion.x,posicion.y-self.apotema,posicion.z+(self.lado/2))
		self.up2.clear_trail()
		self.down1.pos=vector(posicion.x,posicion.y-self.apotema,posicion.z-(self.lado/2))
		self.down1.clear_trail()
		self.resorte12.pos=self.up1.pos
		self.resorte13.pos=self.up2.pos
		self.resorte23.pos=self.down1.pos
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
		self.down2,self.name2=down(vector(posicion.x,posicion.y-self.apotema,posicion.z+(lado/2)),self.velocidad)
		self.down1,self.name3=down(vector(posicion.x,posicion.y-self.apotema,posicion.z-(lado/2)),self.velocidad)
		#propiedades de los resortes
		radio_string=0.4
		color_string=color.white
		#creacion de los resortes
		self.resorte12=helix(pos=self.up1.pos, axis=vector(0,-(3)**0.5*self.lado/2,-0.5*lado), radius=radio_string,color=color_string)
		self.resorte13=helix(pos=self.down2.pos, axis=vector(0,(3)**0.5*self.lado/2,-self.lado/2), radius=radio_string,color=color_string)
		self.resorte23=helix(pos=self.down1.pos, axis=vector(0,0,self.lado), radius=radio_string,color=color_string)
	def evolucion_temporal(self,dt):
		#movimiento de las particulas
		self.up1.pos=vector(self.up1.pos+self.velocidad*dt)
		self.down2.pos=vector(self.down2.pos+self.velocidad*dt)
		self.down1.pos=vector(self.down1.pos+self.velocidad*dt)
		#movimiento de los resortes
		self.resorte12.pos=vector(self.resorte12.pos + self.velocidad*dt)
		self.resorte13.pos=vector(self.resorte13.pos + self.velocidad*dt)
		self.resorte23.pos=vector(self.resorte23.pos + self.velocidad*dt)
		#movimiento de la particula en general
		self.posicion=vector(self.posicion + self.velocidad*dt)
	def eliminar(self):
		self.up1.visible=False
		self.down2.visible=False
		self.down1.visible=False
		self.resorte12.visible=False
		self.resorte13.visible=False
		self.resorte23.visible=False
	def crear(self):
		self.up1.visible=True
		self.down2.visible=True
		self.down1.visible=True
		self.resorte12.visible=True
		self.resorte13.visible=True
		self.resorte23.visible=True
	def mover(self, posicion):
		self.posicion=posicion
		self.up1.pos=vector(posicion.x,posicion.y+(self.apotema**2+(self.lado/2)**2)**0.5,posicion.z)
		self.up1.clear_trail()
		self.down2.pos=vector(posicion.x,posicion.y-self.apotema,posicion.z+(self.lado/2))
		self.down2.clear_trail()
		self.down1.pos=vector(posicion.x,posicion.y-self.apotema,posicion.z-(self.lado/2))
		self.down1.clear_trail()
		self.resorte12.pos=self.up1.pos
		self.resorte13.pos=self.down2.pos
		self.resorte23.pos=self.down1.pos