# Expense Management using Python PyGame

import math, time
import pygame as pg
from pygame.locals import *

import methods as mt
import ui

appLoop = True
appState = "main"

######################## Init FPS ########################
clock = pg.time.Clock()
FPS = 0
fpsCounter = 0
actualFPS = 0
configFPS = 60
prevTime = time.time()
clock.tick(FPS)
now = time.time()
dt = now - prevTime
prevTime = now

Canvas = mt.initPygame()

while appLoop:
	Canvas.fill((150, 150, 150))

	clock.tick(configFPS)
	now = time.time()
	dt = now - prevTime
	prevTime = now	

	if appState == "main":
		ui.draw(appState, Canvas)
		pg.display.update()
		ui.tick(appState, dt)



	for event in pg.event.get():
		if event.type == QUIT:
			appLoop = False
		pass

