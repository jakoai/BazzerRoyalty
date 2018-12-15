import pygame, pygame.gfxdraw


class player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def movement(self, d):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 250*d
        if keys[pygame.K_RIGHT]:
            self.x += 250*d
        if keys[pygame.K_DOWN]:
            self.y += 250*d
        if keys[pygame.K_LEFT]:
            self.x -= 250*d

    def draw(self, screen):
        pygame.gfxdraw.box(screen, (int(screen.get_width()/2-self.size/2), int(screen.get_height()/2-self.size/2), self.size, self.size), (255, 0, 0))

    def draw_others(self, screen, others):
        for i in others.keys():
            pygame.gfxdraw.box(screen, (int(others[i][0]+screen.get_width()/2-self.x-self.size/2), int(others[i][1]+screen.get_height()/2-self.y-self.size/2), self.size, self.size), (0, 255, 0))
