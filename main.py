import pygame, Server, Client, sys, Map

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
#runserver = int(input("1, kui server: "))
m = Map.map(10, 5)
m.generatemap()
while not STOPALL:
	'''if not (isServer or isClient):
		if runserver == 1:
			server = Server.Server(7777)
			server.start()
			isClient = False
			isServer = True
		else:
			client = Client.Client(ip_address, 7777)
			client.start()
			isClient = client.connected
			isServer = False
	else:
		if isServer:
			server.refresh_clients()
			for client in server.clients:
				if client.newArrived:
					print(client.id, client.receive())

					send = {0:{"msg":"server ütles PEDE"}}
					for other_clients in server.clients:
						if client.id != other_clients.id:
							if other_clients.receive() != None:
								send[client.id] = other_clients.receive()
					client.send(send)

		elif isClient:
			if client.connected:
				if client.newArrived:
					print(client.receive())
				client.send({"msg": "Client ütles vähem pede"})
			else:
				STOPALL = True'''



	pygame_event()
	screen.fill((255, 0, 255))
	m.draw(screen, (50, 255, 50), 50)
	pygame.display.update()

if isServer:
	server.quit()
if isClient:
	client.quit()
pygame.quit()
sys.exit()

for i in range(mapy):
	buf = []
	for j in range(mapx):
		buf.append(0)
	map.append(buf)
