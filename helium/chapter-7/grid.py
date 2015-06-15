
import numpy as np
from element import *

class Grid:
	def __init__(self, grid_size):
		self.grid = [
			[Element(x,y) for x in range(grid_size)] for y in range(grid_size)]

	def set_element(self, location, typ):
		element = self.get_element(location)
		if element is None:
			return
		if typ == 'wumpus':
			element.set_wumpus(self)
		elif typ == 'pit':
			element.set_pit(self)
		elif typ == 'gold':
			element.set_gold(self)
	
	def set_wumpus(self, location):
		self.set_element(location, 'wumpus')

	def set_pit(self, location):
		self.set_element(location, 'pit')

	def set_gold(self, location):
		self.set_element(location, 'gold')
	
	def get_element(self, location):
		if self.is_inside(location):
			return self.grid[location[1]][location[0]]
		else:
			return None
	
	def is_inside(self, location):
		n = len(self.grid)
		return location[0] >= 0 and \
			location[0] < n and \
			location[1] >= 0 and \
			location[1] < n

	def print_grid(self):
		n = len(self.grid)
		block_size = 4+1
		print('_'*(n*block_size+1))
		for row in range(n-1,-1,-1):
			print('|', end="")
			for col in range(n):
				self.grid[row][col].print_element(block_size-1)
				
			print('')
			print('-'*(n*block_size+1))

