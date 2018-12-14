import threading, socket

class Clients(threading.Thread):
    def __init__ (self, conn, addr, id_):
        threading.Thread.__init__(self)
        self.id = id_ 
        self.conn = conn
        self.addr = addr
        self.received = {"pos":(0, 0), "msg":""}
        self.stop = False
        self.newArrived = False

    def run(self):
        print("Client on ip:%s addr:%s connected" % self.addr)
        self.conn.settimeout(0.001)
        while not self.stop:
            try :
                msg = eval(self.conn.recv(1024).decode()) #Receive data from client
                for i in msg.keys():
                    self.received[i] = msg[i]
                self.newArrived = True
            except (OSError, ConnectionAbortedError, ConnectionResetError, socket.timeout, SyntaxError, TypeError):
                pass

        self.conn.close()
        print("Client on ip:%s addr:%s disconnected" % self.addr)

    def receive(self):
        self.newArrived = False
        return self.received

    def send(self, data):
        if data == "":
            return
        try:
            self.conn.send(str(data).encode())
        except OSError:
            self.quit()

    def quit(self):
        self.stop = True


class Server(threading.Thread):
    def __init__ (self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.Socket = socket.socket()
        self.Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.Socket.bind(("0.0.0.0", self.port))
        print("Server started on port:%s" % self.port)
        self.Socket.listen(1)
        self.clients = []
        self.stop = False

    def run(self):
        give_id = 1
        while not self.stop:
            try:
                conn, addr = self.Socket.accept() #Receive connection
                self.refresh_clients()
                self.clients.append(Clients(conn, addr, give_id)) #Add new connection
                self.clients[len(self.clients)-1].start()
                give_id += 1
            except OSError:
                self.quit()
        self.quit()

    def refresh_clients(self):
        for n, i in enumerate(self.clients):
            if i != None:
                if i.stop:
                    del self.clients[n] #Delete disconnected client
                    break

    def quit(self):
        for i in self.clients:
            if i != None:
                i.quit()
        self.Socket.close()
        self.stop = True