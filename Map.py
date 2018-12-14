import random, pygame

class map():
    def __init__(self, mapx, mapy):
        self.map = []
        self.mapx = mapx
        self.mapy = mapy


        for i in range(mapy):
            map_ = []
            for j in range(mapx):
                map_.append(0)
            self.map.append(map_)

    def generatemap(self):
        for ny,item in enumerate(self.map):
            for nx,i in enumerate(item):
                x = random.randint(0,3000)

                if x <= 30:
                    for cx in range(random.randint(1,5)):
                        if nx + cx < self.mapx:
                            for cy in range(random.randint(1,5)):
                                if ny + cy < self.mapy:
                                    z = random.randint(0, 6)
                                    if z <= 2:
                                        self.map[ny + cy][nx + cx] = 1
                x = random.randint(0,3000)

                if x <= 3:
                    for cx in range(random.randint(5,8)):
                        if nx+cx < self.mapx:
                            for cy in range(random.randint(5,8)):
                                if ny+cy < self.mapy:
                                    z = random.randint(0, 6)
                                    if z <= 2:
                                        self.map[ny+cy][nx+cx] = 1
                x = random.randint(0,3000)
                if x <=5:
                    self.map[ny][nx] = 2




    def draw(self, screen, tile, charx, chary):
        for ny,item in enumerate(self.map):
            for nx,i in enumerate(item):
                if i == 1:
                    pygame.draw.rect(screen, (0,255,255), (nx*tile-charx,ny*tile-chary , tile, tile))
                if i == 2:
                    pygame.draw.rect(screen, (0,0,255), (nx*tile-charx,ny*tile-chary , tile, tile))
