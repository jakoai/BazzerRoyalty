import pygame, sys
screen = pygame.display.set_mode([1280,720])

def titlescreen(screen):
    screen.fill([255, 255, 255])
    pygame.display.flip()
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 50)
    sekritfont = pygame.font.SysFont('Comic Sans MS', 15)
    titletext = font.render('Bazzer Royalty', False, (0, 0, 0))
    sekrit = sekritfont.render('dab', False, (0, 0, 0))
    hosttext = font.render('Host', False, (0, 0, 0))
    clienttext = font.render('Client', False, (0, 0, 0))
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
        if mousepress == (1, 0, 0) and 250 > mousepos[0] > 50 and 200 > mousepos[1] > 100:
            pygame.draw.rect(screen, (0, 200, 0), (50, 100, 200, 100))
            screen.blit(clienttext, (82, 110))
        else:
            pygame.draw.rect(screen, (0, 255, 0), (50, 100, 200, 100))
            screen.blit(clienttext, (82, 110))
        if mousepress == (1, 0, 0) and 500 > mousepos[0] > 300 and 300 > mousepos[1] > 100:
            pygame.draw.rect(screen, (0, 200, 0), (300, 100, 200, 100))
            screen.blit(hosttext, (342, 110))
        else:
            pygame.draw.rect(screen, (0, 255, 0), (300, 100, 200, 100))
            screen.blit(hosttext, (342, 110))
        if mousepress == (1, 1, 1):
            screen.blit(sekrit, (770,580))
        pygame.display.flip()
titlescreen(screen)