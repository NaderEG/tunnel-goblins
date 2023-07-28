import pygame
import mole
import population

RES = WIDTH, HEIGHT = 1202, 902
TILE = 100

cols, rows = WIDTH // TILE, HEIGHT // TILE

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

def drawStartAndEnd():
	pygame.draw.rect(sc, pygame.Color('green'), (2, 2, TILE-2, TILE-2))
	pygame.draw.rect(sc, pygame.Color('red'), ((cols-1)*TILE+2, (rows-1)*TILE+2, TILE-2, TILE-2))

def drawCurrentCell(cell):
	x, y = cell.x*TILE, cell.y*TILE
	pygame.draw.rect(sc, pygame.Color('saddlebrown'), (x+2, y+2, TILE-2, TILE-2))

def drawCell(cell):
	x, y = cell.x *TILE, cell.y*TILE
	if cell.visited:
		pygame.draw.rect(sc, pygame.Color('black'), (x, y, TILE, TILE))

	if cell.walls['top']:
		pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x+TILE, y), 2)
	if cell.walls['right']:
		pygame.draw.line(sc, pygame.Color('darkorange'), (x+TILE, y), (x+TILE, y+TILE), 2)
	if cell.walls['bottom']:
		pygame.draw.line(sc, pygame.Color('darkorange'), (x+TILE, y+TILE), (x, y+TILE), 2)
	if cell.walls['left']:
		pygame.draw.line(sc, pygame.Color('darkorange'), (x, y+TILE), (x, y), 2)

def drawGoblin(g):
	x, y = g.x*TILE, g.y*TILE
	pygame.draw.rect(sc, pygame.Color('darkgreen'), (x+2, y+2, TILE-2, TILE-2))

mo = mole.Mole(cols, rows)
g = population.Goblin(rows*cols)
while True:
	sc.fill(pygame.Color('darkslategray')) 

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	if mo.digging:
		[drawCell(cell) for cell in mo.grid]
		drawCurrentCell(mo.currentCell)
		mo.dig()
	elif g.stepsTaken < len(g.dna)-1:
		[drawCell(cell) for cell in mo.grid]
		drawStartAndEnd()
		g.step(mo)
		drawGoblin(g)
		print(g.dna[g.stepsTaken])
		
	else:
		[drawCell(cell) for cell in mo.grid]
		drawStartAndEnd()
		drawGoblin(g)
	pygame.display.flip()
	clock.tick(30)

