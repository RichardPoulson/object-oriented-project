import socket
import threading
import pickle
import sys
from ClientSocket import *
from CheckersBoard import *

class Server:

    def __init__(self, address, port, gameBoard):
        self.clientConnections = []
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((address, port))
        self.serverSocket.listen()
        self.setAdress(address)
        self.setPort(port)
        self.game = gameBoard

    def getAdress(self):
        return self.address

    def setAdress(self, address):
        self.address = address

    def getPort(self):
        return self.port

    def setPort(self, port):
        self.port = port

    def sendState(self):
        readOnlyGameState = pickle.dumps(self.game.getReadOnlyState())
        for connection in self.clientConnections:
            connection.send(readOnlyGameState)

    def clientInputHandler(self, clientSocket):
        while True:
            if (len(self.clientConnections) == 2):
                data = clientSocket.recv(1024)
                for connection in self.clientConnections:
                    connection.send(bytes(data))

    def acceptConnections(self):
        while True:
            clientSocket, address = self.serverSocket.accept()
            clientHandlerThread = threading.Thread(target=self.clientInputHandler, args=(clientSocket,))
            clientHandlerThread.daemon = True
            clientHandlerThread.start()
            self.clientConnections.append(clientSocket)
            print("recieved connection from {}:{}".format(address[0], address[1]))

    def removeConnection(self, clientSocket):
        for socket, i in enumerate(self.connections):
            if (clientSocket == socket):
                clientSocket.close()
                self.connections.pop(i)

    def run(self):
        acceptorThread = threading.Thread(target=self.acceptConnections)
        acceptorThread.daemon=True
        acceptorThread.start()

    def closeServer(self):
        self.serverSocket.close()
