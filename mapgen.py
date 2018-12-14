#Laur Edvard tegi
import pygame
import random
from pygame.locals import *
import time

Y = 100 
X = 100
WHITEFREQ = 0.6
BLACKFREQ = 0.8
BLACKLIM = 1
WHITELIM = 2
screenx = 500 
screeny = 500
cellx = screenx/X
celly = screeny/Y
screen = pygame.display.set_mode((screenx, screeny+50))
pygame.display.set_caption("Surprise me")
# Array tähendab kaarti(just in case)
    
def init(X,Y,WHITEFREQ, BLACKFREQ):

    array = []
    for x in range (X):
        temparray = []
        for y in range(Y):
            randchance = random.random()
            if randchance < WHITEFREQ:
                temparray.append(1)
            elif randchance > BLACKFREQ:
                temparray.append(2)
            else:
                temparray.append(0)
        array.append(temparray)
    return array

array = init(X, Y, WHITEFREQ, BLACKFREQ)

def pause():

    while True:
        time.sleep(0.1)
        for event in pygame.event.get():
            press = pygame.key.get_pressed()
            if press[K_ESCAPE]:
                pygame.quit()
                exit()
            elif press[K_v]:
                return

def mapgen(array, BLACKLIM, WHITELIM):

    while True:
        for event in pygame.event.get():
            press = pygame.key.get_pressed()
            if press[K_ESCAPE]:
                pygame.quit()
                exit()
            elif press[K_v]:
                pause()
            elif press[K_RETURN]:
                return array
        for i in range(X):
            for j in range(Y):
                whiteneigh = 0
                blackneigh = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        try:
                            if array[i+k][j+l] == 1 and array[i][j] == 2:
                                whiteneigh += 1
                            elif array[i+k][j+l] == 2 and array[i][j] == 1:
                                blackneigh += 1
                        except:
                            pass

                if array[i][j] == 1 and blackneigh > WHITELIM:
                    array[i][j] = 0
                    home = 0
                    while home == 0:
                        newhomex = random.randint(0, X-1)
                        newhomey = random.randint(0, Y-1)
                        if array[newhomex][newhomey] == 0:
                            array[newhomex][newhomey] = 1
                            home = 1
                if array[i][j] == 2 and whiteneigh > BLACKLIM:
                    array[i][j] = 0
                    home = 0
                    while home == 0:
                        newhomex = random.randint(0, X-1)
                        newhomey = random.randint(0, Y-1)
                        if array[newhomex][newhomey] == 0:
                            array[newhomex][newhomey] = 2
                            home = 2
                if array[i][j] == 2:
                    pygame.draw.rect(screen, (0, 0, 255), (cellx * i, celly * j, cellx, celly))
                elif array[i][j] == 1:
                    pygame.draw.rect(screen, (0, 255, 0), (cellx * i, celly * j, cellx, celly))
                elif array[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 0), (cellx * i, celly * j, cellx, celly))
        pygame.display.flip()

def createciv(array):

    a = 0
    civcolors = []

    while True:

        for event in pygame.event.get():
            press = pygame.key.get_pressed()
            if press[K_ESCAPE]:
                pygame.quit()
                exit()
            elif press[K_RETURN]:
                return array, civcolors

            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                x = int(pos[0] / (screenx/len(array)))
                y = int(pos[1] / (screeny/len(array[0])))

                try:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if array[x+i][y+j] == 0 or array[x+i][y+j] == 1:
                                array[x+i][y+j] = 3+a
                except:
                    pass

                civcolors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                a += 1

        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 0), (cellx * i, celly * j, cellx, celly))
                elif array[i][j] == 1:
                    pygame.draw.rect(screen, (0, 255, 0), (cellx * i, celly * j, cellx, celly))
                elif array[i][j] == 2:
                    pygame.draw.rect(screen, (0, 0, 255), (cellx * i, celly * j, cellx, celly))
                elif array[i][j] > 2:
                    pygame.draw.rect(screen, civcolors[array[i][j]-3], (cellx * i, celly * j, cellx, celly))

        pygame.display.flip()
  
def game(array, oldmap, civcolors):

    pygame.font.init()
    friendlim = 4
    enemylim = 2
    lowfriendlim = 2
    currentyear = 0
    font = pygame.font.SysFont("Comic Sans MS", 25)
    white = (255, 255, 255)

    while True:

        yearblit = font.render("Current year: %s" % currentyear, 1, white)
        screen.fill((0,0,0))

        screen.blit(yearblit, (40, screeny + 5, 400, 100))

        for event in pygame.event.get():
            press = pygame.key.get_pressed()
            if press[K_ESCAPE]:
                pygame.quit()
                exit()

        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] not in (0,1,2): 
                    friendlies = 0
                    badlings = 0

                    for k in range(-1, 2):
                        for o in range(-1, 2): 
                            try:
                                if o != 0 and k != 0:
                                    if array[i+k][j+o] == array[i][j]:
                                        friendlies += 1
                                    elif array[i+k][j+o] > 2:
                                        badlings += 1
                            except:
                                pass


                    if friendlies < lowfriendlim or friendlies > friendlim or badlings > enemylim:
                        array[i][j] = oldmap[i][j]
                    else:
                        randspawnx = random.randint(-1, 1)
                        randspawny = random.randint(-1, 1)
                        while randspawnx == 0 and randspawny == 0:
                            randspawnx = random.randint(-1, 1)
                            randspawny = random.randint(-1, 1)
                        try:
                            if array[i+randspawnx][j+randspawny] != 2:
                                array[i+randspawnx][j+randspawny] = array[i][j]
                        except:
                            pass

        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 0), (cellx * i, celly * j, cellx, celly))
                elif array[i][j] == 1:
                    pygame.draw.rect(screen, (0, 255, 0), (cellx * i, celly * j, cellx, celly))
                elif array[i][j] == 2:
                    pygame.draw.rect(screen, (0, 0, 255), (cellx * i, celly * j, cellx, celly))
                elif array[i][j] > 2:
                    pygame.draw.rect(screen, civcolors[array[i][j]-3], (cellx * i, celly * j, cellx, celly))
        currentyear += 0.25
        pygame.display.flip()


array = mapgen(array,BLACKLIM,WHITELIM)
oldmap = array[:]
array, civcolors = createciv(array)
game(array, oldmap, civcolors)