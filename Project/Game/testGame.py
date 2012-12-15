import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window 
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

# set up the colors 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE)
self.drawBar(BLUE,60,120,60)

def drawBar(color,left,right,y): 
	pygame.draw.line(DISPLAYSURF, color, (left, y), (right, y), 4)
	pygame.draw.line(DISPLAYSURF, color, (left, y-5), (left, y+5), 4)
	pygame.draw.line(DISPLAYSURF, color, (right, y-5), (right, y+5), 4)

while True: # main game loop
    for event in pygame.event.get():
    	if event.type == QUIT:
    		pygame.quit()
    		sys.exit()
    pygame.display.update()