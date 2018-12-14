from pygame import *


class player:
    def __init__(self):
        self.charx = 100
        self.chary = 100

    def movement(self,):
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[K_UP]:
                self.chary -=10
            if keys[K_RIGHT]:
                self.charx +=10
            if keys[K_DOWN]:
                self.chary += 10
            if keys[K_LEFT]:
                self.charx -= 10

    def playerdraw(self, screen):
        draw.rect(screen, (100, 0, 0), (self.charx, self.chary, 50, 50))
