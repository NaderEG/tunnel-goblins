from random import choice

class Cell:
	def __init__(self, x, y):
		self.x, self.y = x, y
		self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
		self.visited = False # used during maze generation
		self.explored = False # used when a goblin is exploring the maze

class Mole:
	def __init__(self, cols, rows):
		self.grid = [Cell(col, row) for row in range(rows) for col in range(cols)]
		self.currentCell = self.grid[0]
		self.stack = []
		self.cols, self.rows = cols, rows
		self.digging = True

	def dig(self):
		self.currentCell.visited = True

		nextCell = self.randomNeighbor(self.currentCell.x, self.currentCell.y)
		if nextCell:
			nextCell.visited = True
			self.stack.append(self.currentCell)
			self.removeWalls(self.currentCell.x, self.currentCell.y, nextCell.x, nextCell.y)
			self.currentCell = nextCell
		elif self.stack:
			self.currentCell = self.stack.pop()
		else:
			self.digging = False

	def canMove(self, x, y):
		'''returns a Cell if that Cell is within the bounds of the grid'''
		if x < 0 or x > self.cols - 1 or y < 0 or y > self.rows -1:
			return False
		return self.grid[x + y*self.cols]

	def randomNeighbor(self, x, y):
		'''returns a random unvisited Cell neighboring the Cell at coords x and y, or false if no such neighbor exists'''
		moves = []
		up = self.canMove(x, y - 1)
		right = self.canMove(x + 1, y)
		down = self.canMove(x, y + 1)
		left = self.canMove(x - 1, y)

		if up and not up.visited:
			moves.append(up)
		if right and not right.visited:
			moves.append(right)
		if down and not down.visited:
			moves.append(down)
		if left and not left.visited:
			moves.append(left)
		return choice(moves) if moves else False

	def removeWalls(self, cx, cy, nx, ny):
		'''removes the walls between the cell at cx, cy and the cell at nx, ny'''
		dx = cx-nx
		if dx == 1:
			self.grid[cx + cy*self.cols].walls['left'] = False
			self.grid[nx + ny*self.cols].walls['right'] = False
		elif dx == -1:
			self.grid[cx + cy*self.cols].walls['right'] = False
			self.grid[nx + ny*self.cols].walls['left'] = False
		dy = cy-ny
		if dy == 1:
			self.grid[cx + cy*self.cols].walls['top'] = False
			self.grid[nx + ny*self.cols].walls['bottom'] = False
		elif dy == -1:
			self.grid[cx + cy*self.cols].walls['bottom'] = False
			self.grid[nx + ny*self.cols].walls['top'] = False

