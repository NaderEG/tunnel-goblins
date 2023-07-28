import random
import mole

class Goblin:
	def __init__(self, dnaSize, dna=[]):
		if dna:
			self.dna = dna
		else:
			options = ["right", "left", "up", "down"]
			self.dna = random.choices(options, k=dnaSize)
		self.x = self.y = 0
		self.stepsTaken = 0
		self.success = False

		self.backTracking = 0
		self.posRecord = []
		self.collisions = 0
		self.distance = float('inf')
		self.fitness = 0

	def reproduce(self, other):
		splitPoint = random.randint(0, len(self.dna)-1)
		newDna = self.dna[0:splitPoint] + other.dna[splitPoint:]
		print(newDna)
		i = 0
		for d in newDna:
			probability = random.random()
			if probability < 0.1:
				dirs = ["up", "down", "left", "right"]
				dirs.remove(d)
				newDna[i] = random.choice(dirs)
			i+=1
		return Goblin(len(newDna), newDna)

	def step(self, m):
		self.posRecord.append((self.x, self.y))
		if self.canMove(m, self.dna[self.stepsTaken]):
			self.y = self.y-1 if self.dna[self.stepsTaken] == "up" else self.y
			self.y = self.y+1 if self.dna[self.stepsTaken] == "down" else self.y
			self.x = self.x-1 if self.dna[self.stepsTaken] == "left" else self.x
			self.x = self.x+1 if self.dna[self.stepsTaken] == "right" else self.x
		else:
			self.collisions+=1 #penalized for colliding with walls
		if (self.x, self.y) in self.posRecord:
			self.backTracking+=1 #penalized for backtracking
		self.stepsTaken+=1
		self.isSuccess()
		self.isFinished()
		


	def canMove(self, m, d):
		if d == "up" and self.y - 1 >= 0:
			return not m.grid[self.x + self.y*m.cols].walls["top"]
		elif d == "down" and self.y + 1 < m.rows:
			return not m.grid[self.x + self.y*m.cols].walls["bottom"]
		elif d == "left" and self.y - 1 >=0:
			return not m.grid[self.x + self.y*m.cols].walls["left"]
		elif d == "right" and self.y + 1 < m.cols:
			return not m.grid[self.x + self.y*m.cols].walls["right"]

	def getDistance(self, m):
		return ((m.cols-1 - self.x)**2 + (m.rows-1 - self.y)**2)**0.5

	def isSuccess(self, m):
		if self.x == m.cols-1 and self.y == m.rows-1:
			self.finished = True
			self.success = True
			self.distance = self.getDistance(m)

	def isFinished(self, m):
		if self.stepsTaken == len(self.dna):
			self.distance = self.getDistance(m) #penalized for being far from the goal
			self.finished = True
			self.fitness = self.backTracking + self.collisions + self.distance



class Population:
	def __init__(self, populationSize, dnaSize):
		self.genNumber = 1
		self.generation = [Goblin(dnaSize) for _ in range(populationSize)]

	def isGenerationDone(self):
		return all(goblin.finished for goblin in self.generation)

	def isGenerationSuccessful(self):
		return any(goblin.success for goblin in self.generation)

	def nextGeneration(self):
		self.genNumber+=1
		self.generation.sort(key=lambda goblin: goblin.fitness)
		splitIndex = len(self.generation) // 2
		self.generation = self.generation[:splitIndex]
		for i in range(len(self.generation)//2):
			self.generation.append(random.choice(self.generation).reproduce(random.choice(self.generation)))
