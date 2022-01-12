class IO_Money:
	def __init__(self, posX, posY, width=150, height=30):
		self.x = posX
		self.y = posY
		self.w = width
		self.h = height
		self.rect = (self.x, self.y, self.w, self.h)

	def text(self, txt):
		self.text = txt

	def money(self, cash):
		self.money = cash


class IO_Column:
	def __init__(self, posX=5, posY=5):
		self.x = posX
		self.y = posY
		self.rect = (self.x, self.y, 150, 490)

	def calculate(self):
		pass

	def IO_add(self):
		pass

	def save(self):
		pass

	def load(self):
		pass
		