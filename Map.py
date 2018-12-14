import random, pygame, pygame.gfxdraw

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
                x = random.randint(0,1000)
                wall=0
                empty=0

                if x <= 500:
                    for cx in range(random.randint(1,2)):
                        if nx + cx < self.mapx:
                            for cy in range(random.randint(1,1)):
                                if ny + cy < self.mapy:
                                    z = random.randint(0, 6)
                                    if z <= 2:
                                        self.map[ny + cy][nx + cx] = 1
                x = random.randint(0,1000)
                if x <= 2:
                    for cx in range(random.randint(5,20)):
                        if nx+cx < self.mapx:
                            for cy in range(random.randint(5,20)):
                                if ny+cy < self.mapy:
                                    z = random.randint(0, 6)
                                    if z <= 3:
                                        self.map[ny+cy][nx+cx] = 1

                for counter in range(7):
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            try:
                                if self.map[ny + k][nx + l] == 0 and self.map[ny][nx] == 1:
                                    empty += 1
                                elif self.map[ny + k][nx + l] == 1 and self.map[ny][nx] == 0:
                                    wall += 1
                            except:
                                pass

                    if self.map[ny][nx] == 1 and empty > wall:
                        self.map[ny][nx] = 0

                    elif self.map[ny][nx] == 0 and wall > empty:
                        self.map[ny][nx] = 1

                x = random.randint(0,1000)
                if x <=5:
                    self.map[ny][nx] = 2

    def draw(self, screen, tile, charx, chary):
        for ny,item in enumerate(self.map):
            for nx,i in enumerate(item):
                if i == 1:
                    pygame.gfxdraw.box(screen, (nx*tile-charx,ny*tile-chary , tile, tile), (0,255,255))
                if i == 2:
                    pygame.gfxdraw.box(screen, (nx*tile-charx,ny*tile-chary , tile, tile), (0,0,255))


