import threading, socket

class Client(threading.Thread):
    def __init__ (self, ip, port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port

        self.stop = False
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.newArrived = False

        try:
            self.Socket.connect((ip, port))
            self.connected = True
            print("Connected to server")
        except (socket.gaierror, ConnectionRefusedError):
            print("Host not reachable")
            self.stop = True

        self.Socket.settimeout(0.001)
        self.received = {}

    def run(self):
        while not self.stop:
            try:
                try:
                    msg = eval(self.Socket.recv(1024).decode()) #Receive data from the server
                    self.received = msg
                    self.newArrived = True
                except (socket.timeout, SyntaxError, TypeError):
                    pass
            except (OSError, ConnectionAbortedError):
                self.quit()
        self.quit()

    def receive(self):
        self.newArrived = False
        return self.received

    def send(self, data):
        if data == "":
            return
        try:
            self.Socket.send(str(data).encode())
        except (OSError, ConnectionResetError):
            self.quit()

    def quit(self):
        print("Connection aborted")
        try:
            self.Socket.close()
        except OSError:
            pass
        self.connected = False
        self.stop = True