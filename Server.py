from abc import ABCMeta, abstractmethod
import socket

class Server(metaclass=ABCMeta):

    connections = []

    def addConnection(self, player):
        player.connectPlayerSocket(self.address, self.port)
        #clientSocket.connect((self.address, self.port))
        client, address = self.serverSocket.accept()
        self.connections.append((player.getPlayerSocket(), client))

    def removeConnection(self, clientSocket):
        for socket, connection, i in enumerate(self.connections):
            if (clientSocket == socket):
                self.connections.pop(i)

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def closeServer(self):
        pass
