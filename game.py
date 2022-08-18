import numpy as np
from OpenGL.GL import *
import random

temp_dir = "W"

MAX_BLOCKS = 20 * 20

snake_pos = np.zeros([MAX_BLOCKS, 2])
snake_length = 1

snake_pos[0], snake_pos[1] = np.array([[10, 10],[10, 9]])

food = np.zeros([2])

def draw(x, y, r=1, g=0, b=1):

	glBegin(GL_TRIANGLES)
	glColor3f(r,g,b)
	glVertex3f(x-0.45, y-0.45, 1)
	glVertex3f(x+0.45, y-0.45, 1)
	glVertex3f(x+0.45, y+0.45, 1)
	glVertex3f(x-0.45, y-0.45, 1)
	glVertex3f(x-0.45, y+0.45, 1)
	glVertex3f(x+0.45, y+0.45, 1)
	glEnd()

def draw_borders(x, y):

	glBegin(GL_LINE_LOOP)
	glColor3f(1,1,1)
	glVertex3f(x-10.5, y-10.5, 1)
	glVertex3f(x+10.5, y-10.5, 1)
	glVertex3f(x+10.5, y+10.5, 1)
	glVertex3f(x-10.5, y+10.5, 1)
	glEnd()


def snake_walk(dir, xpos=10, ypos=10):
	y = ypos
	x = xpos
	if dir == "W":
		y += 1
	if dir == "S":
		y -= 1
	if dir == "A":
		x -= 1
	if dir == "D":
		x += 1


	return x, y

def gen_food():
	global food
	food = np.array([random.randint(0, 20), random.randint(0, 20)])
	i = snake_length
	while(i > 0):
		if food[0] == snake_pos[i][0] and food[1] == snake_pos[i][1]:
			gen_food()
		i-=1

def eat_food():
	global snake_length
	snake_length += 1
	snake_pos[snake_length][0] = snake_pos[snake_length - 1][0]
	snake_pos[snake_length][1] = snake_pos[snake_length - 1][1]
	gen_food()

def food_draw():
	draw(food[0], food[1], r=1, g=0, b=0)

def snake_move(dir):
	global snake_length
	i = snake_length
	while(i > 0):
		snake_pos[i] = snake_pos[i-1]
		i-=1
	snake_pos[0][0], snake_pos[0][1] = snake_walk(dir, snake_pos[0][0], snake_pos[0][1])
	if snake_pos[0][0] == food[0] and snake_pos[0][1] == food[1]:
		eat_food()

def snake_draw():
	i = snake_length
	while(i > 0):
		draw(snake_pos[i][0], snake_pos[i][1])
		i-=1
	draw(snake_pos[0][0], snake_pos[0][1], r=0, g=0.5, b=0)

