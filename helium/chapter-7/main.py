
from grid import *

grid = Grid(4)
grid.set_wumpus((0,2))
grid.set_pit((2,0))
grid.set_pit((2,2))
grid.set_pit((3,3))
grid.set_gold((1,2))
grid.print_grid()
