import pygame, sys

def titlescreen(screen):
    screen.fill([255, 255, 255])
    pygame.display.flip()
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 50)
    sekritfont = pygame.font.SysFont('Comic Sans MS', 15)
    titletext = font.render('Bazzer Royalty', False, (0, 0, 0))
    sekrit = sekritfont.render('dab', False, (0, 0, 0))
    screen.blit(titletext, (0, 0))
    while True:
        mousepos = pygame.mouse.get_pos()
        mousepress = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if mousepress == (1, 0, 0):
            pygame.draw.rect(screen, [255, 0, 0], (100,100,50,50))
        elif mousepress == (0, 1, 0):
            pygame.draw.rect(screen, [0, 255, 0], (100, 100, 50, 50))
        elif mousepress == (0, 0, 1):
            pygame.draw.rect(screen, [0, 0, 255], (100, 100, 50, 50))
        if mousepress == (0, 0, 0):
            pygame.draw.rect(screen, [255, 255, 255], (100, 100, 50, 50))
        if mousepress == (1, 1, 1):
            screen.blit(sekrit, (770,580))

        pygame.display.flip()