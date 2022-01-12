import pygame as pg
from pygame.locals import *
import methods as mt

class IO_Money:
	def __init__(self, posX, posY, width=150, height=30):
		self.x = posX
		self.y = posY
		self.w = width
		self.h = height
		self.rect = pg.Rect(self.x, self.y, self.w, self.h)

	def text(self, txt):
		self.text = txt

	def money(self, cash):
		self.money = cash

IO_Columns = []

class IO_Column:
	def __init__(self, posX=5, posY=5):
		global IO_Columns
		self.x = posX
		self.y = posY
		self.rect = pg.Rect(self.x, self.y, 150, 490)

	def calculate(self):
		pass

	def IO_add(self):
		pass

	def save(self):
		pass

	def load(self):
		pass

	def destroy(self):
		IO_Columns.remove(self)
		del(self)

	def draw(self, canvas):
		pg.draw.rect(canvas, (150, 150, 150), self)

new_colum_bt = pg.Rect(10, 10, 10, 10)
del_colum_bt = pg.Rect(10, 30, 10, 10)

def draw(appState, canvas):
	if appState == "main":
		pg.draw.rect(canvas, (255, 255, 255), new_colum_bt)
		pg.draw.rect(canvas, (255, 255, 255), del_colum_bt)
		for obj in IO_Columns:
			#obj.draw(canvas)
			pg.draw.rect(canvas, (255, 255, 255), obj.rect)

def tick(appState):
	if appState == "main":
		if mt.coll_mouse_rect((1,0,0), new_colum_bt):
			new = IO_Column(50 * len(IO_Columns) + 10, 5)
			IO_Columns.append(new)
			for i in range(1000):
				i += 1

		if mt.coll_mouse_rect((0,1,0), new_colum_bt):
			IO_Columns[0].destroy



	
