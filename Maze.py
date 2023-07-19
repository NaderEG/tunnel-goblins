import random

class Tile:
	def __init__(self):
		self.explored = False
		self.type = "PATH"

	def setType(self, value):
		self.type = value

	def getType(self):
		return self.type

	def explore(self):
		self.explored = True

	def isExplored(self):
		return self.explored


def generateMaze(width, height):
	'''Start with the outer wall, and add a wall segment touching it at random. 
	Keep on adding wall segments to the Maze at random, but ensure that each 
	new segment touches an existing wall at one end, and has its other end 
	in an unmade portion of the Maze. If you ever added a wall segment where 
	both ends were separate from the rest of the Maze, that would create  
	a detached wall with a loop around it, and if you ever added a segment 
	such that both ends touch the Maze, that would create an inaccessible area.'''

	grid = [[Tile() for _ in range(height)] for _ in range(width)]
	print(len(grid), len(grid[0]))

	for i in range(width):
		grid[i][0].setType("WALL")
		grid[i][-1].setType("WALL")

	for i in range(height):
		grid[0][i].setType("WALL")
		grid[-1][i].setType("WALL")


	while True:
		cell = randomWall(grid)
		x, y = cell
		ranDir = random.choice(["RIGHT", "LEFT", "UP", "DOWN"])
		if ranDir == "RIGHT":
			segLength = width
			for i in range(segLength):
				if canMove(grid, cell, ranDir):
					x+=1
					grid[x][y].setType("WALL")
				else:
					break

				
		elif ranDir == "LEFT":
			segLength = width
			for i in range(segLength):
				if canMove(grid, cell, ranDir):
					x-=1
					grid[x][y].setType("WALL")
				else:
					break
				
		elif ranDir == "UP": 
			segLength = height
			for i in range(segLength):
				if canMove(grid, cell, ranDir):
					y-=1
					grid[x][y].setType("WALL")
				else:
					break
				 
		elif ranDir == "DOWN":
			segLength = height
			for i in range(segLength):
				if canMove(grid, cell, ranDir):
					y+=1
					grid[x][y].setType("WALL")
				else:
					break
			

		printMaze(grid)
	grid[0][1].setType("START")
	grid[-1][-2].setType("END")


	
def canMove(grid, cell, d):
	x, y = cell
	if d == "RIGHT" and x + 2 < len(grid):
		for dx in [1, 2]:
			for dy in [-1, 0, 1]:
				if grid[x+dx][y+dy].getType() != "PATH":
					return False
		return True

	elif d == "LEFT" and x - 2 >= 0:
		for dx in [-1, -2]:
			for dy in [-1, 0, 1]:
				if grid[x+dx][y+dy].getType() != "PATH":
					return False
		return True
	elif d == "UP" and y - 2 >= 0:
		for dy in [-1, -2]:
			for dx in [-1, 0, 1]:
				if grid[x+dx][y+dy].getType() != "PATH":
					return False
		return True
	elif d == "DOWN" and y + 2 < len(grid[0]):
		for dy in [1, 2]:
			for dx in [-1, 0, 1]:
				if grid[x+dx][y+dy].getType() != "PATH":
					return False
		return True


def randomWall(matrix):
	cells = []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j].getType() == "WALL":
				cells.append((i, j))

	if not cells:
		return None  # Return None if no cell with value 0 is found

	randomCell = random.choice(cells)
	return randomCell

def printMaze(grid):
	'''Prints a maze generated using the generateMaze function.
	Used for testing purposes only.'''
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j].getType() == "PATH":
				print("□",  end='')
			elif grid[i][j].getType() == "WALL":
				print("■",  end='')
			elif grid[i][j].getType() == "START":
				print("X",  end='')
			else:
				print("O",  end='')
		print("")

printMaze(generateMaze(100, 100))