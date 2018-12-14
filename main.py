import pygame, Server, Client, sys, Map, time

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
m = Map.map(10, 5)
m.generatemap()
ti = time.time()
map_ = []

while not STOPALL:
	if not (isServer or isClient):
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
			client.send({'msg':"map"})
	else:
		if isServer:
			server.refresh_clients()
			for client in server.clients:
				if client.newArrived:
					client_msg = client.receive()
					if client_msg['msg'] == "others":
						send = {"others":{0:(50, 69)}}
						for other_clients in server.clients:
							if client.id != other_clients.id:
								send["others"][client.id] = other_clients.receive()["pos"]
						client.send(send)
					elif client_msg['msg'] == "map":
						print(len(str(m.map).encode()))
						client.send({"map":m.map})
					print(client.id, client.receive())

		elif isClient:
			if client.connected:
				if client.newArrived:
					print(client.receive())
				if time.time()-ti > 1:
					if client.receive()["msg"]:
						if i == "map":
							print("kys")
							map_ = client.receive()[i]
					ti = time.time()
			else:
				STOPALL = True



	pygame_event()
	screen.fill((255, 0, 255))
	m.draw(screen, 10, 0, 0)
	pygame.display.update()

if isServer:
	server.quit()
if isClient:
	client.quit()
pygame.quit()
sys.exit()