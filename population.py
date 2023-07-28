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
		self.explorer = 0
		self.success = False
		self.finished = False

		self.backTracking = 0
		self.posRecord = [(self.x, self.y)]
		self.collisions = 0
		self.distance = float('inf')
		self.fitness = 0

	def reproduce(self, other):
		splitPoint = random.randint(0, len(self.dna)-1)
		newDna = self.dna[0:splitPoint] + other.dna[splitPoint:]
		i = 0
		for d in newDna:
			probability = random.random()
			if probability < 0.01:
				dirs = ["up", "down", "left", "right"]
				dirs.remove(d)
				newDna[i] = random.choice(dirs)
			i+=1
		return Goblin(len(newDna), newDna)

	def step(self, m):
		
		if not self.finished and self.canMove(m, self.dna[self.stepsTaken]) :
			self.y = self.y-1 if self.dna[self.stepsTaken] == "up" else self.y
			self.y = self.y+1 if self.dna[self.stepsTaken] == "down" else self.y
			self.x = self.x-1 if self.dna[self.stepsTaken] == "left" else self.x
			self.x = self.x+1 if self.dna[self.stepsTaken] == "right" else self.x
			if not m.grid[self.x + self.y*m.cols].explored:
				self.explorer+=1
				m.grid[self.x + self.y*m.cols].explored = True

		else:
			self.collisions+=1 #penalized for colliding with walls
		if (self.x, self.y) in self.posRecord:
			self.backTracking+=1 #penalized for backtracking
		self.stepsTaken+=1
		self.posRecord.append((self.x, self.y))
		self.isSuccess(m)
		self.isFinished(m)
		


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
			self.success = True

	def isFinished(self, m):
		if self.stepsTaken == len(self.dna):
			self.distance = self.getDistance(m) #penalized for being far from the goal
			self.finished = True
			self.calculateFitness()

	def calculateFitness(self):
		collisionWeight = 3
		backtrackWeight = 3
		distanceWeight = 1
		explorerWeight = 2

		self.fitness = (explorerWeight*self.explorer - collisionWeight*self.collisions - backtrackWeight*self.backTracking - distanceWeight*self.distance)



class Population:
	def __init__(self, populationSize, dnaSize):
		self.genNumber = 1
		self.generation = [Goblin(dnaSize) for _ in range(populationSize)]

	def isGenerationDone(self):
		return all(goblin.finished for goblin in self.generation)

	def isGenerationSuccessful(self):
		return any(goblin.success for goblin in self.generation)

	def getSuccessfulGoblin(self):
		return next((goblin for goblin in self.generation if goblin.success), None)

	def nextGeneration(self):
		self.genNumber+=1
		self.generation.sort(key=lambda goblin: goblin.fitness, reverse=True)
		splitIndex = len(self.generation) // 2
		self.generation = self.generation[:splitIndex]
		for g in self.generation:
			g.x = g.y = 0
			g.stepsTaken = 0
			g.success = False
			g.finished = False
			g.explorer = 0
			g.backTracking = 0
			g.posRecord = []
			g.collisions = 0
			g.distance = float('inf')
			g.fitness = 0
			children = []
		for i in range(len(self.generation)):
			children.append(random.choice(self.generation[:len(self.generation)//5]).reproduce(random.choice(self.generation)))
		self.generation.extend(children)

	def generationalStep(self, m):
		for goblin in self.generation:
			goblin.step(m)
		if self.isGenerationDone():
			self.nextGeneration()

