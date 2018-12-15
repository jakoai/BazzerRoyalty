import math
import pygame

class shoot():
    def __init__(self):
        self.bullets = []

    def out_of_bounds(self, position):
        x, y = position
        return False


    def gen_bullets(self, screen, plrx, plry):
        angle = 0
        if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            rise = mouse_position[1] - screen.get_height()/2
            run = mouse_position[0] - screen.get_width()/2
            angle = math.atan2(rise, run)
            vel_x = math.cos(angle) * 3
            vel_y = math.sin(angle) * 3
            self.bullets.append([[screen.get_width()/2, screen.get_height()/2], [vel_x, vel_y]])
        filtered_bullets = []
        for bullet in self.bullets:
            if not self.out_of_bounds(bullet[0]):
                filtered_bullets.append(bullet)

        self.bullets = filtered_bullets

        for bullet in self.bullets:
            bullet[0][0] += bullet[1][0]
            bullet[0][1] += bullet[1][1]

        for bullet in self.bullets:
            pygame.draw.circle(screen, (0, 0, 0), (int(bullet[0][0]), int(bullet[0][1])), 4)