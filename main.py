from OpenGL.GL import *
import glfw
import numpy as np
import game

AREA_SIZE = 20
direction = "W"

def coord_check(coords, window):
	if coords[0][0] == 21 or coords[0][1] == 21:
		glfw.set_window_should_close(window, True)

def setAspect(width, height):
	return width / height

def window_size_callback(window, width, height):
	glfw.set_window_size(window, 400, 400)

def keyboard_callback(window):
	global direction
	if glfw.get_window_attrib(window, glfw.FOCUSED) == glfw.TRUE:
		if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
			glfw.set_window_should_close(window, True)
		if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
			direction = "W"
		if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
			direction = "S"
		if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
			direction = "A"
		if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
			direction = "D"

def main():
	global direction

	glfw.init()
	glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
	glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
	glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_COMPAT_PROFILE)

	window = glfw.create_window(400, 400, "OpenGL game", None, None)

	glfw.make_context_current(window)

	glfw.set_window_size_callback(window, window_size_callback)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	aspect = setAspect(400, 400)
	glOrtho(-1.0, 1.0 * aspect, -1.0, 1.0, -1.0, 100)
	glScalef(1/AREA_SIZE,1/AREA_SIZE,1/AREA_SIZE)
	glTranslatef(-10, -10, -10)

	time = 0
	game.gen_food()

	while not glfw.window_should_close(window):

		keyboard_callback(window)

		glClearColor(0.1, 0.1, 0.3, 1.0)
		glClear(GL_COLOR_BUFFER_BIT)

		game.draw_borders(10, 10)
		game.food_draw()
		game.snake_draw()

		if time == 100:
			game.snake_move(dir=direction)
			coord_check(game.snake_pos, window)
			time = 0
			print(game.snake_pos[0][0], game.snake_pos[0][1])

		time += 1
		glfw.swap_buffers(window)
		glfw.poll_events()


main()