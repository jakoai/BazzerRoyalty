import math
import pygame

class shoot():
    def __init__(self, plrx, plry):
        self.BulletImgRaw = pygame.Surface((30, 20), pygame.SRCALPHA)
        pygame.draw.polygon(self.BulletImgRaw, (190, 150, 90), ((0, 0), (30, 10), (0, 20)))
        self.bullets = []
        self.plrx = plrx
        self.plry = plry

    def out_of_bounds(self, position):
        x, y = position
        return x < -40 or x > 500 or y < -40 or y > 400


    def gen_bullets(self, screen):
        angle = 0
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                rise = mouse_position[1] - self.plrx
                run = mouse_position[0] - self.plry
                angle = math.atan2(rise, run)
                vel_x = math.cos(angle) * 3
                vel_y = math.sin(angle) * 3
                BulletImg = pygame.transform.rotate(self.BulletImgRaw, -math.degrees(angle))
                width, height = BulletImg.get_size()
                self.bullets.append([[self.plrx - width / 2, self.plry - height / 2], [vel_x, vel_y],BulletImg])
        filtered_bullets = []
        for bullet in self.bullets:
            if not shoot.out_of_bounds(self, bullet[0]):
                filtered_bullets.append(bullet)

        self.bullets = filtered_bullets
        print(self.bullets)
        for bullet in self.bullets:
            bullet[0][0] += bullet[1][0]
            bullet[0][1] += bullet[1][1]

        screen.fill((30, 40, 50))


        for bullet in self.bullets:
            screen.blit(bullet[2], bullet[0])
