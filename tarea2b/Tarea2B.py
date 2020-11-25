import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import sys



import transformations as tr
import basic_shapes as bs
import scene_graph as sg
import easy_shaders as es
import ClaseCurso as cc
import ex_curves as cur


# A class to store the application control
class Controller:
	def __init__(self):
		self.fillPolygon = True
		self.semestre = 0
		self.curso = 0
		self.x = 0
		self.y = 0
		self.z = 0
		self.uno = False
		self.dos = False
		self.shift = True
		self.fondoE = "C"



# we will use the global controller as communication with the callback function
controller = Controller()


def on_key(window, key, scancode, action, mods):

	if action != glfw.PRESS:
		return
	
	global controller

	if key == glfw.KEY_SPACE:
		controller.fillPolygon = not controller.fillPolygon

	elif key == glfw.KEY_LEFT_CONTROL:
		controller.showAxis = not controller.showAxis

	elif key == glfw.KEY_A:
		controller.curso -= 1 
		controller.shift = True
		#print("apretando A")

	elif key == glfw.KEY_S:
		controller.semestre += 1
		controller.shift = True
		#print("apretando S")

	elif key == glfw.KEY_D:
		controller.curso += 1
		controller.shift = True
		#print("apretando D")


	elif key == glfw.KEY_W:
		controller.semestre -= 1
		controller.shift = True
		#print("apretando W")

	elif key == glfw.KEY_C:
		controller.fondoE = "C"

	elif key == glfw.KEY_O:
		controller.fondoE = "O"

	elif key == glfw.KEY_R:
		controller.fondoE = "R"

	elif key == glfw.KEY_LEFT:
		#print("apretando flecha izquierda")
		pass

	elif key == glfw.KEY_RIGHT:
		#print("apretando flecha derecha")
		pass

	elif key == glfw.KEY_UP:
		#print("apretando flecha arriba")
		pass

	elif key == glfw.KEY_DOWN:
		#print("apretando flecha abajo")
		pass

	elif key == glfw.KEY_1:
		controller.uno = not controller.uno
		#print("apretando 1")

	elif key == glfw.KEY_2:
		controller.dos = not controller.dos
		#print("apretando 2")

	elif key == glfw.KEY_Z:
		#print("apretando Z")
		pass

	elif key == glfw.KEY_X:
		#print("apretando X")
		pass 

	elif key == glfw.KEY_ESCAPE:
		sys.exit()

	else:
		print('Unknown key')


def crearCubos():
	NormalCube = es.toGPUShape(bs.createTextureCube("base.png"),GL_REPEAT, GL_NEAREST)
	RequisitoDeCube = es.toGPUShape(bs.createTextureCube("base1.png"),GL_REPEAT, GL_NEAREST)
	SelectedCube = es.toGPUShape(bs.createTextureCube("base4.png"),GL_REPEAT, GL_NEAREST)
	RequisitoCube = es.toGPUShape(bs.createTextureCube("base3.png"),GL_REPEAT, GL_NEAREST)

	#Aqui se comienzan a crear los cubos de base 

	cuboRojo = sg.SceneGraphNode("cuboRojo") #Se crea la base para el cubo morado
	cuboRojo.transform = tr.uniformScale(0.5)
	cuboRojo.childs += [NormalCube]

	CuboTurquesa = sg.SceneGraphNode("CuboTurquesa")
	CuboTurquesa.transform = tr.uniformScale(0.5)
	CuboTurquesa.childs += [RequisitoDeCube]

	CuboCeleste = sg.SceneGraphNode("CuboCeleste")
	CuboCeleste.transform = tr.uniformScale(0.5)
	CuboCeleste.childs += [RequisitoCube]

	CuboNaranjo = sg.SceneGraphNode("CuboNaranjo")
	CuboNaranjo.transform = tr.uniformScale(0.5)
	CuboNaranjo.childs += [SelectedCube]

	return cuboRojo,CuboTurquesa,CuboCeleste,CuboNaranjo


