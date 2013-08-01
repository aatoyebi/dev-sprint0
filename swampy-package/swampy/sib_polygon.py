# Polygon excercise from Week 0

# Name: Amaka Atoyebi

import math
from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
bob.delay = .01
pu(bob)
rt(bob)
fd(bob, 50)
pd(bob)

# This is where you put code to move bob
def drawPoly(t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def square(t, length):
	n = 4
	angle = 90
	drawPoly(t, n, length, angle)

square(bob, 100)

def polygon(t, length, n):
	angle = 360/n
	drawPoly(t, n, length, angle)	

polygon(bob, 100, 6)

def arc(t, r, theta):
	arc_side = 2 * math.pi * r * abs(theta)/360
	n = int(arc_side/4) + 1
	step_length = arc_side/n
	step_angle = float(theta)/n

	drawPoly(t, n, step_length, step_angle)

def circle(t, r):
	arc(t, r, 180)

circle(bob, 100)


wait_for_user()					
