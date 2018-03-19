from Server import *
import pickle
import sys

class test:
    def __init__(self):
        self.a = 1
        self.b = 'hello'

class GameServer(Server):
    def __init__(self, address, port, gameBoard):
        self.address = address
        self.port = port
        self.connections = []
        self.serverSocket = socket.socket()
        self.serverSocket.bind((self.address, self.port))
        self.serverSocket.listen()
        self.gameState = gameBoard

    def notify(self):
        for clientSocket, clientConnection in self.connections:
            data = test()
            clientConnection.send(pickle.dumps(data))
            #clientConnection.send(bytes("You have been connected", 'utf-8'))
            #print(str(clientSocket.recv(1024), 'utf-8'))
            data2 = clientSocket.recv(4096)
            dataClass = pickle.loads(data2)
            print(dataClass.b)

    def getGameState(self):
        return self.gameState

    def setGameState(self):
        pass

    def startGameServer(self, player1, player2):
        assert (len(self.connections) == 2), 'Must have two players to start game'
        self.gameState.initializeGameBoard(player1, player2)

    def closeServer(self):
        self.serverSocket.close()

'''
server = GameServer(socket.gethostbyname(''), 1234, None)
client = socket.socket()
server.addConnection(client)
server.notify()
client.close()
server.serverSocket.close()

t = test()
print(sys.getsizeof(t))
'''
