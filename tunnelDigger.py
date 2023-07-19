import random

class Cell:
	def __init__(self, x, y):
		self.x, self.y = x, y
		self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
		self.visited = False
		self.explored = False

class Maze:
	def __init__(self, cols, rows):
		self.cols, self.rows = cols, rows
		self.grid = [Cell(col, row) for row in range(rows) for col in range(cols)]

	def digTunnel(rows, cols):
		currentCell = self.grid[0]
		stack = []

		currentCell.visited = True

	def canMove(x, y):
		if x < 0 or x > cols - 1 or y < 0 or y > rows -1:
			return False
		return self.grid[x + y*cols]

	def randomMove(x, y):
		moves = []
		up = canMove(x, y - 1)
		right = canMove(x + 1, y)
		down = canMove(x, y + 1)
		left = canMove(x - 1, y)

		if up and not up.visited:
			moves.append(up)
		elif right and not right.visited:
			moves.append(right)
		elif down and not down.visited:
			moves.append(down)
		elif left and not left.visited:
			moves.append(left)
		return random.choice(moves) if moves else False

	def removeWalls(cx, cy, nx, ny):
		dx = cx-nx
		if dx == 1:
			grid[cx + cy*cols].walls['left'] = False
			grid[nx + ny*cols].walls['right'] = False
		elif dx == -1:
			grid[cx + cy*cols].walls['right'] = False
			grid[nx + ny*cols].walls['left'] = False
		dy = cy-ny
		if dy == 1:
			grid[cx + cy*cols].walls['top'] = False
			grid[nx + ny*cols].walls['bottom'] = False
		elif dy == -1:
			grid[cx + cy*cols].walls['bottom'] = False
			grid[nx + ny*cols].walls['top'] = False