def crearCurso(cubo):

	cuboRojo = cubo

	#Primer año
	DP101 =  es.toGPUShape(bs.createTextureQuad("DP_101.png"),GL_REPEAT, GL_NEAREST)
	DP102 =  es.toGPUShape(bs.createTextureQuad("DP_102.png"),GL_REPEAT, GL_NEAREST)
	DP103 =  es.toGPUShape(bs.createTextureQuad("DP_103.png"),GL_REPEAT, GL_NEAREST)
	DT104 =  es.toGPUShape(bs.createTextureQuad("DT_104.png"),GL_REPEAT, GL_NEAREST)
	DT105 =  es.toGPUShape(bs.createTextureQuad("DT_105.png"),GL_REPEAT, GL_NEAREST)
	DH106 =  es.toGPUShape(bs.createTextureQuad("DH_106.png"),GL_REPEAT, GL_NEAREST)
	DH107 =  es.toGPUShape(bs.createTextureQuad("DH_107.png"),GL_REPEAT, GL_NEAREST)
	DH108 =  es.toGPUShape(bs.createTextureQuad("DH_108.png"),GL_REPEAT, GL_NEAREST)

	#Segundo año
	DGP201 =  es.toGPUShape(bs.createTextureQuad("DGP_201.png"),GL_REPEAT, GL_NEAREST)
	DGP202 =  es.toGPUShape(bs.createTextureQuad("DGP_202.png"),GL_REPEAT, GL_NEAREST)
	DGP203 =  es.toGPUShape(bs.createTextureQuad("DGP_203.png"),GL_REPEAT, GL_NEAREST)
	DGT204 =  es.toGPUShape(bs.createTextureQuad("DGT_204.png"),GL_REPEAT, GL_NEAREST)
	DGT205 =  es.toGPUShape(bs.createTextureQuad("DGT_205.png"),GL_REPEAT, GL_NEAREST)
	DGH206 =  es.toGPUShape(bs.createTextureQuad("DGH_206.png"),GL_REPEAT, GL_NEAREST)
	DGH207 =  es.toGPUShape(bs.createTextureQuad("DGH_207.png"),GL_REPEAT, GL_NEAREST)
	DGH208 =  es.toGPUShape(bs.createTextureQuad("DGH_208.png"),GL_REPEAT, GL_NEAREST)

	#Quinto Semestre 
	DGP301 =  es.toGPUShape(bs.createTextureQuad("DGP_301.png"),GL_REPEAT, GL_NEAREST)
	DGT302 =  es.toGPUShape(bs.createTextureQuad("DGT_302.png"),GL_REPEAT, GL_NEAREST)
	DGT303 =  es.toGPUShape(bs.createTextureQuad("DGT_303.png"),GL_REPEAT, GL_NEAREST)
	DGT304 =  es.toGPUShape(bs.createTextureQuad("DGT_304.png"),GL_REPEAT, GL_NEAREST)
	DGH305 =  es.toGPUShape(bs.createTextureQuad("DGH_305.png"),GL_REPEAT, GL_NEAREST)
	DGH306 =  es.toGPUShape(bs.createTextureQuad("DGH_306.png"),GL_REPEAT, GL_NEAREST)
	DGH307 =  es.toGPUShape(bs.createTextureQuad("DGH_307.png"),GL_REPEAT, GL_NEAREST)
	DE1 =  es.toGPUShape(bs.createTextureQuad("DE_1.png"),GL_REPEAT, GL_NEAREST)

	#Sexto Semestre 
	DGP401 =  es.toGPUShape(bs.createTextureQuad("DGP_401.png"),GL_REPEAT, GL_NEAREST)
	DGT402 =  es.toGPUShape(bs.createTextureQuad("DGT_402.png"),GL_REPEAT, GL_NEAREST)
	DGT403 =  es.toGPUShape(bs.createTextureQuad("DGT_403.png"),GL_REPEAT, GL_NEAREST)
	DGT404 =  es.toGPUShape(bs.createTextureQuad("DGT_404.png"),GL_REPEAT, GL_NEAREST)
	DGH405 =  es.toGPUShape(bs.createTextureQuad("DGH_405.png"),GL_REPEAT, GL_NEAREST)
	DGH406 =  es.toGPUShape(bs.createTextureQuad("DGH_406.png"),GL_REPEAT, GL_NEAREST)
	DGH407 =  es.toGPUShape(bs.createTextureQuad("DGH_407.png"),GL_REPEAT, GL_NEAREST)
	DE2 =  es.toGPUShape(bs.createTextureQuad("DE_2.png"),GL_REPEAT, GL_NEAREST)

	#Septimo Semestre
	DGP501 =  es.toGPUShape(bs.createTextureQuad("DGP_501.png"),GL_REPEAT, GL_NEAREST)
	DGP502 =  es.toGPUShape(bs.createTextureQuad("DGP_502.png"),GL_REPEAT, GL_NEAREST)
	DGT503 =  es.toGPUShape(bs.createTextureQuad("DGT_503.png"),GL_REPEAT, GL_NEAREST)
	DGH504 =  es.toGPUShape(bs.createTextureQuad("DGH_504.png"),GL_REPEAT, GL_NEAREST)
	DGH505 =  es.toGPUShape(bs.createTextureQuad("DGH_505.png"),GL_REPEAT, GL_NEAREST)
	DGH506 =  es.toGPUShape(bs.createTextureQuad("DGH_506.png"),GL_REPEAT, GL_NEAREST)
	DGH507 =  es.toGPUShape(bs.createTextureQuad("DGH_507.png"),GL_REPEAT, GL_NEAREST)
	DE3 =  es.toGPUShape(bs.createTextureQuad("DE_2.png"),GL_REPEAT, GL_NEAREST)


	#Octavo Semestre
	DGP601 =  es.toGPUShape(bs.createTextureQuad("DGP_601.png"),GL_REPEAT, GL_NEAREST)
	DGP602 =  es.toGPUShape(bs.createTextureQuad("DGP_602.png"),GL_REPEAT, GL_NEAREST)
	DGT603 =  es.toGPUShape(bs.createTextureQuad("DGT_603.png"),GL_REPEAT, GL_NEAREST)
	DGH604 =  es.toGPUShape(bs.createTextureQuad("DGH_604.png"),GL_REPEAT, GL_NEAREST)
	DGH605 =  es.toGPUShape(bs.createTextureQuad("DGH_605.png"),GL_REPEAT, GL_NEAREST)
	DGH606 =  es.toGPUShape(bs.createTextureQuad("DGH_606.png"),GL_REPEAT, GL_NEAREST)
	DE4 =  es.toGPUShape(bs.createTextureQuad("DE_4.png"),GL_REPEAT, GL_NEAREST)


	#Noveno Semestre
	DG701 =  es.toGPUShape(bs.createTextureQuad("DG_701.png"),GL_REPEAT, GL_NEAREST)
	DG702 =  es.toGPUShape(bs.createTextureQuad("DG_702.png"),GL_REPEAT, GL_NEAREST)


	#Decimo Semestre 
	DG801 =  es.toGPUShape(bs.createTextureQuad("DG_801.png"),GL_REPEAT, GL_NEAREST)
	


	#Aqui se comienzan a crear los cursos 

	#Primer año
	Tap_DP_101 = sg.SceneGraphNode("Tap_DP_101") #Se crea la 'tapa' para el cubo
	Tap_DP_101.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DP_101.childs += [DP101]

	TDP_101 = sg.SceneGraphNode("TDP_101") #Se crea el cubo completo ubicado en la posicion correcta
	TDP_101.transform = tr.translate(-2.1,2.1,0)
	TDP_101.childs += [cuboRojo, Tap_DP_101]

	DP_101 = sg.SceneGraphNode("DP_101") #Se crea el cubo completo 
	DP_101.childs += [TDP_101]

	CDP_101 = cc.Curso('DP_101',[],-2.1,2.1,0,['DGP_201','DG_701','DG_702'])




	Tap_DP_102 = sg.SceneGraphNode("Tap_DP_102") #Se crea la 'tapa' para el cubo
	Tap_DP_102.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DP_102.childs += [DP102]

	TDP_102 = sg.SceneGraphNode("TDP_102") #Se crea el cubo completo ubicado en la posicion correcta
	TDP_102.transform = tr.translate(-1.5,2.1,0)
	TDP_102.childs += [cuboRojo, Tap_DP_102]

	DP_102 = sg.SceneGraphNode("DP_102") #Se crea el cubo completo 
	DP_102.childs += [TDP_102]

	CDP_102 = cc.Curso('DP_102',[],-1.5,2.1,0,['DGP_202','DG_701','DG_702'])





	Tap_DP_103 = sg.SceneGraphNode("Tap_DP_103") #Se crea la 'tapa' para el cubo
	Tap_DP_103.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DP_103.childs += [DP103]

	TDP_103 = sg.SceneGraphNode("TDP_103") #Se crea el cubo completo ubicado en la posicion correcta 
	TDP_103.transform = tr.translate(-0.9,2.1,0)
	TDP_103.childs += [cuboRojo, Tap_DP_103]

	DP_103 = sg.SceneGraphNode("DP_103") #Se crea el cubo completo 
	DP_103.childs += [TDP_103]

	CDP_103 = cc.Curso('DP_103',[],-0.9,2.1,0,['DGP_203','DG_701','DG_702'])




	Tap_DT_104 = sg.SceneGraphNode("Tap_DT_104") #Se crea la 'tapa' para el cubo
	Tap_DT_104.transform = tr.matmul([tr.translate(0, 0,0.252),tr.uniformScale(0.5)])
	Tap_DT_104.childs += [DT104]

	TDT_104 = sg.SceneGraphNode("TDT_104") #Se crea el cubo completo ubicado en la posicion correcta
	TDT_104.transform = tr.translate(-0.3,2.1,0)
	TDT_104.childs += [cuboRojo, Tap_DT_104]

	DT_104 = sg.SceneGraphNode("DT_104") #Se crea el cubo completo 
	DT_104.childs += [TDT_104]

	CDT_104 = cc.Curso('DT_104',[],-0.3,2.1,0,['DGT_303','DG_701','DG_702'])




	Tap_DT_105 = sg.SceneGraphNode("Tap_DT_105") #Se crea la 'tapa' para el cubo
	Tap_DT_105.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DT_105.childs += [DT105]

	TDT_105 = sg.SceneGraphNode("TDT_105") #Se crea el cubo completo ubicado en la pisicion correcta
	TDT_105.transform = tr.translate(0.3,2.1,0) 
	TDT_105.childs += [cuboRojo, Tap_DT_105]

	DT_105 = sg.SceneGraphNode("DT_105") #Se crea el cubo completo 
	DT_105.childs += [ TDT_105]

	CDT_105 = cc.Curso('DT_105',[],0.3,2.1,0,['DGT_205','DG_701','DG_702'])




	Tap_DH_106 = sg.SceneGraphNode("Tap_DH_106") #Se crea la 'tapa' para el cubo
	Tap_DH_106.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DH_106.childs += [DH106]

	TDH_106 = sg.SceneGraphNode("TDH_106") #Se crea el cubo completo ubicado en la posicion correcta 
	TDH_106.transform = tr.translate(0.9,2.1,0)
	TDH_106.childs += [cuboRojo, Tap_DH_106]

	DH_106 = sg.SceneGraphNode("DH_106") #Se crea el cubo completo 
	DH_106.childs += [TDH_106]

	CDH_106 = cc.Curso('DH_106',[],0.9,2.1,0,['DGH_206','DG_701','DG_702'])




	Tap_DH_107 = sg.SceneGraphNode("Tap_DH_107") #Se crea la 'tapa' para el cubo
	Tap_DH_107.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DH_107.childs += [DH107]

	TDH_107 = sg.SceneGraphNode("TDH_107") #Se crea el cubo completo ubicado en la posicion correcta 
	TDH_107.transform = tr.translate(1.5,2.1,0)
	TDH_107.childs += [cuboRojo, Tap_DH_107]

	DH_107 = sg.SceneGraphNode("DH_107") #Se crea el cubo completo 
	DH_107.childs += [TDH_107]

	CDH_107 = cc.Curso('DH_107',[],1.5,2.1,0,['DGH_305','DG_701','DG_702'])




	Tap_DH_108 = sg.SceneGraphNode("Tap_DH_108") #Se crea la 'tapa' para el cubo
	Tap_DH_108.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DH_108.childs += [DH108]

	TDH_108 = sg.SceneGraphNode("TDH_108") #Se crea el cubo completo ubicado en la posicion correcta 
	TDH_108.transform = tr.translate(2.1,2.1,0)
	TDH_108.childs += [cuboRojo, Tap_DH_108]

	DH_108 = sg.SceneGraphNode("DH_108") #Se crea el cubo completo 
	DH_108.childs += [TDH_108]

	CDH_108 = cc.Curso('DH_108',[],2.1,2.1,0,['DGH_208','DG_701','DG_702'])









	#Segundo año 
	Tap_DGP_201 = sg.SceneGraphNode("Tap_DGP_201") #Se crea la 'tapa' para el cubo
	Tap_DGP_201.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_201.childs += [DGP201]

	TDGP_201 = sg.SceneGraphNode("TDGP_201") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGP_201.transform = tr.translate(-2.1,1.5,0)
	TDGP_201.childs += [cuboRojo, Tap_DGP_201]

	DGP_201 = sg.SceneGraphNode("DGP_201") #Se crea el cubo completo 
	DGP_201.childs += [TDGP_201]

	CDGP_201 = cc.Curso('DGP_201',['DP_101'],-2.1,1.5,0,['DGP_301','DG_701','DG_702'])




	Tap_DGP_202 = sg.SceneGraphNode("Tap_DGP_202") #Se crea la 'tapa' para el cubo
	Tap_DGP_202.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_202.childs += [DGP202]

	TDGP_202 = sg.SceneGraphNode("TDGP_202") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGP_202.transform = tr.translate(-1.5,1.5,0)
	TDGP_202.childs += [cuboRojo, Tap_DGP_202]

	DGP_202 = sg.SceneGraphNode("DGP_202") #Se crea el cubo completo 
	DGP_202.childs += [TDGP_202]

	CDGP_202 = cc.Curso('DGP_202',['DP_102'],-1.5,1.5,0,['DG_701','DG_702'])




	Tap_DGP_203 = sg.SceneGraphNode("Tap_DGP_203") #Se crea la 'tapa' para el cubo
	Tap_DGP_203.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_203.childs += [DGP203]

	TDGP_203 = sg.SceneGraphNode("TDGP_203") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGP_203.transform = tr.translate(-0.9,1.5,0)
	TDGP_203.childs += [cuboRojo, Tap_DGP_203]

	DGP_203 = sg.SceneGraphNode("DGP_203") #Se crea el cubo completo 
	DGP_203.childs += [TDGP_203]

	CDGP_203 = cc.Curso('DGP_203',['DP_103'],-0.9,1.5,0,['DGP_301','DG_701','DG_702'])




	Tap_DGT_204 = sg.SceneGraphNode("Tap_DGT_204") #Se crea la 'tapa' para el cubo
	Tap_DGT_204.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_204.childs += [DGT204]

	TDGT_204 = sg.SceneGraphNode("TDGT_204") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGT_204.transform = tr.translate(-0.3,1.5,0)
	TDGT_204.childs += [cuboRojo, Tap_DGT_204]

	DGT_204 = sg.SceneGraphNode("DGT_204") #Se crea el cubo completo 
	DGT_204.childs += [TDGT_204]

	CDGT_204 = cc.Curso('DGT_204',[],-0.3,1.5,0,['DGT_304','DG_701','DG_702'])




	Tap_DGT_205 = sg.SceneGraphNode("Tap_DGT_205") #Se crea la 'tapa' para el cubo
	Tap_DGT_205.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_205.childs += [DGT205]

	TDGT_205 = sg.SceneGraphNode("TDGT_205") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGT_205.transform = tr.translate(0.3,1.5,0)
	TDGT_205.childs += [cuboRojo, Tap_DGT_205]

	DGT_205 = sg.SceneGraphNode("DGT_205") #Se crea el cubo completo 
	DGT_205.childs += [TDGT_205]

	CDGT_205 = cc.Curso('DGT_205',['DT_105'],0.3,1.5,0,['DGT_303', 'DGT_302','DG_701','DG_702'])




	Tap_DGH_206 = sg.SceneGraphNode("Tap_DGH_206") #Se crea la 'tapa' para el cubo
	Tap_DGH_206.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_206.childs += [DGH206]

	TDGH_206 = sg.SceneGraphNode("TDGH_206") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_206.transform = tr.translate(0.9,1.5,0)
	TDGH_206.childs += [cuboRojo, Tap_DGH_206]

	DGH_206 = sg.SceneGraphNode("DGH_206") #Se crea el cubo completo 
	DGH_206.childs += [TDGH_206]

	CDGH_206 = cc.Curso('DGH_206',['DH_106'],0.9,1.5,0,['DG_701','DG_702'])




	Tap_DGH_207 = sg.SceneGraphNode("Tap_DGH_207") #Se crea la 'tapa' para el cubo
	Tap_DGH_207.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_207.childs += [DGH207]

	TDGH_207 = sg.SceneGraphNode("TDGH_207") #Se crea el cubo completo ubicado en la posicion correcta
	TDGH_207.transform = tr.translate(1.5,1.5,0) 
	TDGH_207.childs += [cuboRojo, Tap_DGH_207]

	DGH_207 = sg.SceneGraphNode("DGH_207") #Se crea el cubo completo 
	DGH_207.childs += [TDGH_207]

	CDGH_207 = cc.Curso('DGH_207',[],1.5,1.5,0,['DGP_301', 'DGH_306','DG_701','DG_702'])


	

	Tap_DGH_208 = sg.SceneGraphNode("Tap_DGH_208") #Se crea la 'tapa' para el cubo
	Tap_DGH_208.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_208.childs += [DGH208]

	TDGH_208 = sg.SceneGraphNode("TDGH_208") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_208.transform = tr.translate(2.1,1.5,0)
	TDGH_208.childs += [cuboRojo, Tap_DGH_208]

	DGH_208 = sg.SceneGraphNode("DGH_208") #Se crea el cubo completo 
	DGH_208.childs += [TDGH_208]

	CDGH_208 = cc.Curso('DGH_208',['DH_108'],0.9,1.5,0,['DGH_307','DG_701','DG_702'])








	#Quinto Semestre 

	Tap_DGP_301 = sg.SceneGraphNode("Tap_DGP_301") #Se crea la 'tapa' para el cubo
	Tap_DGP_301.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_301.childs += [DGP301]

	TDGP_301 = sg.SceneGraphNode("TDGP_301") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGP_301.transform = tr.translate(-2.1,0.9,0)
	TDGP_301.childs += [cuboRojo, Tap_DGP_301]

	DGP_301 = sg.SceneGraphNode("DGP_301") #Se crea el cubo completo 
	DGP_301.childs += [TDGP_301]

	CDGP_301 = cc.Curso('DGP_301',['DGP_201','DGP_203','DGH_207'],-2.1,0.9,0,['DGP_401','DG_701','DG_702'])




	Tap_DGT_302 = sg.SceneGraphNode("Tap_DGT_302") #Se crea la 'tapa' para el cubo
	Tap_DGT_302.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_302.childs += [DGT302]

	TDGT_302 = sg.SceneGraphNode("TDGT_302") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGT_302.transform = tr.translate(-1.5,0.9,0)
	TDGT_302.childs += [cuboRojo, Tap_DGT_302]

	DGT_302 = sg.SceneGraphNode("DGT_302") #Se crea el cubo completo 
	DGT_302.childs += [TDGT_302]

	CDGT_302 = cc.Curso('DGT_302',['DGT_205'],-1.5,0.9,0,['DGT_402','DG_701','DG_702'])




	Tap_DGT_303 = sg.SceneGraphNode("Tap_DGT_303") #Se crea la 'tapa' para el cubo
	Tap_DGT_303.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_303.childs += [DGT303]

	TDGT_303 = sg.SceneGraphNode("TDGT_303") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGT_303.transform = tr.translate(-0.9,0.9,0)
	TDGT_303.childs += [cuboRojo, Tap_DGT_303]

	DGT_303 = sg.SceneGraphNode("DGT_303") #Se crea el cubo completo 
	DGT_303.childs += [TDGT_303]

	CDGT_303 = cc.Curso('DGT_303',['DGT_205','DT_104'],-0.9,0.9,0,['DGT_403','DG_701','DG_702'])




	Tap_DGT_304 = sg.SceneGraphNode("Tap_DGT_304") #Se crea la 'tapa' para el cubo
	Tap_DGT_304.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_304.childs += [DGT304]

	TDGT_304 = sg.SceneGraphNode("TDGT_304") #Se crea el cubo completo ubicado en la posicion correcta
	TDGT_304.transform = tr.translate(-0.3,0.9,0) 
	TDGT_304.childs += [cuboRojo, Tap_DGT_304]

	DGT_304 = sg.SceneGraphNode("DGT_304") #Se crea el cubo completo 
	DGT_304.childs += [TDGT_304]

	CDGT_304 = cc.Curso('DGT_304',['DGT_204'],-0.3,0.9,0,['DGT_404','DG_701','DG_702'])




	Tap_DGH_305 = sg.SceneGraphNode("Tap_DGH_305") #Se crea la 'tapa' para el cubo
	Tap_DGH_305.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_305.childs += [DGH305]

	TDGH_305 = sg.SceneGraphNode("TDGH_305") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_305.transform = tr.translate(0.3,0.9,0)
	TDGH_305.childs += [cuboRojo, Tap_DGH_305]

	DGH_305 = sg.SceneGraphNode("DGH_305") #Se crea el cubo completo 
	DGH_305.childs += [TDGH_305]

	CDGH_305 = cc.Curso('DGH_305',['DH_107'],0.3,0.9,0,['DGH_505','DG_701','DG_702'])




	Tap_DGH_306 = sg.SceneGraphNode("Tap_DGH_306") #Se crea la 'tapa' para el cubo
	Tap_DGH_306.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_306.childs += [DGH306]

	TDGH_306 = sg.SceneGraphNode("TDGH_306") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_306.transform = tr.translate(0.9,0.9,0)
	TDGH_306.childs += [cuboRojo, Tap_DGH_306]

	DGH_306 = sg.SceneGraphNode("DGH_306") #Se crea el cubo completo 
	DGH_306.childs += [TDGH_306]

	CDGH_306 = cc.Curso('DGH_306',['DGH_207'],0.9,0.9,0,['DGP_401', 'DGH_406','DG_701','DG_702'])




	Tap_DGH_307 = sg.SceneGraphNode("Tap_DGH_307") #Se crea la 'tapa' para el cubo
	Tap_DGH_307.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_307.childs += [DGH307]

	TDGH_307 = sg.SceneGraphNode("TDGH_307") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_307.transform = tr.translate(1.5,0.9,0)
	TDGH_307.childs += [cuboRojo, Tap_DGH_307]

	DGH_307 = sg.SceneGraphNode("DGH_307") #Se crea el cubo completo 
	DGH_307.childs += [TDGH_307]

	CDGH_307 = cc.Curso('DGH_307',['DGH_208'],1.5,0.9,0, ['DGP_401', 'DGH_407','DG_701','DG_702'])




	Tap_DE_1 = sg.SceneGraphNode("Tap_DE_1") #Se crea la 'tapa' para el cubo
	Tap_DE_1.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DE_1.childs += [DE1]

	TDE_1 = sg.SceneGraphNode("TDE_1") #Se crea el cubo completo ubicado en la posicion correcta 
	TDE_1.transform = tr.translate(2.1,0.9,0)
	TDE_1.childs += [cuboRojo, Tap_DE_1]

	DE_1 = sg.SceneGraphNode("DE_1") #Se crea el cubo completo 
	DE_1.childs += [TDE_1]

	CDE_1 = cc.Curso('DE_1',[],2.1,0.9,0,['DE_3','DE_4','DG_701','DG_702'])








	#Sexto Semestre 
	Tap_DGP_401 = sg.SceneGraphNode("Tap_DGP_401") #Se crea la 'tapa' para el cubo
	Tap_DGP_401.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_401.childs += [DGP401]

	TDGP_401 = sg.SceneGraphNode("TDGP_401") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGP_401.transform = tr.translate(-2.1,0.3,0)
	TDGP_401.childs += [cuboRojo, Tap_DGP_401]

	DGP_401 = sg.SceneGraphNode("DGP_401") #Se crea el cubo completo 
	DGP_401.childs += [TDGP_401]

	CDGP_401 = cc.Curso('DGP_401',['DGH_307','DGP_301','DGH_306'],-2.1,0.3,0,['DGP_501','DG_701','DG_702'])




	Tap_DGT_402 = sg.SceneGraphNode("Tap_DGT_402") #Se crea la 'tapa' para el cubo
	Tap_DGT_402.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_402.childs += [DGT402]

	TDGT_402 = sg.SceneGraphNode("TDGT_402") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGT_402.transform = tr.translate(-1.5,0.3,0)
	TDGT_402.childs += [cuboRojo, Tap_DGT_402]

	DGT_402 = sg.SceneGraphNode("DGT_402") #Se crea el cubo completo 
	DGT_402.childs += [TDGT_402]

	CDGT_402 = cc.Curso('DGT_402',['DGT_302'],-1.5,0.3,0,['DGH_507','DG_701','DG_702'])




	Tap_DGT_403 = sg.SceneGraphNode("Tap_DGT_403") #Se crea la 'tapa' para el cubo
	Tap_DGT_403.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_403.childs += [DGT403]

	TDGT_403 = sg.SceneGraphNode("TDGT_403") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGT_403.transform = tr.translate(-0.9,0.3,0)
	TDGT_403.childs += [cuboRojo, Tap_DGT_403]

	DGT_403 = sg.SceneGraphNode("DGT_403") #Se crea el cubo completo 
	DGT_403.childs += [TDGT_403]

	CDGT_403 = cc.Curso('DGT_403',['DGT_303'],-0.9,0.3,0,['DGP_501', 'DGP_502','DG_701','DG_702'])




	Tap_DGT_404 = sg.SceneGraphNode("Tap_DGT_404") #Se crea la 'tapa' para el cubo
	Tap_DGT_404.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_404.childs += [DGT404]

	TDGT_404 = sg.SceneGraphNode("TDGT_404") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGT_404.transform = tr.translate(-0.3,0.3,0)
	TDGT_404.childs += [cuboRojo, Tap_DGT_404]

	DGT_404 = sg.SceneGraphNode("DGT_404") #Se crea el cubo completo 
	DGT_404.childs += [TDGT_404]

	CDGT_404 = cc.Curso('DGT_404',['DGT_304'],-0.3,0.3,0,['DGT_503','DG_701','DG_702'])




	Tap_DGH_405 = sg.SceneGraphNode("Tap_DGH_405") #Se crea la 'tapa' para el cubo
	Tap_DGH_405.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_405.childs += [DGH405]

	TDGH_405 = sg.SceneGraphNode("TDGH_405") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_405.transform = tr.translate(0.3,0.3,0)
	TDGH_405.childs += [cuboRojo, Tap_DGH_405]

	DGH_405 = sg.SceneGraphNode("DGH_405") #Se crea el cubo completo 
	DGH_405.childs += [TDGH_405]

	CDGH_405 = cc.Curso('DGH_405',[],0.3,0.3,0,['DGH_504','DG_701','DG_702'])




	Tap_DGH_406 = sg.SceneGraphNode("Tap_DGH_406") #Se crea la 'tapa' para el cubo
	Tap_DGH_406.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_406.childs += [DGH406]

	TDGH_406 = sg.SceneGraphNode("TDGH_406") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_406.transform = tr.translate(0.9,0.3,0)
	TDGH_406.childs += [cuboRojo, Tap_DGH_406]

	DGH_406 = sg.SceneGraphNode("DGH_406") #Se crea el cubo completo 
	DGH_406.childs += [TDGH_406]

	CDGH_406 = cc.Curso('DGH_406',['DGH_306'],0.9,0.3,0,['DGP_501','DG_701','DG_702'])




	Tap_DGH_407 = sg.SceneGraphNode("Tap_DGH_407") #Se crea la 'tapa' para el cubo
	Tap_DGH_407.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_407.childs += [DGH407]

	TDGH_407 = sg.SceneGraphNode("TDGH_407") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_407.transform = tr.translate(1.5,0.3,0)
	TDGH_407.childs += [cuboRojo, Tap_DGH_407]

	DGH_407 = sg.SceneGraphNode("DGH_407") #Se crea el cubo completo 
	DGH_407.childs += [TDGH_407]

	CDGH_407 = cc.Curso('DGH_407',['DGH_307'],1.5,0.3,0,['DGP_501','DGH_506','DG_701','DG_702'])
	



	Tap_DE_2 = sg.SceneGraphNode("Tap_DE_2") #Se crea la 'tapa' para el cubo
	Tap_DE_2.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DE_2.childs += [DE2]

	TDE_2 = sg.SceneGraphNode("TDE_2") #Se crea el cubo completo ubicado en la posicion correcta 
	TDE_2.transform = tr.translate(2.1,0.3,0)
	TDE_2.childs += [cuboRojo, Tap_DE_2]

	DE_2 = sg.SceneGraphNode("DE_2") #Se crea el cubo completo 
	DE_2.childs += [TDE_2]

	CDE_2 = cc.Curso('DE_2',[],2.1,0.3,0,['DE_4','DG_701','DG_702'])








	#Septimo Semestre

	Tap_DGP_501 = sg.SceneGraphNode("Tap_DGP_501") #Se crea la 'tapa' para el cubo
	Tap_DGP_501.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_501.childs += [DGP501]

	TDGP_501 = sg.SceneGraphNode("TDGP_501") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGP_501.transform = tr.translate(-2.1,-0.3,0)
	TDGP_501.childs += [cuboRojo, Tap_DGP_501]

	DGP_501 = sg.SceneGraphNode("DGP_501") #Se crea el cubo completo 
	DGP_501.childs += [TDGP_501]

	CDGP_501 = cc.Curso('DGP_501',['DGT_403','DGH_407','DGH_406','DGP_401'],-2.1,-0.3,0,['DGP_601','DG_701','DG_702'])




	Tap_DGP_502 = sg.SceneGraphNode("Tap_DGP_502") #Se crea la 'tapa' para el cubo
	Tap_DGP_502.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_502.childs += [DGP502]

	TDGP_502 = sg.SceneGraphNode("TDGP_502") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGP_502.transform = tr.translate(-1.5,-0.3,0)
	TDGP_502.childs += [cuboRojo, Tap_DGP_502]

	DGP_502 = sg.SceneGraphNode("DGP_502") #Se crea el cubo completo 
	DGP_502.childs += [TDGP_502]

	CDGP_502 = cc.Curso('DGP_502',['DGT_403'],-1.5,-0.3,0,['DGP_602','DG_701','DG_702'])




	Tap_DGT_503 = sg.SceneGraphNode("Tap_DGT_503") #Se crea la 'tapa' para el cubo
	Tap_DGT_503.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_503.childs += [DGT503]

	TDGT_503 = sg.SceneGraphNode("TDGT_503") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGT_503.transform = tr.translate(-0.9,-0.3,0)
	TDGT_503.childs += [cuboRojo, Tap_DGT_503]

	DGT_503 = sg.SceneGraphNode("DGT_503") #Se crea el cubo completo 
	DGT_503.childs += [TDGT_503]

	CDGT_503 = cc.Curso('DGT_503',['DGT_404'],-0.9,-0.3,0,['DGT_603','DG_701','DG_702'])




	Tap_DGH_504 = sg.SceneGraphNode("Tap_DGH_504") #Se crea la 'tapa' para el cubo
	Tap_DGH_504.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_504.childs += [DGH504]

	TDGH_504 = sg.SceneGraphNode("TDGH_504") #Se crea el cubo completo ubicado en la posicion correcta
	TDGH_504.transform = tr.translate(-0.3,-0.3,0) 
	TDGH_504.childs += [cuboRojo, Tap_DGH_504]

	DGH_504 = sg.SceneGraphNode("DGH_504") #Se crea el cubo completo 
	DGH_504.childs += [TDGH_504]

	CDGH_504 = cc.Curso('DGH_504',['DGH_405'],-0.3,-0.3,0,['DGH_604','DG_701','DG_702'])




	Tap_DGH_505 = sg.SceneGraphNode("Tap_DGH_505") #Se crea la 'tapa' para el cubo
	Tap_DGH_505.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_505.childs += [DGH505]

	TDGH_505 = sg.SceneGraphNode("TDGH_505") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_505.transform = tr.translate(0.3,-0.3,0)
	TDGH_505.childs += [cuboRojo, Tap_DGH_505]

	DGH_505 = sg.SceneGraphNode("DGH_505") #Se crea el cubo completo 
	DGH_505.childs += [TDGH_505]

	CDGH_505 = cc.Curso('DGH_505',['DGH_305'],0.3,-0.3,0,['DG_701','DG_702'])




	Tap_DGH_506 = sg.SceneGraphNode("Tap_DGH_506") #Se crea la 'tapa' para el cubo
	Tap_DGH_506.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_506.childs += [DGH506]

	TDGH_506 = sg.SceneGraphNode("TDGH_506") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_506.transform = tr.translate(0.9,-0.3,0)
	TDGH_506.childs += [cuboRojo, Tap_DGH_506]

	DGH_506 = sg.SceneGraphNode("DGH_506") #Se crea el cubo completo 
	DGH_506.childs += [TDGH_506]

	CDGH_506 = cc.Curso('DGH_506',['DGH_407'],0.9,-0.3,0,['DGP_601','DGH_606','DG_701','DG_702'])




	Tap_DGH_507 = sg.SceneGraphNode("Tap_DGH_507") #Se crea la 'tapa' para el cubo
	Tap_DGH_507.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_507.childs += [DGH507]

	TDGH_507 = sg.SceneGraphNode("TDGH_507") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_507.transform = tr.translate(1.5,-0.3,0)
	TDGH_507.childs += [cuboRojo, Tap_DGH_507]

	DGH_507 = sg.SceneGraphNode("DGH_507") #Se crea el cubo completo 
	DGH_507.childs += [TDGH_507]

	CDGH_507 = cc.Curso('DGH_507',['DGT_402'],1.5,-0.3,0,['DG_701','DG_702'])




	Tap_DE_3 = sg.SceneGraphNode("Tap_DE_3") #Se crea la 'tapa' para el cubo
	Tap_DE_3.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DE_3.childs += [DE3]

	TDE_3 = sg.SceneGraphNode("TDE_3") #Se crea el cubo completo ubicado en la posicion correcta 
	TDE_3.transform = tr.translate(2.1,-0.3,0)
	TDE_3.childs += [cuboRojo, Tap_DE_3]

	DE_3 = sg.SceneGraphNode("DE_3") #Se crea el cubo completo 
	DE_3.childs += [TDE_3]

	CDE_3 = cc.Curso('DE_3',['DE_1'],2.1,-0.3,0,['DG_701','DG_702'])








	#Octavo Semestre 

	Tap_DGP_601 = sg.SceneGraphNode("Tap_DGP_601") #Se crea la 'tapa' para el cubo
	Tap_DGP_601.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_601.childs += [DGP601]

	TDGP_601 = sg.SceneGraphNode("TDGP_601") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGP_601.transform = tr.translate(-2.1,-0.9,0)
	TDGP_601.childs += [cuboRojo, Tap_DGP_601]

	DGP_601 = sg.SceneGraphNode("DGP_601") #Se crea el cubo completo 
	DGP_601.childs += [TDGP_601]

	CDGP_601 = cc.Curso('DGP_601',['DGH_506','DGP_501'],-2.1,-0.9,0,['DG_701','DG_702'])




	Tap_DGP_602 = sg.SceneGraphNode("Tap_DGP_602") #Se crea la 'tapa' para el cubo
	Tap_DGP_602.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_602.childs += [DGP602]

	TDGP_602 = sg.SceneGraphNode("TDGP_602") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGP_602.transform = tr.translate(-1.5,-0.9,0)
	TDGP_602.childs += [cuboRojo, Tap_DGP_602]

	DGP_602 = sg.SceneGraphNode("DGP_602") #Se crea el cubo completo 
	DGP_602.childs += [TDGP_602]

	CDGP_602 = cc.Curso('DGP_602',['DGP_502'],-1.5,-0.9,0,['DG_701','DG_702'])




	Tap_DGT_603 = sg.SceneGraphNode("Tap_DGT_603") #Se crea la 'tapa' para el cubo
	Tap_DGT_603.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_603.childs += [DGT603]

	TDGT_603 = sg.SceneGraphNode("TDGT_603") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGT_603.transform = tr.translate(-0.9,-0.9,0)
	TDGT_603.childs += [cuboRojo, Tap_DGT_603]

	DGT_603 = sg.SceneGraphNode("DGT_603") #Se crea el cubo completo 
	DGT_603.childs += [TDGT_603]

	CDGT_603 = cc.Curso('DGT_603',['DGT_503'],-0.9,-0.9,0,['DG_701','DG_702'])




	Tap_DGH_604 = sg.SceneGraphNode("Tap_DGH_604") #Se crea la 'tapa' para el cubo
	Tap_DGH_604.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_604.childs += [DGH604]

	TDGH_604 = sg.SceneGraphNode("TDGH_604") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_604.transform = tr.translate(-0.3,-0.9,0)
	TDGH_604.childs += [cuboRojo, Tap_DGH_604]

	DGH_604 = sg.SceneGraphNode("DGH_604") #Se crea el cubo completo 
	DGH_604.childs += [TDGH_604]

	CDGH_604 = cc.Curso('DGH_604',['DGH_504'],-0.3,-0.9,0,['DG_701','DG_702'])




	Tap_DGH_605 = sg.SceneGraphNode("Tap_DGH_605") #Se crea la 'tapa' para el cubo
	Tap_DGH_605.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_605.childs += [DGH605]

	TDGH_605 = sg.SceneGraphNode("TDGH_605") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_605.transform = tr.translate(0.3,-0.9,0)
	TDGH_605.childs += [cuboRojo, Tap_DGH_605]

	DGH_605 = sg.SceneGraphNode("DGH_605") #Se crea el cubo completo 
	DGH_605.childs += [TDGH_605]

	CDGH_605 = cc.Curso('DGH_605',[],0.3,-0.9,0,['DG_701','DG_702'])




	Tap_DGH_606 = sg.SceneGraphNode("Tap_DGH_606") #Se crea la 'tapa' para el cubo
	Tap_DGH_606.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_606.childs += [DGH606]

	TDGH_606 = sg.SceneGraphNode("TDGH_606") #Se crea el cubo completo ubicado en la posicion correcta 
	TDGH_606.transform = tr.translate(0.9,-0.9,0)
	TDGH_606.childs += [cuboRojo, Tap_DGH_606]

	DGH_606 = sg.SceneGraphNode("DGH_606") #Se crea el cubo completo 
	DGH_606.childs += [TDGH_606]

	CDGH_606 = cc.Curso('DGH_606',['DGH_506'],0.9,-0.9,0,['DG_701','DG_702'])




	Tap_DE_4 = sg.SceneGraphNode("Tap_DE_4") #Se crea la 'tapa' para el cubo
	Tap_DE_4.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DE_4.childs += [DE4]

	TDE_4 = sg.SceneGraphNode("TDE_4") #Se crea el cubo completo ubicado en la posicion correcta 
	TDE_4.transform = tr.translate(1.5,-0.9,0)
	TDE_4.childs += [cuboRojo, Tap_DE_4]

	DE_4 = sg.SceneGraphNode("DE_4") #Se crea el cubo completo 
	DE_4.childs += [TDE_4]

	CDE_4 = cc.Curso('DE_4',['DE_1','DE_2'],1.5,-0.9,0,['DG_701','DG_702'])



	Licenciatura_P_Prof = ['DP_101','DP_102','DP_103','DT_104','DT_105','DH_106','DH_107','DH_108',
							'DGP_201','DGP_202','DGP_203','DGT_204','DGT_205','DGH_206','DGH_207','DGH_208',
							'DGP_301','DGT_302','DGT_303','DGT_304','DGH_305','DGH_306','DGH_307','DE_1',
							'DGP_401','DGT_402','DGT_403','DGT_404','DGH_405','DGH_406','DGH_407','DE_2',
							'DGP_501','DGP_502','DGT_503','DGH_504','DGH_505','DGH_506','DGH_507','DE_3',
							'DGP_601','DGP_602','DGT_603','DGH_604','DGH_605','DGH_606','DE_4'] 



	#Noveno semestre 
	Tap_DG_701 = sg.SceneGraphNode("Tap_DG_701") #Se crea la 'tapa' para el cubo
	Tap_DG_701.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DG_701.childs += [DG701]

	TDG_701 = sg.SceneGraphNode("TDG_701") #Se crea el cubo completo ubicado en la posicion correcta 
	TDG_701.transform = tr.translate(-2.1,-1.5,0)
	TDG_701.childs += [cuboRojo, Tap_DG_701]

	DG_701 = sg.SceneGraphNode("DG_701") #Se crea el cubo completo 
	DG_701.childs += [TDG_701]

	CDG_701 = cc.Curso('DG_701',Licenciatura_P_Prof,-2.1,-1.5,0,['DG_801'])




	Tap_DG_702 = sg.SceneGraphNode("Tap_DG_702") #Se crea la 'tapa' para el cubo
	Tap_DG_702.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DG_702.childs += [DG702]

	TDG_702 = sg.SceneGraphNode("TDG_702") #Se crea el cubo completo ubicado en la posicion correcta 
	TDG_702.transform = tr.translate(-1.5,-1.5,0)
	TDG_702.childs += [cuboRojo, Tap_DG_702]

	DG_702 = sg.SceneGraphNode("DG_702") #Se crea el cubo completo 
	DG_702.childs += [TDG_702]

	CDG_702 = cc.Curso('DG_702',Licenciatura_P_Prof,-1.5,-1.5,0,['DG_801'])










	#Decimo semestre 
	Tap_DG_801 = sg.SceneGraphNode("Tap_DG_801") #Se crea la 'tapa' para el cubo
	Tap_DG_801.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DG_801.childs += [DG801]

	TDG_801 = sg.SceneGraphNode("TDG_801") #Se crea el cubo completo ubicado en la posicion correcta 
	TDG_801.transform = tr.translate(-2.1,-2.1,0)
	TDG_801.childs += [cuboRojo, Tap_DG_801]

	DG_801 = sg.SceneGraphNode("DG_801") #Se crea el cubo completo 
	DG_801.childs += [TDG_801]

	CDG_801 = cc.Curso('DG_801',['DG_701','DG_702'],-2.1,-2.1,0)








	#Aqui se comienzan a crear los cursos en un mismo plano 
	semestre1 = sg.SceneGraphNode("semestre1")
	semestre1.childs += [DP_101,DP_102,DP_103,DT_104,DT_105,DH_106,DH_107,DH_108]

	semestre2 = sg.SceneGraphNode("semestre2")
	semestre2.childs += [DGP_201,DGP_202,DGP_203,DGT_204,DGT_205,DGH_206,DGH_207,DGH_208]

	semestre3 = sg.SceneGraphNode("semestre3")
	semestre3.childs += [DGP_301,DGT_302,DGT_303,DGT_304,DGH_305,DGH_306,DGH_307,DE_1]

	semestre4 = sg.SceneGraphNode("semestre4")
	semestre4.childs += [DGP_401,DGT_402,DGT_403,DGT_404,DGH_405,DGH_406,DGH_407,DE_2]

	semestre5 = sg.SceneGraphNode("semestre5")
	semestre5.childs += [DGP_501,DGP_502,DGT_503,DGH_504,DGH_505,DGH_506,DGH_507,DE_3]

	semestre6 = sg.SceneGraphNode("semestre6")
	semestre6.childs += [DGP_601,DGP_602,DGT_603,DGH_604,DGH_605,DGH_606,DE_4]

	semestre7 = sg.SceneGraphNode("semestre7")
	semestre7.childs += [DG_701,DG_702]

	semestre8 = sg.SceneGraphNode("semestre8")
	semestre8.childs += [DG_801]



	Csemestre1 = [CDP_101,CDP_102,CDP_103,CDT_104,CDT_105,CDH_106,CDH_107,CDH_108]

	Csemestre2 = [CDGP_201,CDGP_202,CDGP_203,CDGT_204,CDGT_205,CDGH_206,CDGH_207,CDGH_208]

	Csemestre3 = [CDGP_301,CDGT_302,CDGT_303,CDGT_304,CDGH_305,CDGH_306,CDGH_307,CDE_1]

	Csemestre4 = [CDGP_401,CDGT_402,CDGT_403,CDGT_404,CDGH_405,CDGH_406,CDGH_407,CDE_2]

	Csemestre5 = [CDGP_501,CDGP_502,CDGT_503,CDGH_504,CDGH_505,CDGH_506,CDGH_507,CDE_3]

	Csemestre6 = [CDGP_601,CDGP_602,CDGT_603,CDGH_604,CDGH_605,CDGH_606,CDE_4]

	Csemestre7 = [CDG_701,CDG_702]

	Csemestre8 = [CDG_801]

	Cmalla = [Csemestre1,Csemestre2,Csemestre3,Csemestre4,Csemestre5,Csemestre6,Csemestre7,Csemestre8]



	malla = sg.SceneGraphNode("malla")
	malla.childs = [semestre1,semestre2,semestre3,semestre4,semestre5,semestre6,semestre7,semestre8]
	

	return malla , Cmalla


