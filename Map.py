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
                x = random.randint(0,1000)
                if x <= 20:
                    self.map[ny][nx] = 1

                    if x <= 10:
                        
                        for cx in range(5):
                            if nx+cx < self.mapx:
                                for cy in range(5):
                                    if ny+cy < self.mapy:
                                        z = random.randint(0, 4)
                                        if z <= 3:
                                            self.map[ny+cy][nx+cx] = 1

            print(item)
    def draw(self, screen, color, tile):
        pygame.draw.rect(screen, color, (0, 0, tile, tile))

m = map(30,20)
m.generatemap()
