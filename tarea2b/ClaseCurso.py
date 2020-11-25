import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import sys



import transformations as tr
import basic_shapes as bs
import scene_graph as sg
import easy_shaders as es

#Aqui se hará un intento para crear una clase llamada curso, la cual va a contener la posicion del cubo, la info (requisitos) y el
#nombre del curso 

class Curso:
	def __init__(self,c,r,px,py,pz, rd = []):
		#assert (type(px) is float) and (type(py) is float) and (type(pz) is float)

		self.codigo = c
		self.requisitos = r
		self.requisitosDe = rd
		self.posicion = (px,py,pz)


