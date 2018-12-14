import pygame


class player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -=1
        if keys[pygame.K_RIGHT]:
            self.x +=1
        if keys[pygame.K_DOWN]:
            self.y += 1
        if keys[pygame.K_LEFT]:
            self.x -= 1

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 0, 0), (int(screen.get_width()/2-self.size/2), int(screen.get_height()/2-self.size/2), self.size, self.size))

    def draw_others(self, screen, others):
        print(others)
        for i in others.keys():
            pygame.draw.rect(screen, (100, 100, 200), (int(others[i][0]-self.x-self.size/2), int(others[i][1]-self.y-self.size/2), self.size, self.size))
