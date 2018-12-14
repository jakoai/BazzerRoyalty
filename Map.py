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
                x = random.randint(0,10)
                wall=0
                empty=0

                if x <= 30:
                    for cx in range(random.randint(1,2)):
                        if nx + cx < self.mapx:
                            for cy in range(random.randint(1,2)):
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
                #Lauri sitt
                if x <=1:
                    self.map[ny][nx] = 1

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
                    """
                    home = 0
                    while home == 0:
                        newhomex = random.randint(0, self.mapx - 1)
                        newhomey = random.randint(0, self.mapy - 1)
                        if self.map[newhomex][newhomey] == 0:
                            self.map[newhomex][newhomey] = 1
                            home = 1
                            """


                elif self.map[ny][nx] == 0 and wall > empty:
                    self.map[ny][nx] = 1

                x = random.randint(0,3000)
                if x <=5:
                    self.map[ny][nx] = 2
            print(item)

    def draw(self, screen, tile, charx, chary):
        for ny,item in enumerate(self.map):
            for nx,i in enumerate(item):
                if i == 1:
                    pygame.draw.rect(screen, (0,255,255), (nx*tile-charx,ny*tile-chary , tile, tile))
                if i == 2:
                    pygame.draw.rect(screen, (0,0,255), (nx*tile-charx,ny*tile-chary , tile, tile))


