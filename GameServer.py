import socket

class GameServer:

    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.connections = []
        self.serverSocket = socket.socket()
        self.serverSocket.bind((self.address, self.port))
        self.serverSocket.listen()

    def addConnection(self, clientSocket):
        clientSocket.connect((self.address, self.port))
        c, addr = self.serverSocket.accept()
        self.connections.append((clientSocket, c))

    def notify(self):
        '''
        for conns in self.connections:
            conns[1].send(bytes("You have been connected", 'utf-8'))
            print(str(conns[0].recv(1024), 'utf-8'))
        '''
        pass

'''
# Testing
server = GameServer(socket.gethostbyname(''), 1234)
client = socket.socket()
server.addConnection(client)
server.notify()
client.close()
server.serverSocket.close()
'''
