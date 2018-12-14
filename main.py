import pygame, Server, Client, sys, Map, time, Character

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

isServer = False
isClient = False
ip_address = "localhost"
runserver = int(input("1, kui server: "))
m = Map.map(300, 300)
ti = time.time()
map_ = []
other_players = {}
player = Character.player(100, 100, 10)

while not STOPALL:
	if not (isServer or isClient):
		if runserver == 1:
			server = Server.Server(7777)
			server.start()
			isClient = False
			isServer = True
			m.generatemap()
		else:
			client = Client.Client(ip_address, 7777)
			client.start()
			isClient = client.connected
			isServer = False
			client.send({'msg':"map"})
	else:
		player.movement()
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
						if i == "others":
							other_players = client.receive()['others']
					client.send({'msg':"others", 'pos':(player.x, player.y)})
			else:
				 STOPALL = True



	pygame_event()
	screen.fill((255, 0, 255))
	m.draw(screen, 10, player.x, player.y)
	player.draw_others(screen, other_players)
	player.draw(screen)
	pygame.display.update()

if isServer:
	server.quit()
if isClient:
	client.quit()
pygame.quit()
sys.exit()