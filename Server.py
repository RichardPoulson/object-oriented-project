import socket
import threading
import pickle
import sys
from ClientSocket import *
from CheckersBoard import *
from Player import *

class Server:

    def __init__(self, address, port):
        self.clientConnections = []
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((address, port))
        self.serverSocket.listen()
        self.setAdress(address)
        self.setPort(port)
        self.commandQueue = {'hostingUser': [], 'joiningUser': []}

    def getAdress(self):
        return self.address

    def setAdress(self, address):
        self.address = address

    def getPort(self):
        return self.port

    def setPort(self, port):
        self.port = port

    def getCommandQueue(self):
        return self.commandQueue

    def getNumberOfClientConnections(self):
        return len(self.clientConnections)

    def getNumberCommandsInQueue(self, userKey):
        return len(self.getCommandQueue()[userKey])

    def sendState(self, readOnlyState):
        state = pickle.dumps(readOnlyState)
        for connection in self.clientConnections:
            connection.sendall(state)


    def clientInputHandler(self, clientSocket):
        while True:
            data = clientSocket.recv(1024)
            userKey, pieceID, moveType = pickle.loads(data)
            self.commandQueue[userKey].append((pieceID, moveType))

    def acceptConnections(self, verbose=True):
        while True:
            clientSocket, address = self.serverSocket.accept()
            clientHandlerThread = threading.Thread(target=self.clientInputHandler, args=(clientSocket,))
            clientHandlerThread.daemon = True
            clientHandlerThread.start()
            self.clientConnections.append(clientSocket)
            if verbose:
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
