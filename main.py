from OpenGL.GL import *
import glfw
import numpy as np
import game

AREA_SIZE = 20
direction = "W"
isClicked = False

def coord_check(coords, window):
	i = game.snake_length
	while (i > 0):
		if (coords[0][0] == coords[i][0] and coords[0][1] == coords[i][1]) or (coords[0][0] == 21 or coords[0][1] == 21):
			glfw.set_window_should_close(window, True)
		i -= 1

def setAspect(width, height):
	return width / height

def window_size_callback(window, width, height):
	glfw.set_window_size(window, 400, 400)

def keyboard_callback(window):
	global direction, isClicked
	if glfw.get_window_attrib(window, glfw.FOCUSED) == glfw.TRUE:
		if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
			glfw.set_window_should_close(window, True)
		if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
			if direction != "S" and not isClicked:
				direction = "W"
				isClicked = True
		if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
			if direction != "W" and not isClicked:
				direction = "S"
				isClicked = True
		if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
			if direction != "D" and not isClicked:
				direction = "A"
				isClicked = True
		if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
			if direction != "A" and not isClicked:
				direction = "D"
				isClicked = True

def main():
	global direction, isClicked

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

		if time == 10:
			game.snake_move(dir=direction)
			coord_check(game.snake_pos, window)
			isClicked = False
			time = 0
			#print(game.snake_pos[0][0], game.snake_pos[0][1])

		time += 1
		glfw.swap_buffers(window)
		glfw.poll_events()


main()