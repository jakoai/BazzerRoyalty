import threading, socket

class Clients(threading.Thread):
    def __init__ (self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.received = {}
        self.stop = False

    def run(self):
        print("Client on ip:%s addr:%s connected" % self.addr)
        self.conn.settimeout(0.001)
        while not self.stop:
            try:
                try:
                    try:
                        try:
                            try:
                                try:
                                    msg = eval(self.conn.recv(1024).decode()) #Receive data from client
                                    for i in msg.keys():
                                        self.received[i] = msg[i]
                                except TypeError:
                                    pass
                            except SyntaxError:
                                pass
                        except socket.timeout:
                            pass
                    except ConnectionResetError:
                        pass
                except ConnectionAbortedError:
                    pass
            except OSError:
                pass

        self.conn.close()
        print("Client on ip:%s addr:%s disconnected" % self.addr)

    def receive(self):
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
        while not self.stop:
            try:
                conn, addr = self.Socket.accept() #Receive connection
                self.refresh_clients()
                self.clients.append(Clients(conn, addr)) #Add new connection
                self.clients[len(self.clients)-1].start()
            except OSError:
                self.stop = True
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