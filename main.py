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
ip_address = "localhost"
m = Map.map(100, 100, 25)
ti = time.time()
map_ = []
other_players = {}
player = Character.player(20)

delta = 0
shooting = Shooting.shoot()
item_spawn = 0
send_time = 0
while not STOPALL:
	ti = time.time()
	if not (isServer or isClient):
		if titlescreen.runserver:
			server = Server.Server(7777)
			server.start()
			isClient = False
			isServer = True
			m.generatemap()
			while m.check_collision(screen, player.x, player.y, player.size)[0] != [0, 0]:
				player.randpos()
		else:
			client = Client.Client(ip_address, 7777)
			client.start()
			isClient = client.connected
			isServer = False
			client.send({'msg': "firstmap"})
	else:
		dx, dy = player.get_movement(delta)
		col_pos = [0, 0]
		item = m.check_collision(screen, player.x+dx, player.y, player.size)
		col_pos[0] = item[0][0]
		item2 = m.check_collision(screen, player.x, player.y + dy, player.size)
		col_pos[1] = item2[0][1]
		if col_pos[0] == 0 and col_pos[1] == 0:
			dx = dx * math.sin(math.pi * 45 / 180)
			dy = dy * math.sin(math.pi * 45 / 180)

		if item[1][0] == 1 or item2[1][0] == 1:
			if col_pos[0] != 0:
				dx = 0
			if col_pos[1] != 0:
				dy = 0

		item = m.check_collision(screen, player.x, player.y, player.size)

		if item[1][0] == 2:
			m.map[item[1][2]][item[1][1]] = 0
			player.ammo +=3

		if item[1][0] == 3:
			m.map[item[1][2]][item[1][1]] = 0
			player.health += 10

		if item[1][0] == 4:
			m.map[item[1][2]][item[1][1]] = 0


		#else:
		#	if col_pos[0] != 0:
		#		dx = 0
		#	if col_pos[1] != 0:
		#		dy = 0
		player.set_movement(dx, dy)

		if isServer:
			server.refresh_clients()
			other_players = {}
			for client in server.clients:
				if client.newArrived:
					if "others" == client.receive()['msg']:
						send = {"others":{0:(player.x, player.y)}}
						for other_clients in server.clients:
							if client.id != other_clients.id:
								send["others"][client.id] = other_clients.receive()["pos"]
						client.send(send)
					elif "map" == client.receive()['msg']:
						client.send({"map":m.map})
					elif "firstmap" == client.receive()['msg']:
						client.send({"firstmap":m.map})
					elif "bullets" == client.receive()['msg']:
						client.send({"bullets":shooting.bullets})
					elif "delItem" == client.receive()['msg']:
						print("pede")
						m.map[client.receive()['item'][1]][client.receive()['item'][1]] = 0

				other_players[client.id] = client.receive()["pos"]
			if time.time()-item_spawn > 10:
				m.generateitems()
				item_spawn = time.time()

		elif isClient:
			print(client)
			if client.connected:
				if client.newArrived:
					for i in client.receive().keys():
						if i == "firstmap":
							m.map = client.receive()['firstmap']
							while m.check_collision(screen, player.x, player.y, player.size)[0] != [0, 0]:
								player.randpos()
						elif i == "map":
							m.map = client.receive()['map']
						elif i == "others":
							other_players = client.receive()['others']
						elif i == "bullets":
							shooting.bullets = client.receive()['bullets'] #[[plrx,plry], [vel_x, vel_y]]
				if time.time()-send_time > 0.4:
					client.send({'msg':"bullets"})
					send_time = time.time()
				elif time.time()-send_time > 0.3:
					client.send({'msg': "map"})
				elif time.time()-send_time > 0.2:
					client.send({'msg':"others", 'pos':(player.x, player.y)})
				elif time.time()-send_time > 0.1:
					if item[1][0] == 2 or item[1][0] == 3 or item[1][0] == 4:
						client.send({'msg': "delItem", "item": [item[1][1], item[1][2]]})
			else:
				STOPALL = True

	pygame_event()
	screen.fill((255, 0, 255))
	m.draw(screen, player.x, player.y)
	player.draw_others(screen, other_players)
	player.draw(screen)
	if 0 < player.ammo:
		player.ammo = shooting.gen_bullets(screen, player.x, player.y, player.ammo)
	shooting.draw_bullets(screen, player.x, player.y)
	pygame.display.update()
	delta = time.time()-ti
	#print(int(1/delta))


if isServer:
	server.quit()
if isClient:
	client.quit()
pygame.quit()
sys.exit()
