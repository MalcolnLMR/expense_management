# Expense Management using Python PyGame

import math, time
import pygame as pg
from pygame.locals import *

import methods as mt
import ui

appLoop = True
appState = "main"

Canvas = mt.initPygame()

while appLoop:
	Canvas.fill((150, 150, 150))	

	if appState == "main":
		

	for event in pg.event.get():
		if event.type == QUIT:
			appLoop = False
	pass