def Fondo(fondoE): 
	color = es.toGPUShape(bs.createTextureCube("fondo2.jpg"),GL_REPEAT, GL_NEAREST)
	obama = es.toGPUShape(bs.createTextureCube("marco.png"),GL_REPEAT, GL_NEAREST)
	ricardo = es.toGPUShape(bs.createTextureCube("ricardo.jpg"),GL_REPEAT, GL_NEAREST)

	fondo1 = sg.SceneGraphNode("fondo1")
	fondo1.transform = tr.matmul([tr.translate(0,0,1) ,tr.uniformScale (15)])
	fondo1.childs = [color]

	fondo2 = sg.SceneGraphNode("fondo2")
	fondo2.transform = tr.matmul([tr.translate(0,0,1) ,tr.uniformScale (15)])
	fondo2.childs = [ricardo]

	fondo3 = sg.SceneGraphNode("fondo3")
	fondo3.transform = tr.matmul([tr.translate(0,0,1) ,tr.uniformScale (15)])
	fondo3.childs = [obama]

	fondo = sg.SceneGraphNode("fondo")

	if fondoE == "C" :
		fondo.childs = [fondo1]
	if fondoE == "O" :
		fondo.childs = [fondo3]
	if fondoE == "R" : 
		fondo.childs = [fondo2]

	return fondo


