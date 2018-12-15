import math
import pygame

class shoot():
    def __init__(self):
        self.BulletImgRaw = pygame.Surface((30, 20), pygame.SRCALPHA)
        pygame.draw.polygon(self.BulletImgRaw, (190, 150, 90), ((0, 0), (30, 10), (0, 20)))
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
            BulletImg = pygame.transform.rotate(self.BulletImgRaw, -math.degrees(angle))
            width, height = BulletImg.get_size()
            self.bullets.append([[-width / 4+screen.get_width()/2, -height / 4+screen.get_height()/2], [vel_x, vel_y],BulletImg])
        filtered_bullets = []
        for bullet in self.bullets:
            if not self.out_of_bounds(bullet[0]):
                filtered_bullets.append(bullet)

        self.bullets = filtered_bullets

        for bullet in self.bullets:
            bullet[0][0] += bullet[1][0]
            bullet[0][1] += bullet[1][1]

        for bullet in self.bullets:
            screen.blit(bullet[2], bullet[0])