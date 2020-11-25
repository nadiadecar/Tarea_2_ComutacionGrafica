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


def TapaCursoSelec(codigo):
	#Primer año
	CDP101 =  es.toGPUShape(bs.createTextureQuad("CDP_101.png"),GL_REPEAT, GL_NEAREST)
	CDP102 =  es.toGPUShape(bs.createTextureQuad("CDP_102.png"),GL_REPEAT, GL_NEAREST)
	CDP103 =  es.toGPUShape(bs.createTextureQuad("CDP_103.png"),GL_REPEAT, GL_NEAREST)
	CDT104 =  es.toGPUShape(bs.createTextureQuad("CDT_104.png"),GL_REPEAT, GL_NEAREST)
	CDT105 =  es.toGPUShape(bs.createTextureQuad("CDT_105.png"),GL_REPEAT, GL_NEAREST)
	CDH106 =  es.toGPUShape(bs.createTextureQuad("CDH_106.png"),GL_REPEAT, GL_NEAREST)
	CDH107 =  es.toGPUShape(bs.createTextureQuad("CDH_107.png"),GL_REPEAT, GL_NEAREST)
	CDH108 =  es.toGPUShape(bs.createTextureQuad("CDH_108.png"),GL_REPEAT, GL_NEAREST)

	#Segundo año
	CDGP201 =  es.toGPUShape(bs.createTextureQuad("CDGP_201.png"),GL_REPEAT, GL_NEAREST)
	CDGP202 =  es.toGPUShape(bs.createTextureQuad("CDGP_202.png"),GL_REPEAT, GL_NEAREST)
	CDGP203 =  es.toGPUShape(bs.createTextureQuad("CDGP_203.png"),GL_REPEAT, GL_NEAREST)
	CDGT204 =  es.toGPUShape(bs.createTextureQuad("CDGT_204.png"),GL_REPEAT, GL_NEAREST)
	CDGT205 =  es.toGPUShape(bs.createTextureQuad("CDGT_205.png"),GL_REPEAT, GL_NEAREST)
	CDGH206 =  es.toGPUShape(bs.createTextureQuad("CDGH_206.png"),GL_REPEAT, GL_NEAREST)
	CDGH207 =  es.toGPUShape(bs.createTextureQuad("CDGH_207.png"),GL_REPEAT, GL_NEAREST)
	CDGH208 =  es.toGPUShape(bs.createTextureQuad("CDGH_208.png"),GL_REPEAT, GL_NEAREST)

	#Quinto Semestre 
	CDGP301 =  es.toGPUShape(bs.createTextureQuad("CDGP_301.png"),GL_REPEAT, GL_NEAREST)
	CDGT302 =  es.toGPUShape(bs.createTextureQuad("CDGT_302.png"),GL_REPEAT, GL_NEAREST)
	CDGT303 =  es.toGPUShape(bs.createTextureQuad("CDGT_303.png"),GL_REPEAT, GL_NEAREST)
	CDGT304 =  es.toGPUShape(bs.createTextureQuad("CDGT_304.png"),GL_REPEAT, GL_NEAREST)
	CDGH305 =  es.toGPUShape(bs.createTextureQuad("CDGH_305.png"),GL_REPEAT, GL_NEAREST)
	CDGH306 =  es.toGPUShape(bs.createTextureQuad("CDGH_306.png"),GL_REPEAT, GL_NEAREST)
	CDGH307 =  es.toGPUShape(bs.createTextureQuad("CDGH_307.png"),GL_REPEAT, GL_NEAREST)
	CDE1 =  es.toGPUShape(bs.createTextureQuad("CDE_1.png"),GL_REPEAT, GL_NEAREST)

	#Sexto Semestre 
	CDGP401 =  es.toGPUShape(bs.createTextureQuad("CDGP_401.png"),GL_REPEAT, GL_NEAREST)
	CDGT402 =  es.toGPUShape(bs.createTextureQuad("CDGT_402.png"),GL_REPEAT, GL_NEAREST)
	CDGT403 =  es.toGPUShape(bs.createTextureQuad("CDGT_403.png"),GL_REPEAT, GL_NEAREST)
	CDGT404 =  es.toGPUShape(bs.createTextureQuad("CDGT_404.png"),GL_REPEAT, GL_NEAREST)
	CDGH405 =  es.toGPUShape(bs.createTextureQuad("CDGH_405.png"),GL_REPEAT, GL_NEAREST)
	CDGH406 =  es.toGPUShape(bs.createTextureQuad("CDGH_406.png"),GL_REPEAT, GL_NEAREST)
	CDGH407 =  es.toGPUShape(bs.createTextureQuad("CDGH_407.png"),GL_REPEAT, GL_NEAREST)
	CDE2 =  es.toGPUShape(bs.createTextureQuad("CDE_2.png"),GL_REPEAT, GL_NEAREST)

	#Septimo Semestre
	CDGP501 =  es.toGPUShape(bs.createTextureQuad("CDGP_501.png"),GL_REPEAT, GL_NEAREST)
	CDGP502 =  es.toGPUShape(bs.createTextureQuad("CDGP_502.png"),GL_REPEAT, GL_NEAREST)
	CDGT503 =  es.toGPUShape(bs.createTextureQuad("CDGT_503.png"),GL_REPEAT, GL_NEAREST)
	CDGH504 =  es.toGPUShape(bs.createTextureQuad("CDGH_504.png"),GL_REPEAT, GL_NEAREST)
	CDGH505 =  es.toGPUShape(bs.createTextureQuad("CDGH_505.png"),GL_REPEAT, GL_NEAREST)
	CDGH506 =  es.toGPUShape(bs.createTextureQuad("CDGH_506.png"),GL_REPEAT, GL_NEAREST)
	CDGH507 =  es.toGPUShape(bs.createTextureQuad("CDGH_507.png"),GL_REPEAT, GL_NEAREST)
	CDE3 =  es.toGPUShape(bs.createTextureQuad("CDE_2.png"),GL_REPEAT, GL_NEAREST)


	#Octavo Semestre
	CDGP601 =  es.toGPUShape(bs.createTextureQuad("CDGP_601.png"),GL_REPEAT, GL_NEAREST)
	CDGP602 =  es.toGPUShape(bs.createTextureQuad("CDGP_602.png"),GL_REPEAT, GL_NEAREST)
	CDGT603 =  es.toGPUShape(bs.createTextureQuad("CDGT_603.png"),GL_REPEAT, GL_NEAREST)
	CDGH604 =  es.toGPUShape(bs.createTextureQuad("CDGH_604.png"),GL_REPEAT, GL_NEAREST)
	CDGH605 =  es.toGPUShape(bs.createTextureQuad("CDGH_605.png"),GL_REPEAT, GL_NEAREST)
	CDGH606 =  es.toGPUShape(bs.createTextureQuad("CDGH_606.png"),GL_REPEAT, GL_NEAREST)
	CDE4 =  es.toGPUShape(bs.createTextureQuad("CDE_4.png"),GL_REPEAT, GL_NEAREST)


	#Noveno Semestre
	CDG701 =  es.toGPUShape(bs.createTextureQuad("CDG_701.png"),GL_REPEAT, GL_NEAREST)
	CDG702 =  es.toGPUShape(bs.createTextureQuad("CDG_702.png"),GL_REPEAT, GL_NEAREST)


	#Decimo Semestre 
	CDG801 =  es.toGPUShape(bs.createTextureQuad("CDG_801.png"),GL_REPEAT, GL_NEAREST)


	Tap_DP_101 = sg.SceneGraphNode("Tap_DP_101") #Se crea la 'tapa' para el cubo
	Tap_DP_101.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DP_101.childs += [CDP101]


	Tap_DP_102 = sg.SceneGraphNode("Tap_DP_102") #Se crea la 'tapa' para el cubo
	Tap_DP_102.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DP_102.childs += [CDP102]


	Tap_DP_103 = sg.SceneGraphNode("Tap_DP_103") #Se crea la 'tapa' para el cubo
	Tap_DP_103.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DP_103.childs += [CDP103]


	Tap_DT_104 = sg.SceneGraphNode("Tap_DT_104") #Se crea la 'tapa' para el cubo
	Tap_DT_104.transform = tr.matmul([tr.translate(0, 0,0.252),tr.uniformScale(0.5)])
	Tap_DT_104.childs += [CDT104]


	Tap_DT_105 = sg.SceneGraphNode("Tap_DT_105") #Se crea la 'tapa' para el cubo
	Tap_DT_105.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DT_105.childs += [CDT105]


	Tap_DH_106 = sg.SceneGraphNode("Tap_DH_106") #Se crea la 'tapa' para el cubo
	Tap_DH_106.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DH_106.childs += [CDH106]


	Tap_DH_107 = sg.SceneGraphNode("Tap_DH_107") #Se crea la 'tapa' para el cubo
	Tap_DH_107.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DH_107.childs += [CDH107]


	Tap_DH_108 = sg.SceneGraphNode("Tap_DH_108") #Se crea la 'tapa' para el cubo
	Tap_DH_108.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DH_108.childs += [CDH108]




	#Segundo año 
	Tap_DGP_201 = sg.SceneGraphNode("Tap_DGP_201") #Se crea la 'tapa' para el cubo
	Tap_DGP_201.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_201.childs += [CDGP201]


	Tap_DGP_202 = sg.SceneGraphNode("Tap_DGP_202") #Se crea la 'tapa' para el cubo
	Tap_DGP_202.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_202.childs += [CDGP202]


	Tap_DGP_203 = sg.SceneGraphNode("Tap_DGP_203") #Se crea la 'tapa' para el cubo
	Tap_DGP_203.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_203.childs += [CDGP203]


	Tap_DGT_204 = sg.SceneGraphNode("Tap_DGT_204") #Se crea la 'tapa' para el cubo
	Tap_DGT_204.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_204.childs += [CDGT204]


	Tap_DGT_205 = sg.SceneGraphNode("Tap_DGT_205") #Se crea la 'tapa' para el cubo
	Tap_DGT_205.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_205.childs += [CDGT205]


	Tap_DGH_206 = sg.SceneGraphNode("Tap_DGH_206") #Se crea la 'tapa' para el cubo
	Tap_DGH_206.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_206.childs += [CDGH206]


	Tap_DGH_207 = sg.SceneGraphNode("Tap_DGH_207") #Se crea la 'tapa' para el cubo
	Tap_DGH_207.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_207.childs += [CDGH207]
	

	Tap_DGH_208 = sg.SceneGraphNode("Tap_DGH_208") #Se crea la 'tapa' para el cubo
	Tap_DGH_208.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_208.childs += [CDGH208]




	#Quinto Semestre 

	Tap_DGP_301 = sg.SceneGraphNode("Tap_DGP_301") #Se crea la 'tapa' para el cubo
	Tap_DGP_301.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_301.childs += [CDGP301]


	Tap_DGT_302 = sg.SceneGraphNode("Tap_DGT_302") #Se crea la 'tapa' para el cubo
	Tap_DGT_302.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_302.childs += [CDGT302]


	Tap_DGT_303 = sg.SceneGraphNode("Tap_DGT_303") #Se crea la 'tapa' para el cubo
	Tap_DGT_303.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_303.childs += [CDGT303]


	Tap_DGT_304 = sg.SceneGraphNode("Tap_DGT_304") #Se crea la 'tapa' para el cubo
	Tap_DGT_304.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_304.childs += [CDGT304]


	Tap_DGH_305 = sg.SceneGraphNode("Tap_DGH_305") #Se crea la 'tapa' para el cubo
	Tap_DGH_305.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_305.childs += [CDGH305]


	Tap_DGH_306 = sg.SceneGraphNode("Tap_DGH_306") #Se crea la 'tapa' para el cubo
	Tap_DGH_306.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_306.childs += [CDGH306]


	Tap_DGH_307 = sg.SceneGraphNode("Tap_DGH_307") #Se crea la 'tapa' para el cubo
	Tap_DGH_307.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_307.childs += [CDGH307]


	Tap_DE_1 = sg.SceneGraphNode("Tap_DE_1") #Se crea la 'tapa' para el cubo
	Tap_DE_1.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DE_1.childs += [CDE1]




	#Sexto Semestre 
	Tap_DGP_401 = sg.SceneGraphNode("Tap_DGP_401") #Se crea la 'tapa' para el cubo
	Tap_DGP_401.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_401.childs += [CDGP401]


	Tap_DGT_402 = sg.SceneGraphNode("Tap_DGT_402") #Se crea la 'tapa' para el cubo
	Tap_DGT_402.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_402.childs += [CDGT402]


	Tap_DGT_403 = sg.SceneGraphNode("Tap_DGT_403") #Se crea la 'tapa' para el cubo
	Tap_DGT_403.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_403.childs += [CDGT403]


	Tap_DGT_404 = sg.SceneGraphNode("Tap_DGT_404") #Se crea la 'tapa' para el cubo
	Tap_DGT_404.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_404.childs += [CDGT404]


	Tap_DGH_405 = sg.SceneGraphNode("Tap_DGH_405") #Se crea la 'tapa' para el cubo
	Tap_DGH_405.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_405.childs += [CDGH405]


	Tap_DGH_406 = sg.SceneGraphNode("Tap_DGH_406") #Se crea la 'tapa' para el cubo
	Tap_DGH_406.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_406.childs += [CDGH406]


	Tap_DGH_407 = sg.SceneGraphNode("Tap_DGH_407") #Se crea la 'tapa' para el cubo
	Tap_DGH_407.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_407.childs += [CDGH407]


	Tap_DE_2 = sg.SceneGraphNode("Tap_DE_2") #Se crea la 'tapa' para el cubo
	Tap_DE_2.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DE_2.childs += [CDE2]




	#Septimo Semestre

	Tap_DGP_501 = sg.SceneGraphNode("Tap_DGP_501") #Se crea la 'tapa' para el cubo
	Tap_DGP_501.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_501.childs += [CDGP501]


	Tap_DGP_502 = sg.SceneGraphNode("Tap_DGP_502") #Se crea la 'tapa' para el cubo
	Tap_DGP_502.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_502.childs += [CDGP502]


	Tap_DGT_503 = sg.SceneGraphNode("Tap_DGT_503") #Se crea la 'tapa' para el cubo
	Tap_DGT_503.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_503.childs += [CDGT503]


	Tap_DGH_504 = sg.SceneGraphNode("Tap_DGH_504") #Se crea la 'tapa' para el cubo
	Tap_DGH_504.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_504.childs += [CDGH504]


	Tap_DGH_505 = sg.SceneGraphNode("Tap_DGH_505") #Se crea la 'tapa' para el cubo
	Tap_DGH_505.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_505.childs += [CDGH505]


	Tap_DGH_506 = sg.SceneGraphNode("Tap_DGH_506") #Se crea la 'tapa' para el cubo
	Tap_DGH_506.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_506.childs += [CDGH506]


	Tap_DGH_507 = sg.SceneGraphNode("Tap_DGH_507") #Se crea la 'tapa' para el cubo
	Tap_DGH_507.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_507.childs += [CDGH507]


	Tap_DE_3 = sg.SceneGraphNode("Tap_DE_3") #Se crea la 'tapa' para el cubo
	Tap_DE_3.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DE_3.childs += [CDE3]




	#Octavo Semestre 

	Tap_DGP_601 = sg.SceneGraphNode("Tap_DGP_601") #Se crea la 'tapa' para el cubo
	Tap_DGP_601.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_601.childs += [CDGP601]


	Tap_DGP_602 = sg.SceneGraphNode("Tap_DGP_602") #Se crea la 'tapa' para el cubo
	Tap_DGP_602.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_602.childs += [CDGP602]


	Tap_DGT_603 = sg.SceneGraphNode("Tap_DGT_603") #Se crea la 'tapa' para el cubo
	Tap_DGT_603.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_603.childs += [CDGT603]


	Tap_DGH_604 = sg.SceneGraphNode("Tap_DGH_604") #Se crea la 'tapa' para el cubo
	Tap_DGH_604.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_604.childs += [CDGH604]


	Tap_DGH_605 = sg.SceneGraphNode("Tap_DGH_605") #Se crea la 'tapa' para el cubo
	Tap_DGH_605.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_605.childs += [CDGH605]


	Tap_DGH_606 = sg.SceneGraphNode("Tap_DGH_606") #Se crea la 'tapa' para el cubo
	Tap_DGH_606.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_606.childs += [CDGH606]


	Tap_DE_4 = sg.SceneGraphNode("Tap_DE_4") #Se crea la 'tapa' para el cubo
	Tap_DE_4.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DE_4.childs += [CDE4]




	#Noveno semestre 
	Tap_DG_701 = sg.SceneGraphNode("Tap_DG_701") #Se crea la 'tapa' para el cubo
	Tap_DG_701.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DG_701.childs += [CDG701]


	Tap_DG_702 = sg.SceneGraphNode("Tap_DG_702") #Se crea la 'tapa' para el cubo
	Tap_DG_702.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DG_702.childs += [CDG702]




	#Decimo semestre 
	Tap_DG_801 = sg.SceneGraphNode("Tap_DG_801") #Se crea la 'tapa' para el cubo
	Tap_DG_801.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DG_801.childs += [CDG801]


	if codigo == 'DP_101':
		return Tap_DP_101

	elif codigo == 'DP_102':
		return Tap_DP_102

	elif codigo == 'DP_103':
		return Tap_DP_103

	elif codigo == 'DT_104':
		return Tap_DT_104

	elif codigo == 'DT_105':
		return Tap_DT_105

	elif codigo == 'DH_106':
		return Tap_DH_106

	elif codigo == 'DH_107':
		return Tap_DH_107

	elif codigo == 'DH_108':
		return Tap_DH_108

	elif codigo == 'DGP_201':
		return Tap_DGP_201

	elif codigo == 'DGP_202':
		return Tap_DGP_202

	elif codigo == 'DGP_203':
		return Tap_DGP_203

	elif codigo == 'DGT_204':
		return Tap_DGT_204

	elif codigo == 'DGT_205':
		return Tap_DGT_205

	elif codigo == 'DGH_206':
		return Tap_DGH_206

	elif codigo == 'DGH_207':
		return Tap_DGH_207

	elif codigo == 'DGH_208':
		return Tap_DGH_208

	elif codigo == 'DGP_301':
		return Tap_DGP_301

	elif codigo == 'DGT_302':
		return Tap_DGT_302

	elif codigo == 'DGT_303':
		return Tap_DGT_303

	elif codigo == 'DGT_304':
		return Tap_DGT_304

	elif codigo == 'DGH_305':
		return Tap_DGH_305

	elif codigo == 'DGH_306':
		return Tap_DGH_306

	elif codigo == 'DGH_307':
		return Tap_DGH_307

	elif codigo == 'DE_1':
		return Tap_DE_1

	elif codigo == 'DGP_401':
		return Tap_DGP_401

	elif codigo == 'DGT_402':
		return Tap_DGT_402

	elif codigo == 'DGT_403':
		return Tap_DGT_403

	elif codigo == 'DGT_404':
		return Tap_DGT_404

	elif codigo == 'DGH_405':
		return Tap_DGH_405

	elif codigo == 'DGH_406':
		return Tap_DGH_406

	elif codigo == 'DGH_407':
		return Tap_DGH_407

	elif codigo == 'DE_2':
		return Tap_DE_2

	elif codigo == 'DGP_501':
		return Tap_DGP_501

	elif codigo == 'DGP_502':
		return Tap_DGP_502

	elif codigo == 'DGT_503':
		return Tap_DGT_503

	elif codigo == 'DGH_504':
		return Tap_DGH_504

	elif codigo == 'DGH_505':
		return Tap_DGH_505

	elif codigo == 'DGH_506':
		return Tap_DGH_506

	elif codigo == 'DGH_507':
		return Tap_DGH_507

	elif codigo == 'DE_3':
		return Tap_DE_3

	elif codigo == 'DGP_601':
		return Tap_DGP_601

	elif codigo == 'DGP_602':
		return Tap_DGP_602

	elif codigo == 'DGT_603':
		return Tap_DGT_603

	elif codigo == 'DGH_604':
		return Tap_DGH_604

	elif codigo == 'DGH_605':
		return Tap_DGH_605

	elif codigo == 'DGH_606':
		return Tap_DGH_606

	elif codigo == 'DE_4':
		return Tap_DE_4

	elif codigo == 'DG_701':
		return Tap_DG_701

	elif codigo == 'DG_702':
		return Tap_DG_702

	elif codigo == 'DG_801':
		return Tap_DG_801