def enzo(pipeline):
	glUseProgram(pipeline.shaderProgram)
	glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "view"), 1, GL_TRUE, view)
	glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "projection"), 1, GL_TRUE, projection)



if __name__ == "__main__":

	# Initialize glfw
	if not glfw.init():
		sys.exit()

	width = 900
	height = 900

	window = glfw.create_window(width, height, "Malla Diseño Gráfico", None, None)

	if not window:
		glfw.terminate()
		sys.exit()

	glfw.make_context_current(window)

	# Connecting the callback function 'on_key' to handle keyboard events
	glfw.set_key_callback(window, on_key)

	# Assembling the shader program (pipeline) with both shaders
	mvcPipeline = es.SimpleTextureModelViewProjectionShaderProgram()
	embisi = es.SimpleModelViewProjectionShaderProgram()

	

	# As we work in 3D, we need to check which part is in front,
	# and which one is at the back
	glEnable(GL_DEPTH_TEST)

	# Creating shapes on GPU memory
	gpuAxis = es.toGPUShape(bs.createAxis(7))
	cuboR, cuboT, cuboC, cuboN = crearCubos()
	malla, cmalla = crearCurso(cuboR)
	fondo = Fondo(controller.fondoE)

	sem_in = np.random.randint(0,len(cmalla))
	cur_in = np.random.randint(0,len(cmalla[sem_in]))
	controller.semestre = sem_in
	controller.curso = cur_in
	cursoAnterior = cmalla[sem_in][cur_in]

	cH = []
	maHB = False
	indiceKyJ = 0


	#Using the same view and projection matrices in the whole application
	projection = tr.perspective(45, float(width)/float(height), 0.1, 100)
	t0 = glfw.get_time()

	while not glfw.window_should_close(window):
		# Using GLFW to check for input events
		glfw.poll_events()


		# Getting the time difference from the previous iteration
		t1 = glfw.get_time()
		dt = (t1 - t0)*2
		t0 = t1

		semestre = controller.semestre%len(cmalla)
		curso = controller.curso%len(cmalla[semestre])
		cursoActual = cmalla[semestre][curso]

		if (glfw.get_key(window, glfw.KEY_Z) == glfw.PRESS):
			controller.z += dt

		if (glfw.get_key(window, glfw.KEY_X) == glfw.PRESS):
			controller.z -= dt 


		if not controller.dos and not controller.uno: 

			if (glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS):
				controller.x -= dt*0.5
				controller.shift = True

			if (glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS):
				controller.x += dt*0.5
				controller.shift = True

			if (glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS):
				controller.y += dt*0.5
				controller.shift = True

			if (glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS):
				controller.y -= dt *0.5
				controller.shift = True


		if (controller.uno or controller.dos) and not maHB and controller.shift:
			cur_x, cur_y, cur_z = cursoActual.posicion
			pin = np.array([[controller.x, controller.y, 0]]).T
			pfn = np.array([[cur_x, cur_y, 0]]).T
			tan1 = np.array([[ 1, 0, 0 ]]).T
			tan2 = np.array([[ 1, 0, 0 ]]).T

			maH = cur.hermiteMatrix(pin,pfn,tan1,tan2)
			cH = cur.evalCurve(maH,50)
			maHB = True
			controller.shift = False

		if maHB:
			punto = cH[indiceKyJ]
			controller.x = punto[0]
			controller.y = punto[1]

			if indiceKyJ == len(cH) - 1:
				maHB = False
				controller.uno = False
				indiceKyJ = 0

			else: 
				indiceKyJ += 1



		x = controller.x 
		y = controller.y
		z = -controller.z

		view = tr.lookAt(
			np.array([0 + x,-0.0015 + y,7 + z]),
			np.array([x, y,0]),
			np.array([0,0,1])
		)

		# Clearing the screen in both, color and depth
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		enzo(embisi)

		nodoAnterior = sg.findNode(malla, "T" + cursoAnterior.codigo)
		tapaAnt = nodoAnterior.childs[1]
		nodoAnterior.childs = [cuboR, tapaAnt]

		nodoAnterior = sg.findNode(malla, cursoAnterior.codigo)
		nodoAnterior.transform = tr.scale(1,1,1)

		for requisitoAnt in cursoAnterior.requisitos:
			nodoReqAnt = sg.findNode(malla, "T" + requisitoAnt)
			tapaReqAnt = nodoReqAnt.childs[1]
			nodoReqAnt.childs = [cuboR, tapaReqAnt]

			nodoReqAnt = sg.findNode(malla, requisitoAnt)
			nodoReqAnt.transform = tr.scale(1,1,1)

		for requisitoDeAnt in cursoAnterior.requisitosDe:
			nodoReqDeAnt = sg.findNode(malla, "T" + requisitoDeAnt)
			tapaReqDeAnt = nodoReqDeAnt.childs[1]
			nodoReqDeAnt.childs = [cuboR, tapaReqDeAnt]

			nodoReqDeAnt = sg.findNode(malla, requisitoDeAnt)
			nodoReqDeAnt.transform = tr.scale(1,1,1)


		nodoActual = sg.findNode(malla, "T" + cursoActual.codigo)
		tapaAct = nodoActual.childs[1]
		nodoActual.childs = [cuboN, tapaAct]

		nodoActual = sg.findNode(malla, cursoActual.codigo)
		nodoActual.transform = tr.scale(1,1,2)

		for requisito in cursoActual.requisitos:
			nodoReq = sg.findNode(malla, "T" + requisito)
			tapaReq = nodoReq.childs[1]
			nodoReq.childs = [cuboC, tapaReq]

			nodoReq = sg.findNode(malla, requisito)
			nodoReq.transform = tr.scale(1,1,1.5)

		for requisitoDe in cursoActual.requisitosDe:
			nodoReqDe = sg.findNode(malla, "T" + requisitoDe)
			tapaReqDe = nodoReqDe.childs[1]
			nodoReqDe.childs = [cuboT, tapaReqDe]

			nodoReqDe = sg.findNode(malla, requisitoDe)
			nodoReqDe.transform = tr.scale(1,1,1.5)





		# Filling or not the shapes depending on the controller state
		if (controller.fillPolygon):
			glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
		else:
			glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

		#if controller.showAxis:
		#   glUniformMatrix4fv(glGetUniformLocation(embisi.shaderProgram, "model"), 1, GL_TRUE, tr.identity())
		#   embisi.drawShape(gpuAxis, GL_LINES)

		enzo(mvcPipeline)
		# Drawing the Car
		sg.drawSceneGraphNode(fondo, mvcPipeline, "model")
		sg.drawSceneGraphNode(malla, mvcPipeline, "model")
		glFlush()

		cursoAnterior = cursoActual

		# Once the render is done, buffers are swapped, showing only the complete scene.
		glfw.swap_buffers(window)

	
	glfw.terminate()