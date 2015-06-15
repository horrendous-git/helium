

class Element:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.stench = False
		self.wumpus = False
		self.pit = False
		self.breeze = False
		self.location = (x,y)

	def set_wumpus(self, grid):
		self.wumpus = True
		self.update_relatives(grid, lambda e: e.set_stench())

	def set_pit(self, grid):
		self.pit = True
		self.update_relatives(grid, lambda e: e.set_breeze())

	def update_relatives(self, grid, lam1):
		for rel in self.relatives():
			loc_rel = self.get_rel(rel)
			element = grid.get_element(loc_rel)
			if element is not None:
				lam1(element)

	def set_stench(self):
		self.stench = True

	def set_breeze(self):
		self.breeze = True


	def print_element(self, block_size):
		print('%*s|' % (block_size, self.fu()), end='')
		#print('|', end="")

	def fu(self):
		str =  ''
		str += 'w' if self.wumpus else ''
		str += 's' if self.stench else ''
		str += 'p' if self.pit else ''
		str += 'b' if self.breeze else ''
		return str

	def get_rel(self, loc_offset):
		return tuple([sum(x) for x in zip(self.location,loc_offset)])

	def relatives(self):
		return [(+1,0),\
				(0,+1),
				(-1,0),
				(0,-1)]
