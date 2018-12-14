import pygame, Server, Client

STOPALL = False

pygame.init()
screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)
pygame.display.set_caption("AbsoluutseltMitteAgar.io")

def pygame_event():
	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        STOPALL = True

	    #Resizable window
	    if event.type == pygame.VIDEORESIZE:
	        screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

while not STOPALL:
	pygame_event()

pygame.quit()