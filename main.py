import pygame
import mole
import population

RES = WIDTH, HEIGHT = 1202, 902
TILE = 100

cols, rows = WIDTH // TILE, HEIGHT // TILE

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

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

def drawGeneration(gen):
	for g in gen:
		x, y = g.x*TILE, g.y*TILE
		pygame.draw.rect(sc, pygame.Color('darkgreen'), (x+2, y+2, TILE-2, TILE-2))

def drawGenNumber(g):
	text = "Generation: " + str(g.genNumber)
	text_surface = font.render(text, True, pygame.Color('white'))
	sc.blit(text_surface, (WIDTH - text_surface.get_width()-10,text_surface.get_height()))

mo = mole.Mole(cols, rows)
g = population.Population(50, 2*rows*cols)
successCoords = []
while True:
	sc.fill(pygame.Color('darkslategray')) 

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	if mo.digging:
		[drawCell(cell) for cell in mo.grid] 
		drawCurrentCell(mo.currentCell)
		mo.dig()
	elif not g.isGenerationSuccessful():
		[drawCell(cell) for cell in mo.grid]
		drawStartAndEnd()
		g.generationalStep(mo)
		drawGeneration(g.generation)
		drawGenNumber(g)
		
	else:
		[drawCell(cell) for cell in mo.grid]
		if not successCoords:
			winner = g.getSuccessfulGoblin()
			for point in winner.posRecord:
				successCoords.append((point[0]*TILE+TILE*0.5, point[1]*TILE+TILE*0.5))
		pygame.draw.lines(sc, pygame.Color('beige'), False, successCoords, 2)
		drawGenNumber(g)
		drawStartAndEnd()
	pygame.display.flip()
	clock.tick(30)

