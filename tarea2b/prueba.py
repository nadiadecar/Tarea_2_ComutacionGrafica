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
		print("apretando A")

	elif key == glfw.KEY_S:
		controller.semestre += 1
		controller.shift = True
		print("apretando S")

	elif key == glfw.KEY_D:
		controller.curso += 1
		controller.shift = True
		print("apretando D")


	elif key == glfw.KEY_W:
		controller.semestre -= 1
		controller.shift = True
		print("apretando W")

	elif key == glfw.KEY_C:
		controller.fondoE = "C"

	elif key == glfw.KEY_O:
		controller.fondoE = "O"

	elif key == glfw.KEY_R:
		controller.fondoE = "R"

	elif key == glfw.KEY_LEFT:
		print("apretando flecha izquierda")
		pass

	elif key == glfw.KEY_RIGHT:
		print("apretando flecha derecha")
		pass

	elif key == glfw.KEY_UP:
		print("apretando flecha arriba")
		pass

	elif key == glfw.KEY_DOWN:
		print("apretando flecha abajo")
		pass

	elif key == glfw.KEY_1:
		controller.uno = not controller.uno
		print("apretando 1")

	elif key == glfw.KEY_2:
		controller.dos = not controller.dos
		print("apretando 2")

	elif key == glfw.KEY_Z:
		print("apretando Z")
		pass

	elif key == glfw.KEY_X:
		print("apretando X")
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

	CuboMorado = sg.SceneGraphNode("CuboMorado") #Se crea la base para el cubo morado
	CuboMorado.transform = tr.matmul([tr.translate(0.8,0,0), tr.uniformScale(0.5)])
	CuboMorado.childs += [NormalCube]

	CuboTurquesa = sg.SceneGraphNode("CuboTurquesa")
	CuboTurquesa.transform = tr.matmul([tr.translate(0.27,0,0),tr.uniformScale(0.5)])
	CuboTurquesa.childs += [RequisitoDeCube]

	CuboCeleste = sg.SceneGraphNode("CuboCeleste")
	CuboCeleste.transform = tr.matmul([tr.translate(-0.27,0,0),tr.uniformScale(0.5)])
	CuboCeleste.childs += [RequisitoCube]

	CuboNaranjo = sg.SceneGraphNode("CuboNaranjo")
	CuboNaranjo.transform = tr.matmul([tr.translate(-0.8,0,0),tr.uniformScale(0.5)])
	CuboNaranjo.childs += [SelectedCube]

	return CuboMorado,CuboTurquesa,CuboCeleste,CuboNaranjo


if __name__ == "__main__":

    # Initialize glfw
    if not glfw.init():
        sys.exit()

    width = 600
    height = 600

    window = glfw.create_window(width, height, "3D cars via scene graph", None, None)

    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, on_key)

    # Assembling the shader program (pipeline) with both shaders
    mvcPipeline = es.SimpleTextureModelViewProjectionShaderProgram()
    
    # Telling OpenGL to use our shader program
    glUseProgram(mvcPipeline.shaderProgram)

    # Setting up the clear screen color
    glClearColor(1, 1, 1, 1.0)

    # As we work in 3D, we need to check which part is in front,
    # and which one is at the back
    glEnable(GL_DEPTH_TEST)

    # Creating shapes on GPU memory
    cuboM, cuboC, cuboT,cuboN = crearCubos()
   

    # Using the same view and projection matrices in the whole application
    projection = tr.perspective(45, float(width)/float(height), 0.1, 100)
    glUniformMatrix4fv(glGetUniformLocation(mvcPipeline.shaderProgram, "projection"), 1, GL_TRUE, projection)
    
    view = tr.lookAt(
            np.array([0.5,-3,3]),
            np.array([0,0,0]),
            np.array([0,0,1])
        )
    glUniformMatrix4fv(glGetUniformLocation(mvcPipeline.shaderProgram, "view"), 1, GL_TRUE, view)

    while not glfw.window_should_close(window):
        # Using GLFW to check for input events
        glfw.poll_events()

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Filling or not the shapes depending on the controller state
        if (controller.fillPolygon):
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)



        # Moving the red car and rotating its wheels

        # Uncomment to print the red car position on every iteration
        #print(sg.findPosition(redCarNode, "car"))

        # Drawing the Car
        sg.drawSceneGraphNode(cuboM, mvcPipeline, "model")
        sg.drawSceneGraphNode(cuboC, mvcPipeline, "model")
        sg.drawSceneGraphNode(cuboT, mvcPipeline, "model")
        sg.drawSceneGraphNode(cuboN, mvcPipeline, "model")

        # Once the render is done, buffers are swapped, showing only the complete scene.
        glfw.swap_buffers(window)

    
    glfw.terminate()