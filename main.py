import pygame, Server, Client, sys, Map, time, Character, math, Shooting, titlescreen

STOPALL = False

pygame.init()
screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)
pygame.display.set_caption("Bazz")

def pygame_event():
	global STOPALL
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			STOPALL = True

		#Resizable window
		if event.type == pygame.VIDEORESIZE:
			screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

titlescreen.run(screen)

isServer = False
isClient = False
ip_address = "192.168.137.72"
m = Map.map(100, 100, 25)
ti = time.time()
map_ = []
other_players = {}
player = Character.player(20)
shooting = Shooting.shoot()
delta = 0
while not STOPALL:
	ti = time.time()
	if not (isServer or isClient):
		if titlescreen.runserver:
			server = Server.Server(7777)
			server.start()
			isClient = False
			isServer = True
			m.generatemap()
			while m.check_collision(screen, player.x, player.y, player.size) != [0, 0]:
				player.randpos()
		else:
			client = Client.Client(ip_address, 7777)
			client.start()
			isClient = client.connected
			isServer = False
			client.send({'msg':"map"})
	else:
		dx, dy = player.get_movement(delta)
		col_pos = [0, 0]
		col_pos[0] = m.check_collision(screen, player.x+dx, player.y, player.size)[0]
		col_pos[1] = m.check_collision(screen, player.x, player.y+dy, player.size)[1]
		if col_pos[0] != 0 and col_pos[1] != 0:
			dx = dx*math.sin(math.pi * 45 / 180)
			dy = dy*math.sin(math.pi * 45 / 180)
		if col_pos[0] != 0:
			dx = 0
		if col_pos[1] != 0:
			dy = 0
		player.set_movement(dx, dy)

		if isServer:
			server.refresh_clients()
			other_players = {}
			for client in server.clients:
				if client.newArrived:
					if client.receive()['msg'] == "others":
						send = {"others":{0:(player.x, player.y)}}
						for other_clients in server.clients:
							if client.id != other_clients.id:
								send["others"][client.id] = other_clients.receive()["pos"]
						client.send(send)
					elif client.receive()['msg'] == "map":
						print(len(str(m.map).encode()))
						client.send({"map":m.map})

				other_players[client.id] = client.receive()["pos"]

		elif isClient:
			if client.connected:
				if client.newArrived:
					for i in client.receive().keys():
						if i == "map":
							map_ = client.receive()['map']
							m.map = map_
							while m.check_collision(screen, player.x, player.y, player.size) != [0, 0]:
								player.randpos()
						if i == "others":
							other_players = client.receive()['others']
					client.send({'msg':"others", 'pos':(player.x, player.y)})
			else:
				 STOPALL = True



	pygame_event()
	screen.fill((255, 0, 255))
	m.draw(screen, player.x, player.y)
	player.draw_others(screen, other_players)
	player.draw(screen)
	shooting.gen_bullets(screen, player.x, player.y)
	pygame.display.update()
	delta = time.time()-ti
	#print(int(1/delta))


if isServer:
	server.quit()
if isClient:
	client.quit()
pygame.quit()
sys.exit()
