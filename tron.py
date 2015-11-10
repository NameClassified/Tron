from visual import *
from math import *

scene.range = 600
scene.height = 620
scene.width = 600
scene.autoscale = False

topWall = box(pos = (0,600,0), size = vector(1200,10,0), color = color.cyan)
botWall = box(pos = (0,-600,0), size = vector(1200,10,0), color = color.cyan)
leftWall = box(pos = (-600,0,0), size = vector(10,1200,0), color = color.cyan)
rightWall = box(pos = (600,0,0), size = vector(10,1200,0), color = color.cyan)



for i in range(6):
	position = 100*i
	positionNeg = -100*i
 	line = box(pos = (position,0,0), size = vector(2,1200,0), color = color.cyan)
	lineNeg = box(pos = (positionNeg,0,0), size = vector(2,1200,0), color = color.cyan)

for i in range(6):
	position = 100*i
	positionNeg = -100*i
	line = box(pos = (0,position,0), size = vector(1200,2,0), color = color.cyan)
	lineNeg = box(pos = (0,positionNeg,0), size = vector(1200,2,0), color = color.cyan)

title = text(text = 'TRON', font = 'Bauhaus 93', \
color = color.cyan, height = 300, width = 300, depth = -500, pos = (-500,0,20))
directions = text(text = 'PRESS SPACE TO BEGIN', pos = (-300,-300,1), \
color = color.cyan, height = 50, width = 50, font = 'Bauhaus 93')

time = 0
deltat = 0.01

#creates bike 1
humanBike = box(pos = (150,0,0), size = vector(12,12,0),\
color = color.green, make_trail = True, material = materials.emissive)
humanBike.v = vector(0,0,0)
#humanBike.trail_object.material = materials.emissive


#creates bike 2
bike2 = box(pos = (-150,0,0), size = vector(12,12,0), \
color = color.magenta, make_trail = True, material = materials.emissive)
bike2.v = vector(0,0,0)
#bike2.trail_object.material = materials.emissive
end = False




def collisionCheck():
	#BIKE 1 WALL COLLISIONS: DONE
	if humanBike.pos.x - humanBike.size.x <= -600:
		humanBike.v.x = 0
		humanBike.v.y = 0
		deltat = 0
		gameEnd('purple')
	elif humanBike.pos.x + humanBike.size.x >= 600:
		humanBike.v.x = 0
		humanBike.v.y = 0
		deltat = 0
		gameEnd('purple')
	if humanBike.pos.y - humanBike.size.y <= -600:
		humanBike.v.x = 0
		humanBike.v.y = 0
		deltat = 0
		gameEnd('purple')
	elif humanBike.pos.y + humanBike.size.y >= 600:
		humanBike.v.x = 0
		humanBike.v.y = 0
		deltat = 0
		gameEnd('purple')

	#BIKE 2 WALL COLLISIONS: DONE
	if bike2.pos.x - bike2.size.x <= -600:
		bike2.v.x = 0
		bike2.v.y = 0
		deltat = 0
		gameEnd('green')
	elif bike2.pos.x + bike2.size.x >= 600:
		bike2.v.x = 0
		bike2.v.y = 0
		deltat = 0
		gameEnd('green')
	if bike2.pos.y - bike2.size.y <= -600:
		bike2.v.x = 0
		bike2.v.y = 0
		deltat = 0
		gameEnd('green')
	elif bike2.pos.y + bike2.size.y >= 600:
		bike2.v.x = 0
		bike2.v.y = 0
		deltat = 0
		gameEnd('green')

	#BIKE 1 TRAIL COLLISIONS
	for index in humanBike.trail_object.pos[:-1]:
		if humanBike.pos == index:
			humanBike.v.x = 0
			humanBike.v.y = 0
			deltat = 0
			gameEnd('purple')
	for index in bike2.trail_object.pos:
		if humanBike.pos == index:
			humanBike.v.x = 0
			humanBike.v.y = 0
			deltat = 0
			gameEnd('purple')

	#BIKE 2 TRAIL COLLISIONS
	for index in bike2.trail_object.pos[:-1]:
		if bike2.pos == index:
			bike2.v.x = 0
			bike2.v.y = 0
			deltat = 0
			gameEnd('green')
	for index in humanBike.trail_object.pos:
		if bike2.pos == index:
			bike2.v.x = 0
			bike2.v.y = 0
			deltat = 0
			gameEnd('green')
def gameEnd(winner):
	#ends the game
	humanBike.make_trail = False
	humanBike.visible = False

	bike2.make_trail = False
	bike2.visible = False

	if winner == 'green':
			gameOverText = text(text = 'GREEN WINS!', align = 'center', \
			depth = -500, color = color.green, height = 100, width = 100, \
			font = 'Bauhaus 93')

	elif winner == 'purple':
			gameOverText = text(text = 'PURPLE WINS!', align = 'center', \
			depth = -500, color = color.magenta, height = 100, width = 100, \
			font = 'Bauhaus 93')


#RUNS GAME
while end == False:
	rate(100)

	#MOVEMENT CONTROL
	if scene.kb.keys:
		k = scene.kb.getkey()

		#LINES 114-122: BIKE 1 CONTROL
		if k == 'up' and humanBike.v.y != -200:
			humanBike.v = vector(0,200,0)
		elif k == 'down' and humanBike.v.y != 200:
			humanBike.v = vector(0,-200,0)
		elif k == 'left' and humanBike.v.x != 200:
			humanBike.v = vector(-200,0,0)
		elif k == 'right' and humanBike.v.x != -200:
			humanBike.v = vector(200,0,0)

		#LINES 125-132: BIKE 2 CONTROL
		elif k == 'w' and bike2.v.y != -200:
			bike2.v = vector(0,200,0)
		elif k == 's' and bike2.v.y != 200:
			bike2.v = vector(0,-200,0)
		elif k == 'a' and bike2.v.x != 200:
			bike2.v = vector(-200,0,0)
		elif k == 'd' and bike2.v.x != -200:
			bike2.v = vector(200,0,0)

		#TITLE CONTROL
		elif k == ' ' :
			title.visible = False
			directions.visible = False

		#cheats
		elif k == 'g':
			gameEnd('green')
		elif k == 'p':
			gameEnd('purple')
	humanBike.pos = humanBike.pos + (humanBike.v*deltat)
	bike2.pos = bike2.pos + (bike2.v*deltat)


	collisionCheck()
	time += deltat
else:
	gameEnd()
	humanBike.trail_object.visible = False
	if scene.kb.keys:
		k = scene.kb.getkey()
		if k == ' ':
			#deletes trail
			#humanBike.trail_object.visible = False
			del humanBike.trail_object
			humanBike.pos.x = 150
			humanBike.pos.y = 0
			humanBike.make_trail = True
			print 'space'
