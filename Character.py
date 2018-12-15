import pygame, pygame.gfxdraw, random


class player:
    def __init__(self, size):
        self.x = 0
        self.y = 0
        self.size = size

        self.randpos()
    def get_movement(self, d):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            dy -= 250*d
        if keys[pygame.K_RIGHT]:
            dx += 250*d
        if keys[pygame.K_DOWN]:
            dy += 250*d
        if keys[pygame.K_LEFT]:
            dx -= 250*d
        return dx, dy

    def set_movement(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        pygame.gfxdraw.box(screen, (int(screen.get_width()/2-self.size/2), int(screen.get_height()/2-self.size/2), self.size, self.size), (255, 0, 0))

    def draw_others(self, screen, others):
        for i in others.keys():
            pygame.gfxdraw.box(screen, (int(others[i][0]+screen.get_width()/2-self.x-self.size/2), int(others[i][1]+screen.get_height()/2-self.y-self.size/2), self.size, self.size), (0, 255, 0))

    def randpos(self):
        self.x = random.randint(0, 2500)
        self.y = random.randint(0, 2500)