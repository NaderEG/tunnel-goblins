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

	grid = [[Tile() for _ in range(width)] for _ in range(height)]

	for i in range(width):
		grid[i][0].setType("WALL")
		grid[i][-1].setType("WALL")

	for i in range(height):
		grid[0][i].setType("WALL")
		grid[-1][i].setType("WALL")
	grid[0][1].setType("START")
	grid[-1][-2].setType("END")

	dice = random.randint(0, 3)
	#use random four to get the index of a random cell on the exterior wall

	return grid


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

printMaze(generateMaze(10, 10))