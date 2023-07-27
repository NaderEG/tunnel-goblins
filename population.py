import random

class Goblin:
	def __init__(self, dnaSize, dna=[]):
		if dna:
			self.dna = dna
		else:
			options = ["right", "left", "up", "down"]
			self.dna = random.choices(options, k=dnaSize)
		self.fitness = 0
		self.x = self.y = 0

	def reproduce(self, other):
		splitPoint = random.randint(0, len(self.dna)-1)
		newDna = self.dna[0:splitPoint] + other.dna[splitPoint:]
		print(newDna)
		i = 0
		for d in newDna:
			probability = random.random()
			if probability < 0.1:
				print("random mutation at", i)
				newDna[i] = random.choice(["up", "down", "left", "right"].remove(d))
			i+=1
		print(newDna)
		return Goblin(len(newDna), newDna)

	def step(self, m):


	def canMove(self, m, d):
		if d == "up" and self.y - 1 >= 0:
			return not m.grid[self.x + self.y*m.cols.walls["top"]]
		elif d == "down" and self.y + 1 < rows:
			return not m.grid[self.x + self.y*m.cols.walls["bottom"]]
		elif d == "left" and self.y - 1 >=0:
			return not m.grid[self.x + self.y*m.cols.walls["left"]]
		elif d == "right" and self.y + 1 < cols:
			return not m.grid[self.x + self.y*m.cols.walls["right"]]

	def getDistance(self, m):
		return ((m.cols-1 - self.x)**2 + (m.rows-1 - self.y)**2)**0.5 


mom = Goblin(10)
dad = Goblin(10)
child = mom.reproduce(dad)
print(child.dna)