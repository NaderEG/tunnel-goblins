import Tile

class Maze:
	def generateMaze(width, height):
		grid = [[Tile() for _ in range(width)] for _ in range(height)]
		for i in range(width):
			grid[i][0].setType("WALL")
			grid[i][-1].setType("WALL")
			grid[1][0].setType("START")
			grid[-2][-1].setType("END")



	def printMap(grid):
		'''Prints a maze generated using the generateMaze function.
		Used for testing purposes only.'''
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == "PATH":
					print("□",  end='')
				elif grid[i][j] == "WALL":
					print("■",  end='')
				elif grid[i][j] == "START":
					print("X",  end='')
				else:
					print("O",  end='')
			print("")