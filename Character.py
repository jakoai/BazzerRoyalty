import pygame


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
        pygame.draw.rect(screen, (255, 0, 0), (int(screen.get_width()/2-self.size/2), int(screen.get_height()/2-self.size/2), self.size, self.size))

    def draw_others(self, screen, others):
        for i in others.keys():
            pygame.draw.rect(screen, (0, 255, 0), (int(others[i][0]+screen.get_width()/2-self.x-self.size/2), int(others[i][1]+screen.get_height()/2-self.y-self.size/2), self.size, self.size))
