from abc import ABCMeta, abstractmethod
import socket

class Server(metaclass=ABCMeta):

    connections = []

    def addConnection(self, clientSocket):
        clientSocket.connect((self.address, self.port))
        c, addr = self.serverSocket.accept()
        self.connections.append((clientSocket, c))

    def removeConnection(self, clientSocket):
        for socket, connection, i in enumerate(self.connections):
            if (clientSocket == socket):
                self.connections.pop(i)

    @abstractmethod
    def notify(self):
        pass
