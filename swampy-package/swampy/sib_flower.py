# Flower excercise (4.2) from Week 0

# Name: Amaka Atoyebi


import math
from TurtleWorld import *
world = TurtleWorld()			
bob = Turtle()				
bob.delay = .01			



# This is where you put code to move bob
def drawPoly(t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def arc(t, r, theta):
	arc_side = 2 * math.pi * r * abs(theta)/360
	n = int(arc_side/4) + 1
	step_length = arc_side/n
	step_angle = float(theta)/n

	drawPoly(t, n, step_length, step_angle)			

def drawPetal(t, r, angle):
	for i in range(2):
		arc(t, r, angle)
		lt(t, 180-angle)

def drawFlower(t, n, r, angle):
	for i in range(n):
		drawPetal(t, r, angle)
		lt(t, 360/n)

def forward(t, length):
	pu(t)
	fd(t, length)
	pd(t)

drawFlower(bob, 7, 60, 60)

forward(bob, 100)
drawFlower(bob, 10, 40, 80)

forward(bob, 100)
drawFlower(bob, 20, 140, 20)					


wait_for_user()					








wait_for_user()					