def TapaCursoNorm(codigo):
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






	Tap_DP_101 = sg.SceneGraphNode("Tap_DP_101") #Se crea la 'tapa' para el cubo
	Tap_DP_101.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DP_101.childs += [DP101]


	Tap_DP_102 = sg.SceneGraphNode("Tap_DP_102") #Se crea la 'tapa' para el cubo
	Tap_DP_102.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DP_102.childs += [DP102]


	Tap_DP_103 = sg.SceneGraphNode("Tap_DP_103") #Se crea la 'tapa' para el cubo
	Tap_DP_103.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DP_103.childs += [DP103]


	Tap_DT_104 = sg.SceneGraphNode("Tap_DT_104") #Se crea la 'tapa' para el cubo
	Tap_DT_104.transform = tr.matmul([tr.translate(0, 0,0.252),tr.uniformScale(0.5)])
	Tap_DT_104.childs += [DT104]


	Tap_DT_105 = sg.SceneGraphNode("Tap_DT_105") #Se crea la 'tapa' para el cubo
	Tap_DT_105.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DT_105.childs += [DT105]


	Tap_DH_106 = sg.SceneGraphNode("Tap_DH_106") #Se crea la 'tapa' para el cubo
	Tap_DH_106.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DH_106.childs += [DH106]


	Tap_DH_107 = sg.SceneGraphNode("Tap_DH_107") #Se crea la 'tapa' para el cubo
	Tap_DH_107.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DH_107.childs += [DH107]


	Tap_DH_108 = sg.SceneGraphNode("Tap_DH_108") #Se crea la 'tapa' para el cubo
	Tap_DH_108.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DH_108.childs += [DH108]




	#Segundo año 
	Tap_DGP_201 = sg.SceneGraphNode("Tap_DGP_201") #Se crea la 'tapa' para el cubo
	Tap_DGP_201.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_201.childs += [DGP201]


	Tap_DGP_202 = sg.SceneGraphNode("Tap_DGP_202") #Se crea la 'tapa' para el cubo
	Tap_DGP_202.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_202.childs += [DGP202]


	Tap_DGP_203 = sg.SceneGraphNode("Tap_DGP_203") #Se crea la 'tapa' para el cubo
	Tap_DGP_203.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_203.childs += [DGP203]


	Tap_DGT_204 = sg.SceneGraphNode("Tap_DGT_204") #Se crea la 'tapa' para el cubo
	Tap_DGT_204.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_204.childs += [DGT204]


	Tap_DGT_205 = sg.SceneGraphNode("Tap_DGT_205") #Se crea la 'tapa' para el cubo
	Tap_DGT_205.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_205.childs += [DGT205]


	Tap_DGH_206 = sg.SceneGraphNode("Tap_DGH_206") #Se crea la 'tapa' para el cubo
	Tap_DGH_206.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_206.childs += [DGH206]


	Tap_DGH_207 = sg.SceneGraphNode("Tap_DGH_207") #Se crea la 'tapa' para el cubo
	Tap_DGH_207.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_207.childs += [DGH207]
	

	Tap_DGH_208 = sg.SceneGraphNode("Tap_DGH_208") #Se crea la 'tapa' para el cubo
	Tap_DGH_208.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_208.childs += [DGH208]




	#Quinto Semestre 

	Tap_DGP_301 = sg.SceneGraphNode("Tap_DGP_301") #Se crea la 'tapa' para el cubo
	Tap_DGP_301.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_301.childs += [DGP301]


	Tap_DGT_302 = sg.SceneGraphNode("Tap_DGT_302") #Se crea la 'tapa' para el cubo
	Tap_DGT_302.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_302.childs += [DGT302]


	Tap_DGT_303 = sg.SceneGraphNode("Tap_DGT_303") #Se crea la 'tapa' para el cubo
	Tap_DGT_303.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_303.childs += [DGT303]


	Tap_DGT_304 = sg.SceneGraphNode("Tap_DGT_304") #Se crea la 'tapa' para el cubo
	Tap_DGT_304.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_304.childs += [DGT304]


	Tap_DGH_305 = sg.SceneGraphNode("Tap_DGH_305") #Se crea la 'tapa' para el cubo
	Tap_DGH_305.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_305.childs += [DGH305]


	Tap_DGH_306 = sg.SceneGraphNode("Tap_DGH_306") #Se crea la 'tapa' para el cubo
	Tap_DGH_306.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_306.childs += [DGH306]


	Tap_DGH_307 = sg.SceneGraphNode("Tap_DGH_307") #Se crea la 'tapa' para el cubo
	Tap_DGH_307.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_307.childs += [DGH307]


	Tap_DE_1 = sg.SceneGraphNode("Tap_DE_1") #Se crea la 'tapa' para el cubo
	Tap_DE_1.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DE_1.childs += [DE1]




	#Sexto Semestre 
	Tap_DGP_401 = sg.SceneGraphNode("Tap_DGP_401") #Se crea la 'tapa' para el cubo
	Tap_DGP_401.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_401.childs += [DGP401]


	Tap_DGT_402 = sg.SceneGraphNode("Tap_DGT_402") #Se crea la 'tapa' para el cubo
	Tap_DGT_402.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_402.childs += [DGT402]


	Tap_DGT_403 = sg.SceneGraphNode("Tap_DGT_403") #Se crea la 'tapa' para el cubo
	Tap_DGT_403.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_403.childs += [DGT403]


	Tap_DGT_404 = sg.SceneGraphNode("Tap_DGT_404") #Se crea la 'tapa' para el cubo
	Tap_DGT_404.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_404.childs += [DGT404]


	Tap_DGH_405 = sg.SceneGraphNode("Tap_DGH_405") #Se crea la 'tapa' para el cubo
	Tap_DGH_405.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_405.childs += [DGH405]


	Tap_DGH_406 = sg.SceneGraphNode("Tap_DGH_406") #Se crea la 'tapa' para el cubo
	Tap_DGH_406.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_406.childs += [DGH406]


	Tap_DGH_407 = sg.SceneGraphNode("Tap_DGH_407") #Se crea la 'tapa' para el cubo
	Tap_DGH_407.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_407.childs += [DGH407]


	Tap_DE_2 = sg.SceneGraphNode("Tap_DE_2") #Se crea la 'tapa' para el cubo
	Tap_DE_2.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DE_2.childs += [DE2]




	#Septimo Semestre

	Tap_DGP_501 = sg.SceneGraphNode("Tap_DGP_501") #Se crea la 'tapa' para el cubo
	Tap_DGP_501.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_501.childs += [DGP501]


	Tap_DGP_502 = sg.SceneGraphNode("Tap_DGP_502") #Se crea la 'tapa' para el cubo
	Tap_DGP_502.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_502.childs += [DGP502]


	Tap_DGT_503 = sg.SceneGraphNode("Tap_DGT_503") #Se crea la 'tapa' para el cubo
	Tap_DGT_503.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_503.childs += [DGT503]


	Tap_DGH_504 = sg.SceneGraphNode("Tap_DGH_504") #Se crea la 'tapa' para el cubo
	Tap_DGH_504.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_504.childs += [DGH504]


	Tap_DGH_505 = sg.SceneGraphNode("Tap_DGH_505") #Se crea la 'tapa' para el cubo
	Tap_DGH_505.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_505.childs += [DGH505]


	Tap_DGH_506 = sg.SceneGraphNode("Tap_DGH_506") #Se crea la 'tapa' para el cubo
	Tap_DGH_506.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_506.childs += [DGH506]


	Tap_DGH_507 = sg.SceneGraphNode("Tap_DGH_507") #Se crea la 'tapa' para el cubo
	Tap_DGH_507.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_507.childs += [DGH507]


	Tap_DE_3 = sg.SceneGraphNode("Tap_DE_3") #Se crea la 'tapa' para el cubo
	Tap_DE_3.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DE_3.childs += [DE3]




	#Octavo Semestre 

	Tap_DGP_601 = sg.SceneGraphNode("Tap_DGP_601") #Se crea la 'tapa' para el cubo
	Tap_DGP_601.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_601.childs += [DGP601]


	Tap_DGP_602 = sg.SceneGraphNode("Tap_DGP_602") #Se crea la 'tapa' para el cubo
	Tap_DGP_602.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGP_602.childs += [DGP602]


	Tap_DGT_603 = sg.SceneGraphNode("Tap_DGT_603") #Se crea la 'tapa' para el cubo
	Tap_DGT_603.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGT_603.childs += [DGT603]


	Tap_DGH_604 = sg.SceneGraphNode("Tap_DGH_604") #Se crea la 'tapa' para el cubo
	Tap_DGH_604.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_604.childs += [DGH604]


	Tap_DGH_605 = sg.SceneGraphNode("Tap_DGH_605") #Se crea la 'tapa' para el cubo
	Tap_DGH_605.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_605.childs += [DGH605]


	Tap_DGH_606 = sg.SceneGraphNode("Tap_DGH_606") #Se crea la 'tapa' para el cubo
	Tap_DGH_606.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DGH_606.childs += [DGH606]


	Tap_DE_4 = sg.SceneGraphNode("Tap_DE_4") #Se crea la 'tapa' para el cubo
	Tap_DE_4.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DE_4.childs += [DE4]




	#Noveno semestre 
	Tap_DG_701 = sg.SceneGraphNode("Tap_DG_701") #Se crea la 'tapa' para el cubo
	Tap_DG_701.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DG_701.childs += [DG701]


	Tap_DG_702 = sg.SceneGraphNode("Tap_DG_702") #Se crea la 'tapa' para el cubo
	Tap_DG_702.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DG_702.childs += [DG702]




	#Decimo semestre 
	Tap_DG_801 = sg.SceneGraphNode("Tap_DG_801") #Se crea la 'tapa' para el cubo
	Tap_DG_801.transform = tr.matmul([tr.translate(0,0,0.252),tr.uniformScale(0.5)])
	Tap_DG_801.childs += [DG801]



	if codigo == 'DP_101':
		return Tap_DP_101

	elif codigo == 'DP_102':
		return Tap_DP_102

	elif codigo == 'DP_103':
		return Tap_DP_103

	elif codigo == 'DT_104':
		return Tap_DT_104

	elif codigo == 'DT_105':
		return Tap_DT_105

	elif codigo == 'DH_106':
		return Tap_DH_106

	elif codigo == 'DH_107':
		return Tap_DH_107

	elif codigo == 'DH_108':
		return Tap_DH_108

	elif codigo == 'DGP_201':
		return Tap_DGP_201

	elif codigo == 'DGP_202':
		return Tap_DGP_202

	elif codigo == 'DGP_203':
		return Tap_DGP_203

	elif codigo == 'DGT_204':
		return Tap_DGT_204

	elif codigo == 'DGT_205':
		return Tap_DGT_205

	elif codigo == 'DGH_206':
		return Tap_DGH_206

	elif codigo == 'DGH_207':
		return Tap_DGH_207

	elif codigo == 'DGH_208':
		return Tap_DGH_208

	elif codigo == 'DGP_301':
		return Tap_DGP_301

	elif codigo == 'DGT_302':
		return Tap_DGT_302

	elif codigo == 'DGT_303':
		return Tap_DGT_303

	elif codigo == 'DGT_304':
		return Tap_DGT_304

	elif codigo == 'DGH_305':
		return Tap_DGH_305

	elif codigo == 'DGH_306':
		return Tap_DGH_306

	elif codigo == 'DGH_307':
		return Tap_DGH_307

	elif codigo == 'DE_1':
		return Tap_DE_1

	elif codigo == 'DGP_401':
		return Tap_DGP_401

	elif codigo == 'DGT_402':
		return Tap_DGT_402

	elif codigo == 'DGT_403':
		return Tap_DGT_403

	elif codigo == 'DGT_404':
		return Tap_DGT_404

	elif codigo == 'DGH_405':
		return Tap_DGH_405

	elif codigo == 'DGH_406':
		return Tap_DGH_406

	elif codigo == 'DGH_407':
		return Tap_DGH_407

	elif codigo == 'DE_2':
		return Tap_DE_2

	elif codigo == 'DGP_501':
		return Tap_DGP_501

	elif codigo == 'DGP_502':
		return Tap_DGP_502

	elif codigo == 'DGT_503':
		return Tap_DGT_503

	elif codigo == 'DGH_504':
		return Tap_DGH_504

	elif codigo == 'DGH_505':
		return Tap_DGH_505

	elif codigo == 'DGH_506':
		return Tap_DGH_506

	elif codigo == 'DGH_507':
		return Tap_DGH_507

	elif codigo == 'DE_3':
		return Tap_DE_3

	elif codigo == 'DGP_601':
		return Tap_DGP_601

	elif codigo == 'DGP_602':
		return Tap_DGP_602

	elif codigo == 'DGT_603':
		return Tap_DGT_603

	elif codigo == 'DGH_604':
		return Tap_DGH_604

	elif codigo == 'DGH_605':
		return Tap_DGH_605

	elif codigo == 'DGH_606':
		return Tap_DGH_606

	elif codigo == 'DE_4':
		return Tap_DE_4

	elif codigo == 'DG_701':
		return Tap_DG_701

	elif codigo == 'DG_702':
		return Tap_DG_702

	elif codigo == 'DG_801':
		return Tap_DG_801


