import random, pygame, pygame.gfxdraw, Collision, math

class map():
    def __init__(self, mapx, mapy, size):
        self.map = []
        self.mapx = mapx
        self.mapy = mapy
        self.size = size

    def generatemap(self):
        for i in range(self.mapy):
            map_ = []
            for j in range(self.mapx):
                map_.append(0)
            self.map.append(map_)

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
    def generateitems(self):
        for ny,item in enumerate(self.map):
            for nx,i in enumerate(item):
                if self.map[ny][nx] != 1:
                    x = random.randint(0,1000)
                    if x ==2:
                        self.map[ny][nx] = 2
                    if x ==3:
                        self.map[ny][nx] = 3
                    if x ==4:
                        self.map[ny][nx] = 4

    def draw(self, screen, charx, chary):
        for ny,item in enumerate(self.map):
            for nx,i in enumerate(item):
                if i == 1:
                    pygame.gfxdraw.box(screen, (nx*self.size-charx+screen.get_width()/2,ny*self.size-chary+screen.get_height()/2, self.size, self.size), (0,255,255))
                elif i == 2:
                    pygame.gfxdraw.box(screen, (nx*self.size-charx+screen.get_width()/2,ny*self.size-chary+screen.get_height()/2, self.size, self.size), (200,0,255))
                elif i == 3:
                    pygame.gfxdraw.box(screen, (nx*self.size-charx+screen.get_width()/2,ny*self.size-chary+screen.get_height()/2, self.size, self.size), (0,120,120))
                elif i == 4:
                    pygame.gfxdraw.box(screen, (nx*self.size-charx+screen.get_width()/2,ny*self.size-chary+screen.get_height()/2, self.size, self.size), (100,100,255))

    def check_collision(self, screen, charx, chary, charsize):
        for ny, i in enumerate(self.map):
            for nx, j in enumerate(i):
                if j == 1 or j == 2 or j == 3 or j ==4:
                    collided = Collision.rect_collision(int((nx)*self.size-charx+screen.get_width()/2), int((ny)*self.size-chary+screen.get_height()/2), self.size, self.size, int(screen.get_width()/2-charsize/2), int(screen.get_height()/2-charsize/2), charsize, charsize, "pos")
                    if collided[0] != 0 and collided[1] != 0:
                        return (collided, [j, nx, ny])
        '''
        posx = int((charx+charsize/2)/self.size)
        posy = int((chary+charsize/2)/self.size)
        try:
            if self.map[posy][posx] == 1:
                return Collision.rect_collision(charx, chary, charsize, charsize, posx*self.size, posy*self.size, self.size, self.size, "pos")
        except IndexError:
            pass
        posx = int((charx-charsize/2)/self.size)
        posy = int((chary+charsize/2)/self.size)
        try:
            if self.map[posy][posx] == 1:
                return Collision.rect_collision(charx-charsize/2, chary, charsize, charsize, posx*self.size, posy*self.size, self.size, self.size, "pos")
        except IndexError:
            pass
        posx = int((charx+charsize/2)/self.size)
        posy = int((chary-charsize/2)/self.size)
        try:
            if self.map[posy][posx] == 1:
                return Collision.rect_collision(charx, chary-charsize/2, charsize, charsize, posx*self.size, posy*self.size, self.size, self.size, "pos")
        except IndexError:
            pass'''
        return ([0, 0], [-1, 0, 0])

