"""
Conway's Game of life with pygame
Pablo Villanueva Domingo
December 2017
"""

import pygame, random

# Some initial specifications
pygame.init()
width, height = 600, 600
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Game of life")

blue=(0,0,255)
green=(0,255,0)
ncells=40
wsq=width/ncells

reloj = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font(None, 40)

# 31x31 elements
cell = [[0 for x in range(ncells+1)] for y in range(ncells+1)]
newcell = [[0 for x in range(ncells+1)] for y in range(ncells+1)]

# Shapes
def blinker(x):
    cell[x+1][x]=1
    cell[x][x]=1
    cell[x-1][x]=1

def block(x,y):
    cell[x][y]=1
    cell[x][y+1]=1
    cell[x+1][y]=1
    cell[x+1][y+1]=1

def toad(x,y):
    cell[x][y]=1
    cell[x+1][y]=1
    cell[x+1][y+1]=1
    cell[x+2][y+1]=1
    cell[x+2][y]=1
    cell[x+3][y+1]=1

def boat(x,y):
    cell[x][y]=1
    cell[x+1][y]=1
    cell[x][y+1]=1
    cell[x+2][y+1]=1
    cell[x+1][y+2]=1

def glider(x,y):
    cell[x][y-1]=1
    cell[x+1][y]=1
    cell[x+1][y+1]=1
    cell[x][y+1]=1
    cell[x-1][y+1]=1

# Initial conditions, set some shapes (comment if not wanted)
blinker(15)
block(5,5)
toad(15,5)
boat(1,17)
glider(2,10)
glider(9,8)

# Random initial conditions (comment if random initial conditions are not wanted)
cell = [[random.randint(0,1) for x in range(ncells+1)] for y in range(ncells+1)]

# Start the loop
iter=0
while 1:

    reloj.tick(5)

    screen.fill(blue)

    # Draw the cells
    for x in range(ncells+1):
        for y in range(ncells+1):

            if cell[x][y] == 1:
                pygame.draw.rect(screen,green,((x-0.5)*wsq, (y-0.5)*wsq, wsq, wsq))
            else:
                pygame.draw.rect(screen,blue,((x-0.5)*wsq, (y-0.5)*wsq, wsq, wsq))

    screen.blit(font.render("Time: "+str(iter),True, (255,0,0)),(width-9*wsq,width-2*wsq))

    # Boundary conditions
    for x in range(0,ncells+1):
        newcell[x][0]=0
        newcell[x][ncells]=newcell[x][0]
    for y in range(0,ncells+1):
        newcell[0][y]=0
        newcell[ncells][y]=newcell[0][y]

    for x in range(1,ncells):
        for y in range(1,ncells):

            # Calculate number of alive neighbors
            neigh = cell[x-1][y-1] + cell[x-1][y] + cell[x][y-1] + cell[x+1][y] + cell[x][y+1] + cell[x+1][y+1] + cell[x+1][y-1] + cell[x-1][y+1]

            # Set the state of each cell
            if cell[x][y]==1:
                
                if (neigh==2) or (neigh==3):
                    newcell[x][y]=1
                else:
                    newcell[x][y]=0

            if cell[x][y]==0:
                if neigh==3:
                    newcell[x][y]=1
                else:
                    newcell[x][y]=0

    for x in range(0,ncells+1):
        for y in range(0,ncells+1):
            cell[x][y] = newcell[x][y]

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)

    pygame.display.flip()

    iter+=1
